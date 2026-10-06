#!/usr/bin/env bash
# Real install tests: install this repo into each coding CLI and check that every
# skill is discovered. Each CLI runs with a throwaway HOME, so your own config is
# never touched. Tests that need a login are skipped, not faked.
#
# Usage: scripts/test_installs.sh [--source DIR] <cli>... | all
#   cli: skills gh claude codex gemini gemini-skills copilot qwen droid grok agy pi opencode kimi hermes devin muse cursor
# The source is a fresh git clone of the committed HEAD, so commit before testing.
# Env: WORK (scratch dir), KEEP=1 (keep scratch dir), REQUIRE=1 (a missing CLI is a failure).
# Exit code: 0 when nothing failed (skips allowed), 1 otherwise.

set -u

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SOURCE="$ROOT"
ALL="skills gh claude codex gemini gemini-skills copilot qwen droid grok agy pi opencode kimi hermes devin muse cursor"
WORK="${WORK:-$(mktemp -d "${TMPDIR:-/tmp}/ai-agent-skills-install-test.XXXXXX")}"
REPO="$WORK/ai-agent-skills" # the clone directory name doubles as the marketplace name for some CLIs
SKILLS="$(cd "$ROOT/skills" && ls -d */ | tr -d '/')"
EXPECTED="$(echo "$SKILLS" | wc -l | tr -d ' ')"
FAILED=0

pass() { printf 'PASS  %-15s %s\n' "$1" "$2"; }
skip() { printf 'SKIP  %-15s %s\n' "$1" "$2"; }
fail() {
  printf 'FAIL  %-15s %s\n' "$1" "$2"
  [ -f "$WORK/logs/$1.log" ] && tail -n 12 "$WORK/logs/$1.log" | sed 's/^/        | /'
  FAILED=1
}

# macOS has no timeout(1). perl alarm kills the command after N seconds.
to() { local s="$1"; shift; perl -e 'alarm shift; exec @ARGV' "$s" "$@"; }

log() { mkdir -p "$WORK/logs"; echo "$WORK/logs/$1.log"; }
new_home() { mkdir -p "$WORK/home/$1"; echo "$WORK/home/$1"; }

# How many of the repo's skill names appear in a file.
count_skills() {
  local n=0 s
  for s in $SKILLS; do grep -q -- "$s" "$1" && n=$((n + 1)); done
  echo "$n"
}

need() {
  if command -v "$1" >/dev/null 2>&1; then return 0; fi
  if [ "${REQUIRE:-0}" = "1" ]; then fail "$2" "$1 is not installed"; else skip "$2" "$1 is not installed"; fi
  return 1
}

# check_count <test> <file>: all skills must show up in the file.
check_count() {
  local got
  got="$(count_skills "$2")"
  if [ "$got" -ge "$EXPECTED" ]; then pass "$1" "$got/$EXPECTED skills discovered"; else fail "$1" "$got/$EXPECTED skills discovered"; fi
}

prepare_source() {
  if [ -n "$(git -C "$SOURCE" status --porcelain 2>/dev/null)" ]; then
    echo "note: working tree has uncommitted changes. Tests use the committed HEAD only." >&2
  fi
  git clone -q "$SOURCE" "$REPO" || { echo "cannot clone $SOURCE" >&2; exit 2; }
}

t_skills() {
  need npx skills || return
  local h f; h="$(new_home skills)"; f="$(log skills)"
  (export HOME="$h" DISABLE_TELEMETRY=1; to 120 npx -y skills add "$REPO" --list) >"$f" 2>&1 || { fail skills "npx skills add --list failed"; return; }
  check_count skills "$f"
}

t_gh() {
  need gh gh || return
  local h f n; h="$(new_home gh)"; f="$(log gh)"
  (export HOME="$h" GH_CONFIG_DIR="$h/gh"; to 60 gh skill install --from-local "$REPO" --all --agent github-copilot --scope user) >"$f" 2>&1 || { fail gh "gh skill install failed"; return; }
  n="$(find "$h" -name SKILL.md | wc -l | tr -d ' ')"
  if [ "$n" -ge "$EXPECTED" ]; then pass gh "$n SKILL.md files installed"; else fail gh "$n/$EXPECTED SKILL.md files installed"; fi
}

