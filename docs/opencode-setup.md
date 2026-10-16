# OpenCode

## Install

From npm (recommended when you want registry installs and cache behavior):

```bash
opencode plugin @ysskrishna/ai-agent-skills --global
```

Or add the package name in `opencode.json`.

OpenCode 1.x, in `opencode.json`:

```json
{
  "plugin": ["@ysskrishna/ai-agent-skills"]
}
```

```json
{
  "plugin": ["ai-agent-skills@git+https://github.com/ysskrishna/ai-agent-skills.git"]
}
```

OpenCode 2.0.4 or later uses the key `plugins`:

```json
{
  "plugins": ["@ysskrishna/ai-agent-skills"]
}
```

```json
{
  "plugins": ["ai-agent-skills@git+https://github.com/ysskrishna/ai-agent-skills.git"]
}
```

Restart OpenCode. To pin a git release, add `#v1.3.0` after `.git`.

## Verify

```bash
opencode debug skill > skills.json   # write to a file, piping truncates the output
```

Or ask the agent to list its skills.

## Update and remove

Remove the line from `opencode.json`. Updates can be held back by OpenCode's package cache, which pins a git dependency. If a new version does not appear, clear OpenCode's cache or reinstall.

## Without a plugin

OpenCode reads `.agents/skills`, `.claude/skills` and `~/.agents/skills`, so this also works with no plugin:

```bash
npx skills add ysskrishna/ai-agent-skills
```

## Notes

- `index.js` only registers the repo's `skills/` folder. It adds no prompt text and no tools.
- OpenCode 1.x requires each skill `name` to match its folder. All skills here do.
- On Windows, git-based plugin specs can fail in some OpenCode builds. Use the `npx skills` route there.

## Status

OpenCode 1.18.34 loaded all skills from the git plugin spec. OpenCode 2.x was **not** tested: no 2.x build was available. The 2.x path in `index.js` follows the documented plugin API and is unverified.
