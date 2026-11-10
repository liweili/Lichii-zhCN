#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Install (or remove) the Lichii-zhCN language pack into a Lichii install.

    python tools/install.py --target "D:/Lichii"
    python tools/install.py --target "D:/Lichii" --uninstall

The target directory is where lichii.exe (or `lichii`) lives. The pack is just
one file: <target>/languages/zh_CN.qm. A patched build of Lichii scans that
directory at startup and lists the pack in Settings -> Interface -> Language.
"""
from __future__ import annotations

import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
QM = ROOT / "dist" / "zh_CN.qm"
NAME = "zh_CN.qm"
NOTE = """Lichii-zhCN 中文语言包
========================

zh_CN.qm 由本项目的 lang/zh_CN.ts 编译而来。
把它保留在此目录即可在 Lichii 的「设置 -> 界面 -> 语言」中选择
「Chinese (China)」（中文系统下显示为「中文(中国)」）。

更新语言包：替换本文件并重启 Lichii。
移除语言包：删除本文件（或运行 tools/install.py --uninstall）。

前提：Lichii 需应用 patch/external-language-loader.patch，
      或使用已内置该补丁的构建。
项目地址与许可见项目根目录 README.md。
"""


def find_exe(target: Path) -> str | None:
    for name in ("lichii.exe", "lichii", "Lichii.app"):
        if (target / name).exists():
            return name
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", required=True, type=Path, help="Lichii 程序目录")
    parser.add_argument("--uninstall", action="store_true", help="移除语言包")
    args = parser.parse_args()

    target = args.target.resolve()
    if not target.is_dir():
        raise SystemExit(f"[!] 目录不存在: {target}")
    languages = target / "languages"
    dest = languages / NAME

    if args.uninstall:
        if not dest.is_file():
            print("[*] 未安装语言包，无需移除")
            return 0
        dest.unlink()
        print(f"[+] 已移除 {dest}")
        note = languages / "README.txt"
        if note.is_file():
            note.unlink()
        return 0

    if not QM.is_file():
        raise SystemExit(f"[!] 找不到 {QM}，请先运行 tools/build_langpack.py")
    exe = find_exe(target)
    if exe is None:
        print(f"[!] 警告：在 {target} 中未找到 lichii.exe / lichii，请确认目录是否正确")
    else:
        print(f"[*] 找到 {exe}")

    languages.mkdir(parents=True, exist_ok=True)
    if dest.is_file():
        backup = dest.with_suffix(".qm.bak")
        shutil.copy2(dest, backup)
        print(f"[*] 已备份旧语言包 -> {backup.name}")
    shutil.copy2(QM, dest)
    (languages / "README.txt").write_text(NOTE, encoding="utf-8")
    print(f"[+] 已安装 {dest} ({dest.stat().st_size:,} bytes)")
    print("\n下一步：")
    print("  1. 确认 Lichii 已应用外部语言加载补丁（见 patch/README.md 或项目 README）")
    print("  2. 重启 Lichii")
    print("  3. 设置 -> 界面 -> 语言，选择 Chinese (China) / 中文(中国)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
