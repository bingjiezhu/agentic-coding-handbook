# Agentic Coding Handbook

**把链接发给 Codex、Claude Code 等 AI，让它按这套方法带你做项目。**

简体中文 · [English](README.md)

从说清想法、调研方案、用 Spec Kit 写计划，到小步实现、实际检查和保存进度，由 AI 帮你判断下一步。你负责目标和重要选择，不必先读完整份教程，也不必记住每条命令。

> **给 AI 的入口：** 用户把本仓库作为项目方法交给你时，请读取 [START.md](START.md) 和 [Project Guide 技能](skills/project-guide/SKILL.md)，用用户的语言开始引导项目。已有项目想法就接着推进；只收到链接时，先问：“你想做什么项目，给谁用，最先想解决什么问题？”不要只介绍仓库内容。
>
> 可直接读取的文本：[START.md 原文](https://raw.githubusercontent.com/bingjiezhu/agentic-coding-handbook/main/START.md) · [SKILL.md 原文](https://raw.githubusercontent.com/bingjiezhu/agentic-coding-handbook/main/skills/project-guide/SKILL.md)

## 直接开始

把这个链接发给能读取 GitHub 的 AI：

```text
https://github.com/bingjiezhu/agentic-coding-handbook
```

也可以把你的想法一起发过去：

```text
请按这个仓库的方法带我开始项目：
https://github.com/bingjiezhu/agentic-coding-handbook
我想做一个待办工具，添加事项后，刷新页面还能看到。
```

接下来，AI 应该根据项目情况带你推进：

| 到了哪一步 | AI 应该帮你做什么 |
| --- | --- |
| 只有模糊想法 | 问清给谁用、第一版先做什么、怎样算做好 |
| 要选择方案 | 先查项目已有内容和现成工具，比较直接使用、改造或自己做 |
| 需要写计划 | 检查项目里的 Spec Kit，调用对应步骤整理需求、调研、计划和任务 |
| 开始实现 | 先做通一段完整操作，保留可恢复版本和尝试记录 |
| 检查结果 | 对照原始要求实际运行，说明通过、失败和还没测的部分 |
| 下次继续 | 读取进度、核对当前文件，再接着做未完成的任务 |

你确认目标和重要取舍后，AI 在已允许的范围内继续做，不需要每一步都让你手动选提示词。明确的小改动也不必为了走流程而搭一整套工具。

## 它怎样自己调用 Spec Kit

进入需要详细计划的阶段，AI 会按[接入与调用规则](skills/project-guide/references/spec-kit.md)，检查**你的项目**实际安装了什么、正在处理哪个功能，然后选择相应的 Spec Kit 步骤并核对结果。

还没接入时，AI 会先帮你检查安装条件，在你允许的范围内完成项目接入。若当前工具把某个步骤设为只能由用户调用，它会告诉你在聊天里输入哪条命令，等实际结果后再继续。它不会只写出命令就声称做完。

AI 需要能读取链接、访问项目并使用相应工具；链接本身不会安装软件或增加权限。

## 想在以后的项目里也继续用

本次项目直接按 [START.md](START.md) 使用即可。想长期复用时，可以让 AI 按当前工具支持的方式安装仓库中的 [`skills/project-guide`](skills/project-guide) 文件夹，不用把整个仓库复制到你的应用里。

在带有 Skill Installer 的 Codex 中，可以发送：

```text
请使用 $skill-installer 安装这个项目引导技能：
https://github.com/bingjiezhu/agentic-coding-handbook/tree/main/skills/project-guide
```

安装后可用 `$project-guide` 明确调用；支持自动选择技能的工具，也可以在适合的项目引导任务中选用它。只分享链接不会自动修改全局设置或安装技能。

## 想了解背后的方法

中英文教程各有十二章、十三条提示词示例，按需查阅：

| 版本 | 在线阅读 | 提示词 | PDF 下载 |
| --- | --- | --- | --- |
| 简体中文 | [阅读目录](docs/zh/README.md) | [13 条示例](prompts/zh.md) | [中文 PDF](https://github.com/bingjiezhu/agentic-coding-handbook/releases/download/v1.2.0/vibe-coding-in-practice-zh.pdf) |
| English | [Reading guide](docs/en/README.md) | [13 examples](prompts/en.md) | [English PDF](https://github.com/bingjiezhu/agentic-coding-handbook/releases/download/v1.2.0/vibe-coding-in-practice-en.pdf) |

[版本下载页](https://github.com/bingjiezhu/agentic-coding-handbook/releases/tag/v1.2.0)提供可安装技能、中英文 PDF 和 LaTeX 源码包。仓库包含项目流程、参考章节、提示词示例与 SVG 图。

[资料来源](REFERENCES.md) · [术语对照](TERMINOLOGY.md) · [参与改进](CONTRIBUTING.md) · [维护说明](DEVELOPMENT.md)

作者：**[朱炳杰 · Bingjie Zhu](https://github.com/bingjiezhu)**。引导方法、教程、翻译和提示词采用 **[CC BY 4.0](LICENSE)**，辅助代码采用 [MIT](LICENSE-CODE)。分享与改编请注明作者、附授权链接并说明修改。第三方工具遵循各自授权。
