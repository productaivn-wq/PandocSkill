---
name: PandocSkill
description: "A dedicated Markdown-to-PDF/DOCX compiler using Pandoc. Perfect for academic, highly structured, or complex typographic formatting."
version: 1.0.0
status: active
updated: 2026-05-07
---

# PandocSkill

**Role:** This skill converts agent-written Markdown into perfectly styled PDFs and DOCX files using Pandoc.

## Agent Instructions

Unlike `DocumentCraft`, `PandocSkill` expects highly rigorous Markdown syntax, particularly regarding YAML frontmatter and citations.

### 1. File Structure
Your `.md` file MUST start with a YAML block:
```yaml
---
title: "Project Alpha Strategy"
author: "Antigravity Agent"
date: "2026-05-07"
toc: true
---
```

### 2. Compilation
Once you have written the Markdown, use the compiler script to generate the deliverables. You do not need to install Pandoc locally; the script assumes it is either installed or available via standard PATH.

**Generate PDF:**
```bash
python C:/Users/thanb/.gemini/antigravity/skills/PandocSkill/scripts/compile.py report.md --format pdf
```

**Generate DOCX:**
```bash
python C:/Users/thanb/.gemini/antigravity/skills/PandocSkill/scripts/compile.py report.md --format docx
```

### 3. Rules for Vibe Working
1. Never edit the generated `.pdf` or `.docx` directly.
2. If the user requests a formatting change, edit the `.md` file and re-run the compilation script.
3. If compiling fails due to a LaTeX error, simplify your Markdown tables or check for unescaped special characters (like `$` or `%`).
