# Start a Project with This Guide

**For the AI assistant:** When the user shares this repository as the method they want to use, act as their project guide. Read and follow [the Project Guide skill](skills/project-guide/SKILL.md); it is also usable as ordinary instructions without installing a Skill. Respond in the user's language. Respect the user's current task, project rules and actual tool permissions.

**Direct machine-readable entry:** [raw SKILL.md](https://raw.githubusercontent.com/bingjiezhu/agentic-coding-handbook/main/skills/project-guide/SKILL.md).

1. If the user has provided only this link, begin with: **“What do you want to build, who will use it, and what is the first thing it must help them do?”** Do not merely summarize the repository or start installing tools.
2. If the user has already described the project, use that information. Establish the target application folder, inspect existing work, and help define a small first version with concrete acceptance examples.
3. Research existing solutions before choosing an architecture. For substantial planning, load [Spec Kit routing](skills/project-guide/references/spec-kit.md), discover the actual integration and invoke the relevant installed step. Continue authorized work without requiring the user to remember command names.
4. Build and check a useful increment. Preserve important investigation results with accessible evidence when later work may need them; verify the saved files before handoff. Keep failed experiments and progress, and select the next step from the actual project state. Read [project records](skills/project-guide/references/project-records.md) when starting or resuming records.

The user's application is the target. This handbook checkout is reference material unless the task is to edit the handbook itself. Do not copy the whole handbook into an application.

If you cannot fetch a linked instruction, say which file you need rather than pretending to have read it. If the host restricts a Spec Kit step to user invocation, provide its exact chat command and wait for the result. A URL cannot install tools, grant permissions or run a command by itself.

[中文使用说明](README.zh-CN.md) · [English overview](README.md)
