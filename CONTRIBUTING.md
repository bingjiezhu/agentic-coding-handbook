# Contributing · 参与改进

Reports about unclear instructions, inaccurate translations and outdated tool behavior are welcome. Please include the language, chapter, relevant sentence, what you expected it to mean and a suggested correction. For tool-specific claims, include the version and a primary source or reproducible observation. Do not include credentials, private project data or unrelated chat history.

欢迎反馈看不懂的说明、翻译问题或过时的工具用法。请写明语言、章节、具体句子、你的理解和修改建议。工具问题请附版本与官方资料或可复现观察，不要上传密钥和私密数据。

## Editing

1. Edit the appropriate chapter under `src/zh/` or `src/en/`.
2. Preserve corresponding meaning and prompt boundaries in the other language. Explain any intentional difference.
3. Run `python3 scripts/export_markdown.py`; do not separately maintain generated `docs/` or `prompts/`.
4. For PDF changes, follow [BUILDING.md](BUILDING.md), run the checks and inspect the rendered pages. Do not report a check as passed if it was not run.
5. Keep a contribution focused and explain the correction and its evidence in the pull request.

Issues and pull requests can be written in English or Chinese. This is an independent educational handbook, not official documentation for any named tool.
