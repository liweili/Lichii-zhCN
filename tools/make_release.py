#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pack an end-user zip: drop it next to lichii.exe and pick Chinese in Settings.

    python tools/make_release.py [--version 0.1.0]
"""
from __future__ import annotations

import argparse
import zipfile
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RELEASE = ROOT / "release"

INSTALL_GUIDE = """Lichii 中文语言包 —— 安装说明
================================

【最简用法】（适用于已内置外部语言加载补丁的 Lichii 构建）
  1. 把本压缩包里的 languages 文件夹解压到 Lichii 程序目录
     （即 lichii.exe 所在的目录）。
  2. 重启 Lichii。
  3. 打开「设置 -> 界面 -> 语言」，选择 Chinese (China) / 中文(中国)。
  界面会立即切换为简体中文，无需重新编译。

【官方原版 Lichii 为什么不能直接生效】
  上游把 .qm 语言文件编译进 exe 内部的 Qt 资源(:/languages/)，
  并且 CMake 选项 ENABLE_QT_TRANSLATION 默认是 OFF，官方发布构建
  也没有打开它。因此原版程序的语言下拉里只有「<系统>」和「English」，
  而且它不会去读程序目录下的任何语言文件。

  要让语言包可插拔，需要给源码打一次最小补丁（两处函数 + 一个 include）：
     patch/external-language-loader.patch
  打补丁后编译一次 Lichii，之后更新/更换语言包只需替换 .qm 文件。
  详细步骤见项目 README.md 与 docs/技术原理.md。

【文件清单】
  languages/zh_CN.qm                      编译好的简体中文语言包
  languages/README.txt                    目录说明
  patch/external-language-loader.patch    上游源码补丁（git apply 可用）
  README.md / CHANGELOG.md / LICENSE.txt  项目说明与许可

【更新语言包】
  替换 languages/zh_CN.qm 并重启 Lichii 即可。
"""

LANG_README = """把 zh_CN.qm 保留在此目录（lichii.exe 同级的 languages 文件夹）。
在 Lichii「设置 -> 界面 -> 语言」中选择 Chinese (China) 即可启用。
更新语言包：替换本文件并重启 Lichii。
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", default="0.1.0")
    args = parser.parse_args()

    qm = ROOT / "dist" / "zh_CN.qm"
    if not qm.is_file():
        raise SystemExit("[!] 缺少 dist/zh_CN.qm，请先运行 tools/build_langpack.py")

    RELEASE.mkdir(parents=True, exist_ok=True)
    out = RELEASE / f"Lichii-zhCN-v{args.version}.zip"
    stamp = date.today().isoformat()

    files = {
        "languages/zh_CN.qm": qm.read_bytes(),
        "languages/README.txt": LANG_README.encode("utf-8"),
        "安装说明.txt": INSTALL_GUIDE.replace("{DATE}", stamp).encode("utf-8"),
        "patch/external-language-loader.patch": (ROOT / "patch/external-language-loader.patch").read_bytes(),
    }
    for name in ("README.md", "CHANGELOG.md", "LICENSE.txt"):
        path = ROOT / name
        if path.is_file():
            files[name] = path.read_bytes()

    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for name, data in files.items():
            zf.writestr(name, data)
    print(f"[+] {out} ({out.stat().st_size:,} bytes)")
    for name in files:
        print(f"    {name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
