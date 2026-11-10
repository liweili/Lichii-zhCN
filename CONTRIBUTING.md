# 贡献与合规约定

## 一、这个项目的边界

Lichii-zhCN 是**第三方独立语言包**，不是 Lichii / Eden / yuzu 的官方项目，也不隶属于它们。

- 不直接修改上游仓库，不擅自向 `zortos293/Lichii` 或 `zortos293/eglantine` 提交 Issue / PR；
- 不分发、不修改、不重新打包 Lichii 主程序；
- 不包含游戏 ROM、固件、密钥、`prod.keys` 或任何任天堂受版权保护的资源；
- 补丁以纯文本 diff 提供，用户自行决定是否应用、自行编译。

## 二、上游规范（调研结论，2026-11-09 核对 `nx2` 分支）

| 文档 | 关键要求 |
|---|---|
| `dist/languages/README.md` | 翻译文件与 Eden 的 Transifex 项目同步（`tx pull -t -a`）；译文贡献请到 Transifex 提交；译者须保证译文准确、不含违规内容；**暂不受理新语言请求** |
| `CONTRIBUTING.md` | Issue / PR 提交到 `zortos293/eglantine`；改动保持聚焦；说明测了什么，并区分「编译检查」与「实际游戏测试」；保留原有版权与第三方许可 |
| `.tx/config` | `qt-translations` 资源：`dist/languages/<lang>.ts`，源文件 `dist/languages/en.ts` |
| `AGENTS.md` / `docs/Coding.md` | 编码与协作指引 |
| `CMakeLists.txt:75` | `ENABLE_QT_TRANSLATION` 默认 OFF |

因此，若希望把本项目补译的文案回馈上游，**请自行通过 Transifex（Eden 项目）或按 `CONTRIBUTING.md` 到 `zortos293/eglantine` 提交**，并遵循其模板与审查流程。本项目不代替用户做这一步。

## 三、改译文的正确姿势

1. 权威词库是 `lang/translations.json`（`英文原文 → 中文`），润色已有译文直接改它。
   新增长句译文放 `lang/extras.zh.json`（同样以英文原文为键）；`additions.zh.txt` 按 `docs/missing-strings.json` 的序号维护新增条目。
   `lang/extras.zh.txt` 只是人工编辑底稿，**构建时不读取**，请勿依赖它的行号。
2. 若某条译文来自上游且需要润色，改 `lang/translations.json` 中对应 `source` 的中文；`build_langpack.py` 会把历史词库带回新构建。
3. 运行 `python tools/build_langpack.py`，检查输出里的覆盖率与占位符告警。
4. 运行 `verify_qm.py` 实测，再运行 `make_release.py` 打包。

约束：

- **不要改 `lang/lichii_source.ts` 里的 `<source>`**：它是 `lupdate` 从源码提取的英文原文，Qt 用它做查找键。
- 保留 `%1` / `%2` / `%n` / `%L1` 占位符、`&` 助记符、HTML 标签结构；构建脚本会校验占位符。
- 不要引入与模拟器无关的推广、外链或任何可能被视为夹带内容的文字。
- 产品名统一用 `Lichii`；历史项目名（Eden / Eglantine / yuzu / Sudachi）在描述继承关系时保留。

## 四、源码升级流程

```bash
python tools/refresh_skeleton.py --source /path/to/Lichii   # lupdate 重新提取
python tools/sync_strings.py --source /path/to/Lichii \
       --json docs/missing-strings.json --report docs/missing-strings.md
python tools/build_langpack.py                             # 旧译文自动沿用
```

新出现的英文条目会显示为「未翻译」并出现在 `docs/missing-strings.md`；补进 `additions.zh.txt` 后重建即可。

## 五、提交前自查

- [ ] `python tools/build_langpack.py` 无占位符告警
- [ ] `verify_qm.py` 抽检全部命中
- [ ] `apply_patch.py --check` 在干净上游源码上通过
- [ ] 未把任何密钥、token、个人路径写进 Issue / 提交 / 发布包
- [ ] 发布包内不含 Lichii 主程序与任何游戏资源