t_claude() {
  need claude claude || return
  local h f; h="$(new_home claude)"; f="$(log claude)"
  (
    export HOME="$h" CLAUDE_CONFIG_DIR="$h/.claude"
    claude plugin validate "$REPO" &&
      claude plugin marketplace add "$REPO" &&
      claude plugin install ai-agent-skills@ai-agent-skills &&
      claude plugin install five-whys@ai-agent-skills &&
      claude plugin details ai-agent-skills
  ) >"$f" 2>&1 || { fail claude "validate/add/install failed"; return; }
  check_count claude "$f"
  # The first init event lists loaded skills before any model call, so a dummy key is enough.
  (
    export HOME="$h" CLAUDE_CONFIG_DIR="$h/.claude" ANTHROPIC_API_KEY=dummy
    to 40 claude -p hi --output-format stream-json --verbose
  ) >"$f.init" 2>/dev/null
  grep -m1 '"subtype":"init"' "$f.init" >"$f.initline" || true
  check_count claude-init "$f.initline"
}

t_codex() {
  need codex codex || return
  local h f; h="$(new_home codex)"; f="$(log codex)"
  (
    export HOME="$h" CODEX_HOME="$h/.codex"
    mkdir -p "$CODEX_HOME"
    codex plugin marketplace add "$REPO" &&
      codex plugin add ai-agent-skills@ai-agent-skills --json &&
      codex debug prompt-input hi
  ) >"$f" 2>&1 || { fail codex "marketplace add / install failed"; return; }
  check_count codex "$f"
}

t_gemini() {
  need gemini gemini || return
  local h f; h="$(new_home gemini)"; f="$(log gemini)"
  (
    export HOME="$h" GEMINI_CLI_HOME="$h"
    gemini extensions validate "$REPO" &&
      { yes | gemini extensions install "$REPO" --consent; } &&
      gemini extensions list &&
      gemini skills list
  ) >"$f" 2>&1 || { fail gemini "extension validate/install failed"; return; }
  check_count gemini "$f"
}

t_gemini_skills() {
  need gemini gemini-skills || return
  local h f; h="$(new_home gemini-skills)"; f="$(log gemini-skills)"
  (
    export HOME="$h" GEMINI_CLI_HOME="$h"
    { yes | gemini skills install "$REPO" --path skills --consent; } &&
      gemini skills list
  ) >"$f" 2>&1 || { fail gemini-skills "skills install failed"; return; }
  check_count gemini-skills "$f"
}

t_copilot() {
  need copilot copilot || return
  local h f; h="$(new_home copilot)"; f="$(log copilot)"
  (
    export HOME="$h" COPILOT_HOME="$h/.copilot" COPILOT_CACHE_HOME="$h/cache"
    copilot plugin marketplace add "$REPO" &&
      copilot plugin install ai-agent-skills@ai-agent-skills &&
      copilot plugin list --json &&
      copilot skill list
  ) >"$f" 2>&1 || { fail copilot "marketplace add / install failed"; return; }
  check_count copilot "$f"
}

t_qwen() {
  need qwen qwen || return
  local h f; h="$(new_home qwen)"; f="$(log qwen)"
  (
    export HOME="$h" QWEN_HOME="$h/.qwen"
    qwen extensions install "$REPO:ai-agent-skills" --consent &&
      qwen extensions list
  ) >"$f" 2>&1 || { fail qwen "extension install failed"; return; }
  check_count qwen "$f"
}

t_droid() {
  need droid droid || return
  local h f; h="$(new_home droid)"; f="$(log droid)"
  (
    export HOME="$h"
    droid plugin marketplace add "$REPO" &&
      droid plugin install ai-agent-skills@ai-agent-skills --scope user &&
      droid plugin list --scope user
  ) >"$f" 2>&1 || { fail droid "marketplace add / install failed"; return; }
  # Droid loads <plugin>/skills/<name>/SKILL.md. Check the cached copy has them all.
  local n; n="$(find "$h/.factory/plugins" -path '*/skills/*/SKILL.md' 2>/dev/null | wc -l | tr -d ' ')"
  if [ "$n" -ge "$EXPECTED" ]; then pass droid "$n SKILL.md files in the plugin cache (live discovery needs a login)"; else fail droid "$n/$EXPECTED SKILL.md files in the plugin cache"; fi
}

