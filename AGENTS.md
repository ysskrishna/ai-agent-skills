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

- [README.md](README.md) — **Skills** table (including **Registry** badge column), **Installation** section, and footer ClawHub link when applicable.
- [scripts/publish_clawhub.py](scripts/publish_clawhub.py) — `clawhub_slug_map` entry (and publish when listing on ClawHub).
- [.claude-plugin/marketplace.json](.claude-plugin/marketplace.json) — `plugins` catalog for Claude Code.
- Claude Code install line: `/plugin install {skill-name}@ai-agent-skills`.
- [skills.sh](https://skills.sh) install line: `npx skills add ysskrishna/ai-agent-skills --skill {skill-name}`.
- GitHub CLI install line: `gh skill install ysskrishna/ai-agent-skills {skill-name}`.

## README registry badges (ClawHub)

The README **Skills** table has a right-hand **Registry** column (generic label—not “ClawHub” in the header). Each cell is a shields.io badge linking to that skill’s public listing on [ClawHub](https://clawhub.ai/user/ysskrishna).

**Per-skill badge** (copy pattern; substitute `{clawhub-slug}`):

```markdown
[![Clawhub](https://img.shields.io/badge/Clawhub-informational)](https://clawhub.ai/ysskrishna/{clawhub-slug})
```

**Listing URL:** `https://clawhub.ai/ysskrishna/{clawhub-slug}`

**Slug source:** `clawhub_slug_map` in [scripts/publish_clawhub.py](scripts/publish_clawhub.py). Keys are skill **directory** names under `skills/`; values are the ClawHub slug. When they match, use the directory name as the slug. Remapped today:

| Directory | ClawHub slug |
| --------- | ------------ |
| `six-thinking-hats` | `six-hats-thinking` |
| `first-principles-thinking` | `first-principles-reasoning` |

Add a new row to `clawhub_slug_map` whenever you publish a skill to ClawHub, then add the matching **Registry** badge in the README table. 

## Creating a new skill

Skills follow the [Agent Skills Open Standard](https://agentskills.io/).

1. Create `skills/{skill-name}/SKILL.md` with the required frontmatter (see below).
2. Add optional deep-dive files under `skills/{skill-name}/references/` and link them from the body of `SKILL.md` instead of inflating the main file.
3. Register the skill in [README.md](README.md).
   - Add a row to the **Skills** table with a **Registry** badge (see [README registry badges (ClawHub)](#readme-registry-badges-clawhub)).
   - Add the skill to `clawhub_slug_map` in [scripts/publish_clawhub.py](scripts/publish_clawhub.py) if it is published on ClawHub.
   - Extend **Installation** with a Claude Code line: `/plugin install {skill-name}@ai-agent-skills`.
   - Extend **Installation** with a [skills.sh](https://skills.sh) line: `npx skills add ysskrishna/ai-agent-skills --skill {skill-name}`.
   - Extend **Installation** with a GitHub CLI line: `gh skill install ysskrishna/ai-agent-skills {skill-name}`.
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
description: >
  Use this skill when the user ... (intent and triggers). Optional: skip when
  ... (task-shape boundaries only—do not route to other skills by name).
---
```

| Field         | Required | Constraints |
| ------------- | -------- | ----------- |
| `name`        | Yes      | 1–64 chars. Lowercase alphanumeric and hyphens only. Must match the directory name. |
| `description` | Yes    | 1–1024 chars. Primary trigger signal: imperative when-to-use, user intent, concrete triggers (see **Description field** below). |
| `license`     | No       | License name or reference to a bundled license file. |
| `metadata`    | No       | Arbitrary key-value pairs (e.g. `author`, `version`). |

When you ship meaningful updates to a skill, bump `metadata.version` (or your chosen versioning field) if the skill uses one—see [skills/six-thinking-hats/SKILL.md](skills/six-thinking-hats/SKILL.md) for an example.

### Name field rules

- Lowercase letters, numbers, and hyphens only (`a-z`, `0-9`, `-`).
- Must not start or end with `-`.
- Must not contain consecutive hyphens (`--`).
- Must match the parent directory name.

### Description field (critical)

The description is how agents decide whether to activate the skill. See [Optimizing skill descriptions](https://agentskills.io/skill-creation/optimizing-descriptions) for trigger testing and iteration.

Write the `description` so it works at a glance:

1. **Imperative open** — start with **“Use this skill when…”** (or equivalent). The agent is choosing an action; tell it when to load this skill, not only what the skill contains.
2. **User intent first** — say what the user is trying to accomplish (decide, audit, brainstorm in a fixed structure, etc.), then the method labels. Avoid opening with implementation-only framing (“Applies the X framework…”) without a when-to-use clause in the same breath.
3. **Obvious phrasing early** — if people often say the skill name or a stock phrase (“critical thinking”, “six thinking hats”), put that **near the start**, not only buried in a long parenthetical list. You can still add indirect triggers after.
4. **Concrete triggers** — topics, tasks, casual and indirect phrasing, and “even if they don’t say …” style coverage where it helps recall.
5. *(Optional)* **When not to use** — only if it materially cuts false activations. State boundaries as **task shape** (execution-only, plain factual lookup, single-angle hot take with no structured pass, etc.). **Do not** point at other skills in this repo by name, method, or “use skill Y instead” routing—those lists do not scale as the catalog grows and they go stale fast. The [Agent Skills Open Standard](https://agentskills.io/) does not require negatives—many published skills omit them.

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

### Skill authoring quality (recommended)

- Use **minimal, consistent tagging**; avoid parallel bracket vocabularies (e.g. Setup vs phases) without a one-line rule for where each applies. Prefer prose in Setup and a small tag set only where structure matters.
- Keep **checklists aligned** with body and execution rules—no bullets that contradict optional paths. Either specify branching fully or **prefer a fixed canonical phase order** unless the skill truly needs skips or reorders; if phases vary by run, **Setup must state the exact sequence** for that response.
- When a rule **forbids** something in a phase (e.g. no new factual assertions), say **what to do instead** (structural gap label, ask the user, etc.).
- **Thread early distinctions** through later phases and Conclusion (e.g. factual vs normative): if you introduce a split up front, say how later steps use it.
- Align **falsifiers, uncertainty, and voice** to the skill’s **Focus** (whose claim, which party, impersonal review)—avoid ambiguous first person.
- Frame short **example lists** (biases, fallacies, prompts) as **examples**, not exhaustive catalogs, unless you intend completeness.
- Prefer **one plain sentence** on strength of case or uncertainty over **ordinal scales** (e.g. High / Medium / Low) unless you commit to maintaining a rubric in the skill.
- When a **named workflow step** could be mistaken for generic **Setup**, state explicitly whether Setup satisfies that step or a **separate labeled section** is required.
- For content shared across many skills, use **one** `references/*.md` and **one-line links** from each skill instead of duplicating large routing or comparison blocks.

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
