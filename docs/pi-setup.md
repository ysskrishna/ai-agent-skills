# Pi

## Install

```bash
pi install git:github.com/ysskrishna/ai-agent-skills
```

Add `-l` to install for the current project only.

## Verify

```bash
pi list
```

Pi puts each skill's name and description in the system prompt. Force one with `/skill:five-whys`.

## Update and remove

```bash
pi update
pi remove git:github.com/ysskrishna/ai-agent-skills
```

## Notes

- Pi finds the `skills/` folder by convention, so no Pi-specific manifest is needed.
- Pi warns that packages can run code. This repo ships skills only. Its `index.js` is the OpenCode entry point.
- Pi's package gallery lists npm packages with the `pi-package` keyword. This repo is not published to npm, so it is not listed there. The git install needs no listing.

## Status

Install, list, remove, and the skill list over Pi's RPC interface were run against this repo.
