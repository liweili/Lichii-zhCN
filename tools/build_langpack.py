#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Lichii-zhCN Qt language pack (zh_CN.ts -> zh_CN.qm).

Why this exists
---------------
Upstream ships `dist/languages/zh_CN.ts`, but Lichii renamed a lot of UI text
from "Eden" to "Lichii" and added new panels. Qt looks translations up by the
*source* string, so every renamed entry silently falls back to English.
`lang/lichii_source.ts` is generated with `lupdate` from the actual Lichii
source tree and therefore has the correct contexts, sources and disambiguation
comments. This script merges into that authoritative skeleton:

  1. exact (context, source) match from the upstream zh_CN.ts,
  2. source-only match (context drift),
  3. "Eden" -> "Lichii" normalised match (brand rename),
  4. translations from lang/additions.zh.txt (new Lichii-only strings),
  5. leave the entry unfinished (Qt then shows the English original).

Usage:
    python tools/build_langpack.py
    python tools/build_langpack.py --lrelease /path/to/lrelease.exe
    python tools/build_langpack.py --no-qm       # only regenerate the .ts
"""
from __future__ import annotations

import argparse
import html
import json
import os
import re
import shutil
import subprocess
import sys
import sysconfig
import xml.etree.ElementTree as ET
from pathlib import Path
from xml.sax.saxutils import escape as xml_escape

ROOT = Path(__file__).resolve().parent.parent
LANG = ROOT / "lang"
DIST = ROOT / "dist"
DOCS = ROOT / "docs"

BRAND_RE = re.compile(r"\bEden\b(?![-./])")
PLACEHOLDER_RE = re.compile(r"%(?:[0-9]+|L[0-9]+|n)")
WS_RE = re.compile(r"\s+")


def norm(text: str) -> str:
    """Normalise a source string so an Eden-era entry can match a Lichii one."""
    return WS_RE.sub(" ", BRAND_RE.sub("Lichii", text)).strip()


def message_text(translation_el: ET.Element | None) -> str:
    if translation_el is None:
        return ""
    forms = translation_el.findall("numerusform")
    if forms:
        return "".join(forms[0].itertext())
    return "".join(translation_el.itertext())


def load_baseline(path: Path) -> dict[str, dict[str, str]]:
    """Build three lookup tables from the upstream zh_CN.ts."""
    by_key: dict[str, str] = {}
    by_source: dict[str, str] = {}
    by_norm: dict[str, str] = {}
    root = ET.parse(path).getroot()
    for context in root.findall("context"):
        name = context.findtext("name") or ""
        for message in context.findall("message"):
            source_el = message.find("source")
            if source_el is None:
                continue
            source = html.unescape("".join(source_el.itertext()))
            translation = message_text(message.find("translation"))
            if not translation.strip():
                continue
            tr_el = message.find("translation")
            if tr_el is not None and tr_el.get("type") in {"unfinished", "vanished", "obsolete"}:
                continue
            by_key.setdefault(name + "\x00" + source, translation)
            by_source.setdefault(source, translation)
            by_norm.setdefault(norm(source), translation)
    return {"key": by_key, "source": by_source, "norm": by_norm}


def load_additions(txt: Path, missing_json: Path) -> dict[str, str]:
    """Pair additions.zh.txt rows with missing-strings.json entries by line number."""
    if not missing_json.is_file():
        print(f"[!] 缺少 {missing_json}，跳过新增译文")
        return {}
    items = json.loads(missing_json.read_text(encoding="utf-8"))
    lines = [ln.rstrip("\n") for ln in txt.read_text(encoding="utf-8").splitlines()
             if ln.strip() and not ln.lstrip().startswith("#")]
    by_index: dict[int, str] = {}
    for line in lines:
        if "\t" not in line:
            continue
        head, value = line.split("\t", 1)
        try:
            by_index[int(head.strip())] = value
        except ValueError:
            continue
    out: dict[str, str] = {}
    skipped = 0
    for index, item in enumerate(items, 1):
        value = by_index.get(index, "-").strip()
        if not value or value == "-":
            skipped += 1
            continue
        out[item["source"]] = value
        out.setdefault(norm(item["source"]), value)
    print(f"[*] 新增译文表    : {len(items) - skipped} 条（跳过 {skipped} 条）")
    # translations.json is the previous build's glossary. Folding it back in
    # lets a refreshed lupdate skeleton keep every already-translated string,
    # so upgrading Lichii never silently reverts the UI to English.
    glossary_path = LANG / "translations.json"
    if glossary_path.is_file():
        previous = json.loads(glossary_path.read_text(encoding="utf-8"))
        for key, value in previous.items():
            out.setdefault(key, value)
            out.setdefault(norm(key), value)
        print(f"[*] 沿用上次词库  : {len(previous)} 条")
    return out


def load_extras(path: Path) -> dict[str, str]:
    """Load source-keyed leftover translations (lang/extras.zh.json).

    Keyed by the English source rather than by position, so refreshing the
    lupdate skeleton can never shift a translation onto a different string.
    """
    if not path.is_file():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    out: dict[str, str] = {}
    for source, value in data.items():
        if not isinstance(value, str) or not value.strip():
            continue
        out.setdefault(source, value)
        out.setdefault(norm(source), value)
    print(f"[*] 补遗译文表    : {len(data)} 条")
    return out


def find_lrelease(explicit: str | None) -> str | None:
    if explicit:
        return explicit if Path(explicit).is_file() else shutil.which(explicit)
    env = os.environ.get("LRELEASE")
    if env and Path(env).is_file():
        return env
    for name in ("lrelease", "lrelease-qt6", "lrelease6", "pyside6-lrelease"):
        found = shutil.which(name)
        if found:
            return found
    # PySide6 ships the real Qt binaries inside its package directory.
    candidates = [
        Path(sysconfig.get_paths().get("purelib", "")) / "PySide6" / "lrelease.exe",
        Path(sysconfig.get_paths().get("purelib", "")) / "PySide6" / "lrelease",
        Path.home() / "AppData/Roaming/Python/Python312/site-packages/PySide6/lrelease.exe",
        Path.home() / "AppData/Roaming/Python/Python313/site-packages/PySide6/lrelease.exe",
        Path("/usr/lib/qt6/bin/lrelease"),
    ]
    for candidate in candidates:
        if candidate.is_file():
            return str(candidate)
    return None


def build_ts(skeleton: Path, baseline: dict, additions: dict, extras: dict, out: Path) -> dict:
    root = ET.parse(skeleton).getroot()
    total = inherited = added = extras_used = unfinished = 0
    warnings: list[str] = []
    glossary: dict[str, str] = {}

    chunks = [
        '<?xml version="1.0" encoding="utf-8"?>\n',
        '<!DOCTYPE TS>\n',
        '<TS version="2.1" language="zh_CN" sourcelanguage="en_US">\n',
    ]

    for context in root.findall("context"):
        name = context.findtext("name") or ""
        chunks.append("<context>\n")
        chunks.append(f"    <name>{xml_escape(name)}</name>\n")
        for message in context.findall("message"):
            total += 1
            source_el = message.find("source")
            if source_el is None:
                continue
            source = html.unescape("".join(source_el.itertext()))
            key = name + "\x00" + source
            nsource = norm(source)

            translation = None
            origin = ""
            if source.strip():  # 空白占位串不参与匹配，避免长句被误配到它上面
                for table, probe in (("key", key), ("source", source), ("norm", nsource)):
                    if probe in baseline[table]:
                        translation = baseline[table][probe]
                        origin = f"baseline:{table}"
                        break
                if translation is None:
                    for probe in (source, nsource):
                        if probe in additions:
                            translation = additions[probe]
                            origin = "additions"
                            break
                if translation is None:
                    for probe in (source, nsource):
                        if probe in extras:
                            translation = extras[probe]
                            origin = "extras"
                            break

            if translation and origin.startswith("baseline"):
                # Lichii renamed the product; keep translations factually correct.
                translation = BRAND_RE.sub("Lichii", translation)
                inherited += 1
            elif translation and origin == "extras":
                extras_used += 1
            elif translation:
                added += 1
            else:
                unfinished += 1

            if translation:
                src_ph = sorted(PLACEHOLDER_RE.findall(source))
                dst_ph = sorted(PLACEHOLDER_RE.findall(translation))
                if src_ph != dst_ph:
                    warnings.append(f"{name}: {source[:60]!r} 原文{src_ph} 译文{dst_ph}")
                glossary[source] = translation

            # Keep every non-translation child: <comment> is the disambiguation
            # Qt hashes together with (context, source); dropping it breaks lookups.
            pieces = []
            for child in message:
                if child.tag == "translation":
                    continue
                pieces.append("        " + ET.tostring(child, encoding="unicode").strip())
            numerus = message.get("numerus") == "yes"
            if translation:
                body = xml_escape(translation)
                tr = (f"        <translation><numerusform>{body}</numerusform></translation>"
                      if numerus else f"        <translation>{body}</translation>")
                pieces.append(tr)
            else:
                pieces.append('        <translation type="unfinished"></translation>')
            chunks.append("    <message" + (' numerus="yes"' if numerus else "") + ">\n")
            chunks.append("\n".join(pieces) + "\n")
            chunks.append("    </message>\n")
        chunks.append("</context>\n")
    chunks.append("</TS>\n")

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("".join(chunks), encoding="utf-8")

    # Machine-readable glossary: source -> translation, independent of context.
    (LANG / "translations.json").write_text(
        json.dumps(dict(sorted(glossary.items())), ensure_ascii=False, indent=2),
        encoding="utf-8")

    if warnings:
        (DOCS / "placeholder-warnings.txt").write_text("\n".join(warnings) + "\n",
                                                        encoding="utf-8")
    print(f"[*] 骨架条目      : {total}")
    print(f"[*] 继承上游译文  : {inherited}")
    print(f"[*] 新增译文覆盖  : {added}")
    print(f"[*] 补遗译文覆盖  : {extras_used}")
    print(f"[*] 未翻译(留英文): {unfinished}")
    print(f"[*] 译文覆盖率    : {(total - unfinished) / total * 100:.1f}%")
    print(f"[!] 占位符不一致  : {len(warnings)} 条 -> docs/placeholder-warnings.txt")
    print(f"[+] {out}")
    return {"total": total, "inherited": inherited, "added": added,
            "unfinished": unfinished, "warnings": len(warnings)}


def compile_qm(lrelease: str, ts: Path, qm: Path) -> bool:
    qm.parent.mkdir(parents=True, exist_ok=True)
    result = subprocess.run([lrelease, str(ts), "-qm", str(qm)],
                            capture_output=True, text=True)
    print(result.stdout.strip())
    if result.returncode != 0:
        print("[!] lrelease 失败: " + result.stderr.strip())
        return False
    if not qm.is_file() or qm.stat().st_size < 1000:
        print("[!] QM 文件异常")
        return False
    print(f"[+] {qm} ({qm.stat().st_size:,} bytes)")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skeleton", type=Path, default=LANG / "lichii_source.ts")
    parser.add_argument("--baseline", type=Path, default=LANG / "baseline.zh_CN.ts")
    parser.add_argument("--additions", type=Path, default=LANG / "additions.zh.txt")
    parser.add_argument("--extras", type=Path, default=LANG / "extras.zh.json")
    parser.add_argument("--missing", type=Path, default=DOCS / "missing-strings.json")
    parser.add_argument("--out", type=Path, default=LANG / "zh_CN.ts")
    parser.add_argument("--qm", type=Path, default=DIST / "zh_CN.qm")
    parser.add_argument("--lrelease", default=None, help="lrelease 可执行文件路径")
    parser.add_argument("--no-qm", action="store_true", help="只生成 .ts")
    args = parser.parse_args()

    for path in (args.skeleton, args.baseline):
        if not path.is_file():
            raise SystemExit(f"[!] 缺少文件: {path}")

    baseline = load_baseline(args.baseline)
    additions = load_additions(args.additions, args.missing)
    extras = load_extras(args.extras)
    stats = build_ts(args.skeleton, baseline, additions, extras, args.out)
    if args.no_qm:
        return 0

    lrelease = find_lrelease(args.lrelease)
    if not lrelease:
        print("\n[!] 未找到 lrelease。请安装 Qt 6 LinguistTools 或 `pip install PySide6`，"
              "再用 --lrelease 指定路径。")
        print("    .ts 已生成，可用 Qt Linguist 打开。")
        return 1
    print(f"[*] lrelease: {lrelease}")
    return 0 if compile_qm(lrelease, args.out, args.qm) else 1


if __name__ == "__main__":
    sys.exit(main())
