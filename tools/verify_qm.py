#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verify that dist/zh_CN.qm is a real, loadable Qt translation.

Run with a Python that has PySide6/PyQt6 installed, e.g.:
    C:/Users/<you>/AppData/Local/Programs/Python/Python312/python.exe tools/verify_qm.py

It loads the .qm through QTranslator (the same code path Lichii uses) and
checks representative strings, including the ones upstream's Eden-era
translation could never match after the Lichii rename.
"""
from __future__ import annotations

import sys
from pathlib import Path

try:
    from PySide6.QtCore import QCoreApplication, QTranslator
except ImportError:
    raise SystemExit("需要 PySide6：pip install PySide6（或 Qt 6 的 PyQt6）")

ROOT = Path(__file__).resolve().parent.parent
QM = ROOT / "dist" / "zh_CN.qm"

CASES = [
    ("AboutDialog", "About Lichii", None, "关于 Lichii"),
    ("ConfigureDialog", "Lichii Configuration", None, "Lichii 设置"),
    ("MainWindow", "Lichii", None, "Lichii"),
    ("MainWindow", "Are you sure you want to close Lichii?", None, None),
    ("ConfigureUi", "Screenshots Path: ", None, "截图保存位置： "),
    ("NupEditDialog", "Chinese (Simplified)", None, "简体中文"),
    ("ShaderWarmDialog", "Reading game files", None, "正在读取游戏文件"),
    ("ConfigurationShared", "Ask", None, "询问"),
    ("IconSearch", "Find Icon", None, "查找图标"),
    ("UpdateDialog", "Skip This Version", None, "跳过此版本"),
]


def main() -> int:
    if not QM.is_file():
        raise SystemExit(f"[!] 找不到 {QM}，请先运行 tools/build_langpack.py")
    app = QCoreApplication(sys.argv)
    translator = QTranslator()
    if not translator.load(str(QM)):
        raise SystemExit("[!] QTranslator 无法加载 zh_CN.qm（文件损坏或 Qt 版本不兼容）")
    app.installTranslator(translator)
    print(f"[+] 已加载 {QM.name} ({QM.stat().st_size:,} bytes)")

    passed = 0
    for context, source, disambiguation, expected in CASES:
        actual = translator.translate(context, source, disambiguation, -1)
        status = "OK" if actual else "MISS"
        if expected and actual == expected:
            passed += 1
            status = "OK(精确)"
        elif actual and actual != source:
            passed += 1
        print(f"  [{status:8}] {context}.{source[:46]!r} -> {actual[:60]!r}")
    print(f"\n[*] 命中 {passed}/{len(CASES)} 条抽检")
    return 0 if passed >= len(CASES) - 1 else 1


if __name__ == "__main__":
    sys.exit(main())