t_grok() {
  need grok grok || return
  local h f; h="$(new_home grok)"; f="$(log grok)"
  (
    export HOME="$h"
    grok plugin validate "$REPO" &&
      grok plugin install "$REPO" --trust &&
      grok inspect --json
  ) >"$f" 2>&1 || { fail grok "validate/install failed"; return; }
  check_count grok "$f"
}

t_agy() {
  need agy agy || return
  local h f; h="$(new_home agy)"; f="$(log agy)"
  (
    export HOME="$h"
    agy plugin validate "$REPO" &&
      agy plugin install "$REPO" &&
      agy plugin list
  ) >"$f" 2>&1 || { fail agy "validate/install failed"; return; }
  local n; n="$(find "$h/.gemini" -path '*/skills/*/SKILL.md' 2>/dev/null | wc -l | tr -d ' ')"
  if [ "$n" -ge "$EXPECTED" ]; then pass agy "$n SKILL.md files installed (model-level listing needs a Google login)"; else fail agy "$n/$EXPECTED SKILL.md files installed"; fi
}

t_pi() {
  need pi pi || return
  local h f; h="$(new_home pi)"; f="$(log pi)"
  (
    export HOME="$h"
    pi install "$REPO" &&
      pi list &&
      { echo '{"id":"1","type":"get_commands"}'; sleep 6; } | pi --mode rpc --no-session
  ) >"$f" 2>&1 || { fail pi "install failed"; return; }
  check_count pi "$f"
}

t_opencode() {
  need opencode opencode || return
  local h f; h="$(new_home opencode)"; f="$(log opencode)"
  mkdir -p "$h/.config/opencode"
  printf '{"plugin":["ai-agent-skills@git+file://%s"]}\n' "$REPO" >"$h/.config/opencode/opencode.json"
  (
    export HOME="$h" XDG_CONFIG_HOME="$h/.config" XDG_DATA_HOME="$h/.local/share" XDG_CACHE_HOME="$h/.cache" XDG_STATE_HOME="$h/.local/state"
    # Write to a file: piping truncates large output.
    to 90 opencode debug skill >"$f.skills"
  ) 2>"$f" || { fail opencode "opencode debug skill failed"; return; }
  check_count opencode "$f.skills"
}

t_kimi() {
  need kimi kimi || return
  local h f port; h="$(new_home kimi)"; f="$(log kimi)"; port=$((20000 + RANDOM % 10000))
  python3 "$ROOT/scripts/kimi_tui_install.py" "$h" "$REPO" >"$f" 2>&1 || { fail kimi "TUI plugin install failed"; return; }
  mkdir -p "$h/.kimi-code"
  printf 'default_model = "mock"\n\n[providers.mock]\ntype = "openai"\nbase_url = "http://127.0.0.1:%s/v1"\napi_key = "dummy"\n\n[models.mock]\nprovider = "mock"\nmodel = "mock-model"\nmax_context_size = 128000\n' "$port" >"$h/.kimi-code/config.toml"
  python3 "$ROOT/scripts/mock_openai.py" "$port" "$f.request" &
  local mock=$!
  sleep 1
  (cd "$h" && HOME="$h" KIMI_CODE_HOME="$h/.kimi-code" to 90 kimi -p hi) >>"$f" 2>&1
  kill "$mock" 2>/dev/null; wait "$mock" 2>/dev/null
  [ -s "$f.request" ] || { fail kimi "mock model server got no request"; return; }
  # The system prompt Kimi sends to the model must list every skill from the plugin.
  check_count kimi "$f.request"
}

t_hermes() {
  need hermes hermes || return
  local h f; h="$(new_home hermes)"; f="$(log hermes)"
  (
    export HOME="$h" HERMES_HOME="$h/.hermes"
    hermes plugins validate "$REPO" &&
      hermes plugins install "file://$REPO" --enable &&
      hermes plugins list --plain --no-bundled
  ) >"$f" 2>&1 || { fail hermes "plugin validate/install failed"; return; }
  grep -q "enabled.*ai-agent-skills" "$f" || { fail hermes "plugin not enabled"; return; }
  # Plugin skills are not advertised to the model on Hermes, so the documented route is a skills tap.
  # This leg reads GitHub, so it tests whatever is on the default branch of the public repo.
  (
    export HOME="$h" HERMES_HOME="$h/.hermes"
    hermes skills tap add ysskrishna/ai-agent-skills &&
      hermes skills install ysskrishna/ai-agent-skills/five-whys --yes &&
      hermes skills list --source hub
  ) >"$f.tap" 2>&1 || { fail hermes "skills tap install failed"; return; }
  grep -q "five-whys" "$f.tap" && pass hermes "plugin validates and enables; tap installs five-whys (plugin skills are not model-advertised)" || fail hermes "tap-installed skill not listed"
}

