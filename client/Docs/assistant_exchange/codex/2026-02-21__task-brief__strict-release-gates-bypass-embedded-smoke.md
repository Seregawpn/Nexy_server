# Strict Release Gates: bypass/env, embedded key, mandatory smoke

## Task
Добавить дополнительные release-гейты для конфликтов/рисков:
- запрет bypass-флагов в strict release,
- запрет embedded API key в strict release,
- обязательный post-package smoke в strict release.

## Architecture Fit
- Owner release policy: `packaging/build_final.sh`.
- Runtime/owner path браузера не изменялся.

## Implementation
1. Добавлен флаг strict режима:
- `NEXY_STRICT_RELEASE_MODE` (default `0` для текущего тестового цикла, включается явно в production).

2. В strict режиме (`=1`) packaging блокируется если:
- `NEXY_SKIP_GEMINI_API_LIVE_CHECK=1`
- `NEXY_SKIP_PLAYWRIGHT_BROWSERS_BUNDLE=1`
- `NEXY_REQUIRE_UNIVERSAL_CHROMIUM_RUNTIME=0`

3. В strict режиме добавлен блокирующий check на embedded API keys:
- если `EMBEDDED_GEMINI_API_KEY`/`EMBEDDED_GEMINI_API_KEY_FALLBACK` непустые -> fail.

4. В strict режиме `NEXY_POST_PACKAGE_SMOKE_CMD` стал обязательным:
- если не задан -> packaging fail.

## Verification
- `bash -n packaging/build_final.sh` — OK
- Поиск новых strict-gates в скрипте — OK

## Информация об изменениях
- что изменено:
  - Добавлены strict release policy gates.
  - Добавлен запрет embedded key для release в strict режиме.
  - Добавлена обязательность post-package smoke в strict режиме.
- список файлов:
  - `packaging/build_final.sh`
  - `Docs/assistant_exchange/codex/2026-02-21__task-brief__strict-release-gates-bypass-embedded-smoke.md`
- причина/цель изменений:
  - Закрыть эксплуатационные конфликты и избежать “случайного” релиза с bypass/embedded режимом.
- проверка (что выполнено для валидации):
  - Bash syntax check и проверка наличия новых gate секций.
