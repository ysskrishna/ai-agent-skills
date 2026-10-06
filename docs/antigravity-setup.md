# Antigravity

## Install

```bash
agy plugin install https://github.com/ysskrishna/ai-agent-skills
```

From a local clone: `agy plugin install ./ai-agent-skills`.

## Verify

```bash
agy plugin list
```

Inside Antigravity, type `/ai-agent-skills:` to see the namespaced skills. Listing skills through the model needs a Google login.

## Update and remove

```bash
agy plugin install https://github.com/ysskrishna/ai-agent-skills   # reinstall to update
agy plugin uninstall ai-agent-skills
```

## Notes

- Antigravity reads the root `plugin.json` (Agent Plugins 1.0) in this repo. `agy plugin validate <path>` needs that file.
- Plugins install under `~/.gemini/config/plugins/`.
- Antigravity's own marketplace is curated, with no public submission process. The install above needs no approval.

## Status

Validate, install and uninstall were run against this repo, and all `SKILL.md` files landed in the plugin folder. Skill discovery in a model session was not tested (needs login).
