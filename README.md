# 刷题室 · Study Room

[![check](https://github.com/color19/Studyroom/actions/workflows/check.yml/badge.svg)](https://github.com/color19/Studyroom/actions/workflows/check.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Single file](https://img.shields.io/badge/app-single%20HTML%20file-brightgreen)
![No backend](https://img.shields.io/badge/backend-none-lightgrey)
![Offline](https://img.shields.io/badge/works-offline-success)

**适用于任意选择题考试的单文件刷题应用。** 支持 CFA、计算机考研 408、软考、AWS 认证、教师资格、法律职业资格等。
导入自有题库，借助 AI 将讲义转化为知识卡，即可在浏览器中完成练习、间隔复习与计时模考。

- **零部署**：单个 HTML 文件，双击即可运行，无需安装或服务器
- **本地优先**：全部数据仅保存在本地浏览器，不上传至任何服务器
- **考试无关**：科目、权重、题量、时长均可自定义
- **中英双语**：左下角「🌐 中文 / EN」一键切换界面语言

[在线体验](https://color19.github.io/studyroom/) · [数据格式](docs/FORMAT.md) · [AI 流程](docs/AI_PIPELINE.md) · [English](#english)

![学习首页：按考纲权重查看各科持仓，自动指出低配科目](docs/img/home.png)

> [!IMPORTANT]
> 本项目仅提供工具，**不包含任何真题或讲义**。内置的 20 道 CFA 示例题为原创演示内容。请仅使用您合法持有的材料，**限个人学习使用，不得传播**。

---

## 目录

- [功能概览](#功能概览)
- [快速开始](#快速开始)
- [数据准备](#数据准备)
- [适配其他考试](#适配其他考试)
- [AI 知识卡流程](#ai-知识卡流程)
- [项目结构与构建](#项目结构与构建)
- [版权与合规](#版权与合规)
- [参与贡献](#参与贡献)
- [许可证](#许可证)

## 功能概览

| 模块 | 说明 |
|---|---|
| **学习仪表盘** | 以投资组合视角呈现进度：考纲权重为目标仓位，已做题量为实际仓位，薄弱科目一目了然 |
| **章节练习** | 按来源、科目、章节筛选；支持 10 / 20 / 全部题量，随机或顺序作答 |
| **模拟考试** | 整套原卷计时，或按科目权重随机组卷；交卷后生成成绩单与逐题解析 |
| **冲刺计划** | 设定考试日期后，把剩余题目（可选刷 1 至 3 遍，第 3 遍可只刷错题）与全部 Mock 自动排进考前每一天；支持每天多科混合（按考纲权重 × 薄弱程度分配）或按科目专项；最后两天只复习；每天按最新进度自动重排 |
| **错题本与间隔复习** | 错题自动收录，按 1 / 2 / 4 / 7 / 15 天间隔复习；设定考试日期后，复习计划将自动压缩至考前两天完成 |
| **错因分析** | 按概念不清、计算错误、审题失误、粗心四类标记与筛选 |
| **同类题推荐** | 针对错题推送同一知识点下尚未作答的新题 |
| **知识卡** | 每个知识点一张卡片，支持 LaTeX 公式、要点与易错点；作答后随解析展示，可在页面内直接编辑 |
| **考前速览** | 自动汇总最薄弱的知识点及对应卡片，支持打印 |
| **其他** | 暂停与断点续做、作答记录、学习报告、按章节组织的笔记、术语高亮 |

作答后即时显示解析、易错提醒与错因标签，并可一键练习同类新题：

![做题与解析](docs/img/practice.png)

错题本按知识点汇总薄弱环节，点击即可针对性复习：

![错题本：薄弱知识点排行](docs/img/weak.png)

## 快速开始

1. **打开应用**：访问 [color19.github.io/studyroom](https://color19.github.io/studyroom/)，或下载本仓库（Code → Download ZIP）后直接打开 `index.html`。
2. **体验示例**：使用内置示例题熟悉各项功能。
3. **导入题库**：进入「导入题库」页面，上传题目 CSV。科目名称不限，页面内提供模板下载，字段说明见 [docs/FORMAT.md](docs/FORMAT.md)。
4. **导入知识卡（可选）**：参照 [docs/AI_PIPELINE.md](docs/AI_PIPELINE.md) 生成 `cards.json` 后导入。

> [!TIP]
> **跨设备迁移**：在「导入题库」页面底部导出题库与学习记录，在新设备上重新导入即可。

## 数据准备

### 题库（CSV）

使用 **UTF-8** 编码的 CSV 文件，每行一道题，首行为表头：

| 科目 | 来源 | 章节 | 题干 | A | B | C | D | 答案 | 中文解析 |
|---|---|---|---|---|---|---|---|---|---|
| 数据结构 | 408真题 | 线性表 | 顺序表随机访问的时间复杂度是 | O(1) | O(n) | O(log n) | O(n²) | A | 按下标直接定位 |

- **必填字段**：科目、题干、A、B、答案；其余字段可留空。
- 科目名称不限；每题最多 5 个选项；答案填写选项字母。
- 来源名称包含「模考」或「mock」的题目将被识别为整套模拟卷。
- 完整字段定义见 [docs/FORMAT.md](docs/FORMAT.md)。

**从 PDF / Word 转换**：将文件提供给 Claude 或 ChatGPT，并附上以下提示词：

```text
把这份题目整理成 CSV，列为：科目,来源,章节,题干,A,B,C,D,答案,中文解析。
答案只写字母。题干里有逗号或换行的用英文双引号包起来。
逐题提取，不要省略，不要改题目内容。
```

题量较大时建议分批处理（每批数十页），最后合并 CSV。

### 讲义（PDF）

- 建议每个科目一个 PDF；PPT、Word 请先导出为 PDF。
- 文字可选中的 PDF 效果最佳；扫描版同样可用，但 AI 处理较慢。
- 讲义本身无需导入应用，仅作为 AI 生成知识卡的输入；导入的是生成的 `cards.json`。
- 讲义为可选项：仅导入题库时，练习、错题本、复习与模考功能均可正常使用。

## 适配其他考试

| 所需内容 | 获取方式 |
|---|---|
| 题库 | 整理为 CSV（科目、题干、选项、答案、解析），可借助 AI 从 PDF / Word 转换 |
| 知识点目录 | 使用 `prompts/00`，将考纲或讲义目录交给 AI 生成 `taxonomy.json` |
| 知识卡 | 使用 `prompts/01`，将讲义交给 AI，为每个知识点生成卡片 |
| 质量核对 | 使用 `prompts/03`，每张卡匹配 4 道题库原题，与官方答案不符时修正 |
| 考试设置（可选） | 在 `bank.json` 中添加 `exam` 字段：考试名称、科目权重、单场题量、单题时长，详见 [FORMAT.md](docs/FORMAT.md) |

知识卡与知识点目录为增强功能；仅导入题库即可使用全部核心功能。

## AI 知识卡流程

`prompts/` 目录收录了经过实际验证的提示词，配合 `tools/` 中的脚本使用：

| 步骤 | 提示词 | 作用 |
|---|---|---|
| 0 | `00_taxonomy_from_syllabus.md` | 考纲 → 知识点目录（CFA 已内置，可跳过） |
| 1 | `01_cards_from_slides.md` | 讲义 → 知识卡（每个知识点一张） |
| 2 | `02_fill_gaps.md` | 补全讲义未覆盖的知识点（标记为「AI 补充」） |
| 3 | `03_verify_with_questions.md` | **以题库核对知识卡**：每张卡匹配 4 道原题，与官方答案矛盾即修正 |
| 4 | `04_explain_questions_zh.md` | 为题目生成中文讲解并标注知识点 |

> [!NOTE]
> **第 3 步至关重要。** 在 CFA 实测中，AI 初版生成的 633 张卡片中有 105 张存在实质性错误；以原题官方答案逐张核对后，又发现 55 张。基于标准答案的核对远比让 AI 凭记忆自查可靠。请务必人工复核修改清单。

## 项目结构与构建

```text
index.html    可直接使用的构建产物（已提交）
src/app.html  应用源码
build.py      构建脚本；--bank 参数可将个人题库打包为私有文件
sample/       原创示例题库、CFA 一级知识点目录、术语表
prompts/      AI 提示词
tools/        CSV 转换、数据校验、知识卡流水线、LaTeX 检查
docs/         数据格式与 AI 流程文档
vendor/       KaTeX 0.16.11（MIT）
```

修改 `src/app.html` 后重新构建：

```bash
python3 build.py                        # 生成 index.html（仅含示例题，可公开发布）
python3 build.py --bank my/bank.json    # 生成 dist/personal.html（内嵌个人题库，可在手机上离线使用）
```

> [!WARNING]
> `dist/personal.html` 包含您的私有题库，已被 `.gitignore` 排除，请勿提交或分享。

## 版权与合规

- 商业题库、官方真题及培训机构讲义通常受版权保护。本仓库不包含、也不接受任何此类内容的 PR。
- 私有文件请存放于 `my/` 或 `dist/` 目录，二者均已被 `.gitignore` 排除。
- 截图分享时请遮盖题目原文。
- CFA® 与 Chartered Financial Analyst® 为 CFA Institute 的注册商标。本项目与 CFA Institute 及任何考试机构均无关联，亦未获其认可。

## 参与贡献

欢迎通过 Issue 和 Pull Request 参与贡献，包括功能建议与问题修复。

## 关于

本项目由一名金融专业学生在备考 CFA 一级期间与 Claude 协作开发，后应朋友需求改造为可用于其他领域刷题的通用版本并开源。

## 支持

如果刷题室帮到了你，可以点页面左下角（手机上在「导入题库」页底部）的「☕ 请作者喝杯咖啡」，用微信赞赏码请我喝杯咖啡。祝考试顺利！

## 许可证

- 代码：[MIT](LICENSE)
- KaTeX：MIT，见 [`vendor/KATEX_LICENSE`](vendor/KATEX_LICENSE)

---

## English

**Study Room** (刷题室) is a single-file practice app for **any multiple-choice exam**. Import your own question bank (CSV or JSON), generate a knowledge-point taxonomy and review cards from your own lecture notes using the prompts in `prompts/`, then practice, review with spaced repetition, and take timed mock exams, all in the browser. No server, no installation: all data stays in your browser.

**Highlights**

- Progress dashboard that compares actual practice volume against syllabus weights
- Topic practice, timed full-length or weighted-random mock exams with score reports
- Mistake log with spaced repetition (1/2/4/7/15 days), compressed to finish before your exam date
- Knowledge cards with LaTeX, shown alongside explanations and editable in place
- Printable one-page review sheet of your weakest topics
- Bilingual UI: switch between English and 中文 with the 🌐 button (defaults to your browser language)

**Quick start**: open [the live demo](https://color19.github.io/studyroom/) or `index.html`, try the sample questions, then go to 「导入题库」(Import) and load your CSV. Subject names are free-form. See [`docs/FORMAT.md`](docs/FORMAT.md) for the data format and [`docs/AI_PIPELINE.md`](docs/AI_PIPELINE.md) for the card pipeline.

This repository ships **no third-party questions or course material**. The 20 sample questions (CFA Level I style) are original. Use only materials you have legally obtained, for personal study.

CFA® and Chartered Financial Analyst® are registered trademarks owned by CFA Institute. This project is not affiliated with or endorsed by CFA Institute or any exam body.

Licensed under [MIT](LICENSE).
