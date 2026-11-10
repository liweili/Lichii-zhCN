# 更新日志

## v0.1.0 (2026-11-09)

首个可用版本，对应上游 `zortos293/Lichii` 的 `nx2` 分支快照。

- 基于 Qt 6.8.3 `lupdate` 从 Lichii 源码重新提取 **2282 条 / 101 个 context** 的可翻译字符串，解决上游 `zh_CN.ts` 因产品改名导致的译文失配。
- 继承并修正上游 1941 条 Eden 时代译文：`Eden → Lichii` 品牌修正，补上 5 条未完成与 2 条空译。
- 新译 Lichii 特有界面 **348 条**：兼容性报告向导、麦克风设置、NUP 转换与元数据编辑、着色器预缓存、更新器、帧生成状态、Switch 2 图形设置等；最终 **2281 条译文**（仅 1 条空白占位串未译）。
- 新增最小外部语言加载补丁：`MainWindow::LoadTranslation` 与 `ConfigureUi::InitializeLanguageComboBox`，让 `<程序目录>/languages/*.qm` 成为可插拔语言包，并出现在设置下拉里。
- 工具链：`apply_patch.py`（幂等/可还原）、`build_langpack.py`、`refresh_skeleton.py`、`sync_strings.py`、`install.py`、`verify_qm.py`、`make_release.py`、`publish.js`（GitHub 发布）。
- 用 PySide6 6.8.3 的 `QTranslator` 实测 `zh_CN.qm`：10/10 抽检精确命中，0 处占位符不一致。

### 已知限制

- 官方原版 exe 不读取外部语言文件，**首次需应用补丁并编译一次 Lichii**；本项目不提供编译好的主程序。
- 上游新增界面文案需要刷新骨架并补译，否则 Qt 会回退显示英文。
- 语言下拉的显示名由 Qt 的 `QLocale::languageToString` 决定（英文环境下为 `Chinese (China)`），补丁未改动该命名逻辑。
