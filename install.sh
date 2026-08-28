#!/usr/bin/env bash
# Discovery OS installer
#
#   Local:  ./install.sh
#   Remote: curl -fsSL https://raw.githubusercontent.com/OWNER/discovery-os/main/install.sh | bash
#
# Installs seven product discovery skills into every AI coding agent it finds on this
# machine. Idempotent: running it again upgrades in place. Nothing is installed outside
# your home directory, and nothing is sent anywhere.
#
#   --uninstall    remove everything this script installed
#   --dry-run      print what would happen, change nothing
#   --dir PATH     install from a specific local checkout

set -euo pipefail

REPO_URL="${DISCOVERY_OS_REPO:-https://github.com/riadchaban994-bot/discovery-os.git}"
SKILLS=(product-discovery discovery-interviewing discovery-synthesis discovery-quant
        discovery-experiments discovery-prototyping discovery-ops)
COMMANDS=(discovery discovery-audit discovery-interview discovery-synthesise
          discovery-experiment discovery-prototype discovery-challenge)

DRY=0; UNINSTALL=0; SRC=""
while [ $# -gt 0 ]; do
  case "$1" in
    --dry-run)   DRY=1 ;;
    --uninstall) UNINSTALL=1 ;;
    --dir)       SRC="${2:-}"; shift ;;
    -h|--help)   sed -n '2,13p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "unknown option: $1" >&2; exit 2 ;;
  esac
  shift
done

bold()  { printf '\033[1m%s\033[0m\n' "$*"; }
dim()   { printf '\033[2m%s\033[0m\n' "$*"; }
ok()    { printf '  \033[32m+\033[0m %s\n' "$*"; }
skip()  { printf '  \033[2m-\033[0m %s\n' "$*"; }
warn()  { printf '  \033[33m!\033[0m %s\n' "$*"; }

run() { if [ "$DRY" = 1 ]; then dim "    would: $*"; else "$@"; fi; }

# ---------------------------------------------------------------- source ----
resolve_source() {
  if [ -n "$SRC" ]; then
    [ -d "$SRC/skills" ] || { echo "no skills/ directory in $SRC" >&2; exit 1; }
    printf '%s' "$SRC"; return
  fi
  local here
  here="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" 2>/dev/null && pwd -P || true)"
  if [ -n "$here" ] && [ -d "$here/skills" ]; then printf '%s' "$here"; return; fi
  command -v git >/dev/null 2>&1 || { echo "git is required to fetch Discovery OS" >&2; exit 1; }
  local tmp; tmp="$(mktemp -d)"
  dim "  fetching $REPO_URL"
  git clone --depth 1 --quiet "$REPO_URL" "$tmp/discovery-os"
  printf '%s' "$tmp/discovery-os"
}

# ---------------------------------------------------------------- targets ---
# Each entry: label|skills dir|commands dir (empty when the runtime has none)
detect_targets() {
  local t=()
  [ -d "$HOME/.claude"  ] && t+=("Claude Code|$HOME/.claude/skills|$HOME/.claude/commands")
  [ -d "$HOME/.codex"   ] && t+=("Codex|$HOME/.codex/skills|$HOME/.codex/prompts")
  [ -d "$HOME/.copilot" ] && t+=("Copilot CLI|$HOME/.copilot/skills|")
  [ -d "$HOME/.gemini"  ] && t+=("Gemini CLI|$HOME/.gemini/skills|")
  # Cross-runtime path read by Codex, Copilot CLI and Gemini CLI. Only useful if one of
  # them is present; Claude Code does not read it.
  if [ -d "$HOME/.codex" ] || [ -d "$HOME/.copilot" ] || [ -d "$HOME/.gemini" ] || [ -d "$HOME/.agents" ]; then
    t+=("cross-runtime|$HOME/.agents/skills|")
  fi
  printf '%s\n' "${t[@]:-}"
}

