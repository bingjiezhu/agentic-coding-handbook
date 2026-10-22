# Agentic Coding Handbook

**Vibe Coding in Practice · Vibe Coding 实战**

A practical guide to turning ideas into verifiable results with AI coding agents.

[简体中文](README.zh-CN.md) · English

Learn how to define a task, research existing solutions, build in small steps, verify real behavior, and keep useful project knowledge across sessions. The handbook also covers independent review, multiple agents, reusable Skills and batch work.

By **[Bingjie Zhu · 朱炳杰](https://github.com/bingjiezhu)**. Available in English and Simplified Chinese, with twelve matching chapters, thirteen copyable prompts per language and translated diagrams.

## Start learning

| Edition | Read on GitHub | Download PDF | Copy the prompts |
| --- | --- | --- | --- |
| English | [Reading guide](docs/en/README.md) | [English PDF](pdf/vibe-coding-in-practice-en.pdf) | [13 prompts](prompts/en.md) |
| 简体中文 | [阅读目录](docs/zh/README.md) | [中文 PDF](pdf/vibe-coding-in-practice-zh.pdf) | [13 条提示词](prompts/zh.md) |

New to coding agents? Start with the [overview](docs/en/00-overview.md), then read chapters 1, 3, 5 and 6 for a complete task. Use the other chapters when the corresponding problem arises; you do not need every tool or workflow before starting.

The guide is for learners, researchers, designers and developers working with tools such as Codex or Claude Code. A coding agent needs access to your project and appropriate tools to execute a task. You remain responsible for choosing the goal and checking the result.

## How to use a prompt

1. Choose the chapter for your current task. In the PDF, copy all the text below the title in its large shaded box. On GitHub, copy the chapter's `text` code block or use the [prompt collection](prompts/en.md).
2. Replace the square-bracketed placeholders with your project, requirements and allowed scope. Say when something is unknown rather than inventing it.
3. Open the project in your coding agent, paste the completed prompt, and inspect the actual files, behavior and check results afterward.

For example, replace `[goal]` with “Add a to-do item and keep it after refreshing the page.” A prompt guides the work; tools, permissions, clear requirements and actual verification determine whether the task can be completed.

## Chapters

| # | English | 简体中文 |
| --- | --- | --- |
| 1 | [Turn an idea into an actionable task](docs/en/01-define-the-task.md) | [把想法变成可执行的任务](docs/zh/01-define-the-task.md) |
| 2 | [Connect project files and responsibilities](docs/en/02-project-files.md) | [项目文件怎样分工和衔接](docs/zh/02-project-files.md) |
| 3 | [Understand the project before changing it](docs/en/03-research-first.md) | [先读懂项目，再决定怎么改](docs/zh/03-research-first.md) |
| 4 | [Connect specs and execution with Spec Kit](docs/en/04-spec-kit.md) | [用 Spec Kit 串起文件与执行](docs/zh/04-spec-kit.md) |
| 5 | [Build in small steps and give specific feedback](docs/en/05-small-steps.md) | [小步实现，给出具体反馈](docs/zh/05-small-steps.md) |
| 6 | [Judge completion through actual use](docs/en/06-acceptance-checks.md) | [从实际使用判断是否完成](docs/zh/06-acceptance-checks.md) |
| 7 | [Diagnose before changing code](docs/en/07-debugging.md) | [出错时，先定位再修改](docs/zh/07-debugging.md) |
| 8 | [Split independent work across agents](docs/en/08-multiple-agents.md) | [多智能体：把独立工作拆开](docs/zh/08-multiple-agents.md) |
| 9 | [Get an independent agent review](docs/en/09-independent-review.md) | [让另一名智能体独立审查](docs/zh/09-independent-review.md) |
| 10 | [Resume long tasks reliably](docs/en/10-long-tasks.md) | [长任务怎样可靠地接着做](docs/zh/10-long-tasks.md) |
| 11 | [Turn effective methods into rules and Skills](docs/en/11-rules-and-skills.md) | [把有效做法写成规则和技能](docs/zh/11-rules-and-skills.md) |
| 12 | [Pilot repeated work before scaling up](docs/en/12-batch-work.md) | [重复任务先小批试跑，再扩大](docs/zh/12-batch-work.md) |

## Sources and translation

The methods draw on primary engineering sources, including DORA, Google SRE, AWS and official tool documentation. [References and scope](REFERENCES.md) explain which sources support which practices. Tool commands and loading behavior depend on the installed version and configuration.

The English edition translates the current Chinese text, including the prompt constraints and figure labels. See the [translation notes and terminology](TRANSLATION.md). Neither edition promises that a prompt succeeds on every project or model.

## Build and contribute

- [Build instructions](BUILDING.md): XeLaTeX sources, fonts, Markdown export and verification.
- [Contributing](CONTRIBUTING.md): report unclear explanations, translation errors or outdated tool details.
- `src/zh/` and `src/en/`: editable LaTeX sources.
- `docs/` and `prompts/`: generated reading pages and prompt collections.
- `assets/diagrams/`: Chinese and English diagrams; `pdf/`: downloadable editions.

Found something confusing? [Open an issue](https://github.com/bingjiezhu/agentic-coding-handbook/issues) with the chapter, language and suggested improvement.

## License

Copyright © 2026 Bingjie Zhu (朱炳杰). The handbook, translations, prompts and original illustrations are shared under **[CC BY 4.0](LICENSE)**. Credit the author, link the license and indicate changes. Build and export scripts are under the [MIT License](LICENSE-CODE). Linked third-party materials retain their own licenses.
