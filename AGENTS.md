# AGENTS.md

This file provides guidance to AI coding agents (Claude Code, Cursor, Copilot, Antigravity, etc.) when working with code in this repository.

## Repository overview

This is a curated collection of skills for AI Agents. Skills are packaged instructions and scripts that extend your coding agents capabilities.


## Repository structure

```
skills/
  {skill-name}/
    SKILL.md
    references/     # optional; add when a skill needs extra on-demand docs
.claude-plugin/     # Claude Code plugin + marketplace metadata
.cursor-plugin/     # Cursor plugin + marketplace metadata
.github/workflows/  # release automation (GitHub Releases on version tags)
```

When you add or rename a skill, keep the [README](README.md) skills table in sync.

## Creating a new skill

Skills follow the [Agent Skills Open Standard](https://agentskills.io/).

1. Create `skills/{skill-name}/SKILL.md` with the required frontmatter (see below).
2. Add optional deep-dive files under `skills/{skill-name}/references/` and link them from the body of `SKILL.md` instead of inflating the main file.
3. Register the skill in [README.md](README.md).
4. If the skill should surface in plugin discovery, consider updating keywords in [.claude-plugin/plugin.json](.claude-plugin/plugin.json) / [.cursor-plugin/plugin.json](.cursor-plugin/plugin.json).

---

## Writing `SKILL.md` files

`SKILL.md` is YAML frontmatter followed by Markdown instructions.

### Frontmatter (required)

```yaml
---
name: skill-name
description: What this skill does and when to use it.
---
```

| Field         | Required | Constraints |
| ------------- | -------- | ----------- |
| `name`        | Yes      | 1–64 chars. Lowercase alphanumeric and hyphens only. Must match the directory name. |
| `description` | Yes    | 1–1024 chars. Describe what the skill does **and** when to use it (this is the primary trigger signal). |
| `license`     | No       | License name or reference to a bundled license file. |
| `metadata`    | No       | Arbitrary key-value pairs (e.g. `author`, `version`). |

When you ship meaningful updates to a skill, bump `metadata.version` (or your chosen versioning field) if the skill uses one—see [skills/six-thinking-hats/SKILL.md](skills/six-thinking-hats/SKILL.md) for an example.

### Name field rules

- Lowercase letters, numbers, and hyphens only (`a-z`, `0-9`, `-`).
- Must not start or end with `-`.
- Must not contain consecutive hyphens (`--`).
- Must match the parent directory name.

### Description field (critical)

The description is how agents decide whether to activate the skill. Include:

1. What the skill does.
2. Concrete triggers (topics, tasks, phrasing) for when to use it.

Put trigger guidance in **frontmatter `description`**, not only in the body—the body loads after the skill is already chosen.

### Body content

Write concise, imperative instructions. Prefer short examples and links to `references/` for long material.

**Suggested structure:**

1. Quick start or core workflow.
2. Key patterns with examples.
3. Pointers to reference files for advanced topics.

### Progressive disclosure

1. **Metadata** — always available to the agent.
2. **Body** — loaded when the skill triggers; keep it lean.
3. **References** — load on demand via links from the body.

---

## Optional reference files

If you add `references/*.md`, use a consistent, scannable format. Example pattern:

```markdown
---
title: Short title
impact: HIGH
tags: keyword-one, keyword-two
---

## Title

Brief explanation.

**Avoid:** bad pattern or snippet.

**Prefer:** good pattern or snippet.
```
