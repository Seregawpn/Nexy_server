## PR: Impact, Flags, Gateways, Contracts

### Summary
- What changed:
- Why:
- Affected components/integrations:

### Impact-gate (before merge)
- [ ] Attached `.impact/change_impact.yaml` (axes, invariants, guards, tests, metrics, rollout)
- [ ] Updated `Docs/STATE_CATALOG.md` and/or `config/interaction_matrix.yaml` (if affected)
- [ ] 8–14 pairwise tests for chosen axes + 2 negative cases
- [ ] Decision logs visible locally (`decision=<...> ctx={...} source=<domain> duration_ms=<int>`)
- [ ] Feature flag + kill-switch specified

### Single Owner Check (required)
- [ ] Owner axis identified (module/file):
- [ ] Source of Truth identified:
- [ ] Duplicate path removed/merged (what exactly):
- [ ] Second decision path NOT introduced (how validated):
- [ ] For any legacy/fallback runtime path: expiry version/date specified:

### Contracts & FSM
- [ ] EventBus contract updated (if needed) and validated
- [ ] FSM guards cover permissions/device/network/firstRun
- [ ] No hidden state writes across domains (EventBus only)
- [ ] Critical event owner preserved (`app.mode_changed`, terminal processing intent)

### Lint & Quality
- [ ] Ruff passed (`ruff check .`)
- [ ] No direct state/cfg access outside `selectors.py`/`gateways.py` (`python scripts/verify_no_direct_state_access.py`)
- [ ] Logs/metrics/tracing follow section 8 and 15.1
- [ ] Architecture guards passed (`python scripts/verify_architecture_guards.py`)

### Rollout
- [ ] Feature flag name:
- [ ] Plan: 1% → 25% → 100%
- [ ] Kill-switch env/config:

### Screenshots / Logs
```text
<paste decision logs and key metrics excerpts>
```
