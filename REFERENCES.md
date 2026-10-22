# References · 资料来源

The following primary sources support the handbook's engineering methods and tool-specific instructions. Select methods for the project's requirements and verify commands against the installed integration.

以下一手资料对应教程中的工程方法和工具用法。方法按项目需求选用，命令以实际安装的工具和集成为准。

| Practice / topic | Primary source | Scope |
| --- | --- | --- |
| Small changes and feedback | [DORA: Working in small batches](https://dora.dev/capabilities/working-in-small-batches/) | Small increments, feedback and diagnosis |
| Evidence-based debugging | [Google SRE: Effective Troubleshooting](https://sre.google/sre-book/effective-troubleshooting/) | Hypotheses, observed behavior and searchable investigation records |
| Architecture decisions | [AWS: ADR process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html) | Alternatives, context, rationale and consequences |
| Context and retrieval | [Anthropic: Effective context engineering](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents) | Indexes, just-in-time retrieval and persistent notes |
| Long-running work | [Anthropic: Effective harnesses](https://www.anthropic.com/research/effective-harnesses-for-long-running-agents) | Incremental work, progress files and version history |
| Agent orchestration | [Anthropic: Building effective agents](https://www.anthropic.com/research/building-effective-agents) | Feedback loops, stopping conditions and common agent patterns |
| Multiple agents | [Anthropic: Multi-agent research system](https://www.anthropic.com/research/multi-agent-research-system) | Separate contexts, orchestration and coordination cost |
| Codex subagent permissions | [OpenAI: Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents) | Codex parent sandbox and approval inheritance |
| Project rules | [OpenAI: AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [Claude Code: memory](https://code.claude.com/docs/en/memory) | Rule discovery, precedence and loading conditions |
| Reusable Skills | [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills) | Task-specific instructions, progressive disclosure and activation |
| Hooks | [Claude Code: Hooks](https://code.claude.com/docs/en/hooks) | Configured events, script results and blocking semantics |
| Secrets | [OWASP: Secrets Management](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html) | Secret storage, access control and rotation |
| Git ignore rules and worktrees | [Git: gitignore](https://git-scm.com/docs/gitignore), [Git: worktree](https://git-scm.com/docs/git-worktree) | Ignore rules, working directories and their isolation boundaries |
| Specification-driven workflow | [Spec Kit quickstart](https://github.github.io/spec-kit/quickstart.html), [Agentic SDD](https://github.github.io/spec-kit/reference/agentic-sdd.html), [plan template](https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/plan.md) | Specification-driven workflow and design artifacts |
| Spec Kit invocation | [Codex integration](https://github.github.io/spec-kit/integrations/codex.html), [Claude Code integration](https://github.github.io/spec-kit/integrations/claude.html) | Integration setup and invocation syntax |
| Human judgment | [NIST: Trustworthy AI characteristics](https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/) | Contextual trade-offs and human judgment |
| Prompt evaluation | [OpenAI: Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices), [Anthropic: Define success and evaluations](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests) | Task-specific evaluation criteria and representative cases |


## Applying the references · 使用原则

Project filenames, progress formats, the queue of specs and the number of parallel assistants can be adapted to the task. Tool-specific instructions apply to the named integration and version; evaluate actual behavior in the project environment.

项目文件组合、进度格式、任务顺序和协作规模可按实际需要调整。具体工具说明适用于相应集成与版本，使用时结合项目环境确认其行为。
