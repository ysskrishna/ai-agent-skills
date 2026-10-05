# AGENTS.md

This file provides guidance to AI coding agents (Claude Code, Cursor, Copilot, Antigravity, etc.) when working with code in this repository.

## Repository overview

This is a curated collection of skills for AI Agents. Skills are packaged instructions and scripts that extend your coding agents capabilities.


## Repository structure

```
skills/
  {skill-name}/
    SKILL.md
    references/
      example.md    # required; one worked example
evals/
  {skill-name}.json # required; trigger eval queries (see evals/README.md)
scripts/            # publish_clawhub.py (ClawHub sync), validate_repo.py (repo checks)
.claude-plugin/     # Claude Code plugin + marketplace metadata
.github/workflows/  # validation on PRs, release automation (GitHub Releases on version tags)
```

Run `bash validate-skills.sh` before every commit. It checks each skill against the spec and runs `scripts/validate_repo.py` (description rules, example and eval files, and that the files below stay in sync).

When you add or rename a skill, keep these in sync:

- [README.md](README.md) — **Skills** table (including **Registry** badge column), **Installation** section, and footer ClawHub link when applicable.
- [evals/](evals/) — `evals/{skill-name}.json` with 8 should-trigger and 8 near-miss should-not-trigger queries.
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

### ClawHub slugs are per owner

Several owners can publish the same slug, so a slug already in use does not block publishing under `ysskrishna`. The cost is ambiguity for users (`clawhub inspect <slug>` and likely `install` report `AMBIGUOUS_SKILL_SLUG`). Policy: use the natural skill name as the slug, accept collisions, and remap only when a name is unusable.

- Check state with `python3 scripts/publish_clawhub.py plan`. It reads my version through the registry's `owner` parameter and lists other owners of the same slug.
- Do not rely on `clawhub inspect <slug>` to decide whether a slug exists. It fails on ambiguous slugs and can miss skills that `clawhub search` finds. Use inspect and search together when scouting a new name.

## Creating a new skill

Skills follow the [Agent Skills Open Standard](https://agentskills.io/).

1. Create `skills/{skill-name}/SKILL.md` with the required frontmatter (see below). Keep it at or under 120 lines.
2. Add `skills/{skill-name}/references/example.md` (one realistic worked case, with invented inputs labeled as such). Add other deep-dive files under `references/` and link them from `SKILL.md` instead of inflating the main file.
3. Add `evals/{skill-name}.json` (see [evals/README.md](evals/README.md)).
4. Register the skill in [README.md](README.md).
   - Add a row to the **Skills** table with a **Registry** badge (see [README registry badges (ClawHub)](#readme-registry-badges-clawhub)).
   - Add the skill to `clawhub_slug_map` in [scripts/publish_clawhub.py](scripts/publish_clawhub.py) if it is published on ClawHub.
   - Extend **Installation** with a Claude Code line: `/plugin install {skill-name}@ai-agent-skills`.
   - Extend **Installation** with a [skills.sh](https://skills.sh) line: `npx skills add ysskrishna/ai-agent-skills --skill {skill-name}`.
   - Extend **Installation** with a GitHub CLI line: `gh skill install ysskrishna/ai-agent-skills {skill-name}`.
   - Follow the examples already in the README.
5. Register the skill in [.claude-plugin/marketplace.json](.claude-plugin/marketplace.json).
   - Add a matching entry to the `plugins` array (`name`, `source`, `description`, and `skills`). The `description` must equal the `SKILL.md` description exactly.
   - Ensure `name` matches the skill directory and the `name` field in `SKILL.md` frontmatter so `/plugin install` resolves correctly.
6. Add the skill name to `keywords` in [.claude-plugin/plugin.json](.claude-plugin/plugin.json).
7. If the skill is a new thinking method, add it to the `thinking-method-selector` table and fallback outlines.
8. Run `bash validate-skills.sh`.

---

## Writing `SKILL.md` files

`SKILL.md` is YAML frontmatter followed by Markdown instructions.

### Frontmatter (required)

```yaml
---
name: skill-name
description: >
  Use for <method name>, or when the user <situation>: "<trigger phrase>",
  "<trigger phrase>", "<trigger phrase>". <What it does in one clause>.
  Skip for <task shapes>.
---
```

| Field         | Required | Constraints |
| ------------- | -------- | ----------- |
| `name`        | Yes      | 1–64 chars. Lowercase alphanumeric and hyphens only. Must match the directory name. |
| `description` | Yes    | 1–1024 chars by the spec; this repo targets 200–350. Primary trigger signal: imperative when-to-use, user intent, concrete triggers (see **Description field** below). |
| `license`     | No       | License name or reference to a bundled license file. |
| `metadata`    | No       | Arbitrary key-value pairs (e.g. `author`, `version`). |

When you ship meaningful updates to a skill, bump `metadata.version` to the release date as `YYYY.M.D` (for example `2026.10.5`). `scripts/publish_clawhub.py` compares it with the ClawHub version and publishes when they differ.

### Name field rules

- Lowercase letters, numbers, and hyphens only (`a-z`, `0-9`, `-`).
- Must not start or end with `-`.
- Must not contain consecutive hyphens (`--`).
- Must match the parent directory name.

### Description field (critical)

The description is how agents decide whether to activate the skill. See [Optimizing skill descriptions](https://agentskills.io/skill-creation/optimizing-descriptions) for trigger testing and iteration.

Write the `description` so it works at a glance:

1. **Imperative open** — start with **“Use …”** (validated: the description must start with `Use `). The agent is choosing an action; tell it when to load this skill, not only what the skill contains.
2. **Method name in sentence one** — people who name the method (“critical thinking”, “six thinking hats”) must still match. Then the situation.
3. **User situation and quoted phrases** — most users never name a method. List the situations and 3–4 realistic phrases ("what could go wrong?", "A or B?") that should load the skill.
4. **One clause on what it does**, then a **Skip** clause (required, validated). State boundaries as **task shape** (execution-only, plain factual lookup, exact data available, etc.). **Do not** point at other skills in this repo by name or “use skill Y instead” routing; those lists go stale as the catalog grows. Cross-skill routing lives in the `thinking-method-selector` body.
5. **No meta text** — never describe how the match works (“naming it or directing use with typos is decisive”). Validation rejects that boilerplate. It wastes the first characters, which listings truncate first.
6. **Length** — 200–350 characters. Claude Code caps each listing entry at 1,536 characters and drops descriptions when the whole listing exceeds its budget (1% of the context window), so every extra character costs every skill.
7. **First 80 characters unique** across skills (validated).

Put trigger guidance in **frontmatter `description`**, not only in the body—the body loads after the skill is already chosen. Test changes against the queries in `evals/{skill-name}.json`, adding queries that failed.

### Body content

Write concise, imperative instructions. Prefer short examples and links to `references/` for long material.

**Suggested structure:**

1. When to use, with a Skip line.
2. Before you start (state focus and pass, gather first, light path).
3. The method steps.
4. Pitfalls, then a checklist.
5. A pointer to `references/example.md` and any deeper files.

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
- Keep every skill **self-contained**. Users install skills one at a time (`--skill`, `/plugin install`, `gh skill install`), so a link to another skill's files or a shared `references/` file will break. Repeat short shared rules (light path, gather first) in each skill.
- **Light path and gather-first:** each skill states how to scale down for a small ask, and tells the agent to read files, search or run queries before marking evidence missing or asking questions.
- **Fixed section order** in the body: When to use (with Skip), Before you start, the method steps, Pitfalls, Checklist.

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
