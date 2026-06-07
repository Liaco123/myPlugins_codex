#!/usr/bin/env bash
set -euo pipefail

if command -v gitnexus >/dev/null 2>&1; then
  exit 0
fi

if ! command -v npm >/dev/null 2>&1; then
  echo "GitNexus plugin: npm is required to install the global GitNexus CLI" >&2
  exit 0
fi

npm install -g gitnexus >/dev/null 2>&1 || {
  echo "GitNexus plugin: failed to install GitNexus CLI with npm install -g gitnexus" >&2
  exit 0
}