# -------------------------------------------------------------- uninstall ---
if [ "$UNINSTALL" = 1 ]; then
  bold "Discovery OS: uninstall"
  while IFS='|' read -r label sdir cdir; do
    [ -n "${label:-}" ] || continue
    echo; bold "$label"
    for s in "${SKILLS[@]}"; do
      if [ -d "$sdir/$s" ]; then run rm -rf "$sdir/$s"; ok "removed skill $s"; else skip "$s not present"; fi
    done
    if [ -n "$cdir" ] && [ -d "$cdir" ]; then
      for c in "${COMMANDS[@]}"; do
        [ -f "$cdir/$c.md" ] && { run rm -f "$cdir/$c.md"; ok "removed command /$c"; }
      done
    fi
  done < <(detect_targets)
  echo; dim "If you installed the Claude Code plugin, also run:  /plugin uninstall discovery-os"
  exit 0
fi

# ---------------------------------------------------------------- install ---
bold "Discovery OS installer"
SRC_DIR="$(resolve_source)"
dim "  source: $SRC_DIR"
[ "$DRY" = 1 ] && dim "  DRY RUN, nothing will change"

VERSION="$(sed -n 's/.*"version"[^"]*"\([^"]*\)".*/\1/p' "$SRC_DIR/.claude-plugin/plugin.json" 2>/dev/null | head -1)"
dim "  version: ${VERSION:-unknown}"

FOUND=0
while IFS='|' read -r label sdir cdir; do
  [ -n "${label:-}" ] || continue
  FOUND=1
  echo; bold "$label"
  run mkdir -p "$sdir"
  for s in "${SKILLS[@]}"; do
    if [ ! -d "$SRC_DIR/skills/$s" ]; then warn "missing in source: $s"; continue; fi
    run rm -rf "$sdir/$s"
    run cp -R "$SRC_DIR/skills/$s" "$sdir/$s"
    ok "$s"
  done
  if [ -n "$cdir" ]; then
    if [ -d "$cdir" ] || [ "$label" = "Claude Code" ]; then
      run mkdir -p "$cdir"
      for c in "${COMMANDS[@]}"; do
        [ -f "$SRC_DIR/commands/$c.md" ] && { run cp "$SRC_DIR/commands/$c.md" "$cdir/$c.md"; ok "/$c"; }
      done
    else
      skip "no commands directory for $label, skills still work by name"
    fi
  fi
done < <(detect_targets)

if [ "$FOUND" = 0 ]; then
  warn "No AI agent found in your home directory."
  echo "  Expected one of: ~/.claude  ~/.codex  ~/.copilot  ~/.gemini"
  echo "  Install one, then run this again. Or copy skills/ manually into your agent's"
  echo "  skills directory."
  exit 1
fi

# ------------------------------------------------------------- self-check ---
echo; bold "Checking"
PY="$(command -v python3 || true)"
if [ -n "$PY" ]; then
  if "$PY" -c 'import sys; sys.exit(0 if sys.version_info>=(3,8) else 1)'; then
    ok "python3 $("$PY" -c 'import platform;print(platform.python_version())') found, analysis scripts will run"
  else
    warn "python3 is older than 3.8. The analysis scripts need 3.8 or newer."
  fi
  "$PY" -c 'import numpy' 2>/dev/null \
    && ok "numpy found, Bayesian and CUPED analysis available" \
    || skip "numpy not installed (optional; only the Bayesian read and CUPED need it)"
else
  warn "python3 not found. Everything works except the five analysis scripts in"
  echo "    discovery-quant/scripts/."
fi

echo
bold "Done"
cat <<'NEXT'

  Start with any of these:

    /discovery            we want to build X, is that the right thing?
    /discovery-audit      grade every claim in a PRD or business case
    /discovery-interview  design a guide, rehearse it, or write up a session
    /discovery-synthesise turn transcripts or tickets into traceable findings
    /discovery-experiment map the assumptions and design the cheapest test
    /discovery-prototype  build a clickable prototype or a fake door
    /discovery-challenge  red-team a plan or a conclusion

  Or just describe the situation. The skills trigger on their own.

  On Codex and other agents without slash commands, say "use the product-discovery
  skill" and describe the situation.

  Uninstall any time:  ./install.sh --uninstall

NEXT
