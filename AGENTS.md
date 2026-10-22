# Working with this repository

When a user shares this repository to adopt its project method, read `START.md` and `skills/project-guide/SKILL.md`. Guide the user's application in its own target directory; do not scaffold an application inside this handbook by mistake.

When maintaining this repository:

- The reusable instructions are in `skills/project-guide/`; keep them self-contained when installed separately.
- `docs/zh/` and `docs/en/` are the bilingual reading edition. Update corresponding meaning when changing it.
- Maintain reusable instructions, the Skill, bilingual chapters and SVG figures in the repository. Distribute PDFs and LaTeX source packages through releases; exclude build outputs, temporary projects and logs.
- Validate with `python3 scripts/validate_repo.py` and `python3 -m unittest discover -s tests -v`.
- Do not promise that sharing a URL installs software, changes permissions or guarantees automatic execution in every host. Distinguish a real tool invocation from showing a chat command.
