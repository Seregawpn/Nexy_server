# Latest Changes (Обязательный журнал текущего цикла)

Статус: ACTIVE
Цикл версии: 1.6.1.40
Обновлено: 2026-02-16

## Правило (обязательно)

- При любом изменении клиентского кода/конфигурации/документов этот файл должен быть обновлен в том же changeset.
- Перед релизным апдейтом файл должен быть заполнен.
- Сразу после завершения апдейта/релиза файл очищается до шаблона (статус `EMPTY`) для нового цикла.

## Изменения текущего цикла

- 2026-02-16 | browser_use integration | removed legacy setup retry loop (`BROWSER_SETUP_IN_PROGRESS`) from orchestration path | lower duplication and fewer false waits
- 2026-02-16 | browser UX | added immediate start TTS on `BROWSER_TASK_STARTED` ("Browser opened. Starting search now.") | removes perceived freeze before first step
- 2026-02-16 | browser_automation (production) | fixed frozen Playwright driver resolution for modern `node + package/cli.js` layout in `Contents/Resources` | prevents repeated install notifications in Production
- 2026-02-16 | instance_manager | lock race hardening and centralized probe config | lower duplicate-start risk
- 2026-02-16 | browser_automation | blocked frozen self-spawn fallback for playwright install | prevents restart/focus loops
- 2026-02-16 | focus policy | disabled tray startup focus fallback by default | reduces focus stealing and VoiceOver conflicts
- 2026-02-16 | docs/governance | added Focus/VoiceOver gates and packaging runtime UX checks | mandatory release validation
- 2026-02-16 | build pipeline | signing script now fails fast on unsigned Mach-O subcomponents | prevents late codesign failure
- 2026-02-16 | browser UX | added user callback for LLM 503/UNAVAILABLE with notification + TTS retry hint | better user feedback
- 2026-02-16 | packaging permissions | removed camera entitlement and NSCameraUsageDescription | aligns with camera-disabled product policy
- 2026-02-16 | assistant governance | codex+antigravity rules now require explicit change information block in every report | improves change traceability
- 2026-02-16 | assistant governance | clarified exact placement of change-information block and updated shared report template | removes reporting ambiguity

## Формат записи

- `YYYY-MM-DD | <scope> | <коротко что изменено> | <риск/влияние>`

Пример:
- `2026-02-16 | instance_manager | hardened lock validation and fallback cleanup | lower duplicate-start risk`
