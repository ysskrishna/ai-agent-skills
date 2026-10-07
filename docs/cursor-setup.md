# Cursor

## Install

Plugin route, no approval needed:

1. Open **Customize, Plugins, Add, From GitHub Repository**.
2. Enter `github.com/ysskrishna/ai-agent-skills`.

In Agent chat you can also run `/add-plugin` and give the repo.

Skills-only route, works on every plan:

```bash
npx skills add ysskrishna/ai-agent-skills --agent cursor
```

Cursor reads skills from `.cursor/skills`, `.agents/skills` and `~/.cursor/skills`.

## Verify

Open **Customize, Skills**. All skills appear there.

## Update and remove

Use the plugin's menu in **Customize, Plugins**. For the skills route, run `npx skills add` again to update.

## Notes

- Cursor reads `.cursor-plugin/marketplace.json` and `.cursor-plugin/plugin.json` from this repo. Both validate against Cursor's own JSON schemas, which reject unknown keys.
- Cursor's `author` field allows only `name` and `email`.
- Cursor does not read the Claude marketplace file in this repo.
- Cursor's official marketplace is manually reviewed and rarely accepts new listings. `cursor.directory` is the community listing and takes a repo URL.

## Status

Manifest schema validation runs in `scripts/test_installs.sh cursor`. The IDE install and skills list were not tested here (GUI). Please confirm them and report anything off.
