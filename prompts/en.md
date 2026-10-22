# Copyable Prompts

Choose one prompt, fill in the brackets and send it to a coding agent with project access. See [the overview](../docs/en/00-overview.md) for instructions.

## 01 · Clarify Requirements and Propose a Minimal Solution

[Chapter](../docs/en/01-define-the-task.md)

```text
I want [users] to accomplish [goal] in [scenario]. The project and reference materials are at [location; say if none exist]. This version must include [scope] and exclude [out of scope]. You may edit [allowed scope].

Check the current state and preserve the original requirements. In the existing requirements document or the current feature's spec.md, record the goal, key user actions, acceptance criteria, behavior to preserve and open questions. Verify what you can; ask about unclear requirements one at a time, offer recommendations and label unconfirmed assumptions.

Propose a minimal solution and small tasks with a check for each. This round is for requirements and an initial outline, not code changes; defer technical choices until research. Follow existing documents or Spec Kit steps. Report inaccessible materials; if you cannot write files, return a draft without claiming it was saved.
```

## 02 · Organize Project Files and Reading Entry Points

[Chapter](../docs/en/02-project-files.md)

```text
Project: [path]. Task: [goal]. Documents you may update: [scope]. Locate the existing rules, requirements, research, plan, tasks, progress and evidence. Add files only when missing and useful. Use the active Spec Kit feature directory rather than creating parallel copies. Report unreadable paths; return a draft if you cannot write.

Keep rules limited to project-specific conventions, edit scope, check commands and document pointers. Use a short index linking research and experiments to their originals. Preserve valid content; do not move or delete originals. List updated paths and when to maintain them. Refresh rules as the tool requires and check their loaded sources; if loading is not observable, mark it unverified. Creating a file does not prove it is active.
```

## 03 · Read the Project and Identify the Change

[Chapter](../docs/en/03-research-first.md)

```text
Goal: [task]. Materials: [location]. Research file you may update: [path]. Check the version, existing changes, rules and runtime requirements. Do not change the program this round; validate only in a test environment. Report unreadable materials; return a draft if you cannot save records.

Find existing implementations and comparable solutions. Compare reuse, adaptation and a new build. Verify package names, official sources and licenses. If offline, label external claims unverified; do not invent sources. Run minimal experiments on architecture-relevant unknowns and explain modules, data flow and dependencies.

Record questions, sources and check dates, observations, alternatives, rationale and unknowns. Separate established facts, inferences and hypotheses; say what new evidence would change the choice. Report actual edits and unverified items. Preserve original materials and verification evidence.
```

## 04 · Advance the Current Feature with Spec Kit

[Chapter](../docs/en/04-spec-kit.md)

```text
Project: [path]. Basis: [requirements and records]. Step for this round: [step]. Allowed edits: [scope]. Check the installed version, invocation, active feature and prerequisites. If installation or inputs are missing, propose how to supply them; do not install or skip ahead on your own.

Preserve existing files. Clarify ambiguity and investigate unknowns. Include required automated tests in the spec and tasks; map each task to requirements and checks.

If only the user can invoke the step, provide the command and wait for its result. Report actual outputs, checks, conflicts and the next step. Do not claim an uninvoked step ran. Surface contradictory requirements rather than choosing silently.
```

## 05 · Implement One Verifiable Increment

[Chapter](../docs/en/05-small-steps.md)

```text
Project and requirements: [location; state requirements if no document exists]. Complete [feature scope] using [key checkpoints]. You may edit [scope]. Preserve [behavior and style]. References: [files or screenshots; say if none].

Inspect existing changes and keep a recoverable baseline using version history or a backup; exclude unrelated work. Implement, check and fix against [runnable acceptance checks] within [budget]. Report missing key inputs. Pause affected work for unauthorized actions, important trade-offs or repeated failures with no new lead. Connect the entry point, processing, persistence and feedback. Label mock data, unfinished features and hard-coded answers.

Explain key changes and data destinations, with file locations. Run the project and provide an accessible address or path, check steps and actual results. For UI changes, click, type, refresh and compare screenshots; without tools, give manual steps and mark those checks unverified. Save this round separately; commit locally only if authorized, without pushing. Update tasks and progress. Use [location, current behavior, desired behavior, things to preserve] for the next change. Avoid unrelated rewrites; explain trade-offs before changing agreed goals.
```

## 06 · Run Acceptance Checks Against Requirements

[Chapter](../docs/en/06-acceptance-checks.md)

```text
Check [project location and version] against [requirements and original materials]. Approved test environment and data: [scope]. List expected outcomes first; clarify important ambiguity. Do not treat current program output as the correct answer. This round is for acceptance, not changing implementation or weakening criteria.

Follow the complete real workflow. Compare displayed results with saved records. Based on risk, check failures, repetition, reopening, recovery and existing features. Add required tests only within scope; a regression check should expose the original error before passing after the fix. For accounts or public endpoints, check unauthorized access, exposed secrets and external input being executed as commands, within authorization.

For each requirement, report steps, expected and observed results, evidence, and pass, fail or unverified status. Identify mock data, substitute services and environment limits. Respect authorization for checks with external effects. If unable to run, give manual steps and mark gaps unverified. No error message is not proof of completion. Do not delete, skip or relax checks to obtain a pass; report conflicts between requirements and checks.
```

## 07 · Investigate a Specific Failure

[Chapter](../docs/en/07-debugging.md)

