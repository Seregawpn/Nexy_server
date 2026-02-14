# Update runtime status from nexy-dev.log

## Scope
- Requested: verify whether update flow currently works.
- Sources used:
  - `/Users/sergiyzasorin/Library/Logs/Nexy/nexy-dev.log`
  - `modules/updater/net.py`
  - `modules/updater/updater.py`

## Runtime check result
- In latest startup window (`2026-02-13 20:25:42`), updater flow is triggered correctly:
  - startup check started
  - manifest requested and parsed
  - newer version found (`1.6.1.34`)
  - update_started emitted
- Update installation does **not** complete:
  - update_failed emitted immediately after download phase start
  - reason: `URL должен использовать HTTPS для безопасности (кроме localhost для тестирования)`

## Root cause
- Artifact URL from appcast/manifest is non-HTTPS.
- Client guard in `modules/updater/net.py` explicitly blocks non-HTTPS URLs in `download_file()`.

## Additional note
- Duplicate startup check regression was not observed in this run (single startup manifest request in that startup second).
- Direct external fetch from this terminal is currently DNS-limited, so final verdict is based on app runtime logs and local code guard.

## Conclusion
- Updater orchestration works.
- End-to-end update is currently broken by artifact URL scheme (server/publish side), not by client startup logic.
