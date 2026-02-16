# Task Brief: mandatory latest changes journal gate

## Request
Create a separate mandatory "latest changes" document, require updating it on each client change, and require clearing it after release update.

## Implemented

1. New mandatory journal
- Added `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/LATEST_CHANGES.md`.
- Includes lifecycle rules and current cycle entries.

2. Automated enforcement script
- Added `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/scripts/verify_latest_changes.py`.
- Checks:
  - if relevant client files changed, `Docs/LATEST_CHANGES.md` must also be changed;
  - journal section must contain at least one non-empty entry.
- Handles monorepo path prefixes (`client/...`) correctly.

3. Gate integration
- Updated `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/scripts/pre_build_gate.sh`.
- Added critical check: "Проверка обязательного журнала Latest Changes".

4. Documentation governance
- Added REQ-034 in:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/PROJECT_REQUIREMENTS.md`
- Added release lifecycle reset rule in:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/RELEASE_VERSIONING_AND_PUBLISHING.md`
- Added packaging checklist block in:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/Docs/PACKAGING_READINESS_CHECKLIST.md`

## Validation
- `python3 scripts/verify_latest_changes.py` -> OK
- `./scripts/pre_build_gate.sh --skip-tests --skip-lint` -> OK

## Outcome
Latest changes journal is now mandatory, machine-enforced in pre-build gate, and explicitly reset after release update by documented process.
