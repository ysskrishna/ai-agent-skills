# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0] - 2026-10-05

### Added

- **Seven new skills** - [`five-whys`](skills/five-whys/SKILL.md), [`swot-analysis`](skills/swot-analysis/SKILL.md), [`pre-mortem`](skills/pre-mortem/SKILL.md), [`tradeoff-analysis`](skills/tradeoff-analysis/SKILL.md), [`prioritization`](skills/prioritization/SKILL.md), [`fermi-estimation`](skills/fermi-estimation/SKILL.md), and [`thinking-method-selector`](skills/thinking-method-selector/SKILL.md), a router that picks a method when the user names none and carries a fallback outline for every other skill.
- **Worked example per skill** - `skills/<name>/references/example.md` for all 17 skills.
- **Trigger eval queries** - `evals/<name>.json` with 8 should-trigger and 8 near-miss queries per skill, plus [`evals/README.md`](evals/README.md).
- **Repository checks** - [`scripts/validate_repo.py`](scripts/validate_repo.py), run by `validate-skills.sh`: description rules, example and eval files, README / marketplace / plugin keywords / ClawHub slug map in sync, router coverage, equal plugin and marketplace versions.

### Changed

- **All descriptions are intent-led** - each opens with the method name, then the situations and phrases it fits, then a Skip clause (253-300 characters, was 549-745 with a shared boilerplate prefix that is now banned).
- **Skill bodies** - every skill gains When to use / Skip, a light path for small asks, a gather-first rule, pitfalls, and one tag vocabulary. `analytical-thinking` and `design-thinking` no longer contradict their own Setup text. `six-thinking-hats` defines the opening Blue block, confirms the closing Blue in Custom mode, and replaces the Depth table with the light path. `lateral-thinking` concept fan follows de Bono (directions, concepts, ideas). `strategic-thinking` states its time horizons per domain.
- **[README.md](README.md)** - skills grouped by the job to be done with short "use it when" lines, install lines for all 17 skills, usage examples that describe a problem instead of naming a method.
- **[AGENTS.md](AGENTS.md)** - new description rules, required example and eval files, self-contained skills, per-owner ClawHub slug policy, calendar skill versions.
- **CI** - [validate-skills.yml](.github/workflows/validate-skills.yml) also runs on changes to `evals/`, `scripts/`, `README.md` and `.claude-plugin/`.

### Fixed

- **`scripts/publish_clawhub.py`** - `plan` reported `critical-thinking`, `design-thinking` and `lateral-thinking` as new because `clawhub inspect` fails on slugs shared with other owners. State now comes from the registry with the owner parameter, retries on rate limits, stops on unexpected errors, and lists other owners of a slug.
- **CHANGELOG** - `[1.1.0]` now has its release date.

## [1.1.0] - 2026-05-19

### Added

- **Thinking-partner skills** — Nine new sequential workflows aligned with the six-thinking-hats pattern: [`critical-thinking`](skills/critical-thinking/SKILL.md), [`systems-thinking`](skills/systems-thinking/SKILL.md), [`creative-thinking`](skills/creative-thinking/SKILL.md), [`strategic-thinking`](skills/strategic-thinking/SKILL.md), [`analytical-thinking`](skills/analytical-thinking/SKILL.md), [`lateral-thinking`](skills/lateral-thinking/SKILL.md), [`design-thinking`](skills/design-thinking/SKILL.md), [`first-principles-thinking`](skills/first-principles-thinking/SKILL.md), and [`ethical-thinking`](skills/ethical-thinking/SKILL.md). Each is registered in [README.md](README.md) and [.claude-plugin/marketplace.json](.claude-plugin/marketplace.json).
- **Skill validation** — [`validate-skills.sh`](validate-skills.sh) audits each `skills/*/SKILL.md` against the [Agent Skills specification](https://agentskills.io/specification.md) (frontmatter, naming, description length, optional structure). [`.github/workflows/validate-skills.yml`](.github/workflows/validate-skills.yml) runs it on pushes and pull requests when skills or the script change.

### Changed

- **Thinking-partner skills** — Removed fixed **Modes** / **Depth** tables from the nine skills above; each skill now uses one **default pass** with optional user-requested tweaks.
- **[`six-thinking-hats`](skills/six-thinking-hats/SKILL.md)** — Tighter body and refreshed frontmatter `description` triggers (aligned with the newer skills’ activation phrasing).
- **[README.md](README.md)** — CI, license, and release badges; overview and install guidance (skills.sh first, per-skill `npx skills add … --skill …`, expanded Claude Code marketplace commands); full skills table; usage examples.
- **[AGENTS.md](AGENTS.md)** — Updated authoring and release guidance for the larger catalog.
- **[`.claude-plugin/marketplace.json`](.claude-plugin/marketplace.json)** — Catalog entries and descriptions for every skill; plugin [keywords](.claude-plugin/plugin.json) extended for discoverability.

### Removed

- **Bundled Cursor plugin files** — Removed `.cursor-plugin/` from the repository (last shipped in [v1.0.1 tree](https://github.com/ysskrishna/ai-agent-skills/tree/v1.0.1/.cursor-plugin)); skills remain installable via the Agent Skills standard and other documented paths.
- **`gemini-extension.json`** — Removed the standalone Gemini extension manifest from the repo root.


## [1.0.1]

### Changed

- **Documentation** — [AGENTS.md](AGENTS.md) now lists every manifest and changelog location to update when cutting a repository release, alongside per-skill `metadata.version` guidance.
- **Plugin metadata** — Bumped bundled `version` fields to `1.0.1` in Claude plugin, Cursor plugin, both marketplace manifests, and [gemini-extension.json](gemini-extension.json).


## [1.0.0]

### Added

- **`six-thinking-hats` skill** — Six Thinking Hats workflow with hat-set modes (Full, Creative, Risk, Decision, Custom) and depth levels (Quick, Standard, Deep Dive).
- **Cursor plugin** — `.cursor-plugin/` metadata and marketplace listing for distributing skills in Cursor.
- **Claude Code plugin** — `.claude-plugin/` metadata and marketplace listing for Claude Code.
- **Repository foundations** — README, MIT license, CODEOWNERS, and GitHub Sponsors funding metadata.


[1.2.0]: https://github.com/ysskrishna/ai-agent-skills/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/ysskrishna/ai-agent-skills/compare/v1.0.1...v1.1.0
[1.0.1]: https://github.com/ysskrishna/ai-agent-skills/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/ysskrishna/ai-agent-skills/releases/tag/v1.0.0
