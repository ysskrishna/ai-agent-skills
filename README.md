# AI Agent Skills

[![Tests](https://github.com/ysskrishna/ai-agent-skills/actions/workflows/validate-skills.yml/badge.svg)](https://github.com/ysskrishna/ai-agent-skills/actions/workflows/validate-skills.yml) [![License: MIT](https://img.shields.io/github/license/ysskrishna/ai-agent-skills)](https://github.com/ysskrishna/ai-agent-skills/blob/main/LICENSE) [![GitHub release](https://img.shields.io/github/v/release/ysskrishna/ai-agent-skills?label=release)](https://github.com/ysskrishna/ai-agent-skills/releases) [![ClawHub](https://img.shields.io/badge/ClawHub-ysskrishna-informational)](https://clawhub.ai/user/ysskrishna) [![Author site](https://img.shields.io/badge/author-ysskrishna.space-informational)](https://ysskrishna.space)

A curated collection of cognitive workflows designed to upgrade your AI agents from simple code generators into strong collaborators for **decision support**, **brainstorming**, and **structured thinking**. Compatible with **Claude Code**, **Cursor**, **Codex CLI**, **Gemini CLI**, **Windsurf**, **Antigravity**, **OpenClaw**, and any tool that supports the same specification.

## Overview

Most coding assistants default to quick answers. Instead of one-off mega-prompts, this repository provides modular [`SKILL.md`](https://agentskills.io/) packs from the [Agent Skills](https://agentskills.io/) open standard—reusable frameworks for trade-offs, architectural choices, ideation, and explicit thinking in your agent's loop, grouped into three pillars:

- **Thinking lenses:** Six Thinking Hats; critical, systems, creative, strategic, analytical, and lateral thinking; design thinking; first-principles thinking; ethical reasoning.
- **Decision support:** Structured trade-off analysis, synthesis, and evaluation passes.
- **Brainstorming and critique:** Facilitation-style sequences for ideation and review (including adversarial angles where a skill calls for it).

## Skills

| Name | Description | Registry |
|------|-------------|----------|
| [`six-thinking-hats`](skills/six-thinking-hats/SKILL.md) | Use when the user asks for Six Thinking Hats, parallel thinking, or Edward de Bono (naming or directing use/apply/run with typos is decisive), or wants sequential six-hat facilitation: facts, feelings, risks, benefits, new ideas, then synthesis for decisions and brainstorms. | [![Clawhub](https://img.shields.io/badge/Clawhub-informational)](https://clawhub.ai/ysskrishna/six-hats-thinking) |
| [`critical-thinking`](skills/critical-thinking/SKILL.md) | Use when the user asks for critical thinking (naming or directing use/apply/run with typos is decisive), or wants claim and argument audit: assumptions, evidence, logic gaps, bias and fallacy scan, red team, devil's advocate, epistemic calibration. | [![Clawhub](https://img.shields.io/badge/Clawhub-informational)](https://clawhub.ai/ysskrishna/critical-thinking) |
| [`systems-thinking`](skills/systems-thinking/SKILL.md) | Use when the user asks for systems thinking (naming or directing use/apply/run with typos is decisive), or wants feedback loops, delays, stocks and flows, leverage points, unintended consequences, and holistic propagation across teams, products, and policies. | [![Clawhub](https://img.shields.io/badge/Clawhub-informational)](https://clawhub.ai/ysskrishna/systems-thinking) |
| [`creative-thinking`](skills/creative-thinking/SKILL.md) | Use when the user asks for creative thinking (naming or directing use/apply/run with typos is decisive), or wants divergent ideation: fluency, reframes, novel combinations, blue-sky variety, optional light convergence before commitment. | [![Clawhub](https://img.shields.io/badge/Clawhub-informational)](https://clawhub.ai/ysskrishna/creative-thinking) |
| [`strategic-thinking`](skills/strategic-thinking/SKILL.md) | Use when the user asks for strategic thinking (naming or directing use/apply/run with typos is decisive), or wants bets under constraints: where to play, how to win, roadmap narrative, tradeoffs, risks, portfolio prioritization, sequenced path. | [![Clawhub](https://img.shields.io/badge/Clawhub-informational)](https://clawhub.ai/ysskrishna/strategic-thinking) |
| [`analytical-thinking`](skills/analytical-thinking/SKILL.md) | Use when the user asks for analytical thinking (naming or directing use/apply/run with typos is decisive), or wants structured breakdown: hypotheses, metrics, evidence, MECE-ish trees, decision tables, explicit uncertainty in synthesis. | [![Clawhub](https://img.shields.io/badge/Clawhub-informational)](https://clawhub.ai/ysskrishna/analytical-thinking) |
| [`lateral-thinking`](skills/lateral-thinking/SKILL.md) | Use when the user asks for lateral thinking (naming or directing use/apply/run with typos is decisive), or wants provocations, concept fans, challenge questions, reframes to escape local optima when ideation stalls or feels incremental. | [![Clawhub](https://img.shields.io/badge/Clawhub-informational)](https://clawhub.ai/ysskrishna/lateral-thinking) |
| [`design-thinking`](skills/design-thinking/SKILL.md) | Use when the user asks for design thinking (naming or directing use/apply/run with typos is decisive), or wants human-centered discovery: empathize, define POV and HMW, ideate, low-fi prototype intent, falsifiable test plan for HCD and UX sprints. | [![Clawhub](https://img.shields.io/badge/Clawhub-informational)](https://clawhub.ai/ysskrishna/design-thinking) |
| [`first-principles-thinking`](skills/first-principles-thinking/SKILL.md) | Use when the user asks for first-principles thinking or first principles (naming or directing use/apply/run with typos is decisive), or wants to strip analogies, tag fundamentals, rebuild logic from bedrock, challenge defaults, sanity-check copycat strategies. | [![Clawhub](https://img.shields.io/badge/Clawhub-informational)](https://clawhub.ai/ysskrishna/first-principles-reasoning) |
| [`ethical-thinking`](skills/ethical-thinking/SKILL.md) | Use when the user asks for ethical thinking (naming or directing use/apply/run with typos is decisive), or wants values, harms, benefits, power asymmetry, justice, consent, fair process—moral review, AI and data ethics, stakeholder harm scans beyond legality. | [![Clawhub](https://img.shields.io/badge/Clawhub-informational)](https://clawhub.ai/ysskrishna/ethical-thinking) |




## Installation

### skills.sh (recommended)

Install via the [skills.sh](https://skills.sh) CLI (`npx skills`). It installs skills into each agent’s directory and works across **Claude Code**, **Codex**, **Cursor**, **Gemini CLI**, **Windsurf**, **Antigravity**, **OpenClaw**, **GitHub Copilot**, and [many more](https://github.com/vercel-labs/skills#supported-agents).

```bash
# Install all skills from this repo
npx skills add ysskrishna/ai-agent-skills

# List available skills
npx skills add ysskrishna/ai-agent-skills --list

# Or install individual skills (--skill names match plugin / directory names)
npx skills add ysskrishna/ai-agent-skills --skill six-thinking-hats
npx skills add ysskrishna/ai-agent-skills --skill critical-thinking
npx skills add ysskrishna/ai-agent-skills --skill systems-thinking
npx skills add ysskrishna/ai-agent-skills --skill creative-thinking
npx skills add ysskrishna/ai-agent-skills --skill strategic-thinking
npx skills add ysskrishna/ai-agent-skills --skill analytical-thinking
npx skills add ysskrishna/ai-agent-skills --skill lateral-thinking
npx skills add ysskrishna/ai-agent-skills --skill design-thinking
npx skills add ysskrishna/ai-agent-skills --skill first-principles-thinking
npx skills add ysskrishna/ai-agent-skills --skill ethical-thinking
```

### GitHub CLI (`gh skill`)

Install via [GitHub CLI](https://cli.github.com/) Agent Skills support (`gh skill`). Requires GitHub CLI v2.90.0 or later.

```bash
# Browse this repo's skills interactively
gh skill install ysskrishna/ai-agent-skills

# Install specific skills directly
gh skill install ysskrishna/ai-agent-skills six-thinking-hats
gh skill install ysskrishna/ai-agent-skills critical-thinking
gh skill install ysskrishna/ai-agent-skills systems-thinking
gh skill install ysskrishna/ai-agent-skills creative-thinking
gh skill install ysskrishna/ai-agent-skills strategic-thinking
gh skill install ysskrishna/ai-agent-skills analytical-thinking
gh skill install ysskrishna/ai-agent-skills lateral-thinking
gh skill install ysskrishna/ai-agent-skills design-thinking
gh skill install ysskrishna/ai-agent-skills first-principles-thinking
gh skill install ysskrishna/ai-agent-skills ethical-thinking

# Target a specific host and scope when needed
gh skill install ysskrishna/ai-agent-skills critical-thinking --agent codex --scope user
```

`gh skill` installs to the correct skill directory for the selected host, including GitHub Copilot, Claude Code, Codex, Cursor, and Gemini CLI.

### Claude Code marketplace

```bash
# Add the marketplace
/plugin marketplace add ysskrishna/ai-agent-skills

# Update marketplace
/plugin marketplace update ai-agent-skills

# Install plugin(s) from the catalog
/plugin install six-thinking-hats@ai-agent-skills
/plugin install critical-thinking@ai-agent-skills
/plugin install systems-thinking@ai-agent-skills
/plugin install creative-thinking@ai-agent-skills
/plugin install strategic-thinking@ai-agent-skills
/plugin install analytical-thinking@ai-agent-skills
/plugin install lateral-thinking@ai-agent-skills
/plugin install design-thinking@ai-agent-skills
/plugin install first-principles-thinking@ai-agent-skills
/plugin install ethical-thinking@ai-agent-skills
```

## Usage

Call skills directly with `/skill-name`, or describe your goal and the agent will infer the best match.

```text
/six-thinking-hats Pizza or pasta for dinner?

Use Six Thinking Hats for pizza or pasta for dinner.
```

## Changelog

See [CHANGELOG](https://github.com/ysskrishna/ai-agent-skills/blob/main/CHANGELOG.md) for release history.

## Support

If you find this library helpful:

- ⭐ Star the repository
- 🐛 Report issues
- 🔀 Submit pull requests
- 💝 [Sponsor on GitHub](https://github.com/sponsors/ysskrishna)

## License

MIT © [Y. Siva Sai Krishna](https://github.com/ysskrishna) — see [LICENSE](https://github.com/ysskrishna/ai-agent-skills/blob/main/LICENSE) for details.

---

<p align="left">
  <a href="https://github.com/ysskrishna">Author's GitHub</a> •
  <a href="https://linkedin.com/in/ysskrishna">Author's LinkedIn</a> •
  <a href="https://ysskrishna.space">Author's site</a> •
  <a href="https://clawhub.ai/user/ysskrishna">ClawHub</a> •
  <a href="https://github.com/ysskrishna/ai-agent-skills/issues">Report Issues</a>
</p>
