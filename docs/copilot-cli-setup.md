# GitHub Copilot CLI

## Install

```bash
copilot plugin marketplace add ysskrishna/ai-agent-skills
copilot plugin install ai-agent-skills@ai-agent-skills
```

Single skills work too, for example `copilot plugin install five-whys@ai-agent-skills`.

Through GitHub CLI instead:

```bash
gh skill install ysskrishna/ai-agent-skills --all --agent github-copilot
```

`gh skill` rewrites each installed `SKILL.md` to record where it came from. Log in first with `gh auth login` to avoid API rate limits.

## Verify

```bash
copilot plugin list
copilot skill list
```

## Update and remove

```bash
copilot plugin update ai-agent-skills
copilot plugin uninstall ai-agent-skills
```

## Notes

- Do not use `copilot plugin install ysskrishna/ai-agent-skills`. Direct installs still work but are deprecated.
- Copilot de-duplicates skills by name. A project or personal skill with the same name wins over a plugin skill.
- No approval is needed. The `awesome-copilot` marketplace is optional and takes an issue form with a release tag and commit SHA.

## Status

Marketplace add, bundle install, and the skill list were run against this repo.
