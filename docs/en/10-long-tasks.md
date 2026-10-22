[English](../en/10-long-tasks.md) · [简体中文](../zh/10-long-tasks.md) · [Home](../../README.md)

# Resume Long Tasks Reliably

![Resume Long Tasks Reliably](../../assets/diagrams/en/p_resume.svg)

Long tasks need clear specs, staged acceptance and persistent records. Review a dependency-ordered queue of specs before execution. Save before interruptions, usage limits or repeated drift; verify the current state before resuming.

## Keep analysis that another session can check

After substantial research, calculation or debugging, retain the question, key assumptions, necessary reasoning or experiments, sources, conclusion and unresolved parts. Reuse the project's existing research file; add a short index only when several records need navigation. A minor edit needs no separate record. This captures the AI's reviewable explanation, not undisclosed internal reasoning.

For example, a temporary partner contract may specify the units of a retry delay. If a later task will implement that behavior, preserve the conversion, applicable host and request method, and an authorized copy of the contract or a durable source link. “We thought it meant milliseconds” alone gives the next agent nothing to verify. On the later task, read the relevant record and check it against the current contract and code; revalidate when the conditions change.

Before handoff, open the saved file and check its contents and source. The optional [local handoff packet helper](../../skills/project-guide/scripts/handoff_packet.py) creates an index and SHA-256 manifest for selected files so missing or changed files can be detected; a matching hash does not establish that a conclusion is true. Packets go into the project's Git-ignored `.agent-handoff/` directory by default and may contain private material. Review them separately before sharing. If file tools are unavailable, return a Markdown draft clearly marked as unsaved and explain how to save it manually.

## Save before stopping; verify before resuming

`PROGRESS.md` is a text progress file; reuse an existing equivalent. Use the first prompt before ending a session and the second after restarting.

### Save Progress

```text
Update [progress file]: goals and decisions, project path and version, changed files and uncommitted edits, checks and evidence, failures and unverified items, unfinished work, recovery and next steps. If unable to write, return saveable text without claiming it is on disk.

Index key experiments with assumptions, conditions, results and evidence. Keep reviewable analysis and permitted original sources for important investigations; open saved files before handoff, and do not present a draft as saved. Mark superseded decisions, preserve requirements and evidence, and list spec status and next checks. Mark missing history unknown; do not call plans complete.
```

Update records after each verifiable stage. On resuming, reread the current spec, progress and relevant experiments. A chat claim of completion does not replace a traceable result.

### Read Progress and Continue

```text
Read [progress file], requirements, plan and tasks. Check the directory, version, existing edits and verification records. Without Git, compare file snapshots. Report missing or unreadable records before guessing progress; do not overwrite others' work.

Continue with the first actionable unfinished task, updating actual results after each verifiable increment. Reuse results only when related code, software, configuration and data are unchanged; recheck if uncertain. Still run the full checks required by the project.

Work within [allowed edit and execution scope] and [budget]. If blocked, advance independent work. Save before the budget runs out; return a handoff if unable to write. Pause affected work when goals must change, permissions must expand or an important unresolved choice needs a decision.
```

## Use acceptance criteria and stop conditions

Within a budget, let AI propose, execute, check and keep useful results without lowering acceptance criteria. Stop when done; save before limits. Pause affected work after repeated failures without new evidence or at unresolved trade-offs. Repetition does not guarantee convergence; restoring code does not undo external actions.
