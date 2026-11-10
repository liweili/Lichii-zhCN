#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Apply / revert the Lichii-zhCN external language loader patch.

The patch is deliberately tiny (two functions + one include):

  * MainWindow::LoadTranslation()       -> look in <app>/languages/*.qm first
  * ConfigureUi::InitializeLanguageComboBox() -> list those packs in the UI

It is applied by exact text substitution rather than `git apply`, so it works
on a source tarball as well as a git checkout. Every operation is idempotent
and the original files are backed up before the first modification.

Usage:
    python tools/apply_patch.py --source /path/to/Lichii
    python tools/apply_patch.py --source /path/to/Lichii --check
    python tools/apply_patch.py --source /path/to/Lichii --revert
    python tools/apply_patch.py --make-diff       # regenerate patch/*.patch
"""
from __future__ import annotations

import argparse
import difflib
import shutil
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PATCH_DIR = PROJECT_ROOT / "patch"
BACKUP_SUFFIX = ".zhcn-orig"

INCLUDE_OLD = """#include <QClipboard>
#include <QDesktopServices>"""
INCLUDE_NEW = """#include <QClipboard>
#include <QCoreApplication>
#include <QDesktopServices>"""

LOAD_TRANSLATION_OLD = """void MainWindow::LoadTranslation() {
    bool loaded;

    if (UISettings::values.language.GetValue().empty()) {
        // If the selected language is empty, use system locale
        loaded = translator.load(QLocale(), {}, {}, QStringLiteral(":/languages/"));
    } else {
        // Otherwise load from the specified file
        loaded = translator.load(QString::fromStdString(UISettings::values.language.GetValue()),
                                 QStringLiteral(":/languages/"));
    }

    if (loaded)
        qApp->installTranslator(&translator);
    else
        UISettings::values.language = std::string("en");
}"""

LOAD_TRANSLATION_NEW = """void MainWindow::LoadTranslation() {
    // Lichii-zhCN: language packs in <app>/languages take priority over the
    // translations embedded in :/languages/. Upstream defaults
    // ENABLE_QT_TRANSLATION to OFF, so an unpacked .qm is the only way to add
    // or update a language without rebuilding the whole emulator.
    const QString external_dir =
        QCoreApplication::applicationDirPath() + QStringLiteral("/languages");

    bool loaded;
    if (UISettings::values.language.GetValue().empty()) {
        // If the selected language is empty, use system locale
        loaded = translator.load(QLocale(), {}, {}, external_dir + QStringLiteral("/"));
        if (!loaded) {
            loaded = translator.load(QLocale(), {}, {}, QStringLiteral(":/languages/"));
        }
    } else {
        // Otherwise load from the specified file
        const QString locale =
            QString::fromStdString(UISettings::values.language.GetValue());
        loaded = translator.load(locale, external_dir + QStringLiteral("/"));
        if (!loaded) {
            loaded = translator.load(locale, QStringLiteral(":/languages/"));
        }
    }

    if (loaded)
        qApp->installTranslator(&translator);
    else
        UISettings::values.language = std::string("en");
}"""

LANGUAGE_COMBO_OLD = """void ConfigureUi::InitializeLanguageComboBox() {
    ui->language_combobox->addItem(tr("<System>"), QString{});
    ui->language_combobox->addItem(tr("English"), QStringLiteral("en"));
    QDirIterator it(QStringLiteral(":/languages"), QDirIterator::NoIteratorFlags);
    while (it.hasNext()) {
        QString locale = it.next();
        locale.truncate(locale.lastIndexOf(QLatin1Char{'.'}));
        locale.remove(0, locale.lastIndexOf(QLatin1Char{'/'}) + 1);
        const QString lang = QLocale::languageToString(QLocale(locale).language());
        const QString country = QLocale::territoryToString(QLocale(locale).territory());
        ui->language_combobox->addItem(QStringLiteral("%1 (%2)").arg(lang, country), locale);
    }
"""

LANGUAGE_COMBO_NEW = """void ConfigureUi::InitializeLanguageComboBox() {
    ui->language_combobox->addItem(tr("<System>"), QString{});
    ui->language_combobox->addItem(tr("English"), QStringLiteral("en"));

    // Lichii-zhCN: also list .qm files dropped into <app>/languages, so a
    // language pack shows up in this combo without rebuilding the emulator.
    const auto collect_locales = [this](const QString& path) {
        QDirIterator it(path, QDirIterator::NoIteratorFlags);
        while (it.hasNext()) {
            QString locale = it.next();
            if (!locale.endsWith(QStringLiteral(".qm"), Qt::CaseInsensitive)) {
                continue;
            }
            locale.truncate(locale.lastIndexOf(QLatin1Char{'.'}));
            locale.remove(0, locale.lastIndexOf(QLatin1Char{'/'}) + 1);
            if (locale.isEmpty() || ui->language_combobox->findData(locale) >= 0) {
                continue;
            }
            const QString lang = QLocale::languageToString(QLocale(locale).language());
            const QString country = QLocale::territoryToString(QLocale(locale).territory());
            ui->language_combobox->addItem(QStringLiteral("%1 (%2)").arg(lang, country), locale);
        }
    };
    collect_locales(QStringLiteral(":/languages"));
    collect_locales(QCoreApplication::applicationDirPath() + QStringLiteral("/languages"));
"""

PATCHES = [
    {
        "file": "src/yuzu/main_window.cpp",
        "marker": "// Lichii-zhCN: language packs in <app>/languages take priority",
        "changes": [
            (INCLUDE_OLD, INCLUDE_NEW),
            (LOAD_TRANSLATION_OLD, LOAD_TRANSLATION_NEW),
        ],
    },
    {
        "file": "src/yuzu/configuration/configure_ui.cpp",
        "marker": "// Lichii-zhCN: also list .qm files dropped into",
        "changes": [(LANGUAGE_COMBO_OLD, LANGUAGE_COMBO_NEW)],
    },
]


def build_diff(text: str, patched: str, rel_path: str) -> str:
    old_lines = text.splitlines(keepends=True)
    new_lines = patched.splitlines(keepends=True)
    diff = difflib.unified_diff(
        old_lines, new_lines,
        fromfile=f"a/{rel_path}", tofile=f"b/{rel_path}", n=3,
    )
    return "".join(diff)


def make_diff(root: Path) -> int:
    """Regenerate a reviewable, `git apply`-compatible .patch from pristine sources."""
    PATCH_DIR.mkdir(parents=True, exist_ok=True)
    out = PATCH_DIR / "external-language-loader.patch"
    chunks = [
        "# Lichii-zhCN external language loader\n",
        "# Generated by: python tools/apply_patch.py --source <Lichii> --make-diff\n",
        "# Apply with:   git apply patch/external-language-loader.patch\n",
        "# (or just run  python tools/apply_patch.py --source <Lichii> )\n\n",
    ]
    for entry in PATCHES:
        path = root / entry["file"]
        if not path.is_file():
            raise SystemExit(f"[!] 找不到上游文件: {path}")
        text = path.read_text(encoding="utf-8")
        patched = text
        for old, new in entry["changes"]:
            if old not in patched:
                raise SystemExit(f"[!] 锚点未匹配，无法生成 diff: {entry['file']}")
            patched = patched.replace(old, new, 1)
        chunks.append(build_diff(text, patched, entry["file"]))
    out.write_text("".join(chunks), encoding="utf-8")
    print(f"[+] {out}")
    return 0


def process(entry: dict, root: Path, check: bool, revert: bool) -> tuple[bool, str]:
    rel = entry["file"]
    path = root / rel
    backup = path.with_name(path.name + BACKUP_SUFFIX)

    if not path.is_file():
        return False, f"文件不存在: {path}"

    if revert:
        if not backup.is_file():
            return True, f"无需还原（无备份）: {rel}"
        if check:
            return True, f"可还原: {rel}"
        shutil.copy2(backup, path)
        return True, f"已还原: {rel}"

    text = path.read_text(encoding="utf-8")
    if entry["marker"] in text:
        return True, f"已打过补丁，跳过: {rel}"

    patched = text
    for old, new in entry["changes"]:
        if old not in patched:
            return False, (f"锚点未匹配: {rel}\n"
                           f"    上游代码可能已变化。请对照 patch/external-language-loader.patch 手工合并，\n"
                           f"    或在 Lichii 的 nx2 分支对应提交上运行本工具。")
        patched = patched.replace(old, new, 1)

    if check:
        return True, f"可应用: {rel}"

    if not backup.is_file():
        shutil.copy2(path, backup)
    path.write_text(patched, encoding="utf-8")
    return True, f"已打补丁（原文件备份为 {path.name}{BACKUP_SUFFIX}）: {rel}"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, help="Lichii 源码根目录")
    parser.add_argument("--check", action="store_true", help="只检查，不修改")
    parser.add_argument("--revert", action="store_true", help="从备份还原")
    parser.add_argument("--make-diff", action="store_true", help="从干净上游源码重新生成可审阅的 .patch（需 --source）")
    args = parser.parse_args()

    if not args.source:
        parser.error("需要 --source")
    root = args.source.resolve()
    if not root.is_dir():
        raise SystemExit(f"[!] 源码目录不存在: {root}")
    if args.make_diff:
        return make_diff(root)

    ok = True
    for entry in PATCHES:
        success, message = process(entry, root, args.check, args.revert)
        print(("[+] " if success else "[!] ") + message)
        ok &= success
    if not ok:
        print("\n补丁未完整应用。请勿在半补丁状态下编译。")
        return 1
    if not args.check and not args.revert:
        print("\n下一步：用 -DENABLE_QT_TRANSLATION=OFF 正常编译 Lichii，"
              "再把 langpack 的 zh_CN.qm 放到 lichii.exe 同级的 languages/ 目录。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
