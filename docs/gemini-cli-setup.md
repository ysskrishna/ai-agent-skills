# Gemini CLI

## Install

As an extension (all skills in one install):

```bash
gemini extensions install https://github.com/ysskrishna/ai-agent-skills
```

Or install only the skills:

```bash
gemini skills install https://github.com/ysskrishna/ai-agent-skills.git --path skills
```

Add `--consent` to skip the confirmation prompt. Add `--scope workspace` to limit skills to the current project.

## Verify

```bash
gemini skills list
gemini extensions list
```

Gemini shows a confirmation before it activates a skill the first time.

## Update and remove

```bash
gemini extensions update ai-agent-skills
gemini extensions uninstall ai-agent-skills
gemini skills uninstall five-whys      # skills installed with `gemini skills install`
```

## Notes

- The extension install uses the **latest GitHub Release**, not the default branch. A new version reaches users after a release is published.
- `gemini-extension.json` sets no `contextFileName`, so nothing is added to every prompt. Skills load by description.
- Gemini's extension gallery lists public repos that have the GitHub topic `gemini-cli-extension` and a root `gemini-extension.json`. No submission is needed.
- Needs Node 20 or later and `git`.

## Status

Extension install, `gemini extensions validate`, and the `gemini skills install --path skills` route were run against this repo. The gallery listing depends on the repo topic and has not been checked.
