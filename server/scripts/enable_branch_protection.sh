#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT_DIR"

if ! command -v gh >/dev/null 2>&1; then
  echo "[branch-protection] gh CLI not found"
  exit 1
fi

if ! gh auth status >/dev/null 2>&1; then
  echo "[branch-protection] gh is not authenticated. Run: gh auth login"
  exit 1
fi

REMOTE_URL="$(git remote get-url origin)"

REPO_PATH="$(python3 - <<'PY' "$REMOTE_URL"
import re
import sys

url = sys.argv[1].strip()
match = re.search(r"github\.com[:/](?P<owner>[^/]+)/(?P<repo>[^/.]+)(?:\.git)?$", url)
if not match:
    raise SystemExit(1)
print(f"{match.group('owner')}/{match.group('repo')}")
PY
)"

if [[ -z "$REPO_PATH" ]]; then
  echo "[branch-protection] failed to parse repository from origin URL"
  exit 1
fi

BRANCHES=("$@")
if [[ ${#BRANCHES[@]} -eq 0 ]]; then
  BRANCHES=("main" "develop")
fi

for BRANCH in "${BRANCHES[@]}"; do
  echo "[branch-protection] applying rules to ${REPO_PATH}:${BRANCH}"
  gh api \
    --method PUT \
    -H "Accept: application/vnd.github+json" \
    "/repos/${REPO_PATH}/branches/${BRANCH}/protection" \
    -f required_status_checks.strict=true \
    -f required_status_checks.contexts[]="Server Quality Gate / quality" \
    -f enforce_admins=true \
    -f required_pull_request_reviews.required_approving_review_count=1 \
    -f required_pull_request_reviews.dismiss_stale_reviews=true \
    -f required_pull_request_reviews.require_code_owner_reviews=false \
    -F restrictions='null' \
    -F required_linear_history='true' \
    -F allow_force_pushes='false' \
    -F allow_deletions='false' \
    -F block_creations='false' \
    -F required_conversation_resolution='true' \
    -F lock_branch='false' \
    -F allow_fork_syncing='false' >/dev/null

  echo "[branch-protection] done for ${BRANCH}"
done

echo "[branch-protection] all requested branches updated"
