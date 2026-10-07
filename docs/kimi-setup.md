# Kimi Code

## Install

Kimi Code has no `plugins` subcommand. Install from inside the app:

```text
/plugins install https://github.com/ysskrishna/ai-agent-skills
```

Choose **Trust and install**, then run `/reload` or start a new session.

You can also install a local clone: `/plugins install /path/to/ai-agent-skills`.

## Verify

The system prompt Kimi sends lists each skill with its path under `~/.kimi-code/plugins/managed/ai-agent-skills/`. Open `/plugins` to see the plugin.

## Update and remove

Manage the plugin in `/plugins`. A URL install takes the latest release, or the default branch if there is no release.

## Without a plugin

Kimi reads `~/.agents/skills` and `.agents/skills`, so `npx skills add ysskrishna/ai-agent-skills` also works.

## Notes

- Kimi cuts each skill description to about 250 characters in its prompt. Our descriptions run 200 to 350 characters, so the "Skip for ..." ending can be clipped for the longer ones.
- Kimi asks you to trust the folder on first launch and to confirm each third-party plugin.
- Plugins install per user.

## Status

The local-path install was driven through Kimi's TUI by `scripts/kimi_tui_install.py`. A mock model server then captured the system prompt, which listed all skills. The GitHub URL form follows Kimi's docs and was not run.
