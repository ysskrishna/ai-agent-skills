# Devin CLI

## Install

```bash
devin plugins install ysskrishna/ai-agent-skills
```

Devin reads this repo's `.claude-plugin/plugin.json` and the `skills/` folder. Only the whole plugin installs, not single skills.

## Verify

```bash
devin plugins info ai-agent-skills
devin skills list
```

## Update and remove

Use `devin plugins update ai-agent-skills` and `devin plugins uninstall ai-agent-skills`.

## Without a plugin

`npx skills add ysskrishna/ai-agent-skills` writes to `.agents/skills`, which `devin skills list` shows.

## Notes

- Plugins are in beta, and organisations can disable them.
- No public Devin directory exists.

## Status

**Not verified.** Every `devin plugins` command, even with `--local`, needs a Devin login, so the install could not run here. `scripts/test_installs.sh devin` skips until you are logged in. If you have an account, run:

```bash
devin auth login
devin plugins install --local ./ai-agent-skills -y
devin plugins info ai-agent-skills
```
