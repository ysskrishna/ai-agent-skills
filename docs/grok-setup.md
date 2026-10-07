# Grok Build

## Install

```bash
grok plugin install ysskrishna/ai-agent-skills --trust
```

Without `--trust`, Grok prints a warning and stops.

## Verify

```bash
grok plugin list
grok inspect        # lists skills with the plugin that provides them
```

## Update and remove

```bash
grok plugin update ai-agent-skills
grok plugin uninstall ai-agent-skills
```

## Notes

- Install directly. Do not use `grok plugin marketplace add` with this repo: the single-skill plugins in it have no skills for Grok, and the bundle entry (source `./`) is skipped.
- A native skill with the same name wins over a plugin skill. The plugin copy stays reachable as `ai-agent-skills:<skill>`.
- No approval is needed. xAI's official marketplace takes a pull request with a pinned 40-character commit SHA and runs a security audit. It is optional.

## Status

Validate, install, inspect, update and uninstall were run against this repo.
