# Task Brief: Focus/VoiceOver documentation gates

## Request
Add explicit project documentation requirements so future changes do not conflict with VoiceOver and do not break user focus behavior.

## What was updated

1. Requirements gate
- Added `REQ-033: Focus/VoiceOver runtime safety gate` in:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/PROJECT_REQUIREMENTS.md`
- Added REQ-033 row to Implementation Map.

2. Architecture policy
- Added `1.2 Focus & VoiceOver Safety Policy (обязательно)` in:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/ARCHITECTURE_OVERVIEW.md`
- Policy captures defaults, owner boundaries, emergency exception, and release verification.

3. Pre-release verification
- Added mandatory manual section `Runtime Focus/VoiceOver Smoke` in:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/PRE_PACKAGING_VERIFICATION.md`

4. Packaging checklist
- Added explicit release check section `Runtime UX Safety (Focus/VoiceOver)` in:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/PACKAGING_READINESS_CHECKLIST.md`

5. Feature/config registry clarity
- Added focus policy config entries in:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/FEATURE_FLAGS.md`

## Architecture gates check
- Single owner: preserved (`main.py` + `SimpleModuleCoordinator` for focus policy decisions).
- Zero duplication: policy centralized in requirements + architecture + release checklist.
- Anti-race: no new runtime state or concurrent paths introduced.
- Flag lifecycle: focus config keys documented with defaults and release policy.

## Outcome
The project now has explicit, enforceable documentation gates so new changes must preserve:
- no forced focus stealing in normal runtime,
- VoiceOver compatibility,
- mandatory packaging-time smoke validation for these behaviors.
