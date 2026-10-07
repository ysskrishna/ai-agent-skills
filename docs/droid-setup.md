# Factory Droid

## Install

```bash
droid plugin marketplace add ysskrishna/ai-agent-skills
droid plugin install ai-agent-skills@ai-agent-skills --scope user
```

Use `--scope project` to limit it to the current repo.

## Verify

```bash
droid plugin list --scope user
```

Droid reads skills from `<plugin>/skills/<name>/SKILL.md` inside the installed plugin.

## Update and remove

Droid needs the full `plugin@marketplace` id here:

```bash
droid plugin update ai-agent-skills@ai-agent-skills
droid plugin uninstall ai-agent-skills@ai-agent-skills
```

## Notes

- Install the `ai-agent-skills` bundle only. The single-skill plugins in the marketplace install without error but load no skills, because their `SKILL.md` sits at the plugin root.
- Droid tracks git installs by commit, so the manifest version is informational.
- `gh skill install ysskrishna/ai-agent-skills --all --agent droid` is another route. It copies skills to `~/.factory/skills/`.
- Factory's own plugin repo takes vendored plugins only, so there is nothing to submit.

## Status

Marketplace add, install, update and uninstall were run against this repo, and the plugin cache holds all `SKILL.md` files. Live skill discovery needs a Factory login and was not tested.
