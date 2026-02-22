# Extra Packaging Gates: certifi + Chromium Arch + Optional Smoke

## Task
Добавить недостающие release-gates в упаковку для снижения рисков browser-use на пользовательских macOS.

## Architecture Fit
- Owner release path: `packaging/build_final.sh`.
- Runtime owner-модули не изменялись.

## Implementation
1. Добавлен preflight TLS CA bundle:
- проверка `certifi.where()` и существования CA файла.
- fail блокирует packaging.

2. Расширена `verify_packaged_browser_runtime()`:
- добавлена проверка macOS архитектурных директорий Chromium runtime,
- по умолчанию требуется universal-ready layout (`chrome-mac` + `chrome-mac-arm64`),
- управляется флагом `NEXY_REQUIRE_UNIVERSAL_CHROMIUM_RUNTIME` (default=1).

3. Добавлен optional post-package smoke hook:
- `NEXY_POST_PACKAGE_SMOKE_CMD` (если задан, выполняется и блокирует релиз при fail).

## Verification
- `bash -n packaging/build_final.sh` — OK
- Поиск новых секций в скрипте — OK

## Информация об изменениях
- что изменено:
  - Добавлен certifi gate в preflight.
  - Усилена проверка packaged Chromium runtime по архитектурным директориям.
  - Добавлен подключаемый post-package smoke gate.
- список файлов:
  - `packaging/build_final.sh`
  - `Docs/assistant_exchange/codex/2026-02-21__task-brief__extra-packaging-gates-certifi-arch-smoke.md`
- причина/цель изменений:
  - Закрыть остаточные риски runtime/TLS/архитектурного mismatch до публикации DMG/PKG.
- проверка (что выполнено для валидации):
  - Bash syntax check + подтверждение наличия новых gate-блоков через grep.
