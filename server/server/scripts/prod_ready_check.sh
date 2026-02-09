#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

if [[ -t 1 ]]; then
  GREEN="\033[0;32m"
  RED="\033[0;31m"
  YELLOW="\033[0;33m"
  NC="\033[0m"
else
  GREEN=""
  RED=""
  YELLOW=""
  NC=""
fi

fail() {
  echo -e "${RED}[prod_ready] FAIL:${NC} $1" >&2
  exit 1
}

warn() {
  echo -e "${YELLOW}[prod_ready] WARN:${NC} $1" >&2
}

echo "[prod_ready] Starting server readiness checks..."

# 1) Full quality gate (syntax + basedpyright + pytest)
"${ROOT_DIR}/scripts/full_quality_scan.sh"

# 2) Feature flags registry consistency
echo "[prod_ready] Verifying feature flags registry..."
python3 "${ROOT_DIR}/scripts/verify_feature_flags.py"

# 3) Config.env sanity checks
CONFIG_ENV="${ROOT_DIR}/config.env"
if [[ ! -f "${CONFIG_ENV}" ]]; then
  fail "Missing config.env at ${CONFIG_ENV}"
fi

echo "[prod_ready] Checking config.env placeholders..."
ROOT_DIR="$ROOT_DIR" python3 - <<'PY'
import os
from pathlib import Path

cfg_path = Path(os.environ["ROOT_DIR"]) / "config.env"
text = cfg_path.read_text()

def get_val(key: str) -> str:
    for line in text.splitlines():
        if line.startswith(key + "="):
            return line.split("=", 1)[1].strip()
    return ""

def is_placeholder(val: str) -> bool:
    return ("YOUR_" in val) or ("_HERE" in val) or (val.strip() == "")

subscription_enabled = get_val("SUBSCRIPTION_ENABLED").lower() == "true"
forward_actions = get_val("FORWARD_ASSISTANT_ACTIONS").lower() == "true"

# Always-required keys
required = [
    "GEMINI_API_KEY",
    "AZURE_SPEECH_KEY",
]

missing = []
for key in required:
    val = get_val(key)
    if is_placeholder(val):
        missing.append(key)

# Stripe keys are required only if subscriptions are enabled
if subscription_enabled:
    for key in ["STRIPE_SECRET_KEY", "STRIPE_PUBLISHABLE_KEY", "STRIPE_PRICE_ID"]:
        val = get_val(key)
        if is_placeholder(val):
            missing.append(key)

if missing:
    raise SystemExit("Missing or placeholder config keys: " + ", ".join(missing))

# Guard for action forwarding
if not forward_actions:
    print("FORWARD_ASSISTANT_ACTIONS=false (actions disabled)")

print("config.env looks sane for current flags")
PY

# 4) Optional gRPC smoke test (only if explicitly requested)
if [[ "${RUN_GRPC_SMOKE:-false}" == "true" ]]; then
  echo "[prod_ready] Running gRPC smoke test..."
  python3 - <<'PY'
import os
import grpc
from pathlib import Path

root = Path(__file__).resolve().parents[2] / "server"
import sys
sys.path.insert(0, str(root))
from modules.grpc_service import streaming_pb2, streaming_pb2_grpc

host = os.getenv("GRPC_HOST", "127.0.0.1")
port = os.getenv("GRPC_PORT", "50051")

channel = grpc.insecure_channel(f"{host}:{port}")
stub = streaming_pb2_grpc.StreamingServiceStub(channel)

# Minimal request — requires a running server
req = streaming_pb2.StreamRequest(prompt="ping", hardware_id="test_hardware_id_32_chars____", session_id="test_session_id")

try:
    responses = stub.StreamAudio(req, timeout=5)
    # Consume one response to confirm stream opens
    next(responses)
    print("gRPC smoke test OK")
except Exception as e:
    raise SystemExit(f"gRPC smoke test failed: {e}")
PY
else
  warn "gRPC smoke test skipped (set RUN_GRPC_SMOKE=true to enable)"
fi

# 5) Optional Web Search smoke test (only if explicitly requested)
if [[ "${RUN_WEB_SEARCH_SMOKE:-false}" == "true" ]]; then
  echo "[prod_ready] Running Web Search smoke test..."
  QUERY="${WEB_SEARCH_QUERY:-latest news about SpaceX}" \
  TIMEOUT="${WEB_SEARCH_TIMEOUT:-12}" \
  python3 "${ROOT_DIR}/scripts/web_search_smoke_test.py"
else
  warn "Web Search smoke test skipped (set RUN_WEB_SEARCH_SMOKE=true to enable)"
fi

echo -e "${GREEN}[prod_ready] READY:${NC} all checks passed"
