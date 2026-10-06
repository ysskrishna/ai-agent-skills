# Muse

Plugins are experimental in Muse, so set `MUSE_EXPERIMENTAL_PLUGINS=1`.

## Install

```bash
git clone https://github.com/ysskrishna/ai-agent-skills.git
export MUSE_EXPERIMENTAL_PLUGINS=1
muse plugins install ./ai-agent-skills --scope user
muse plugins approve ai-agent-skills
```

Muse asks you to approve a new plugin before it loads.

## Verify

```bash
muse plugins validate ./ai-agent-skills --json
muse skills list --source plugin
```

## Update and remove

```bash
muse plugins update ai-agent-skills
muse plugins remove ai-agent-skills
```

## Notes

- `muse plugins marketplace add ... https://github.com/ysskrishna/ai-agent-skills` does not work for this repo today: the single-skill entries have no manifest of their own and Muse skips them. Install from a clone.
- Muse prints `agent-overlay-inactive` warnings for `.claude-plugin/plugin.json`. They are harmless: Muse uses the root `plugin.json` instead.
- Muse also reads `~/.agents/skills` and `~/.claude/skills`.
- There is no public Muse plugin directory.

## Status

Validate, install, approve, skill list, update and remove were run against this repo. Whether the model advertises plugin skills in a session was not tested (needs a Meta key).
