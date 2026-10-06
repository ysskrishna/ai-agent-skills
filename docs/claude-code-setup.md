# Claude Code

## Install

```text
/plugin marketplace add ysskrishna/ai-agent-skills
/plugin install ai-agent-skills@ai-agent-skills
```

`ai-agent-skills` installs every skill. To pick one, install it by name, for example `/plugin install five-whys@ai-agent-skills`. The full list is in the [README](../README.md#claude-code).

From a terminal:

```bash
claude plugin marketplace add ysskrishna/ai-agent-skills
claude plugin install ai-agent-skills@ai-agent-skills
```

## Verify

```bash
claude plugin list
claude plugin details ai-agent-skills   # lists every skill
```

Skills are namespaced by plugin, for example `/ai-agent-skills:five-whys`.

## Update and remove

```text
/plugin marketplace update ai-agent-skills
/plugin uninstall ai-agent-skills@ai-agent-skills
```

## Notes

- `marketplace add owner/repo` clones over SSH. If you see `Permission denied (publickey)`, run `git config --global url."https://github.com/".insteadOf git@github.com:` once.
- No approval is needed. Anthropic's official directory is separate and optional.
- Maintainers: `claude plugin validate .` checks the manifests.

## Status

Install, marketplace add, bundle and single-skill plugins, and the startup skill list were run against this repo.
