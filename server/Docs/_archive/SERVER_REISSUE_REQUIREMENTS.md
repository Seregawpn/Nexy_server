# Server Reissue Requirements Snapshot

Purpose: Canonical checklist for reissuing the server infrastructure on a new Azure account.

Sources of Truth:
- server/Docs/SERVER_DEPLOYMENT_GUIDE.md
- server/SCALING_100_USERS_GUIDE.md
- server/Docs/ARCHITECTURE_OVERVIEW.md
- server/Docs/FEATURE_FLAGS.md
- /Users/sergiyzasorin/Fix_new/Docs/PROJECT_REQUIREMENTS.md

Scope:
- Azure VM + networking + ingress + runtime + update server + verification.
- No architecture changes; configuration remains centralized in unified_config.

---

## 1) Account & CI Requirements (Mandatory)
- GitHub Actions secret: `AZURE_CREDENTIALS` in `Seregawpn/Nexy_server` with correct subscription/tenant/client.
- Azure subscription has permission to create: Resource Group, VNet/Subnet, Public IP (Static), NSG, VM, NIC.
- If IP/domain changes: update references in health checks and client config.

## 2) VM & OS Requirements
- OS: Ubuntu 22.04 LTS.
- Size: 2 vCPU / 4-8 GB RAM (B2s/B2ms) unless load testing indicates higher.
- Disk: 50-100 GB Standard SSD.
- SSH access with keys; password auth disabled if possible.

## 3) Network & Ingress Requirements
- NSG allows inbound: 22 (restricted to admin IP), 80/443 (public).
- Only external ingress: HTTPS 443 via Nginx.
- Internal services must bind to localhost:
  - gRPC: 127.0.0.1:50051
  - HTTP health/status: 127.0.0.1:8080
  - Update server: 127.0.0.1:8081
- Nginx config must place `/health` and `/status` locations before `/`.
- gRPC proxy: `grpc_pass grpc://127.0.0.1:50051;`

## 4) Runtime & Config Requirements
- Python 3.11 with `requirements.txt`.
- Service managed by systemd: `voice-assistant.service`.
- Single source of truth for config:
  - `config/unified_config.yaml`
  - `config/unified_config.py`
  - `config.env` for env overrides.
- No hardcoded ports/limits in code; all values via unified_config.

## 5) Update Server Requirements
- Directories present and writable:
  - `server/updates/downloads`
  - `server/updates/keys`
  - `server/updates/manifests`
- Cache-Control headers:
  - `/appcast.xml` -> `max-age=60`
  - `/updates/health` -> `max-age=30`
  - `/health` -> `max-age=30`

## 6) Observability & Limits
- Decision logs must include `decision=...` and `scope=grpc` where required.
- Backpressure limits from unified_config; no duplicates.
- Load testing available in `server/load_testing/` and documented in `server/SCALING_100_USERS_GUIDE.md`.

## 7) Verification Checklist (DoD)
- HTTPS health: `https://<ip_or_domain>/health` returns JSON OK.
- HTTPS status: `https://<ip_or_domain>/status` returns JSON OK.
- Update health: `https://<ip_or_domain>/updates/health` returns 200.
- Cache-Control headers match required values.
- gRPC smoke test succeeds (or logs skipped if offline).
- Internal ports (50051/8080/8081) not publicly reachable.

## 8) Known Pitfalls
- If `/health` and `/status` are after `/` in Nginx, 502 occurs (gRPC proxy intercepts).
- Missing `get_config` import in gRPC server breaks startup (see deployment guide).
- Update server may fail without write permissions; keep directories and ownership correct.
