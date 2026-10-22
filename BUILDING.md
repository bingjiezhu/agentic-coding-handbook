# Building the Handbook · 构建说明

You can read the Markdown or download the PDFs without installing anything. The steps below are for editing the source or rebuilding the artifacts.

只阅读教程或下载 PDF 不需要安装软件。下面用于修改源码和重新构建。

## Requirements

- Python 3.9 or later; `python3 -m pip install -r requirements.txt` for verification.
- XeLaTeX with the packages used in `src/shared/style.tex` and each language's style file. A full TeX Live or MacTeX installation is the simplest option. For a minimal Linux setup, include XeTeX, the recommended and extra LaTeX collections, pictures, language support and fonts.
- Noto Serif CJK SC and Noto Sans CJK SC for Chinese. Charter, Avenir Next and Menlo reproduce the original macOS typography when available. Fallbacks are TeX Gyre Schola, TeX Gyre Heros and DejaVu Sans Mono. Do not copy proprietary fonts into the repository.
- Poppler (`pdftoppm`) for rendered page checks.

The English edition has its own typography settings to accommodate English text. Font substitutions may change pagination. Inspect the output rather than shrinking text to force a page count.

英文有单独的排版参数。更换字体可能改变分页，请检查生成结果，不要为了凑页数盲目缩小字体。

## Edit and export

Run commands from the repository root:

```sh
python3 scripts/export_markdown.py
python3 scripts/build.py --lang all
python3 scripts/verify.py --candidate --render
```

- `export_markdown.py` generates `docs/zh/`, `docs/en/` and both prompt collections from the corresponding LaTeX chapters. Do not edit generated Markdown separately.
- `build.py` compiles twice, checks for missing characters and overflow, and records input hashes under `verification/`. Candidate PDFs go into `build/zh/main.pdf` and `build/en/main.pdf`; it does not publish them.
- `verify.py` checks both languages, prompt bodies and placeholders, local Markdown links, diagram usage, English-only text and PDF content. With `--render`, page PNGs and contact sheets are written under `tmp/qa/` for visual review.

Review every rendered page. After the checks and visual review, promote the exact candidates:

```sh
python3 scripts/publish_artifacts.py
python3 scripts/verify.py
```

The promotion script copies both PDFs into `pdf/` and writes a SHA-256 artifact manifest. It requires candidate checks for the current PDF hashes; visual inspection remains a separate human or agent responsibility. The default verification checks the published PDFs and source fingerprints. The GitHub workflow checks committed artifacts and that generated Markdown is current; it does not run learner tasks or prove prompt reliability.

## Diagrams

The PDFs already include checked-in vector diagram PDFs, so diagram rendering is optional for normal builds. English SVGs preserve the Chinese diagrams' relationships and geometry while translating labels.

To regenerate the English figures after editing the translation map:

```sh
python3 scripts/translate_diagrams.py
npm install --no-save playwright
npx playwright install chromium
node scripts/render_diagrams.cjs
```

Use `BROWSER_EXECUTABLE` to point to an existing Chromium/Chrome executable instead of Playwright's browser. The renderer checks label bounds and text overlap, then exports SVG-based PNG/PDF assets. It uses installed fonts and blocks network requests. English figure typography uses Noto Sans or DejaVu Sans. Inspect regenerated diagrams and rerun the document checks before publishing.

Chinese figures are preserved from the confirmed source edition. Their `data.json`, SVG, PNG and PDF files are included for reference and editing; the English translation map covers the labels in the included figures.

## Source of truth

- `src/{zh,en}/*.tex`: language-specific text and prompt cards.
- `src/shared/style.tex`: shared visual settings and font fallbacks.
- `assets/diagrams/{zh,en}/`: figure assets.
- `verification/origin.json`: the Chinese source edition and original fingerprints.
- `verification/artifacts.json`: published PDF/source integrity manifest.

Chapter structure and thirteen prompt cards are aligned across languages. The Chinese edition preserves the confirmed text; changing meaning requires reviewing the corresponding English text as well.
