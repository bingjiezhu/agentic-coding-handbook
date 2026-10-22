---
name: project-guide
description: Guide a new software project or substantial feature from an idea through research, Spec Kit planning, implementation and verification. Use when the user adopts this handbook, asks to be guided through a project, or wants the same method continued in an existing project. A small unrelated edit does not require the full workflow.
metadata:
  author: bingjiezhu
---

# Project Guide

Guide the user through the project workflow. Use the user's language and explain technical choices through their effect on the project. The user decides the goal and important trade-offs; you manage the next useful step and execute authorized work.

## Establish the actual project

- Work in the user's application directory. This handbook or installed skill directory is reference material, not the application to scaffold. Reuse information and authorization already supplied.
- If the user has shared only the repository link, ask one practical opening question: **“What do you want to build, who will use it, and what is the first thing it must help them do?”** In Chinese: **“你想做什么项目，给谁用，最先想解决什么问题？”** Do not begin with an installation checklist.
- If the goal is already clear, inspect the target folder, existing changes and applicable project instructions. Ask for a location only when it is missing or ambiguous. The optional read-only helper is `python3 scripts/inspect_project.py <project-path>` relative to this skill.
- Continue an existing project from its real state. Do not restart a workflow or replace its architecture merely because it uses different filenames.

## Choose and carry out the next step

| Situation | Guide's action | Useful result |
| --- | --- | --- |
| Vague idea | Ask one important question at a time; suggest a small first version and what can wait | Agreed users, goal, scope and observable acceptance criteria |
| Goal clear, design undecided | Inspect existing code and research reuse, adaptation and a new build; check primary sources and key unknowns | A short recommendation with reasons, alternatives and remaining questions |
| A new project or substantial feature needs a plan | Read [Spec Kit routing](references/spec-kit.md), inspect the integration, and actually invoke the next relevant installed skill | A spec, researched implementation plan and ordered tasks in the active feature directory |
| Ready to implement | Implement one complete user workflow, preserving a recoverable version; run the relevant checks | Working behavior with actual verification evidence |
| Something fails | Reproduce the issue; record a hypothesis and the smallest discriminating experiment before changing code | A bounded fix, retained failed attempts and a regression check where useful |
| Important work is ready for acceptance | Check the real workflow against the original requirements; use a separate reviewer where available and appropriate | Pass, fail and unverified items with concrete evidence |
| Session is ending or work will resume | Follow [Project records](references/project-records.md); compare saved progress with current files before resuming | A trustworthy next action, not just a chat summary |
| Repetition is becoming useful | Capture effective rules or Skills; pilot batch work before scaling | A reused method shown to help on another task |

Do not ask the user to choose among handbook prompts or remember Spec Kit command names. Route by the actual task. A minor, well-defined change can use a short plan and existing checks; do not introduce Spec Kit scaffolding unless it is useful or explicitly requested. If the user explicitly requires Spec Kit, use it when supported and report a real blocker otherwise.

## Keep decisions and execution connected

1. Preserve the user's original request. Write a short first-version proposal: user, goal, in/out of scope, key actions and acceptance examples. Ask about unresolved choices that materially change the product, cost or allowed actions; do not repeatedly reconfirm settled decisions.
2. Research before committing to a stack or architecture. Reuse the current project where possible. Discuss module responsibilities, data flow and interfaces at the level needed for this task; do not treat an official source as proof that a design fits.
3. Once the user has agreed to a direction and asked you to build, continue within that scope. Advance routine planning, implementation, verification and progress updates within that scope. Preserve the scope of a plan-only request.
4. Keep Spec Kit artifacts in its active feature directory. Maintain its spec, plan and tasks as the design changes. Do not create a second competing set of spec/plan/task files.
5. Add a brief pointer to this workflow in an existing project rules or progress file when project documentation changes are authorized. Link the active feature and the next step. Do not replace existing rules or install a global skill merely because the user shared a URL.

## Work and report concretely

Before editing an existing application, run the smallest relevant existing check or smoke test when authorized and feasible. Record pre-existing failures separately from failures introduced by the change. Scope the baseline check to the affected workflow; a small documentation edit does not require starting the full application.

Complete one real path from user action through processing and persistence to visible feedback. For UI work, use the user's examples to clarify the intended experience, then click, type, refresh and check saved data when tools permit. Preserve approved behavior rather than rewriting everything in response to each comment.

Use test data and preserve unrelated work. Instructions such as “read-only” are not enforced permissions. A method guide grants no extra right to publish, send messages, change production data or install system-wide tools; use the user's actual authorization.

Report the current stage, what actually changed, what was run, what passed or failed, and what is still unknown. Keep implementation detail out of ordinary user explanations unless it affects a decision. If tools or access are missing, give the specific next action or a usable draft; do not call an unrun step completed. Save progress before usage limits, repeated failures without new evidence, or an unresolved important decision.

## Read only what the task needs

- Planning and Spec Kit setup/invocation: [Spec Kit routing](references/spec-kit.md).
- New project notes, failed experiments and resuming: [Project records](references/project-records.md).
- Deeper explanation or a prompt example: use the corresponding chapter in the online [Chinese](https://github.com/bingjiezhu/agentic-coding-handbook/tree/main/docs/zh) or [English](https://github.com/bingjiezhu/agentic-coding-handbook/tree/main/docs/en) handbook. Do not load all chapters into every session.