t_devin() {
  need devin devin || return
  local h f; h="$(new_home devin)"; f="$(log devin)"
  # Plugin commands need a Devin login, which a throwaway HOME never has.
  if ! HOME="$h" devin plugins list >"$f" 2>&1; then
    skip devin "needs a Devin login (run: devin plugins install --local <clone> -y, then devin plugins info ai-agent-skills)"
    return
  fi
  (HOME="$h" devin plugins install --local "$REPO" -y && HOME="$h" devin plugins info ai-agent-skills) >"$f" 2>&1 || { fail devin "plugin install failed"; return; }
  pass devin "plugin installed"
}

t_muse() {
  need muse muse || return
  local h f; h="$(new_home muse)"; f="$(log muse)"
  (
    export HOME="$h" MUSE_EXPERIMENTAL_PLUGINS=1
    muse plugins validate "$REPO" --json &&
      muse plugins install "$REPO" --scope user &&
      muse plugins approve ai-agent-skills &&
      muse skills list --source plugin
  ) >"$f" 2>&1 || { fail muse "validate/install/approve failed"; return; }
  check_count muse "$f"
}

t_cursor() {
  need node cursor || return
  local f; f="$(log cursor)"
  # Cursor's own JSON schemas, the same ones its marketplace CI runs.
  (
    set -e
    mkdir -p "$WORK/cursor-schema" && cd "$WORK/cursor-schema"
    for s in plugin marketplace; do
      curl -fsSL "https://raw.githubusercontent.com/cursor/plugins/main/schemas/$s.schema.json" -o "$s.schema.json"
    done
    npm install --silent --no-audit --no-fund --prefix . ajv@8 ajv-formats@3
    node -e '
      const Ajv = require("ajv"), fmts = require("ajv-formats"), fs = require("fs");
      const ajv = new Ajv({ allErrors: true, strict: false }); fmts(ajv);
      const repo = process.argv[1];
      let bad = 0;
      for (const [schema, file] of [["plugin", ".cursor-plugin/plugin.json"], ["marketplace", ".cursor-plugin/marketplace.json"]]) {
        const ok = ajv.compile(JSON.parse(fs.readFileSync(schema + ".schema.json")))(JSON.parse(fs.readFileSync(repo + "/" + file)));
        console.log(file, ok ? "valid" : "INVALID");
        if (!ok) bad++;
      }
      process.exit(bad ? 1 : 0);
    ' "$REPO"
  ) >"$f" 2>&1 && pass cursor "manifests validate against Cursor's schemas (IDE install is manual)" || fail cursor "schema validation failed"
}

main() {
  local want=() a
  while [ $# -gt 0 ]; do
    case "$1" in
      --source) SOURCE="$2"; shift 2 ;;
      all) want=($ALL); shift ;;
      *) want+=("$1"); shift ;;
    esac
  done
  [ ${#want[@]} -gt 0 ] || { sed -n '2,13p' "$0"; exit 2; }
  prepare_source
  echo "source: $SOURCE (HEAD $(git -C "$SOURCE" rev-parse --short HEAD)), $EXPECTED skills, scratch: $WORK"
  for a in "${want[@]}"; do
    case "$a" in
      gemini-skills) t_gemini_skills ;;
      skills|gh|claude|codex|gemini|copilot|qwen|droid|grok|agy|pi|opencode|kimi|hermes|devin|muse|cursor) "t_$a" ;;
      *) echo "unknown cli: $a" >&2; FAILED=1 ;;
    esac
  done
  [ "${KEEP:-0}" = "1" ] || [ "$FAILED" = "1" ] || rm -rf "$WORK"
  exit "$FAILED"
}

main "$@"
