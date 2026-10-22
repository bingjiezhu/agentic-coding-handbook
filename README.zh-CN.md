# Agentic Coding Handbook

**Vibe Coding 实战 · Vibe Coding in Practice**

用 AI 编程智能体，把想法逐步做成可以检查、可以使用的结果。

简体中文 · [English](README.md)

这份教程介绍怎样说清需求、调研已有方案、小步实现、实际验收，以及保存项目资料和进度。后半部分还包括独立审查、多智能体协作、规则与 Skill、重复任务的批量处理。

作者：**[朱炳杰 · Bingjie Zhu](https://github.com/bingjiezhu)**。中英文各有十二章、十三条可复制提示词，图表也有对应翻译。

## 从这里开始

| 版本 | GitHub 在线阅读 | 下载 PDF | 复制提示词 |
| --- | --- | --- | --- |
| 简体中文 | [阅读目录](docs/zh/README.md) | [中文 PDF](pdf/vibe-coding-in-practice-zh.pdf) | [13 条提示词](prompts/zh.md) |
| English | [Reading guide](docs/en/README.md) | [English PDF](pdf/vibe-coding-in-practice-en.pdf) | [13 prompts](prompts/en.md) |

初次使用编程智能体，可以先看[工作框架](docs/zh/00-overview.md)，再读第 1、3、5、6 章，走完一次“说需求—查方案—做出来—检查结果”的过程。其他章节遇到对应问题时再用，不必一开始就安装所有工具、走完所有流程。

适合希望使用 Codex、Claude Code 等工具学习和做项目的学生、研究者、设计师与开发者。执行任务时，工具需要能够访问项目并具备相应能力；目标和最后是否接受结果，由你判断。

## 提示词具体怎么用

1. 按当前任务选一章。PDF 中，复制本章浅色大框里标题下的全部文字；GitHub 页面中，复制对应的 `text` 代码块，也可以直接用[提示词合集](prompts/zh.md)。
2. 把方括号替换为自己的项目位置、要求和允许修改范围。不清楚的地方直接说明，不用猜填。
3. 在编程智能体中打开项目，粘贴并发送，完成后查看实际文件、操作结果与检查记录。

例如，把 `[目标]` 换成“添加待办事项，刷新后仍能看到”。提示词帮助交代工作，能否完成仍要看材料、工具和实际检查。

## 十二章目录

| 章 | 内容 |
| --- | --- |
| 1 | [把想法变成可执行的任务](docs/zh/01-define-the-task.md) |
| 2 | [项目文件怎样分工和衔接](docs/zh/02-project-files.md) |
| 3 | [先读懂项目，再决定怎么改](docs/zh/03-research-first.md) |
| 4 | [用 Spec Kit 串起文件与执行](docs/zh/04-spec-kit.md) |
| 5 | [小步实现，给出具体反馈](docs/zh/05-small-steps.md) |
| 6 | [从实际使用判断是否完成](docs/zh/06-acceptance-checks.md) |
| 7 | [出错时，先定位再修改](docs/zh/07-debugging.md) |
| 8 | [多智能体：把独立工作拆开](docs/zh/08-multiple-agents.md) |
| 9 | [让另一名智能体独立审查](docs/zh/09-independent-review.md) |
| 10 | [长任务怎样可靠地接着做](docs/zh/10-long-tasks.md) |
| 11 | [把有效做法写成规则和技能](docs/zh/11-rules-and-skills.md) |
| 12 | [重复任务先小批试跑，再扩大](docs/zh/12-batch-work.md) |

## 依据与翻译

核心方法参考 DORA、Google SRE、AWS 以及工具官方文档，具体见[资料来源与适用范围](REFERENCES.md)。工具入口和加载机制需要以安装版本、实际配置为准。

英文按当前中文定稿翻译，保留提示词中的条件与限制，不另加效果承诺。术语对应见[翻译说明](TRANSLATION.md)。公开版中文沿用已确认内容，不重新改写正文。

## 源码与参与改进

- [构建说明](BUILDING.md)：编译 PDF、生成在线阅读版和提示词、运行检查。
- [贡献方式](CONTRIBUTING.md)：反馈看不懂的段落、翻译错误或过时的工具说明。
- `src/zh/`、`src/en/`：可编辑的 LaTeX 源文件。
- `docs/`、`prompts/`：由源码生成的在线阅读版和提示词。
- `assets/diagrams/`：中英文图表；`pdf/`：两种语言的下载版。

如果某段看不懂，欢迎[提交 Issue](https://github.com/bingjiezhu/agentic-coding-handbook/issues)，写明章节、语言和你的建议。

## 转载与使用

Copyright © 2026 朱炳杰（Bingjie Zhu）。教程、翻译、提示词和原创插图采用 **[CC BY 4.0](LICENSE)**：允许注明作者后分享、翻译和改编，请附授权链接并说明修改。构建与导出脚本采用 [MIT License](LICENSE-CODE)。引用链接指向的第三方材料遵循各自授权。
