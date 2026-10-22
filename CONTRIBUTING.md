# Contributing · 参与改进

Help make the project guide useful in actual work. Reports about confusing questions, wrong stage selection, failed Spec Kit integration or inaccurate translations are welcome. Include the language, task, tool/version, relevant file, what actually happened and the smallest useful reproduction. Exclude secrets and private project data.

欢迎反馈引导问题不清楚、下一步判断不对、Spec Kit 接入失败或翻译不准确。请写明语言、任务、工具与版本、具体文件、实际结果和可复现步骤，不上传密钥或私密数据。

## Making a change

1. For agent behavior, edit `START.md` or the self-contained `skills/project-guide/` package. For teaching material, edit corresponding files in `docs/zh/`, `docs/en/` and `prompts/`.
2. Preserve existing user goals and project conventions. Use a full Spec Kit workflow when useful, not for every tiny edit. Avoid adding repeated warnings or turning one example into a universal rule.
3. Use current official sources for integration and command claims. Distinguish a step invoked through the host from displaying its command or running CLI setup.
4. Follow [DEVELOPMENT.md](DEVELOPMENT.md) and run the relevant checks. Use temporary projects outside the real application for setup tests.
5. Keep changes focused. Do not commit local validation logs, temporary app files or duplicate PDF/image rendering assets.

Issues and pull requests can be in Chinese or English. Explain what behavior changed and what was actually tested; no need to invent a success rate.
