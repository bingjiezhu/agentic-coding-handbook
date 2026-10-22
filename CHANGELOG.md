# Changelog · 更新记录

## v1.1.1 · 2026-10-22

Repository correctness fixes; handbook content and project workflow unchanged.

- Corrected CFF citation metadata: the repository is a software artifact, with a preferred manual citation for the handbook.
- Project inventory now recognizes commented YAML booleans and reports ambiguous or unsupported invocation settings as unknown.
- Added regression checks for these cases and the CFF root type.

修正引用元数据与项目检查脚本的配置识别，补充回归检查；教程正文与项目引导流程保持原样。

## v1.1.0 · 2026-10-22

Project-guide entry point and reusable Skill.

- START.md instructs an agent how to begin from the shared repository link.
- Project Guide selects the next stage and routes substantial planning to the actual installed Spec Kit integration.
- Added conditional setup/invocation instructions, progress handoffs and a read-only project inspector.
- Simplified main to reusable guidance, bilingual reading material and SVG diagrams; publication PDFs and LaTeX sources remain in the v1.0.0 release.
- Existing guide and project permissions remain authoritative. URL access, Skill loading and user-only invocation restrictions are reported explicitly.

新增给 AI 的项目引导入口和可安装技能。根据项目阶段衔接需求、调研、Spec Kit 计划、实现、验收和续做；精简主分支，出版文件保留在教程发布页。

## v1.0.0 · 2026-10-22

First bilingual public edition of **Agentic Coding Handbook / Vibe Coding in Practice**.

- English and Simplified Chinese PDFs, 15 pages each.
- Twelve matching chapters, thirteen copyable prompts per language and translated diagrams.
- GitHub reading pages generated from editable LaTeX sources.
- Primary-source references, translation terminology, build instructions and artifact verification.
- Chinese text preserved from the confirmed October 21 manuscript; English translated for this release.
- Educational content under CC BY 4.0; build and export scripts under MIT.

首个中英文公开版：两份15页PDF、十二章、每种语言十三条提示词，以及对应图表。提供GitHub在线阅读、LaTeX源码、资料来源、术语对照和构建检查。中文沿用已确认稿，英文按对应内容翻译。教程采用CC BY 4.0，构建与导出脚本采用MIT。
