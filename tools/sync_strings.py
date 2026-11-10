#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Scan translatable strings in the Lichii source tree and diff them against zh_CN.ts.

This is a lightweight, dependency-free alternative to `lupdate` for auditing
which strings a language pack covers. It intentionally errs on the side of
reporting extra candidates; entries that Qt would not extract (debug strings,
format strings with concatenated literals, etc.) are filtered heuristically.

Usage:
    python tools/sync_strings.py --source /path/to/Lichii [--ts lang/zh_CN.ts]
                                 [--report docs/missing-strings.md]
                                 [--json docs/missing-strings.json]
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path

SKIP_DIR_NAMES = {
    "dynarmic", "tests", "web_service", "shader_recompiler", ".git", "build",
    "externals", "vulkan", "android", "yuzu_cmd", "dedicated_room",
}
SCAN_DIRS = ("src/yuzu", "src/qt_common", "src/frontend_common", "src/common")

# C++ string literal, non-greedy, tolerates escaped quotes.
LIT = r'"((?:\\.|[^"\\])*)"'
TR_RE = re.compile(r"(?<![\w:])tr\s*\(\s*" + LIT, re.S)
TRANSLATE_RE = re.compile(r"QCoreApplication::translate\s*\(\s*" + LIT + r"\s*,\s*" + LIT, re.S)
NOOP_RE = re.compile(r"QT_TRANSLATE_NOOP\s*\(\s*" + LIT + r"\s*,\s*" + LIT, re.S)
TR_NOOP_RE = re.compile(r"QT_TR_NOOP\s*\(\s*" + LIT + r"\)", re.S)


def unescape_cpp(value: str) -> str:
    """Decode the small subset of C++ escapes found in translatable literals."""
    out, i = [], 0
    table = {"n": "\n", "t": "\t", "r": "\r", "\\": "\\", '"': '"', "'": "'", "0": "\0"}
    while i < len(value):
        ch = value[i]
        if ch == "\\" and i + 1 < len(value):
            nxt = value[i + 1]
            out.append(table.get(nxt, nxt))
            i += 2
        else:
            out.append(ch)
            i += 1
    return "".join(out)


def ui_strings(path: Path) -> list[tuple[str, str]]:
    """Return (context, source) pairs from a Qt .ui XML file."""
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError:
        return []
    class_name = ""
    for elem in root.iter("class"):
        class_name = (elem.text or "").strip()
        break
    result = []
    for elem in root.iter("string"):
        if elem.get("notr", "").lower() == "true":
            continue
        text = "".join(elem.itertext())
        if text.strip():
            result.append((class_name, text))
    return result


def cpp_strings(path: Path) -> list[tuple[str, str]]:
    """Return (context, source) pairs from a C++ source/header file."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return []
    stem = path.stem
    result = []
    for match in TR_RE.finditer(text):
        result.append((stem, unescape_cpp(match.group(1))))
    for match in TRANSLATE_RE.finditer(text):
        result.append((unescape_cpp(match.group(1)), unescape_cpp(match.group(2))))
    for match in NOOP_RE.finditer(text):
        result.append((unescape_cpp(match.group(1)), unescape_cpp(match.group(2))))
    for match in TR_NOOP_RE.finditer(text):
        result.append((stem, unescape_cpp(match.group(1))))
    return result


def collect_sources(root: Path) -> dict[tuple[str, str], set[str]]:
    """Map (context, source) -> {originating files} across the source tree."""
    found: dict[tuple[str, str], set[str]] = defaultdict(set)
    bases = [root / d for d in SCAN_DIRS if (root / d).is_dir()]
    if not bases:
        raise SystemExit(f"[!] No source directories found under {root}")
    for base in bases:
        for path in base.rglob("*"):
            if not path.is_file() or any(part in SKIP_DIR_NAMES for part in path.parts):
                continue
            pairs = []
            if path.suffix == ".ui":
                pairs = ui_strings(path)
            elif path.suffix in {".cpp", ".h", ".hpp", ".cc"}:
                pairs = cpp_strings(path)
            for context, source in pairs:
                source = source.strip()
                if not source or "\n" in source and len(source) > 400:
                    continue
                found[(context, source)].add(str(path.relative_to(root)).replace("\\", "/"))
    return found


def collect_ts(ts_path: Path) -> tuple[set[tuple[str, str]], set[str], int]:
    """Return (context, source) pairs, bare source strings, and message count."""
    root = ET.parse(ts_path).getroot()
    pairs: set[tuple[str, str]] = set()
    sources: set[str] = set()
    count = 0
    for context in root.findall("context"):
        name = (context.findtext("name") or "").strip()
        for message in context.findall("message"):
            count += 1
            source = message.findtext("source")
            if source is None:
                # <byte> payloads (custom lupdate encodings) are not comparable.
                continue
            source = html.unescape(source)
            pairs.add((name, source))
            sources.add(source)
    return pairs, sources, count


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, type=Path, help="Lichii source tree root")
    parser.add_argument("--ts", type=Path, default=Path(__file__).resolve().parent.parent / "lang/zh_CN.ts")
    parser.add_argument("--report", type=Path, default=None)
    parser.add_argument("--json", dest="json_out", type=Path, default=None)
    args = parser.parse_args()

    if not args.ts.is_file():
        raise SystemExit(f"[!] Translation file not found: {args.ts}")

    src_map = collect_sources(args.source)
    ts_pairs, ts_sources, ts_count = collect_ts(args.ts)

    missing: list[dict] = []
    for (context, source), files in sorted(src_map.items(), key=lambda item: (item[0][0], item[0][1].lower())):
        if (context, source) in ts_pairs or source in ts_sources:
            continue
        missing.append({"context": context, "source": source, "files": sorted(files)})

    print(f"源码可翻译字符串（去重）: {len(src_map)}")
    print(f"zh_CN.ts 消息总数        : {ts_count}")
    print(f"源码中未被 TS 覆盖       : {len(missing)}")
    print(f"TS 中不再被源码引用(约)  : {len(ts_sources - {s for _, s in src_map})}")

    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(missing, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"[+] JSON  -> {args.json_out}")
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        lines = [
            "# 待补译字符串", "",
            f"- 源码可翻译字符串（去重）：{len(src_map)}",
            f"- `zh_CN.ts` 消息总数：{ts_count}",
            f"- 源码中未被 TS 覆盖：**{len(missing)}**", "",
            "> 本表由 `tools/sync_strings.py` 静态扫描生成，可能包含 Qt lupdate 不会提取的字符串。",
            "> 请以 `lupdate` 的实际输出为准。", "",
            "| Context | Source | 出现文件 |", "| --- | --- | --- |",
        ]
        for item in missing:
            src = item["source"].replace("|", "\\|").replace("\n", " ")[:240]
            lines.append(f"| `{item['context']}` | {src} | `{', '.join(item['files'][:2])}` |")
        args.report.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"[+] Markdown -> {args.report}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
