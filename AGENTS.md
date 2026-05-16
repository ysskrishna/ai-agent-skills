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
.github/workflows/  # release automation (GitHub Releases on version tags)
```

When you add or rename a skill, keep these in sync:

- [README.md](README.md) — **Skills** table and **Installation** section.
- [.claude-plugin/marketplace.json](.claude-plugin/marketplace.json) — `plugins` catalog for Claude Code.
- Claude Code install line: `/plugin install {skill-name}@ai-agent-skills`.
- [skills.sh](https://skills.sh) install line: `npx skills add ysskrishna/ai-agent-skills/{skill-name}`.

## Creating a new skill

Skills follow the [Agent Skills Open Standard](https://agentskills.io/).

1. Create `skills/{skill-name}/SKILL.md` with the required frontmatter (see below).
2. Add optional deep-dive files under `skills/{skill-name}/references/` and link them from the body of `SKILL.md` instead of inflating the main file.
3. Register the skill in [README.md](README.md).
   - Add a row to the **Skills** table.
   - Extend **Installation** with a Claude Code line: `/plugin install {skill-name}@ai-agent-skills`.
   - Extend **Installation** with a [skills.sh](https://skills.sh) line: `npx skills add ysskrishna/ai-agent-skills/{skill-name}`.
   - Follow the examples already in the README.
4. Register the skill in [.claude-plugin/marketplace.json](.claude-plugin/marketplace.json).
   - Add a matching entry to the `plugins` array (`name`, `source`, `description`, and `skills` as needed).
   - Ensure `name` matches the skill directory and the `name` field in `SKILL.md` frontmatter so `/plugin install` resolves correctly.
5. If the skill should surface in plugin discovery, consider updating keywords.
   - [.claude-plugin/plugin.json](.claude-plugin/plugin.json)

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

---

## Repository release versioning

When you ship a **repository** semver release (distinct from per-skill `metadata.version` in `SKILL.md`, documented under **Writing `SKILL.md` files** above), update these together:

- [CHANGELOG.md](CHANGELOG.md) — add `## [X.Y.Z]` with release notes and a footer reference link at the bottom (e.g. `releases/tag/vX.Y.Z`, or `compare/vA.B.C...vX.Y.Z` per [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)).
- [.claude-plugin/plugin.json](.claude-plugin/plugin.json) — top-level `version`.
- [.claude-plugin/marketplace.json](.claude-plugin/marketplace.json) — `metadata.version`.

Then push an annotated Git tag `vX.Y.Z`; [.github/workflows/release.yml](.github/workflows/release.yml) creates the GitHub Release (notes prefer the tag message, else the matching changelog section).
