# PR Title

## Summary
- What & why
- Scope (modules/integrations/config/grpc)

## Impact Gate
- [ ] Attached `.impact/change_impact.yaml`
- [ ] Updated `Docs/STATE_CATALOG.md`; included link or diff to `client/config/interaction_matrix.yaml` if client inputs change
- [ ] 8–14 pairwise tests + 2 negative
- [ ] Decision logs visible locally
- [ ] `/health` returns `latest_version` and `latest_build` as strings matching `/appcast.xml`; update logs clean
- [ ] Feature flag + kill-switch defined

## Rollout
- Flag name:
- Plan: 1% → 25% → 100% (shadow-mode if applicable)
- Kill-switch: `NEXY_KS_<FEATURE>`

## Testing
- Unit/contract tests:
- gRPC smoke:
- Health/status endpoints verified

## Risks & Mitigations
- Risks:
- Mitigations:

## Docs
- [ ] ARCHITECTURE_OVERVIEW updated (if architecture/contract/config touched)
- [ ] ADR added (if decision changes behavior)
