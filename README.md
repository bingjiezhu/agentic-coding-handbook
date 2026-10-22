# Agentic Coding Handbook

**A project guide for Codex, Claude Code and other AI coding agents.**

[简体中文](README.zh-CN.md) · English

Share this repository link with your coding agent. It can use the guide to clarify your idea, research existing solutions, plan with Spec Kit, implement a small version, verify it and keep progress for the next session.

> **AI entry point:** If the user shares this repository as their project method, read [START.md](START.md) and then [the Project Guide skill](skills/project-guide/SKILL.md). Begin guiding their project in the user's language. If the goal is missing, ask what they want to build. Do not stop at summarizing the repository.
>
> Direct text: [raw START.md](https://raw.githubusercontent.com/bingjiezhu/agentic-coding-handbook/main/START.md) · [raw SKILL.md](https://raw.githubusercontent.com/bingjiezhu/agentic-coding-handbook/main/skills/project-guide/SKILL.md)

## Start a project

Send this link to an AI that can read GitHub:

```text
https://github.com/bingjiezhu/agentic-coding-handbook
```

You can include an idea immediately:

```text
Use this guide to help me start a project:
https://github.com/bingjiezhu/agentic-coding-handbook
I want to build a to-do tool that keeps my items after a page refresh.
```

The guide starts from your goal and current project. You do not need to pick a prompt card or remember tool commands.

| Stage | What the AI guide does |
| --- | --- |
| Clarify | Helps define who the project is for, the first useful version and concrete acceptance criteria |
| Research | Checks existing code, reusable tools and alternatives before choosing an architecture |
| Plan | Detects the actual Spec Kit integration and invokes the appropriate installed step |
| Build | Completes a small real workflow, preserves accepted behavior and records failed experiments |
| Verify | Checks actual use against the original requirements and reviews important results |
| Continue | Saves progress, verifies current files after a restart and advances the next useful task |

You choose the goal and important trade-offs. The agent manages the next step within the scope you authorize. Minor changes can follow a short plan without adding a full toolchain.

## How Spec Kit becomes part of the work

When substantial planning is needed, the guide reads [Spec Kit routing](skills/project-guide/references/spec-kit.md), checks what is installed in **your project**, and selects the next step: requirements, clarification, research/design, tasks or implementation. It checks outputs before continuing.

If Spec Kit is absent, the agent helps set up a project-local integration when authorized. If your host restricts a step to user invocation, it gives you the exact chat command. It does not treat a printed command as execution. A link alone cannot install tools or grant file access; the AI needs access to the link, your project and the required tools.

## Optional: install as a reusable Skill

Reading [START.md](START.md) is enough to adopt the method for the current task. For reuse across projects, ask your agent to install only [`skills/project-guide`](skills/project-guide), following its supported Skill installation process. In Codex with the built-in installer:

```text
Use $skill-installer to install the project-guide skill from:
https://github.com/bingjiezhu/agentic-coding-handbook/tree/main/skills/project-guide
```

Then explicitly invoke `$project-guide`, or let a supporting host select it for a matching project-guidance request. Do not copy the whole handbook into your application. Sharing the link does not silently change global settings or install anything.

## Learn the method

The accompanying handbook explains the reasoning behind the workflow. Both languages contain twelve matching chapters and thirteen prompt examples.

| Edition | Read on GitHub | Prompts | PDF download |
| --- | --- | --- | --- |
| English | [Reading guide](docs/en/README.md) | [13 examples](prompts/en.md) | [English PDF](https://github.com/bingjiezhu/agentic-coding-handbook/releases/download/v1.0.0/vibe-coding-in-practice-en.pdf) |
| 简体中文 | [阅读目录](docs/zh/README.md) | [13 条示例](prompts/zh.md) | [中文 PDF](https://github.com/bingjiezhu/agentic-coding-handbook/releases/download/v1.0.0/vibe-coding-in-practice-zh.pdf) |

The main branch keeps the guide, skill, reading material and SVG diagrams. Publication PDFs and the original LaTeX publication sources are available through the [handbook release](https://github.com/bingjiezhu/agentic-coding-handbook/releases/tag/v1.0.0). Local build products and authoring records are not needed to use the workflow.

[References](REFERENCES.md) · [Translation notes](TRANSLATION.md) · [Contributing](CONTRIBUTING.md) · [Development](DEVELOPMENT.md)

By **[Bingjie Zhu · 朱炳杰](https://github.com/bingjiezhu)**. Guide, handbook, translations and prompts: **[CC BY 4.0](LICENSE)**. Helper code: [MIT](LICENSE-CODE). Credit the author, link the license and indicate changes. Linked third-party tools retain their own licenses.
