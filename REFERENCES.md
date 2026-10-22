# References and Scope · 资料来源与适用范围

The handbook combines the author's practical teaching material with the following primary sources. A vendor's implementation is an example or tool-specific fact, not an industry-wide standard. Statements about tool behavior were reviewed against documentation on **October 21, 2026**; the bilingual publication was prepared on October 22, 2026. Check your installed version when applying commands.

核心方法参考以下一手资料。厂商的实现经验不等于全行业统一标准，具体工具行为以安装版本和配置为准。正文工具资料核对日期为 2026-10-21，中英文公开版整理日期为 2026-10-22。

| Practice / topic | Primary source | Scope |
| --- | --- | --- |
| Small changes and feedback | [DORA: Working in small batches](https://dora.dev/capabilities/working-in-small-batches/) | Small batches support feedback and diagnosis; improvement is still measured, not guaranteed |
| Evidence-based debugging | [Google SRE: Effective Troubleshooting](https://sre.google/sre-book/effective-troubleshooting/) | Hypotheses, observed behavior and searchable investigation records |
| Architecture decisions | [AWS: ADR process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html) | Alternatives, context, rationale and consequences |
| Context and retrieval | [Anthropic: Effective context engineering](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents) | Indexes, just-in-time retrieval and persistent notes; not a guarantee of perfect memory |
| Long-running work | [Anthropic: Effective harnesses](https://www.anthropic.com/research/effective-harnesses-for-long-running-agents) | Incremental work, progress files and version history; compaction alone is insufficient |
| Agent orchestration | [Anthropic: Building effective agents](https://www.anthropic.com/research/building-effective-agents) | Feedback loops, stopping conditions and common patterns; the article is not current product documentation |
| Multiple agents | [Anthropic: Multi-agent research system](https://www.anthropic.com/research/multi-agent-research-system) | Separate contexts, coordination and additional cost; benchmark gains are not generalized here |
| Codex subagent permissions | [OpenAI: Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents) | The specific tool's parent sandbox and approval inheritance, not a rule for every agent product |
| Project rules | [OpenAI: AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [Claude Code: memory](https://code.claude.com/docs/en/memory) | Discovery, precedence and loading conditions depend on tool and version |
| Reusable Skills | [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills) | Task-specific instructions and progressive disclosure; file creation alone does not prove activation |
| Hooks | [Claude Code: Hooks](https://code.claude.com/docs/en/hooks) | Configured events, script results and blocking semantics; a logging hook is not automatically a gate |
| Secrets | [OWASP: Secrets Management](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html) | A local file or environment variable is not sufficient protection by itself |
| Git ignore rules and worktrees | [Git: gitignore](https://git-scm.com/docs/gitignore), [Git: worktree](https://git-scm.com/docs/git-worktree) | Ignore rules are not access control; worktrees do not isolate external databases or credentials |
| Specification-driven workflow | [Spec Kit quickstart](https://github.github.io/spec-kit/quickstart.html), [Agentic SDD](https://github.github.io/spec-kit/reference/agentic-sdd.html), [plan template](https://raw.githubusercontent.com/github/spec-kit/main/templates/commands/plan.md) | An optional tool and its current workflow; not the definition of a specification or a mandatory standard |
| Spec Kit invocation | [Codex integration](https://github.github.io/spec-kit/integrations/codex.html), [Claude Code integration](https://github.github.io/spec-kit/integrations/claude.html) | Commands and skill syntax can change; inspect the installed integration |
| Human judgment | [NIST: Trustworthy AI characteristics](https://airc.nist.gov/airmf-resources/airmf/3-sec-characteristics/) | Contextual trade-offs and human judgment; “taste” is a teaching definition in this guide |
| Prompt evaluation | [OpenAI: Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices), [Anthropic: Define success and evaluations](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests) | Use task-specific criteria and representative cases; no universal prompt-success guarantee |

The Markdown filenames, progress-record layout, “queue of specs” and recommendation to start with two assistants are practical organizing choices. They can be adapted to the project. Prompt review and document verification are not cross-model execution benchmarks, a security audit or independent human review.

文件组合、进度格式、“规格队列”和两个助手起步是可调整的实践建议。文档核查不等于多模型成功率测试、安全审计或独立人工审稿。
