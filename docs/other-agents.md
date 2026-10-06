# Other agents

## skills.sh

```bash
npx skills add ysskrishna/ai-agent-skills            # all skills, pick agents interactively
npx skills add ysskrishna/ai-agent-skills --list     # list skills only
npx skills add ysskrishna/ai-agent-skills --skill five-whys --agent cursor
```

The [skills CLI](https://github.com/vercel-labs/skills) copies each skill into the folder your agent reads. That covers Windsurf, Cline, Kiro, Goose, Junie, Continue, Roo Code, Augment, Amp and the other agents it supports.

- Set `DISABLE_TELEMETRY=1` to turn off its install telemetry.
- skills.sh builds its public listing from that telemetry. There is nothing to submit.

## GitHub CLI

```bash
gh skill install ysskrishna/ai-agent-skills --all --agent <agent> --scope user
```

Agents include `github-copilot`, `claude-code`, `cursor`, `codex`, `gemini-cli`, `antigravity`, `droid`, `grok`, `kimi-cli`, `opencode` and more. Run `gh skill install --help` for the full list. Needs GitHub CLI v2.90.0 or later and `gh auth login`.

## Any agent that reads SKILL.md

Copy the folders from `skills/` into the folder your agent reads, or point your agent at the repo. The files follow the [Agent Skills](https://agentskills.io/) standard.

## Status

`npx skills add --list` and `gh skill install --from-local` run in `scripts/test_installs.sh` and list or install all skills. Installing into each individual agent was not run.
