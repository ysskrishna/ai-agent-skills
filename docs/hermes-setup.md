# Hermes Agent

## Install (recommended: skills tap)

```bash
hermes skills tap add ysskrishna/ai-agent-skills
hermes skills install ysskrishna/ai-agent-skills/five-whys
```

Repeat the second command for each skill you want. Installed skills are normal Hermes skills.

## Verify

```bash
hermes skills list --source hub
```

## Update and remove

```bash
hermes skills update
hermes skills uninstall five-whys
hermes skills tap remove ysskrishna/ai-agent-skills
```

## Plugin route (with a caveat)

```bash
hermes plugins install ysskrishna/ai-agent-skills --enable
```

This installs and enables the plugin, but Hermes does not list plugin skills in the model's skill index. They load only when something calls `skill_view("ai-agent-skills:<skill>")`. Use the tap if you want skills picked automatically.

## Notes

- `hermes plugins validate` accepts the root `plugin.json` (Agent Plugins 1.0).
- Hermes prints a notice that the plugin "declares Node dependencies" because of `package.json`. The file declares none, and Hermes skips the step.
- Hermes also installs from skills.sh and ClawHub sources.
- A catalog listing is optional and needs a pull request to the Hermes repo.

## Status

Plugin validate, install and enable ran against a local clone. The tap route ran against the public repo and installed `five-whys`. Whether a model auto-selects tap-installed skills was not tested.
