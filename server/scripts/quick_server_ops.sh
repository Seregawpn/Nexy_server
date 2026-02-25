#!/usr/bin/env bash
set -euo pipefail

# Unified quick entrypoint for deploy + monitor operations.
# Examples:
#   bash server/scripts/quick_server_ops.sh deploy --tag v1.6.1.44
#   bash server/scripts/quick_server_ops.sh check
#   bash server/scripts/quick_server_ops.sh monitor-start
#   bash server/scripts/quick_server_ops.sh monitor-once
#   bash server/scripts/quick_server_ops.sh monitor-stop

ACTION="${1:-}"
if [[ -z "$ACTION" ]]; then
  echo "Usage: $0 <deploy|check|monitor-start|monitor-once|monitor-stop|monitor-bridge-setup> [args...]" >&2
  exit 2
fi
shift || true

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
export AZURE_RESOURCE_GROUP="${AZURE_RESOURCE_GROUP:-NexyNewRG}"
export AZURE_VM_NAME="${AZURE_VM_NAME:-NexyNew}"
export PUBLIC_HOST="${PUBLIC_HOST:-nexy-prod-sergiy.canadacentral.cloudapp.azure.com}"

case "$ACTION" in
  deploy)
    bash "$REPO_ROOT/server/scripts/deploy_server_one_click.sh" "$@"
    ;;
  check)
    curl -fsS "https://${PUBLIC_HOST}/health" >/dev/null
    curl -fsS "https://${PUBLIC_HOST}/status" >/dev/null
    curl -fsS "https://${PUBLIC_HOST}/updates/health" >/dev/null
    python3 "$REPO_ROOT/server/scripts/grpc_smoke.py" "$PUBLIC_HOST" 443 >/dev/null
    echo "CHECK_OK host=${PUBLIC_HOST}"
    ;;
  monitor-start)
    INTERVAL_SECONDS="${INTERVAL_SECONDS:-3600}" \
      bash "$REPO_ROOT/server/scripts/start_local_server_monitor.sh"
    ;;
  monitor-once)
    bash "$REPO_ROOT/server/scripts/publish_server_incident_local.sh"
    bash "$REPO_ROOT/server/scripts/pull_remote_server_monitor_status.sh"
    ;;
  monitor-stop)
    bash "$REPO_ROOT/server/scripts/stop_local_server_monitor.sh"
    ;;
  monitor-bridge-setup)
    bash "$REPO_ROOT/server/scripts/setup_remote_server_monitor_bridge.sh"
    ;;
  *)
    echo "Unknown action: $ACTION" >&2
    exit 2
    ;;
esac
