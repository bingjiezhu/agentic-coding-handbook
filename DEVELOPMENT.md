# Development · 开发与维护

## Repository structure

| Path | Purpose |
| --- | --- |
| `START.md` | Project-guide entry point |
| `skills/project-guide/` | Self-contained, installable Skill |
| `docs/zh/`, `docs/en/` | Chinese and English reference chapters |
| `prompts/` | Copyable prompt collections |
| `assets/diagrams/` | SVG illustrations used by the chapters |
| `scripts/`, `tests/` | Repository validation and helper tests |

The project inspector reads project structure and declared invocation settings without executing project code. Unsupported or ambiguous flag syntax is reported as unknown and must be checked with the host. The optional handoff helper packages only explicitly selected local files; its hashes check file integrity, not the truth of an analysis.

## Development requirements

Python 3.9 or later is sufficient for the repository checks and inspector tests:

```sh
python3 scripts/validate_repo.py
python3 -m unittest discover -s tests -v
```

Keep the Skill self-contained so that installing its folder does not require files from elsewhere in the repository. Skill discovery remains enabled by default.

The handoff helper should reject missing, outside-project and symbolic-link sources; refuse an already tracked packet area; and detect changes to packet files. Its local `.agent-handoff/` output is for the target application's private working records and is excluded from ordinary Git adds. Review any file before intentionally sharing it.

## Documentation changes

Maintain corresponding meaning in both languages. Keep prompt collections consistent with the examples in each chapter. Repository validation compares every prompt body in chapter order and rejects divergent or reordered collections. Preserve filenames, executable identifiers and command syntax. Add primary references when changing tool-specific instructions.

## Integration changes

Use separate temporary projects for each supported host. Verify the generated Spec Kit skills, active feature selection and planning prerequisites. Cover new-project guidance, existing projects, missing tools, user-invocable-only skills and interrupted work. Setup tests and application acceptance tests serve different purposes; record their results separately.

## Distribution

[Release downloads](https://github.com/bingjiezhu/agentic-coding-handbook/releases) provide the Skill archive, bilingual PDFs and LaTeX source packages. Each source package contains its own compilation instructions. Exclude temporary applications, build outputs, logs and credentials from repository commits.

## 中文维护要点

- 保持中英文含义对应，章节示例与提示词合集一致。
- 技能文件夹独立安装后应能使用，不依赖仓库其他文件。
- 修改工具接入方式时，在独立测试项目中验证。
- 发布技能包、PDF 和排版源码；临时项目、日志与构建产物不纳入仓库。
