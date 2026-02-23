#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "[quick_check] Running fast server checks..."

if [[ -x "$ROOT_DIR/.venv/bin/basedpyright" ]]; then
  echo "[quick_check] basedpyright server"
  "$ROOT_DIR/.venv/bin/basedpyright" server
elif command -v basedpyright >/dev/null 2>&1; then
  echo "[quick_check] basedpyright server"
  basedpyright server
else
  echo "[quick_check] basedpyright not found (skip type check)"
  echo "[quick_check] install tip: pip install basedpyright"
fi

echo "[quick_check] pytest server/tests -q"
python3 -m pytest server/tests -q

echo "[quick_check] Config sanity: feature flags"
ROOT_DIR="$ROOT_DIR" python3 - <<'PY'
import os
import sys
import pathlib
root = pathlib.Path(os.environ["ROOT_DIR"])
if str(root) not in sys.path:
    sys.path.insert(0, str(root))
from config.unified_config import get_config, get_allowed_commands
from config.prompts import build_system_prompt

cfg = get_config()
allowed = get_allowed_commands(cfg.features, cfg)

print("BROWSER_USE_ENABLED:", cfg.browser_use.enabled)
print("WEB_SEARCH_ENABLED:", cfg.features.web_search_enabled)
print("MESSAGES_ENABLED:", cfg.features.messages_enabled)
print("WHATSAPP_ENABLED:", cfg.whatsapp.enabled)
print("PAYMENT_ACTIVE:", cfg.subscription.is_active())
print("ALLOWED_COMMANDS:", allowed)

prompt = build_system_prompt(
    whatsapp_enabled=cfg.whatsapp.enabled,
    browser_enabled=cfg.browser_use.enabled,
    payment_enabled=cfg.subscription.is_active(),
    messages_enabled=cfg.features.messages_enabled,
    web_search_enabled=cfg.features.web_search_enabled,
)
prompt_has_buy = "buy_subscription" in prompt
prompt_has_manage = "manage_subscription" in prompt
if cfg.subscription.is_active():
    if not (prompt_has_buy and prompt_has_manage):
        raise SystemExit("[quick_check] Payment commands missing in prompt")

dtype = cfg.audio.format
codec = cfg.audio.audio_format
if dtype in ("pcm", "mp3"):
    raise SystemExit(f"[quick_check] AUDIO_FORMAT must be dtype, got {dtype}")
print("AUDIO_DTYPE:", dtype, "AUDIO_CODEC:", codec)
PY

REPO_ROOT="$(cd "$ROOT_DIR/../.." && pwd)"
if [[ -f "$REPO_ROOT/scripts/verify_runtime_flag_alignment.py" ]]; then
  echo "[quick_check] Cross-layer config sanity: runtime alignment"
  python3 "$REPO_ROOT/scripts/verify_runtime_flag_alignment.py"
fi

echo "[quick_check] Done."
