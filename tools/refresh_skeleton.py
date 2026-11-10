#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Refresh lang/lichii_source.ts from a Lichii checkout using Qt's lupdate.

Run this whenever Lichii adds/renames UI strings:

    python tools/refresh_skeleton.py --source /path/to/Lichii
    python tools/build_langpack.py

The second command folds lang/translations.json (the previous build's glossary)
back in, so existing Chinese text survives a source update. Only genuinely new
strings need a new translation; they are listed by tools/sync_strings.py.
"""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sysconfig
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKELETON = ROOT / "lang" / "lichii_source.ts"
LOCATION_RE = re.compile(r'(<location\s+filename=")([^"]+)(")')


def normalize_locations(ts_path: Path) -> int:
    """Rewrite lupdate's <location filename="..."> paths to repo-relative form.

    lupdate records paths relative to the TS file's location, which leaks the
    maintainer's checkout directory (e.g. ../../.tmp/Lichii-src/src/yuzu/...).
    Qt only uses these for Linguist's "go to source", so collapsing everything
    before /src/ both removes local paths and keeps the references useful.
    """
    text = ts_path.read_text(encoding="utf-8")
    changed = 0

    def rewrite(match: re.Match) -> str:
        nonlocal changed
        original = match.group(2)
        normalized = original.replace("\\", "/")
        idx = normalized.find("/src/")
        if idx >= 0:
            normalized = normalized[idx + 1:]
        elif normalized.startswith("src/"):
            pass
        else:
            return match.group(0)
        if normalized != original:
            changed += 1
        return match.group(1) + normalized + match.group(3)

    result = LOCATION_RE.sub(rewrite, text)
    if changed:
        ts_path.write_text(result, encoding="utf-8")
    return changed


def find_lupdate(explicit: str | None) -> str | None:
    if explicit:
        return explicit if Path(explicit).is_file() else shutil.which(explicit)
    for name in ("lupdate", "lupdate-qt6", "lupdate6", "pyside6-lupdate"):
        found = shutil.which(name)
        if found:
            return found
    candidates = [
        Path(sysconfig.get_paths().get("purelib", "")) / "PySide6" / "lupdate.exe",
        Path.home() / "AppData/Roaming/Python/Python312/site-packages/PySide6/lupdate.exe",
        Path.home() / "AppData/Roaming/Python/Python313/site-packages/PySide6/lupdate.exe",
        Path("/usr/lib/qt6/bin/lupdate"),
    ]
    for candidate in candidates:
        if candidate.is_file():
            return str(candidate)
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, help="Lichii 源码根目录")
    parser.add_argument("--lupdate", default=None, help="lupdate 可执行文件路径")
    parser.add_argument("--normalize-only", action="store_true",
                        help="只规范化现有骨架里的 location 路径，不运行 lupdate")
    args = parser.parse_args()

    if args.normalize_only:
        if not SKELETON.is_file():
            raise SystemExit(f"[!] 骨架不存在: {SKELETON}")
        n = normalize_locations(SKELETON)
        print(f"[+] 规范化 {n} 条 location 路径 -> {SKELETON}")
        return 0

    if not args.source:
        parser.error("需要 --source（或使用 --normalize-only）")
    source = args.source.resolve()
    scan = [source / "src" / "yuzu", source / "src" / "qt_common"]
    for path in scan:
        if not path.is_dir():
            raise SystemExit(f"[!] 源码目录不存在: {path}")

    tool = find_lupdate(args.lupdate)
    if not tool:
        raise SystemExit("[!] 未找到 lupdate，请安装 Qt 6 LinguistTools / PySide6，或用 --lupdate 指定")
    print(f"[*] lupdate: {tool}")

    if SKELETON.is_file():
        shutil.copy2(SKELETON, SKELETON.with_suffix(".ts.bak"))
    cmd = [tool, "-recursive", "-noobsolete", *[str(p) for p in scan],
           "-ts", str(SKELETON), "-source-language", "en_US", "-target-language", "zh_CN"]
    result = subprocess.run(cmd, capture_output=True, text=True, cwd=source)
    print(result.stdout.strip()[-1500:])
    if result.returncode != 0:
        print("[!] " + result.stderr.strip()[-1500:])
        return 1
    n = normalize_locations(SKELETON)
    print(f"[*] 规范化 {n} 条 location 路径（避免写入本机绝对路径）")
    print(f"[+] {SKELETON}")
    print("[*] 接着运行: python tools/build_langpack.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
