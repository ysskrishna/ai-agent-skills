# Install guides

One guide per CLI. The short version lives in the [README](../README.md#installation).

| CLI | Guide | Native install | Status |
|-----|-------|----------------|--------|
| Claude Code | [claude-code-setup.md](claude-code-setup.md) | Plugin marketplace | Skills discovered |
| Codex CLI / App | [codex-setup.md](codex-setup.md) | Plugin marketplace | Skills discovered (CLI) |
| Gemini CLI | [gemini-cli-setup.md](gemini-cli-setup.md) | Extension, or `gemini skills install` | Skills discovered |
| Cursor | [cursor-setup.md](cursor-setup.md) | Plugin from GitHub | Manifests valid, IDE step manual |
| Antigravity | [antigravity-setup.md](antigravity-setup.md) | `agy plugin install` | Installed |
| GitHub Copilot CLI | [copilot-cli-setup.md](copilot-cli-setup.md) | Plugin marketplace | Skills discovered |
| Factory Droid | [droid-setup.md](droid-setup.md) | Plugin marketplace | Installed |
| Qwen Code | [qwen-code-setup.md](qwen-code-setup.md) | Extension | Skills discovered |
| Grok Build | [grok-setup.md](grok-setup.md) | `grok plugin install` | Skills discovered |
| OpenCode | [opencode-setup.md](opencode-setup.md) | Plugin in `opencode.json` | Skills discovered (v1) |
| Pi | [pi-setup.md](pi-setup.md) | `pi install` | Skills discovered |
| Kimi Code | [kimi-setup.md](kimi-setup.md) | `/plugins install` | Skills discovered |
| Hermes Agent | [hermes-setup.md](hermes-setup.md) | Skills tap | Skills installed |
| Devin CLI | [devin-setup.md](devin-setup.md) | `devin plugins install` | Not verified |
| Muse | [muse-setup.md](muse-setup.md) | `muse plugins install` | Skills discovered |
| Everything else | [other-agents.md](other-agents.md) | `npx skills`, `gh skill` | Listing verified |

## What the repo ships for each CLI

The skills live once in `skills/`. Each CLI gets a small manifest that points at them. No skill text is changed per CLI, and nothing runs at session start.

| File | Used by |
|------|---------|
| `.claude-plugin/marketplace.json`, `.claude-plugin/plugin.json` | Claude Code, Copilot CLI, Qwen Code, Antigravity, Grok, Devin, Muse |
| `.agents/plugins/marketplace.json`, `.codex-plugin/plugin.json` | Codex, Factory Droid |
| `.cursor-plugin/marketplace.json`, `.cursor-plugin/plugin.json` | Cursor |
| `gemini-extension.json` | Gemini CLI |
| `.kimi-plugin/plugin.json` | Kimi Code |
| `plugin.json` (Agent Plugins 1.0) | Hermes, Antigravity validation, and any CLI that follows the open spec |
| `package.json`, `index.js` | OpenCode |

The `ai-agent-skills` plugin is a bundle of every skill with its source at the repo root. Claude Code also lists each skill as its own plugin. Codex, Droid, Grok and Cursor read skills from `<plugin>/skills/<name>/SKILL.md` only, so they need the bundle.

## How this is tested

`scripts/test_installs.sh` installs a fresh clone of the committed branch into each CLI with a throwaway `HOME`, then checks that every skill is discovered. Your own config is never touched.

```bash
bash scripts/test_installs.sh all            # every CLI found on PATH
bash scripts/test_installs.sh codex kimi     # selected CLIs
REQUIRE=1 bash scripts/test_installs.sh all  # a missing CLI counts as a failure
```

What each check proves:

| Proof | CLIs |
|-------|------|
| The CLI itself lists all skills after install | Claude Code (also its startup event), Codex, Gemini, Copilot, Qwen, Grok, Pi, OpenCode, Muse |
| The model's system prompt contains all skills (captured from a mock model server) | Kimi Code |
| The plugin cache holds every `SKILL.md`, but listing needs a login | Factory Droid, Antigravity |
| Vendor JSON schemas accept the manifests | Cursor |

Not proven, and why:

- Hermes Agent: not in CI until the vendor Linux installer is reliable; install and tap flow are documented in [hermes-setup.md](hermes-setup.md).
- Devin: plugin commands need a Devin login.
- Cursor IDE and Codex App: GUI steps. Follow the guide and report back if one fails.
- OpenCode 2.x: no 2.x build was available. The code path exists but never ran.
- Whether a model picks the right skill in Droid, Antigravity, Devin and Muse needs a paid login.
- Tests install from a local clone. The GitHub URL forms follow each vendor's docs and get re-checked after each release.

`validate-skills.sh` checks every manifest offline: it parses them, requires one version across all of them, and rejects keys that a CLI's schema forbids.

## No approval needed

Every CLI above installs straight from this public repo. Official directories (Anthropic, OpenAI, Cursor, Copilot, xAI and others) are optional extras for discovery. Installs never wait on them.

## Known limits

- Kimi Code cuts skill descriptions to about 250 characters in its prompt, so the trailing "Skip for ..." clause can be clipped.
- Grok and Factory Droid do not load the single-skill Claude plugins. Use the bundle.
- Gemini CLI and Qwen Code install from the latest GitHub Release, so they get a new version only after a release is published.
