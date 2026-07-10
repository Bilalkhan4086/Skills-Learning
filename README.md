# Skills Learning

This repository is a workspace for creating, improving, and testing Codex/OpenAI-style skills.

The repo currently includes a local `seo-reviewer` skill and supporting files. The `.agents/` directory may contain installed or cached skills used during local development, but it is ignored by Git and should be treated as local machine state.

## Repository Layout

```text
.
├── skills/
│   └── seo-reviewer/
│       ├── SKILL.md
│       ├── evals/
│       │   └── evals.json
│       └── references/
│           └── audit-checklist.md
├── skills-lock.json
└── README.md
```

## What Is a Skill?

A skill is a folder that teaches Codex how to perform a specialized workflow. Each skill must include a `SKILL.md` file with YAML frontmatter:

```markdown
---
name: seo-reviewer
description: Review websites, landing pages, web apps, and source code for SEO...
---
```

The `description` controls when the skill is triggered. The body of `SKILL.md` explains how Codex should perform the task.

Optional folders:

- `references/`: deeper documentation loaded only when needed.
- `evals/`: test prompts and expectations for validating skill behavior.
- `scripts/`: reusable scripts for deterministic or repetitive work.
- `assets/`: templates, images, or other files used by the skill.

## Included Skill

### `seo-reviewer`

Use this skill when you want Codex to audit websites, landing pages, web apps, or source code for SEO issues.

Example prompts:

```text
Use the seo-reviewer skill to audit https://example.com for technical SEO and metadata issues.
```

```text
Review this Next.js app for SEO before launch. Focus on metadata, sitemap, robots, structured data, and rendering issues.
```

```text
Audit this product page HTML for ecommerce SEO and AI search readiness.
```

The skill is located at:

```text
skills/seo-reviewer/SKILL.md
```

Its deeper checklist is in:

```text
skills/seo-reviewer/references/audit-checklist.md
```

Its test prompts are in:

```text
skills/seo-reviewer/evals/evals.json
```

## Using a Skill with Codex

In a Codex prompt, reference the skill by name or path:

```text
[$seo-reviewer](skills/seo-reviewer/SKILL.md) audit my landing page for SEO.
```

You can also ask naturally:

```text
Audit this website for SEO and tell me the highest-impact fixes.
```

If the skill is installed or available in the active Codex environment, Codex should load the skill instructions before performing the work.

## Adding a New Skill

Create a new folder under `skills/`:

```text
skills/my-new-skill/
└── SKILL.md
```

Minimum `SKILL.md` structure:

```markdown
---
name: my-new-skill
description: Explain what this skill does and when Codex should use it.
---

# My New Skill

Use this skill to...
```

Guidelines:

- Keep the skill body focused and actionable.
- Put trigger wording in the frontmatter `description`.
- Move long checklists or domain references into `references/`.
- Add realistic test prompts in `evals/evals.json`.
- Prefer reusable scripts in `scripts/` when a workflow is repetitive.

## Validating a Skill

If the local `skill-creator` helper is available, validate a skill with:

```bash
python3 .agents/skills/skill-creator/scripts/quick_validate.py skills/seo-reviewer
```

Validate eval JSON with:

```bash
python3 -m json.tool skills/seo-reviewer/evals/evals.json >/dev/null
```

Check for trailing whitespace or unresolved merge markers:

```bash
rg -n "[ \t]$|^<{7}|^={7}$|^>{7}" skills/seo-reviewer
```

## Running Skill Evals

The `evals/evals.json` file contains realistic prompts and expectations. These are used to compare skill behavior across iterations.

When using the `skill-creator` workflow, place run outputs in a sibling workspace, usually:

```text
seo-reviewer-workspace/
└── iteration-1/
```

Then use the local skill-creator viewer to review outputs and benchmark results.

## Lock File

`skills-lock.json` records external skill sources and hashes used in this workspace. It is useful for tracking where installed skills came from, but the actual local skill source in this repo lives under `skills/`.

If you add or update external skills, refresh the lock file using the same tool or workflow that installed those skills.

## Development Notes

- Do not commit generated outputs, local caches, logs, or `.agents/` contents unless intentionally needed.
- Keep `SKILL.md` files readable and under roughly 500 lines when possible.
- Prefer evidence-based workflows over generic checklists.
- When a skill supports multiple domains or frameworks, use `references/` files so Codex only loads the relevant details.
