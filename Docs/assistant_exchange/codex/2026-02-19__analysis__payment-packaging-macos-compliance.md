# Analysis: payment packaging docs vs macOS compliance

## Context
User asked what must be changed in packaging/release docs before enabling payment in macOS app.

## Current state found
1. `client/Docs/PACKAGING_FINAL_GUIDE.md` says Payment is NOT packaged.
2. Actual bundle path includes full `integration/` directory in `client/packaging/Nexy.spec`, so payment integration code is bundled when feature is enabled at runtime.
3. Main app `info_plist` in `Nexy.spec` has `CFBundleURLTypes: []`, while payment integration still contains deep-link handling (`nexy://payment/...`).
4. Payment success server page now uses close-window UX, no “Open App” deep-link button.
5. ATS policy is broad (`NSAllowsArbitraryLoads=true`) in multiple plist sources.

## Required doc-level changes (for compliance and architecture consistency)
- Align packaging docs with actual packaging behavior (remove incorrect “not packaged” statement or document feature-gated packaging model).
- Decide single owner for payment return path:
  - either browser close-window flow (no deep-link),
  - or deep-link flow (requires URL scheme registration in app plist and verification gate).
- Add explicit payment release gate section:
  - payment feature flag state (on/off) and target server mode,
  - Stripe mode expectation (test vs live),
  - no payment-card-data handling in app (Stripe Checkout only),
  - webhook/reconcile completion path validation.
- Add ATS policy guidance for payment endpoints (avoid arbitrary loads where possible).
- Add release checklist items for payment smoke tests and data-safety/logging checks.

## Suggested files to update
- `client/Docs/PACKAGING_FINAL_GUIDE.md`
- `client/Docs/PACKAGING_READINESS_CHECKLIST.md`
- `client/Docs/RELEASE_VERSIONING_AND_PUBLISHING.md`
- Optional: `client/Docs/PROJECT_REQUIREMENTS.md` (new payment release requirement IDs)

## Notable risks if unchanged
- Documentation/runtime mismatch for payment packaging state.
- Ambiguous payment return owner-path (deep-link vs browser close-window).
- Overly broad ATS in production packaging profile.
