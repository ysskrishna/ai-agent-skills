# AI Agent Skills

[![Tests](https://github.com/ysskrishna/ai-agent-skills/actions/workflows/validate-skills.yml/badge.svg)](https://github.com/ysskrishna/ai-agent-skills/actions/workflows/validate-skills.yml) [![License: MIT](https://img.shields.io/github/license/ysskrishna/ai-agent-skills)](https://github.com/ysskrishna/ai-agent-skills/blob/main/LICENSE) [![GitHub release](https://img.shields.io/github/v/release/ysskrishna/ai-agent-skills?label=release)](https://github.com/ysskrishna/ai-agent-skills/releases) [![ClawHub](https://img.shields.io/badge/ClawHub-ysskrishna-informational)](https://clawhub.ai/user/ysskrishna) [![Author site](https://img.shields.io/badge/author-ysskrishna.space-informational)](https://ysskrishna.space)

A curated collection of cognitive workflows designed to upgrade your AI agents from simple code generators into strong collaborators for **decision support**, **brainstorming**, and **structured thinking**. Compatible with **Claude Code**, **Codex**, **Gemini CLI**, **Cursor**, **Antigravity**, **GitHub Copilot CLI**, **Factory Droid**, **Qwen Code**, **Grok Build**, **OpenCode**, **Pi**, **Kimi Code**, **Hermes Agent**, **Devin**, **Muse**, **Windsurf**, **OpenClaw**, and any tool that supports the same specification. See [Installation](#installation).

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

Fastest path, works in 70+ agents:

```bash
npx skills add ysskrishna/ai-agent-skills
```

Want a native install for your CLI? Find it below and expand it. Each plugin install gives you all skills in one step (`ai-agent-skills`).

| CLI | Install | Status |
|-----|---------|--------|
| [Claude Code](#claude-code) | `/plugin marketplace add ysskrishna/ai-agent-skills` | Skills discovered |
| [Codex CLI / App](#codex-cli-and-app) | `codex plugin marketplace add ysskrishna/ai-agent-skills` | Skills discovered (CLI) |
| [Gemini CLI](#gemini-cli) | `gemini extensions install https://github.com/ysskrishna/ai-agent-skills` | Skills discovered |
| [Cursor](#cursor) | Plugins, Add, From GitHub Repository | Manifests valid, IDE install is manual |
| [Antigravity](#antigravity) | `agy plugin install https://github.com/ysskrishna/ai-agent-skills` | Installed |
| [GitHub Copilot CLI](#github-copilot-cli) | `copilot plugin marketplace add ysskrishna/ai-agent-skills` | Skills discovered |
| [Factory Droid](#factory-droid) | `droid plugin marketplace add ysskrishna/ai-agent-skills` | Installed |
| [Qwen Code](#qwen-code) | `qwen extensions install ysskrishna/ai-agent-skills:ai-agent-skills` | Skills discovered |
| [Grok Build](#grok-build) | `grok plugin install ysskrishna/ai-agent-skills --trust` | Skills discovered |
| [OpenCode](#opencode) | `plugin` entry in `opencode.json` | Skills discovered (v1) |
| [Pi](#pi) | `pi install git:github.com/ysskrishna/ai-agent-skills` | Skills discovered |
| [Kimi Code](#kimi-code) | `/plugins install https://github.com/ysskrishna/ai-agent-skills` | Skills discovered |
| [Hermes Agent](#hermes-agent) | `hermes skills tap add ysskrishna/ai-agent-skills` | Skills installed |
| [Devin CLI](#devin-cli) | `devin plugins install ysskrishna/ai-agent-skills` | Not verified (login) |
| [Muse](#muse) | `muse plugins install ./ai-agent-skills` | Skills discovered |
| Windsurf, Cline, Kiro, Amp, Goose, Junie, Continue, Roo Code, Augment and more | `npx skills add ysskrishna/ai-agent-skills` | Listing verified |

**Status** is what the [install tests](docs/README.md#how-this-is-tested) proved against a clone of this repo: *Skills discovered* means the CLI listed all 17 skills after install, *Installed* means the install succeeded but listing skills needs a login. Details and limits are in [docs/](docs/README.md).

### Claude Code

<details>
<summary><b>Install, update, remove</b></summary>

```text
/plugin marketplace add ysskrishna/ai-agent-skills

# All skills in one plugin
/plugin install ai-agent-skills@ai-agent-skills
```

Or install single skills as separate plugins:

```text
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

Update with `/plugin marketplace update ai-agent-skills`. Remove with `/plugin uninstall ai-agent-skills@ai-agent-skills`. Check with `/plugin`.

If the marketplace add fails with `Permission denied (publickey)`, run `git config --global url."https://github.com/".insteadOf git@github.com:` once. More in [docs/claude-code-setup.md](docs/claude-code-setup.md).

</details>

### Codex CLI and App

<details>
<summary><b>Install, update, remove</b></summary>

```bash
codex plugin marketplace add ysskrishna/ai-agent-skills
codex plugin add ai-agent-skills@ai-agent-skills
```

Start a new session, then describe your problem or call a skill with `@`. Update with `codex plugin marketplace upgrade ai-agent-skills`. Remove with `codex plugin remove ai-agent-skills@ai-agent-skills`. Needs Codex CLI v0.122 or later. More in [docs/codex-setup.md](docs/codex-setup.md).

</details>

### Gemini CLI

<details>
<summary><b>Install, update, remove</b></summary>

```bash
# Extension: all skills in one install
gemini extensions install https://github.com/ysskrishna/ai-agent-skills

# Or only the skills, without the extension wrapper
gemini skills install https://github.com/ysskrishna/ai-agent-skills.git --path skills
```

Check with `gemini skills list`. Update with `gemini extensions update ai-agent-skills`. Remove with `gemini extensions uninstall ai-agent-skills`. The extension install uses the latest GitHub Release. More in [docs/gemini-cli-setup.md](docs/gemini-cli-setup.md).

</details>

### Cursor

<details>
<summary><b>Install, update, remove</b></summary>

In Cursor, open **Customize, Plugins, Add, From GitHub Repository** and enter `github.com/ysskrishna/ai-agent-skills`. In Agent chat you can also run `/add-plugin`.

Without the plugin route, install the skills into Cursor's skills folder:

```bash
npx skills add ysskrishna/ai-agent-skills --agent cursor
```

Check under **Customize, Skills**. More in [docs/cursor-setup.md](docs/cursor-setup.md).

</details>

### Antigravity

<details>
<summary><b>Install, update, remove</b></summary>

```bash
agy plugin install https://github.com/ysskrishna/ai-agent-skills
```

Reinstall with the same command to update. Remove with `agy plugin uninstall ai-agent-skills`. Skills are namespaced as `ai-agent-skills:<skill>`. More in [docs/antigravity-setup.md](docs/antigravity-setup.md).

</details>

### GitHub Copilot CLI

<details>
<summary><b>Install, update, remove</b></summary>

```bash
copilot plugin marketplace add ysskrishna/ai-agent-skills
copilot plugin install ai-agent-skills@ai-agent-skills
```

Check with `copilot skill list`. Update with `copilot plugin update ai-agent-skills`. Remove with `copilot plugin uninstall ai-agent-skills`. You can also install through GitHub CLI (see [GitHub CLI](#github-cli-gh-skill)). More in [docs/copilot-cli-setup.md](docs/copilot-cli-setup.md).

</details>

### Factory Droid

<details>
<summary><b>Install, update, remove</b></summary>

```bash
droid plugin marketplace add ysskrishna/ai-agent-skills
droid plugin install ai-agent-skills@ai-agent-skills --scope user
```

Install the `ai-agent-skills` bundle. The single-skill plugins load no skills on Droid. Update with `droid plugin update ai-agent-skills@ai-agent-skills`. Remove with `droid plugin uninstall ai-agent-skills@ai-agent-skills`. More in [docs/droid-setup.md](docs/droid-setup.md).

</details>

### Qwen Code

<details>
<summary><b>Install, update, remove</b></summary>

```bash
qwen extensions install ysskrishna/ai-agent-skills:ai-agent-skills
```

Skills appear as `ai-agent-skills:<skill>`. The install uses the latest GitHub Release. Update with `qwen extensions update ai-agent-skills`. Remove with `qwen extensions uninstall ai-agent-skills`. More in [docs/qwen-code-setup.md](docs/qwen-code-setup.md).

</details>

### Grok Build

<details>
<summary><b>Install, update, remove</b></summary>

```bash
grok plugin install ysskrishna/ai-agent-skills --trust
```

Check with `grok plugin list`. Update with `grok plugin update ai-agent-skills`. Remove with `grok plugin uninstall ai-agent-skills`. Install directly: the marketplace route does not work for this repo. More in [docs/grok-setup.md](docs/grok-setup.md).

</details>

### OpenCode

<details>
<summary><b>Install, update, remove</b></summary>

Add the plugin to `opencode.json` and restart OpenCode:

```json
{
  "plugin": ["ai-agent-skills@git+https://github.com/ysskrishna/ai-agent-skills.git"]
}
```

OpenCode 2.0.4 or later uses the key `plugins` instead of `plugin`. Check by asking the agent to list skills. OpenCode also reads `.agents/skills`, so `npx skills add ysskrishna/ai-agent-skills` works without a plugin. More in [docs/opencode-setup.md](docs/opencode-setup.md).

</details>

### Pi

<details>
<summary><b>Install, update, remove</b></summary>

```bash
pi install git:github.com/ysskrishna/ai-agent-skills
```

Check with `pi list`. Update with `pi update`. Remove with `pi remove git:github.com/ysskrishna/ai-agent-skills`. More in [docs/pi-setup.md](docs/pi-setup.md).

</details>

### Kimi Code

<details>
<summary><b>Install, update, remove</b></summary>

Inside Kimi Code:

```text
/plugins install https://github.com/ysskrishna/ai-agent-skills
```

Choose **Trust and install**, then run `/reload`. Manage it later in `/plugins`. More in [docs/kimi-setup.md](docs/kimi-setup.md).

</details>

### Hermes Agent

<details>
<summary><b>Install, update, remove</b></summary>

Use a skills tap. Hermes then treats each skill as a normal skill:

```bash
hermes skills tap add ysskrishna/ai-agent-skills
hermes skills install ysskrishna/ai-agent-skills/five-whys
```

Repeat the install for each skill you want. Update with `hermes skills update`. Remove with `hermes skills uninstall five-whys`.

A plugin install also works (`hermes plugins install ysskrishna/ai-agent-skills --enable`), but Hermes does not advertise plugin skills to the model, so use the tap. More in [docs/hermes-setup.md](docs/hermes-setup.md).

</details>

### Devin CLI

<details>
<summary><b>Install, update, remove</b></summary>

```bash
devin plugins install ysskrishna/ai-agent-skills
```

Check with `devin plugins info ai-agent-skills`. Not yet verified, because plugin commands need a Devin login. More in [docs/devin-setup.md](docs/devin-setup.md).

</details>

### Muse

<details>
<summary><b>Install, update, remove</b></summary>

```bash
git clone https://github.com/ysskrishna/ai-agent-skills.git
MUSE_EXPERIMENTAL_PLUGINS=1 muse plugins install ./ai-agent-skills --scope user
MUSE_EXPERIMENTAL_PLUGINS=1 muse plugins approve ai-agent-skills
```

Check with `muse skills list --source plugin`. Update with `muse plugins update ai-agent-skills`. Remove with `muse plugins remove ai-agent-skills`. More in [docs/muse-setup.md](docs/muse-setup.md).

</details>

### skills.sh (`npx skills`)

<details>
<summary><b>Install all skills or pick individual ones</b></summary>

[skills.sh](https://skills.sh) installs skills into each agent's own folder. It supports **Claude Code**, **Codex**, **Cursor**, **Gemini CLI**, **Windsurf**, **Antigravity**, **OpenClaw**, **GitHub Copilot**, and [many more](https://github.com/vercel-labs/skills#supported-agents).

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

</details>

### GitHub CLI (`gh skill`)

<details>
<summary><b>Install all skills or pick individual ones</b></summary>

Requires GitHub CLI v2.90.0 or later.

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

`gh skill` installs to the correct skill directory for the selected host, including GitHub Copilot, Claude Code, Codex, Cursor, Gemini CLI and Factory Droid.

</details>

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
