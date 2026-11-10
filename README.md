# Lichii-zhCN · Lichii 简体中文语言包（可插拔插件）

给 [zortos293/Lichii](https://github.com/zortos293/Lichii)（实验性 Nintendo Switch / Switch 2 模拟器）做的**简体中文界面语言包**。目标：在「设置 → 界面 → 语言」下拉里能直接选到中文，并且**换翻译只需替换一个文件、重启即可**，不必重新编译模拟器。

> 当前对应上游分支：`nx2`（2026-11-09 快照）。语言包版本 `v0.1.0`。
>
> 项目地址：<https://github.com/liweili/Lichii-zhCN> · 成品包见 [Releases](https://github.com/liweili/Lichii-zhCN/releases)。

---

## 一、为什么需要这个项目

调研上游仓库后发现的三个事实：

| 现象 | 原因 |
|---|---|
| 官方 exe 的语言下拉里只有 `<系统>` 和 `English` | `CMakeLists.txt:75` 的 `ENABLE_QT_TRANSLATION` 默认 **OFF**，Release 工作流也没有打开它 |
| 把 `.qm` 放到程序目录里没反应 | `MainWindow::LoadTranslation()` 只从 `:/languages/`（编译进 exe 的 Qt 资源）加载 |
| 就算开了翻译，很多界面仍是英文 | 上游 `dist/languages/zh_CN.ts` 是 Eden 时代的：Lichii 把源码里的 `About Eden` 改名成 `About Lichii`、并新增了兼容性报告 / 麦克风 / NUP 等面板；Qt 按**英文原文**查找译文，改名和新增的条目全部失配 |

所以「中文插件」= **一份重做过的 `zh_CN.qm` + 一段极小的外部加载补丁**。

补丁只改 2 个函数、加 1 个 include：

- `MainWindow::LoadTranslation()`：优先读 `<程序目录>/languages/<locale>.qm`，失败再回退内置资源；
- `ConfigureUi::InitializeLanguageComboBox()`：下拉框同时枚举内置资源和 `<程序目录>/languages/*.qm`，并按 locale 去重。

不改变默认行为、不改设置项、不碰模拟核心，也不强制开启 `ENABLE_QT_TRANSLATION`。

---

## 二、快速开始

### 情况 A：你手上的 Lichii 已经内置了这个补丁

1. 从 [GitHub Releases](https://github.com/liweili/Lichii-zhCN/releases) 下载 `Lichii-zhCN-v0.1.0.zip`（本仓库 `release/` 下也有同一份），把里面的 `languages/` 文件夹解压到 **lichii.exe 同级目录**；
   或本地运行：
   ```bash
   python tools/install.py --target "D:/Lichii"
   ```
2. 重启 Lichii → 设置 → 界面 → 语言 → 选 `Chinese (China)`（中文系统下显示为`中文(中国)`）。
3. 以后更新汉化，只替换 `languages/zh_CN.qm` 再重启。

### 情况 B：官方原版 Lichii（首次需要编译一次）

原版程序不会读取外部文件，因此**必须打一次补丁并编译一次**。之后就是情况 A。

```bash
# 1. 取源码（按上游 docs/Build.md 准备 Qt 6 / clang / Vulkan SDK 等依赖）
git clone --depth 1 -b nx2 https://github.com/zortos293/Lichii.git
cd Lichii

# 2. 打补丁（二选一）
python <本项目>/tools/apply_patch.py --source .
# 或： git apply <本项目>/patch/external-language-loader.patch

# 3. 按上游官方构建指南正常编译（无需开 ENABLE_QT_TRANSLATION）
#    参考 https://github.com/zortos293/Lichii/blob/nx2/docs/Build.md
cmake --build build --parallel
```

补丁是幂等的，会为两个源文件生成 `.zhcn-orig` 备份；`--check` 只检查、`--revert` 可还原。

> 本项目**不提供**编译好的 Lichii 主程序，也不修改任何上游二进制。
> 如果你从社区拿到已打补丁的构建，可直接跳到情况 A。

---

## 三、语言包数据

| 项目 | 数值 |
|---|---|
| 上游 `dist/languages/zh_CN.ts` | 1941 条（Eden 时代，5 条未译） |
| `lupdate` 从 `nx2` 源码重新提取 | **2282 条 / 101 个 context** |
| 继承并修正上游译文 | 1933 条（含 `Eden → Lichii` 品牌修正） |
| 新译 Lichii 新增界面文案 | 348 条（含 67 条长句补遗） |
| 最终已译 | **2281 条（约 100%）**，剩余 1 条为空白占位串 |
| `dist/zh_CN.qm` | 239,493 字节 |
| 工具链 | Qt **6.8.3** `lupdate` / `lrelease`（与 Lichii 一致） |
| 验证 | `QTranslator` 实测加载，10/10 抽检精确命中，0 处占位符错误 |

已覆盖 Lichii 特有界面：兼容性报告向导、麦克风设置、NUP 转换/元数据编辑、着色器预缓存对话框、更新器、帧生成状态提示、Switch 2 相关设置项等。

---

## 四、目录结构

```
Lichii-zhCN/
├─ README.md                    本文件
├─ CONTRIBUTING.md              译文维护与上游合规约定
├─ CHANGELOG.md
├─ LICENSE.txt                  许可说明
├─ lang/
│  ├─ zh_CN.ts                  最终可编译的中文语言包源（编译产物见 dist/）
│  ├─ baseline.zh_CN.ts         上游 nx2 原始 zh_CN.ts 快照（审计用）
│  ├─ lichii_source.ts          lupdate 从源码生成的权威骨架（location 已规范化为 src/...）
│  ├─ translations.json         source → 中文 词库（与 context 解耦）
│  ├─ additions.zh.txt          481 条新增文案译文（按 missing 序号）
│  ├─ extras.zh.json            67 条补遗译文（按英文原文索引，构建用）
│  └─ extras.zh.txt             补遗译文的人工编辑底稿
├─ dist/zh_CN.qm                编译产物，即「插件」本体
├─ patch/
│  ├─ external-language-loader.patch   可 git apply 的统一 diff
│  └─ README.md
├─ tools/
│  ├─ apply_patch.py            幂等打补丁 / 还原 / 生成 diff
│  ├─ build_langpack.py         合并译文 → zh_CN.ts → lrelease → zh_CN.qm
│  ├─ refresh_skeleton.py       Lichii 升级后用 lupdate 刷新骨架（自动清洗 location）
│  ├─ sync_strings.py           静态扫描源码，报告未覆盖字符串
│  ├─ install.py                安装 / 卸载 qm 到 Lichii 程序目录
│  ├─ verify_qm.py              用 QTranslator 实测 QM
│  ├─ make_release.py           打最终 zip
│  └─ publish.js                维护者发布到 GitHub（凭据由环境变量传入）
├─ docs/                        技术原理、使用说明、扫描报告
└─ release/Lichii-zhCN-v0.1.0.zip
```

---

## 五、维护者：改译文 / 跟进上游

```bash
# 改译文：改 lang/translations.json（权威词库）或 lang/extras.zh.json
python tools/build_langpack.py                       # 重生成 .ts + .qm

# 用 Qt 验证（需要装 PySide6 的 Python）
<python-with-pyside6> tools/verify_qm.py

# 静态审计：当前源码有哪些字符串没被覆盖
python tools/sync_strings.py --source /path/to/Lichii \
       --json docs/missing-strings.json --report docs/missing-strings.md

# Lichii 升级后：刷新骨架再重建（旧译文由 translations.json 自动沿用）
python tools/refresh_skeleton.py --source /path/to/Lichii
python tools/build_langpack.py

# 打发布包
python tools/make_release.py --version 0.1.0
```

`build_langpack.py` 的合并优先级：
`(context, source)` 精确匹配 → `source` 匹配 → `Eden→Lichii` 归一化匹配 → 历史词库 / 新增译文表 / 补遗表（均以英文原文为键）→ 留空（显示英文）。空白占位串不参与匹配，避免长句被误配到它上面。
它会校验 `%1` / `%2` / `%n` / `%L1` 等占位符是否一致，并保留 `<comment>`（Qt 的消歧键，丢了会导致翻译不命中）。

`lrelease` 找不到时会自动探测 `lrelease` / `pyside6-lrelease` / PySide6 包内二进制，也可用 `--lrelease` 指定；没有 Qt 环境时仍可用 `--no-qm` 只生成 `.ts`，交给 Qt Linguist 处理。

---

## 六、合规与上游关系

- Lichii 及其界面源码为 **GPL-3.0-or-later**（见上游 `LICENSE.txt` 与源文件 SPDX 头）。本项目提供的补丁同样以 GPL-3.0-or-later 提供。
- 译文基础来自上游 `dist/languages/zh_CN.ts`，该目录由 [Eden 的 Transifex 项目](https://app.transifex.com/edenemu/eden-emulator) 同步；上游 `dist/languages/README.md` 要求译文贡献走 Transifex，且明确「暂不受理新语言请求」。
- 上游 `CONTRIBUTING.md` 指明 Issue / PR 提交到 `zortos293/eglantine`，并要求改动聚焦、说明测试内容。
- **本项目是独立的第三方语言包，不擅自向上游仓库提交 Issue / PR，也不改上游仓库文件。** 若要把改进回馈上游，请按上述 Transifex 流程与贡献规范自行提交。
- 本项目不含游戏 ROM、固件、密钥、prod.keys 或任何受版权保护的任天堂资源，仅包含界面文字翻译。
- Lichii 名称与标识归其各自权利人所有；本项目与其无隶属关系。

详见 `CONTRIBUTING.md` 与 `docs/合规说明.md`。

---

## 七、常见问题

**Q：下拉里看不到中文？**
确认三件事：① 用的 Lichii 已应用补丁；② `zh_CN.qm` 在 **lichii.exe 同级**的 `languages/` 目录里；③ 文件名正好是 `zh_CN.qm`（locale 由文件名决定）。

**Q：部分文字还是英文？**
这是 Qt 的正常回退：未收录的字符串显示英文原文。本项目对当前 `nx2` 快照覆盖约 100%；若上游新增了文案，按第五节刷新骨架并补译即可。

**Q：能不能不改源码？**
可以只做「纯语言包」：把 `lang/zh_CN.ts` 放进上游 `dist/languages/`，用 `-DENABLE_QT_TRANSLATION=ON` 自行编译。但这样每次改译文都要重编译，且官方发布版仍选不到中文。

**Q：切换语言后要重启吗？**
不需要。上游 `ConfigureUi` 会发信号让主窗口立即 `retranslateUi`。但**首次放入新 `.qm` 文件**需要重启，因为下拉列表在界面初始化时枚举目录。

---

## 八、许可

本项目补丁与工具：GPL-3.0-or-later。译文数据继承自上游 GPL-3.0-or-later 项目并遵循其贡献约定。详见 `LICENSE.txt`。
