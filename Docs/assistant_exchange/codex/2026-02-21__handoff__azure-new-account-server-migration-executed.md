# Azure New Account Server Migration — Executed

## Target
- Subscription: `56a06a09-c7fd-4511-b0fe-88d876343d60`
- Resource Group: `NexyNewRG`
- VM: `NexyNew`
- Public IP: `20.104.80.82`
- Region: `canadacentral`

## Executed Actions
1. Created infrastructure (RG/VNet/Subnet/Public IP/NSG/NIC/VM).
2. Applied SSH key login (`azureuser`, key-based auth).
3. Fixed runtime bootstrap issues discovered during setup:
   - corrected `systemd` unit to canonical `ExecStart=/home/azureuser/voice-assistant/venv/bin/python3 server/main.py`
   - installed `python3.11` + rebuilt venv
   - installed and configured `nginx` with TLS and reverse proxy routes
   - aligned protobuf/grpc runtime: `protobuf>=6.31.1,<7`, `grpcio*>=1.75.1,<2`
4. Synced runtime config:
   - copied `config.env` to `/home/azureuser/voice-assistant/config.env`
   - set permissions: `root:azureuser`, `640`

## Verification
- Service status: `active`
- Local endpoints (VM):
  - `http://127.0.0.1:8080/health` -> OK
  - `http://127.0.0.1:8080/status` -> OK
  - `http://127.0.0.1:8081/health` -> OK
- Public endpoints (443/nginx):
  - `https://20.104.80.82/health` -> 200
  - `https://20.104.80.82/status` -> 200
  - `https://20.104.80.82/updates/health` -> 200
- Cache headers:
  - `/health` -> `Cache-Control: max-age=30`
  - `/updates/appcast.xml` -> `Cache-Control: max-age=60`
- Internal ports exposure check:
  - direct curl to `:50051/:8080/:8081` on public IP returns timeout (not publicly reachable)

## Known Notes
- `server/scripts/verify_deployment.sh` gives false negatives in this environment due parser/exit-code handling (`000000` HTTP code concatenation and brittle run-command parsing).
- Current runtime version reported by health: `1.6.1.34` (from deployed repo state on VM).

## Next Operational Step
- Perform DNS cutover to `20.104.80.82` and monitor error rate/latency for 30-60 minutes.
