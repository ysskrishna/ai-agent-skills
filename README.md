# AI Agent Skills

[![Tests](https://github.com/ysskrishna/ai-agent-skills/actions/workflows/validate-skills.yml/badge.svg)](https://github.com/ysskrishna/ai-agent-skills/actions/workflows/validate-skills.yml) [![License: MIT](https://img.shields.io/github/license/ysskrishna/ai-agent-skills)](https://github.com/ysskrishna/ai-agent-skills/blob/main/LICENSE) [![GitHub release](https://img.shields.io/github/v/release/ysskrishna/ai-agent-skills?label=release)](https://github.com/ysskrishna/ai-agent-skills/releases) [![ClawHub](https://img.shields.io/badge/ClawHub-ysskrishna-informational)](https://clawhub.ai/user/ysskrishna) [![Author site](https://img.shields.io/badge/author-ysskrishna.space-informational)](https://ysskrishna.space)

A curated collection of cognitive workflows designed to upgrade your AI agents from simple code generators into strong collaborators for **decision support**, **brainstorming**, and **structured thinking**. Compatible with **Claude Code**, **Cursor**, **Codex CLI**, **Gemini CLI**, **Windsurf**, **Antigravity**, **OpenClaw**, and any tool that supports the same specification.

## Overview

Most coding assistants default to quick answers. This repository packages structured thinking methods as modular [`SKILL.md`](https://agentskills.io/) skills from the [Agent Skills](https://agentskills.io/) open standard, so an agent can run a method on a real decision instead of improvising one.

- **Describe the problem, not the method.** Each skill's description lists the situations and phrases it fits ("what could go wrong?", "A or B?", "why does this keep happening?") and when to skip it. You do not need to name the method.
- **Not sure which one?** Start with [`thinking-method-selector`](skills/thinking-method-selector/SKILL.md). It picks a method for your situation and runs it.
- **Each skill is standalone.** Install one or all. Every skill has a light path for small questions and a worked example in its `references/` folder.

## Skills

### Start here

| Skill | Use it when | Registry |
|-------|-------------|----------|
| [`thinking-method-selector`](skills/thinking-method-selector/SKILL.md) | You have a problem or decision but no method in mind. Picks one and runs it. | [![Clawhub](https://img.shields.io/badge/Clawhub-informational)](https://clawhub.ai/ysskrishna/thinking-method-selector) |

### Understand a problem

| Skill | Use it when | Registry |
|-------|-------------|----------|
| [`five-whys`](skills/five-whys/SKILL.md) | Something failed or keeps recurring and you need the real cause. | [![Clawhub](https://img.shields.io/badge/Clawhub-informational)](https://clawhub.ai/ysskrishna/five-whys) |
| [`analytical-thinking`](skills/analytical-thinking/SKILL.md) | A number moved or a question needs a driver tree, hypotheses and evidence. | [![Clawhub](https://img.shields.io/badge/Clawhub-informational)](https://clawhub.ai/ysskrishna/analytical-thinking) |
| [`systems-thinking`](skills/systems-thinking/SKILL.md) | A change may have side effects, or a problem keeps coming back across teams or services. | [![Clawhub](https://img.shields.io/badge/Clawhub-informational)](https://clawhub.ai/ysskrishna/systems-thinking) |
| [`first-principles-thinking`](skills/first-principles-thinking/SKILL.md) | You want to test an inherited default or a copied approach from scratch. | [![Clawhub](https://img.shields.io/badge/Clawhub-informational)](https://clawhub.ai/ysskrishna/first-principles-reasoning) |
| [`design-thinking`](skills/design-thinking/SKILL.md) | You need to understand users before designing or building. | [![Clawhub](https://img.shields.io/badge/Clawhub-informational)](https://clawhub.ai/ysskrishna/design-thinking) |

### Assess and decide

| Skill | Use it when | Registry |
|-------|-------------|----------|
| [`swot-analysis`](skills/swot-analysis/SKILL.md) | You want to assess where a team, product or company stands, then act on it. | [![Clawhub](https://img.shields.io/badge/Clawhub-informational)](https://clawhub.ai/ysskrishna/swot-analysis) |
| [`tradeoff-analysis`](skills/tradeoff-analysis/SKILL.md) | You must pick between concrete options (A or B, build vs buy). | [![Clawhub](https://img.shields.io/badge/Clawhub-informational)](https://clawhub.ai/ysskrishna/tradeoff-analysis) |
| [`prioritization`](skills/prioritization/SKILL.md) | There is more work than capacity and you need an order and a cut line. | [![Clawhub](https://img.shields.io/badge/Clawhub-informational)](https://clawhub.ai/ysskrishna/prioritization) |
| [`strategic-thinking`](skills/strategic-thinking/SKILL.md) | You must choose a direction under constraints. | [![Clawhub](https://img.shields.io/badge/Clawhub-informational)](https://clawhub.ai/ysskrishna/strategic-thinking) |
| [`fermi-estimation`](skills/fermi-estimation/SKILL.md) | You need a rough number fast (capacity, cost, size). | [![Clawhub](https://img.shields.io/badge/Clawhub-informational)](https://clawhub.ai/ysskrishna/fermi-estimation) |

### Check and de-risk

| Skill | Use it when | Registry |
|-------|-------------|----------|
| [`critical-thinking`](skills/critical-thinking/SKILL.md) | You want a claim, plan or decision checked for weak spots. | [![Clawhub](https://img.shields.io/badge/Clawhub-informational)](https://clawhub.ai/ysskrishna/critical-thinking) |
| [`pre-mortem`](skills/pre-mortem/SKILL.md) | Before a launch or commitment: imagine it failed and find out why. | [![Clawhub](https://img.shields.io/badge/Clawhub-informational)](https://clawhub.ai/ysskrishna/pre-mortem) |
| [`ethical-thinking`](skills/ethical-thinking/SKILL.md) | A plan could harm or unfairly burden people. | [![Clawhub](https://img.shields.io/badge/Clawhub-informational)](https://clawhub.ai/ysskrishna/ethical-thinking) |

### Generate ideas

| Skill | Use it when | Registry |
|-------|-------------|----------|
| [`creative-thinking`](skills/creative-thinking/SKILL.md) | You want many fresh options before choosing. | [![Clawhub](https://img.shields.io/badge/Clawhub-informational)](https://clawhub.ai/ysskrishna/creative-thinking) |
| [`lateral-thinking`](skills/lateral-thinking/SKILL.md) | Ideas feel stuck or incremental and you need a different angle. | [![Clawhub](https://img.shields.io/badge/Clawhub-informational)](https://clawhub.ai/ysskrishna/lateral-thinking) |

### See it from several angles

| Skill | Use it when | Registry |
|-------|-------------|----------|
| [`six-thinking-hats`](skills/six-thinking-hats/SKILL.md) | You want facts, feelings, risks, benefits and new ideas examined separately. | [![Clawhub](https://img.shields.io/badge/Clawhub-informational)](https://clawhub.ai/ysskrishna/six-hats-thinking) |

The full trigger text for each skill is in its `SKILL.md` frontmatter.

## Installation

### skills.sh (recommended)

Install via the [skills.sh](https://skills.sh) CLI (`npx skills`). It installs skills into each agent’s directory and works across **Claude Code**, **Codex**, **Cursor**, **Gemini CLI**, **Windsurf**, **Antigravity**, **OpenClaw**, **GitHub Copilot**, and [many more](https://github.com/vercel-labs/skills#supported-agents).

```bash
# Install all skills from this repo
npx skills add ysskrishna/ai-agent-skills

# List available skills
npx skills add ysskrishna/ai-agent-skills --list

# Or install individual skills (--skill names match plugin / directory names)
npx skills add ysskrishna/ai-agent-skills --skill thinking-method-selector
npx skills add ysskrishna/ai-agent-skills --skill five-whys
npx skills add ysskrishna/ai-agent-skills --skill analytical-thinking
npx skills add ysskrishna/ai-agent-skills --skill systems-thinking
npx skills add ysskrishna/ai-agent-skills --skill first-principles-thinking
npx skills add ysskrishna/ai-agent-skills --skill design-thinking
npx skills add ysskrishna/ai-agent-skills --skill swot-analysis
npx skills add ysskrishna/ai-agent-skills --skill tradeoff-analysis
npx skills add ysskrishna/ai-agent-skills --skill prioritization
npx skills add ysskrishna/ai-agent-skills --skill strategic-thinking
npx skills add ysskrishna/ai-agent-skills --skill fermi-estimation
npx skills add ysskrishna/ai-agent-skills --skill critical-thinking
npx skills add ysskrishna/ai-agent-skills --skill pre-mortem
npx skills add ysskrishna/ai-agent-skills --skill ethical-thinking
npx skills add ysskrishna/ai-agent-skills --skill creative-thinking
npx skills add ysskrishna/ai-agent-skills --skill lateral-thinking
npx skills add ysskrishna/ai-agent-skills --skill six-thinking-hats
```

### GitHub CLI (`gh skill`)

Install via [GitHub CLI](https://cli.github.com/) Agent Skills support (`gh skill`). Requires GitHub CLI v2.90.0 or later.

```bash
# Browse this repo's skills interactively
gh skill install ysskrishna/ai-agent-skills

# Install specific skills directly
gh skill install ysskrishna/ai-agent-skills thinking-method-selector
gh skill install ysskrishna/ai-agent-skills five-whys
gh skill install ysskrishna/ai-agent-skills analytical-thinking
gh skill install ysskrishna/ai-agent-skills systems-thinking
gh skill install ysskrishna/ai-agent-skills first-principles-thinking
gh skill install ysskrishna/ai-agent-skills design-thinking
gh skill install ysskrishna/ai-agent-skills swot-analysis
gh skill install ysskrishna/ai-agent-skills tradeoff-analysis
gh skill install ysskrishna/ai-agent-skills prioritization
gh skill install ysskrishna/ai-agent-skills strategic-thinking
gh skill install ysskrishna/ai-agent-skills fermi-estimation
gh skill install ysskrishna/ai-agent-skills critical-thinking
gh skill install ysskrishna/ai-agent-skills pre-mortem
gh skill install ysskrishna/ai-agent-skills ethical-thinking
gh skill install ysskrishna/ai-agent-skills creative-thinking
gh skill install ysskrishna/ai-agent-skills lateral-thinking
gh skill install ysskrishna/ai-agent-skills six-thinking-hats

# Target a specific host and scope when needed
gh skill install ysskrishna/ai-agent-skills tradeoff-analysis --agent codex --scope user
```

`gh skill` installs to the correct skill directory for the selected host, including GitHub Copilot, Claude Code, Codex, Cursor, and Gemini CLI.

### Claude Code marketplace

```bash
# Add the marketplace
/plugin marketplace add ysskrishna/ai-agent-skills

# Update marketplace
/plugin marketplace update ai-agent-skills

# Install plugin(s) from the catalog
/plugin install thinking-method-selector@ai-agent-skills
/plugin install five-whys@ai-agent-skills
/plugin install analytical-thinking@ai-agent-skills
/plugin install systems-thinking@ai-agent-skills
/plugin install first-principles-thinking@ai-agent-skills
/plugin install design-thinking@ai-agent-skills
/plugin install swot-analysis@ai-agent-skills
/plugin install tradeoff-analysis@ai-agent-skills
/plugin install prioritization@ai-agent-skills
/plugin install strategic-thinking@ai-agent-skills
/plugin install fermi-estimation@ai-agent-skills
/plugin install critical-thinking@ai-agent-skills
/plugin install pre-mortem@ai-agent-skills
/plugin install ethical-thinking@ai-agent-skills
/plugin install creative-thinking@ai-agent-skills
/plugin install lateral-thinking@ai-agent-skills
/plugin install six-thinking-hats@ai-agent-skills
```

## Usage

Describe your situation and the agent picks a matching skill from the descriptions, or name a skill directly.

```text
We have to pick a job queue: Postgres, Redis or a managed service. Team of four.

What could go wrong with the database cutover next Friday?

Why did last night's deploy fail? Keep asking why until we reach something we can fix.

I have a pile of problems and no idea how to approach them.
```

To call a skill by name, use `/skill-name` after a skills.sh or `gh skill` install (for example `/pre-mortem`). Claude Code plugin installs namespace skills by plugin name (`/<plugin>:<skill>`).

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
