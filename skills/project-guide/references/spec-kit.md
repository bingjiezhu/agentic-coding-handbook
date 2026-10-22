# Spec Kit: route to real project tools

Use this reference when a new project, substantial feature or explicit user request calls for specification-driven planning. Select the stage; execute the installed workflow rather than asking the user to memorize its commands.

## 1. Inspect before setup

In the target project, inspect `.specify/`, applicable instructions and installed skills. Current layouts include:

| Agent | Installed step files | Example chat invocation |
| --- | --- | --- |
| Codex | `.agents/skills/speckit-<step>/SKILL.md` | `$speckit-plan` |
| Claude Code | `.claude/skills/speckit-<step>/SKILL.md` | `/speckit-plan` |
| Other tools / older modes | Discover the actual integration and command files | Use the exposed form, not an invented command |

Check installed skills and their invocation restrictions. Some skills may be user-invocable only, including Claude skills with `disable-model-invocation: true` and Codex skills whose policy disables implicit invocation. The existence of a skill file is not proof that the session loaded it. Do not bypass host restrictions by reading an explicitly user-only skill and treating that as permission to execute it.

The optional `../scripts/inspect_project.py` inventories these files without executing project code or installing anything. Its output reports file presence and declared restrictions, not semantic completeness or guaranteed skill availability in the current session.

## 2. Use or set up the integration

**Already installed:** use the current version and active feature; do not reinstall. If an old layout or flags differ, inspect `specify --help` / `specify init --help` and the installed integration.

**Project initialized, current host integration missing:** inspect `specify integration list`. When setup is authorized, use `specify integration install codex` (or the documented host key) rather than reinitializing the project. Installing another integration does not necessarily change the default; inspect that state before switching it. Preserve existing generated files and customizations.

**Not installed:** explain that Spec Kit adds workflow files to the project. If local setup is already authorized, inspect the official installation instructions and initialize the selected target. If that scope is not yet authorized, ask once about adding the local integration; keep researching in the meantime. No global installation is required for a one-time setup.

Example terminal command for initializing a new project:

```sh
uvx --from specify-cli==1.2.3 specify init my-project --integration codex --script py --non-interactive
```

The example pins version 1.2.3. Select a release compatible with the target integration; use `claude` for Claude Code or the documented integration for another host. If Python or `uvx` is missing, give the supported setup action rather than pretending initialization ran. Prefer an existing supported tool over adding another installation.

For a nonempty application directory, first preserve local work, inspect managed-file conflicts and follow the official existing-project guide. The `--here --force` form can replace conflicting managed files: never use it blindly or as a default retry. Do not overwrite existing user instructions to make setup pass.

Avoid changing global agent configuration or enabling unrelated extensions. New optional hooks, network integrations or publication actions require their own actual scope. Inspect setup changes before starting the feature. If the CLI, network or integration is unavailable, retain a small plan in the existing project format and explicitly state that Spec Kit has not been invoked; retry integration only when the blocker changes or the user requests it.

## 3. Pick the next step from actual state

Resolve the active feature from `SPECIFY_FEATURE_DIRECTORY` when set, otherwise `.specify/feature.json` (`feature_directory`). Verify that it is the intended feature. Do not infer it from the Git branch or choose the most recently modified feature directory. If the configured path is outside the agreed project, clarify scope before reading or writing there.

| Need | Next relevant step |
| --- | --- |
| No project principles yet | `constitution`, scoped to agreed project conventions |
| New feature requirements | `specify` |
| Important behavior still ambiguous | `clarify` |
| Agreed spec needs research and implementation design | `plan` |
| A plan needs dependency-ordered work items | `tasks` |
| Material consistency or requirements-quality concerns | `analyze` / `checklist`, as appropriate |
| Authorized implementation of the agreed tasks | `implement`, bounded to a useful increment |
| Implementation needs a completeness check | `converge`, then actual acceptance checks and review |

Before planning, read the active spec and project constitution. Initialization may copy an unfilled constitution template; settle the applicable project principles before treating it as complete. Resolve product decisions that affect the design, and carry technical unknowns into the planning research phase rather than guessing.

An existing `plan.md` or checked task box is not evidence that its content is correct or the application works. Read the relevant artifacts and reconcile changes before moving downstream. Do not rerun constitution for every small task. For an isolated bug, use the project's debugging workflow; do not force it through a full new-feature process.

## 4. Actually invoke, then check

- If the host exposes the installed step as a callable skill, invoke it through that mechanism with the current goal, agreed constraints and evidence. Wait for its result and inspect the resulting files before the next step.
- In hosts where model-selected skills are used by reading their instructions, load the actual installed, model-invocable `SKILL.md`, follow its supported procedure and execute its required project tools. Respect its scope and prerequisites. A step shown in chat is not execution.
- If the host allows only user invocation, give the exact chat command and arguments and wait for the result. Tell the user where to enter it. Do not send `$speckit-plan` or `/speckit-plan` to a shell, start a nested agent CLI to evade the restriction, or repeatedly claim automatic invocation.
- Check stage outputs against this project's requirements. In the current planning workflow, research and design artifacts belong to the feature directory; external-interface contracts are conditional. Preserve existing documents and follow the installed version's procedure.
- Report the actual artifact paths and checks, then continue to the next authorized stage. If a required prerequisite or quality gate fails, resolve it at the source rather than skipping it. Convergence reports do not replace running the application and acceptance checks.

## Official references

Use the documentation matching the installed integration and version.

- [Spec Kit quickstart](https://github.github.io/spec-kit/quickstart.html)
- [Codex integration](https://github.com/github/spec-kit/blob/main/docs/integrations/codex.md)
- [Claude Code integration](https://github.com/github/spec-kit/blob/main/docs/integrations/claude.md)
- [Invocation and integration management](https://github.github.io/spec-kit/integrations/cli.html)
- [Installation](https://github.com/github/spec-kit/blob/main/docs/installation.md)
- [Existing projects](https://github.com/github/spec-kit/blob/main/docs/guides/existing-projects.md)
