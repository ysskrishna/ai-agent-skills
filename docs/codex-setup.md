# Codex CLI and App

Needs Codex CLI v0.122 or later.

## Install

```bash
codex plugin marketplace add ysskrishna/ai-agent-skills
codex plugin add ai-agent-skills@ai-agent-skills
```

Start a new session afterwards. Codex loads plugin skills only in new sessions. Use a skill with `@`, or describe your problem and let Codex pick.

## Verify

```bash
codex plugin list
codex debug prompt-input hi   # shows entries like ai-agent-skills:five-whys
```

## Update and remove

```bash
codex plugin marketplace upgrade ai-agent-skills
codex plugin remove ai-agent-skills@ai-agent-skills
```

## Notes

- Install the `ai-agent-skills` plugin, not single skills. Codex scans `<plugin>/skills/` only, and the single-skill Claude plugins keep `SKILL.md` at their root, so they install but load nothing.
- Codex finds `.agents/plugins/marketplace.json` first. That file lists the bundle only.
- No approval is needed. OpenAI's plugin directory is optional and needs a verified developer, a logo, and a ZIP upload through the platform dashboard.
- The Codex IDE extension has no plugin support.

## Status

CLI: marketplace add, install, and all skills listed in the prompt were run against this repo. Codex App: not tested (GUI).
