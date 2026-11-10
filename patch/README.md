# external-language-loader.patch

一个极小的上游源码补丁，让 Lichii 把 `<程序目录>/languages/*.qm` 当作可插拔语言包。

## 改了什么

| 文件 | 改动 |
|---|---|
| `src/yuzu/main_window.cpp` | 新增 `#include <QCoreApplication>`；`MainWindow::LoadTranslation()` 先从外部目录加载 `.qm`，失败再回退内置的 `:/languages/` |
| `src/yuzu/configuration/configure_ui.cpp` | `ConfigureUi::InitializeLanguageComboBox()` 同时枚举内置资源与外部目录的 `.qm`，用 `findData(locale)` 去重 |

补丁**不改**默认语言、不改设置存储、不改模拟核心、不强制 `ENABLE_QT_TRANSLATION`。
外部目录不存在时，`QDirIterator` 不会产生条目，行为与打补丁前一致。

## 应用方式

推荐用项目脚本（不需要 git 仓库，自动备份、幂等）：

```bash
python tools/apply_patch.py --source /path/to/Lichii --check   # 先检查锚点
python tools/apply_patch.py --source /path/to/Lichii           # 应用
python tools/apply_patch.py --source /path/to/Lichii --revert  # 还原
```

或在干净的 git 检出里直接：

```bash
git apply patch/external-language-loader.patch
```

文件被改动前会生成同目录的 `*.zhcn-orig` 备份。

## 兼容性

- diff 基于 `nx2` 分支 2026-11-09 快照生成，行号见 patch 文件。
- 若上游改了这两个函数，脚本的「锚点未匹配」会阻止半吊子应用；此时用
  `python tools/apply_patch.py --source <你的源码> --make-diff` 重新生成 diff，
  或对照本文件手工合并。
- 手工合并后请确认新代码里含有 `Lichii-zhCN:` 标记注释，脚本据此判断已打补丁。

## 编译

按上游 `docs/Build.md` 正常编译即可，**不需要** `-DENABLE_QT_TRANSLATION=ON`：
补丁走文件系统加载，与 CMake 的翻译开关无关。

## 审阅要点

- `QCoreApplication::applicationDirPath()` 在 Linux 便携版/AppImage 下同样指向可执行文件所在目录；
- `translator.load(locale, dir)` 的 `dir` 参数沿用上游 `":/languages/"` 的带尾斜杠写法；
- 系统区域设置（`<系统>`）路径同样先试外部目录，再回退内置资源；
- 下拉框用 `findData` 去重，避免内置 `en.qm` 与已添加的 `English` 重复。
