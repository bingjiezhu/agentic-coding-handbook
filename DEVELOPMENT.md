# Development · 维护说明

The main branch is the reusable guide, Skill and reading edition. Keep it small enough for people and agents to navigate. The `v1.0.0` release preserves the original bilingual PDFs and LaTeX publication snapshot; PDF rendering is not part of using the Project Guide.

## Files to maintain

- `START.md`: what an agent should do when a user shares the repository.
- `skills/project-guide/SKILL.md`: the installable, self-contained project workflow.
- `skills/project-guide/references/`: conditional Spec Kit routing and progress guidance.
- `skills/project-guide/scripts/inspect_project.py`: read-only project inventory; no installation or project-code execution. Invocation flags that use unsupported or ambiguous YAML are reported as unknown; inspect them with the host rather than assuming they are enabled.
- `docs/zh/`, `docs/en/`, `prompts/`: the reading edition, edited in corresponding languages.
- `assets/diagrams/`: SVGs used in the reading edition; avoid committing rendering duplicates.

Do not add authoring logs, temporary projects, PDF build directories or repeated image formats to main. Use a local archive or an appropriate release asset for publication sources.

## Checks

Python 3.9+ is enough for the repository checks and helper tests:

```sh
python3 scripts/validate_repo.py
python3 -m unittest discover -s tests -v
```

For Skill frontmatter validation, the Codex Skill Creator's `quick_validate.py` can be used if available. The current Skill allows normal automatic discovery; do not switch it to explicit-only without a user request.

When changing Spec Kit routing, verify the current official integration and installed behavior. A useful isolated smoke test uses a reviewed `specify-cli` version to initialize separate temporary Codex and Claude projects, checks the actual generated skills, and runs the project inventory. Never run initialization against this guide repository to test it. Do not claim that CLI setup alone proves AI planning or implementation succeeded.

When changing an instruction, also walk through: an idea without a folder, an existing project, a planning request with Spec Kit, missing tools, a user-only skill, and resuming interrupted work. Report the distinction between text review, helper tests, real tool invocation and any actual model execution. Changes to the guide should not imply extra rights to install, publish or operate on production systems.

当前主分支用于给读者和 AI 使用。修改入口或技能后检查链接、自包含性与项目检查脚本；PDF、LaTeX 排版和核查记录保留在发布包或本地，不放回日常使用入口。
