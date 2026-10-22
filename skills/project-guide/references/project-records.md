# Small records that support real work

Reuse existing project documents. Use the active Spec Kit feature directory for its spec, research, plan and tasks. Do not demand a particular collection of Markdown files for a tiny change.

## Starting a project

Before a location is chosen, discuss the idea in chat; do not create an application inside the handbook checkout. Once project writes are authorized, preserve the original request and the agreed first version in an existing requirements document or a short `PROJECT_BRIEF.md`:

- Who uses it, in what situation, and the first problem to solve.
- Original user request, preserved verbatim or linked to an accessible record.
- First-version scope, what can wait, and existing behavior to preserve.
- Observable acceptance examples, including data persistence and failure cases where relevant.
- Decisions that still need the user's input; research questions for the agent.
- Allowed changes, execution budget and important external-action boundaries already agreed.

Avoid inventing credentials, infrastructure, deadlines or product requirements. When no project files exist, ask for the target location before writing. A new project directory alone does not authorize remote publication or production data changes.

## After each meaningful increment

Use the existing progress file or a small `PROGRESS.md`. Record goal and active feature, changed files and version, exact run/check commands and their results, pre-existing failures, failed attempts and unknowns, unfinished tasks and the next useful action. Link long logs rather than putting them in always-loaded rules. Never include secrets.

For a failed experiment, preserve the question, hypothesis, version and conditions, action, observed result, evidence and why the approach was abandoned. Old failure records inform the next diagnosis; they do not prove an approach can never work under different conditions.

Before a new session, save while enough budget remains. On resuming, read the current requirements and progress, compare them with actual files and changes, and recheck results affected by new code, configuration, dependencies or data. Distinguish unfinished from unknown outcomes before retrying an operation with external effects.

## Keep the workflow discoverable

When project documentation updates are authorized, add a short pointer in an existing rules or progress file, adapted to the user's language. For example:

```text
This project follows the Agentic Coding Handbook project guide:
https://github.com/bingjiezhu/agentic-coding-handbook/blob/main/START.md
Read the active feature's requirements and PROGRESS.md before resuming.
Use the installed Spec Kit steps when planning substantial changes.
```

Preserve project-specific rules and do not assume writing a pointer means the host loaded it. Sharing a link adopts a workflow for the current task; installing a reusable Skill or modifying global settings is a separate user choice.
