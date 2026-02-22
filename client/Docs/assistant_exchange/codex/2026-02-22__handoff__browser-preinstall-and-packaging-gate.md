## Task
Реализовать порядок: сначала подготовка браузера, затем упаковка приложения; убрать скачивание браузера из release packaging flow.

## Diagnosis
Релизная упаковка не должна выполнять runtime-download браузера.

## Root Cause
Смешанные этапы preparation и packaging приводят к нестабильному owner-path.

## Changes
1. `scripts/prepare_playwright_browser_bundle.sh`
- добавлен `--verify-only` (валидация существующего bundle без скачивания);
- добавлен reuse-путь по умолчанию (если bundle валиден, не переустанавливает);
- добавлен `--force` для принудительной переустановки.

2. `packaging/build_final.sh`
- убран auto-install Chromium внутри packaging;
- оставлен strict fail-fast при отсутствии/невалидности prebuilt bundle.

3. `scripts/verify_packaging_readiness.py`
- добавлен обязательный browser-bundle gate через `prepare_playwright_browser_bundle.sh --verify-only`.

4. `Docs/RELEASE_VERSIONING_AND_PUBLISHING.md`
- добавлен обязательный шаг 0: подготовка browser bundle до packaging.

## Verification
- `bash -n scripts/prepare_playwright_browser_bundle.sh` — OK
- `./scripts/prepare_playwright_browser_bundle.sh --verify-only` — OK
- `./scripts/prepare_playwright_browser_bundle.sh` — OK (reused prebuilt bundle)
- `python .venv/bin/python scripts/verify_packaging_readiness.py` — OK

## Информация об изменениях
- Что изменено:
  - Реализован strict порядок preinstall browser -> package.
  - Исключена переустановка браузера в release packaging.
- Список файлов:
  - `scripts/prepare_playwright_browser_bundle.sh`
  - `packaging/build_final.sh`
  - `scripts/verify_packaging_readiness.py`
  - `Docs/RELEASE_VERSIONING_AND_PUBLISHING.md`
  - `Docs/assistant_exchange/codex/2026-02-22__handoff__browser-preinstall-and-packaging-gate.md`
- Причина/цель изменений:
  - Детерминированная production упаковка без runtime download.
- Проверка:
  - Успешные verify-only/reuse/readiness проверки.
