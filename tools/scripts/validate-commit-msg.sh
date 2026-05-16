#!/usr/bin/env bash

set -euo pipefail

COMMIT_MSG_FILE="${1:-}"

if [ -z "$COMMIT_MSG_FILE" ]; then
  echo "Missing commit message file path."
  exit 1
fi

COMMIT_MSG="$(sed -n '1p' "$COMMIT_MSG_FILE")"

if printf '%s\n' "$COMMIT_MSG" | grep -Eq '^(Merge|Revert) '; then
  exit 0
fi

if printf '%s\n' "$COMMIT_MSG" | grep -Eq '^(build|chore|ci|docs|feat|fix|perf|refactor|revert|style|test)(\([a-z0-9._/-]+\))?!?: .+'; then
  exit 0
fi

cat <<ERROR
Invalid commit message:

  ${COMMIT_MSG}

Expected Conventional Commit format, for example:

  chore(repo): establish toolchain foundation
  docs(adr): record package manager decision
  feat(cli): add init command

Allowed types:

  build, chore, ci, docs, feat, fix, perf, refactor, revert, style, test
ERROR

exit 1