```text
Problem: [steps, expected outcome, actual outcome]. Project and error records: [location]. Recent changes: [details; say if unknown]. Allowed repairs: [scope]. Investigation budget: [time or attempts].

Check the current version, runtime settings, permissions and files before rewriting. Reproduce in an approved test environment. If intermittent, record conditions, attempts and failures. Report missing inputs or tools; do not turn guesses into conclusions.

List possible causes and their predicted observations. Run minimal checks to find the earliest divergence. Preserve key experiments: hypothesis, version, conditions, action, result and evidence; keep unsuccessful paths too. Make a small repair only with supporting evidence and within scope. Where automated reproduction is possible, retain a check that fails before the fix and passes after it, then check related features. If an approach repeatedly fails or the budget is nearly spent, save facts and unknowns and consider an independent review. Return records if you cannot write them. Exclude sensitive information.
```

## 08 · Create Parallel Subtasks

[Chapter](../docs/en/08-multiple-agents.md)

```text
Goal: [task]. Shared materials: [requirements, research, plan and task locations]. Check capabilities and permissions first. If supported, create two read-only subtasks: A checks existing implementation and reuse; B checks [approach, sources or validation risks]. Report missing materials.

Subtasks must not edit files or expand scope. If enforced read-only access is required but cannot be configured, pause before launching and explain. Role instructions are not permission isolation. Give each a scope, inputs, checks and return format: findings, locations, evidence and unknowns. The lead agent may advance independent work within current permissions; wait for dependent results and reconcile conflicts first.

Before any parallel editing, establish authorization, file ownership and integration checks. Record running, completed or failed status; no returned result is not completion. If subagents are unsupported, provide task briefs for separate sessions without pretending they launched.
```

## 09 · Review Independently and Recheck Fixes

[Chapter](../docs/en/09-independent-review.md)

```text
Materials: [original requirements, current requirements, version, change scope and run instructions]. If you helped implement this and tools support it, assign a reviewer who did not participate and does not inherit the implementation conversation. Otherwise provide a handoff brief; you may self-review, but do not call it independent. List missing materials.

Do not edit the implementation under review. Read files first. If execution would write data, use an approved test copy or separate working directory with test data. If writes are prohibited, list checks not run; do not bypass restrictions. Separate directories do not isolate external data.

Check requirements, changes and evidence. Prioritize wrong results, data or permission issues, removed or weakened checks and broken existing behavior. For long-lived projects, also examine obvious duplication and complexity. Give each issue a location, trigger, impact and evidence; distinguish verified defects from risks.

Return a list for the implementer. Hand it off only with authorization and tools; otherwise let the user forward it. After fixes, recheck the current version and summarize resolved, outstanding and unverified items. State when no material issue was found within scope; do not invent findings to meet a quota.
```

## 10 · Save Progress

[Chapter](../docs/en/10-long-tasks.md)

```text
Update [progress file]: goals and decisions, project path and version, changed files and uncommitted edits, checks and evidence, failures and unverified items, unfinished work, recovery and next steps. If unable to write, return saveable text without claiming it is on disk.

Index key experiments with assumptions, conditions, results and evidence. Keep reviewable analysis and permitted original sources for important investigations; open saved files before handoff, and do not present a draft as saved. Mark superseded decisions, preserve requirements and evidence, and list spec status and next checks. Mark missing history unknown; do not call plans complete.
```

## 11 · Read Progress and Continue

[Chapter](../docs/en/10-long-tasks.md)

```text
Read [progress file], requirements, plan and tasks. Check the directory, version, existing edits and verification records. Without Git, compare file snapshots. Report missing or unreadable records before guessing progress; do not overwrite others' work.

Continue with the first actionable unfinished task, updating actual results after each verifiable increment. Reuse results only when related code, software, configuration and data are unchanged; recheck if uncertain. Still run the full checks required by the project.

Work within [allowed edit and execution scope] and [budget]. If blocked, advance independent work. Save before the budget runs out; return a handoff if unable to write. Pause affected work when goals must change, permissions must expand or an important unresolved choice needs a decision.
```

## 12 · Extract Reusable Rules and Skills

[Chapter](../docs/en/11-rules-and-skills.md)

```text
Derive reusable guidance from [accepted results, change records or repeated tasks]. Allowed updates: [file scope]. Reuse project rules. Package repeated methods as a Skill in the current tool's format, and fixed steps as scripts where useful. If Skills or writes are unsupported, return a draft; do not claim activation.

Define applicability, inputs, outputs, essential steps, verification entry points and failure handling. Inspect third-party skills and scripts before use. Preserve valid conventions and avoid unrelated installations.

Report paths and activation steps, including required review, trust, approval or restart. Validate with an authorized independent example; mark unexecuted checks unverified. For automatic checks, verify the trigger and behavior on success, failure and script errors without affecting real data.

Compare quality, communication and rework. Consolidate duplicate or outdated guidance only within scope. Mandatory checks must not depend solely on prompt reminders.
```

## 13 · Pilot and Execute a Batch

[Chapter](../docs/en/12-batch-work.md)

```text
Process [task list] using [rules and template]. Output: [location]. Allowed operations and budget: [scope]. Pilot a few common and high-risk cases and show results with evidence. Repeat representative AI judgments to assess consistency. Clarify rules or acceptance criteria first; report missing tools without claiming processing occurred.

Give each item a unique ID, output format, source record and completion criteria. Parallelize only independent items. Do not overwrite originals or repeat external effects. Use copies or safely repeatable operations for repeated trials. Record status, output and failure reason. Check uncertain outcomes before retrying. Resume unfinished items; recheck affected results when inputs, rules or environment change.

Run required checks for every item, then sample actual content. Sampling does not replace required per-item checks. Scale only after the pilot passes and within authorization; pause scaling if a failure pattern repeats. Report the complete list and gaps, total time, human review and rework, not just generation speed.
```
