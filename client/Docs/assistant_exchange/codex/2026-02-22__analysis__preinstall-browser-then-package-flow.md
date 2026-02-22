## Task
Перевести packaging flow на порядок: сначала установить/подготовить браузер, потом упаковать приложение и нотаризировать.

## Diagnosis
Релизный скрипт не должен скачивать Chromium во время packaging/notarization. Browser runtime должен быть заранее подготовлен и только подхватываться в .app.

## Root Cause
Подготовка browser runtime была смешана с release packaging flow, что усложняло owner-path и делало сборку нестабильной.

## Changes
1. `packaging/build_final.sh`
- `prepare_playwright_browser_bundle()` теперь только проверяет prebuilt bundle.
- Авто-установка браузера внутри release сборки удалена.
- При отсутствии/неполном bundle: fail-fast с инструкцией запустить `scripts/prepare_playwright_browser_bundle.sh`.

2. `scripts/prepare_playwright_browser_bundle.sh`
- Добавлен режим `--verify-only`.
- Скрипт является owner-prestep для подготовки runtime.

3. `scripts/verify_packaging_readiness.py`
- Добавлен обязательный preflight-gate:
  - `bash scripts/prepare_playwright_browser_bundle.sh --verify-only`

4. `Docs/RELEASE_VERSIONING_AND_PUBLISHING.md`
- В раздел `9. Пошаговый Production Release` добавлен обязательный шаг 0:
  - сначала `./scripts/prepare_playwright_browser_bundle.sh`
  - затем `./packaging/build_final.sh`

## Verification
- `bash -n packaging/build_final.sh` — OK
- `bash -n scripts/prepare_playwright_browser_bundle.sh` — OK
- `./scripts/prepare_playwright_browser_bundle.sh --verify-only` — OK
- `python .venv/bin/python scripts/verify_packaging_readiness.py` — OK (включая новый browser bundle gate)

## Информация об изменениях
- Что изменено:
  - Выделен отдельный owner-step подготовки браузера до packaging.
  - Убрано скачивание браузера в release packaging flow.
  - Добавлен preflight-gate и обновлен release runbook.
- Список файлов:
  - `packaging/build_final.sh`
  - `scripts/prepare_playwright_browser_bundle.sh`
  - `scripts/verify_packaging_readiness.py`
  - `Docs/RELEASE_VERSIONING_AND_PUBLISHING.md`
  - `Docs/assistant_exchange/codex/2026-02-22__analysis__preinstall-browser-then-package-flow.md`
- Причина/цель изменений:
  - Жесткий и детерминированный порядок релиза: prepare browser -> package -> notarize.
- Проверка:
  - Синтаксическая проверка скриптов и прохождение readiness gate с verify-only режимом.
