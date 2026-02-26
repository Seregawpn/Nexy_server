# Analysis: Remote server down root cause

Date: 2026-02-20
Assistant: Codex

## Facts collected

1. VM state:
- `az vm list -d -o table` -> `Nexy`, `PowerState: VM stopped`, `PublicIps: 20.63.24.187`.
- `az vm get-instance-view -g NETWORKWATCHERRG -n Nexy --query "instanceView.statuses"` ->
  - `ProvisioningState/failed/VMStoppedToWarnSubscription`
  - message: `This VM has been stopped as a warning to non-paying subscription.`
  - time: `2026-02-20T17:37:35Z`
  - `PowerState/stopped`

2. Subscription write-path status:
- `az vm start -g NETWORKWATCHERRG -n Nexy` -> error `ReadOnlyDisabledSubscription`.
- `az vm run-command invoke ...` (monitor pull script) -> same error `ReadOnlyDisabledSubscription`.
- `az account subscription show --id 6ad75f5a-b865-4a45-9319-cc066ac37723` -> `state: Warned`.

3. Resource health timeline:
- `az monitor activity-log ... category=ResourceHealth` shows PlatformInitiated downtime:
  - `2026-02-20T04:30:18Z` title: `Down: Virtual machine has been unavailable for 15 minutes`, cause `PlatformInitiated`.

4. External symptoms:
- `curl https://20.63.24.187/health` timeout.
- `ssh azureuser@20.63.24.187` timeout.
- `check_grpc_health.py 20.63.24.187 443` -> health/status timeouts.

## Conclusion

Primary root cause is infrastructure/account enforcement at Azure subscription level, not application runtime (gRPC/Nginx/code). Platform stopped VM and blocked write actions, which made service unreachable.

## Next actions

1. Re-enable subscription/payment state in Azure billing.
2. Start VM `Nexy`.
3. Verify: `PowerState/running`, `/health` returns 200/OK, SSH reachable.
4. Re-run `server/scripts/pull_remote_server_monitor_status.sh`.
