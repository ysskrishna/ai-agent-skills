# Qwen Code

## Install

```bash
qwen extensions install ysskrishna/ai-agent-skills:ai-agent-skills
```

The part after the colon picks the plugin from this repo's marketplace. `ai-agent-skills` is the bundle. Add `--consent` to skip the security prompt. Without a colon Qwen asks you to pick a plugin, which needs an interactive terminal.

## Verify

```bash
qwen extensions list   # shows the extension and its skills
```

Skills are registered as `ai-agent-skills:<skill>`.

## Update and remove

```bash
qwen extensions update ai-agent-skills
qwen extensions uninstall ai-agent-skills
```

## Notes

- GitHub installs use the **latest GitHub Release**. A new version reaches users after a release is published and marked latest.
- Qwen converts the Claude plugin layout on install. Single-skill plugins work too (`ysskrishna/ai-agent-skills:five-whys`).
- Qwen has no submission process. A listing in Gemini's gallery also reaches Qwen users.

## Status

Install, list, update and uninstall were run against this repo (from a local clone). The GitHub form depends on the latest release.
