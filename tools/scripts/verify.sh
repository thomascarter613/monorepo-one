#!/usr/bin/env bash

set -euo pipefail

say() {
  printf '\n==> %s\n' "$1"
}

require_command() {
  if ! command -v "$1" >/dev/null 2>&1; then
    echo "Missing required command: $1"
    exit 1
  fi
}

say "Checking required commands"
require_command bun
require_command git

say "Checking Git whitespace"
git diff --check

say "Checking Bun lockfile"
if [ ! -f bun.lock ]; then
  echo "Missing bun.lock. Run: bun install"
  exit 1
fi

say "Checking Biome"
bun run check:biome

say "Checking TypeScript"
bun run typecheck

say "Checking Turbo"
bun run verify:turbo

say "Checking moon"
bun run verify:moon

say "Checking Lefthook"
bun run verify:lefthook

say "Repository verification passed"
