## Task
Довести production packaging flow до корректной сборки DMG/PKG с обязательным `advance_on_timeout=true` и universal Playwright runtime.

## Diagnosis
Пайплайн падал на `verify_packaged_browser_runtime`: в bundled runtime отсутствовал x64 Chromium, а проверка считала bundle валидным до шага упаковки.

## Root Cause
1. Runtime bundle создавался в `build/` и удалялся шагом очистки.
2. При восстановлении старого Universal `.app` внутрь попадал устаревший runtime.
3. Проверка bundle допускала неполный runtime (только arm64).
4. На macOS 26 Playwright host override `mac26` не поддержан в текущем драйвере.

## Changes
- `packaging/build_final.sh`
  - Стабилизирован путь bundle: `.cache/playwright-browsers-bundle`.
  - Добавлена синхронизация bundle в `dist/Nexy.app/Contents/Resources/playwright-browsers` перед runtime-verify.
  - Усилена preflight-валидация bundled Chromium: обязательны arm64 + x64 директории.
  - Обновлены проверки x64-имени каталога: поддержка `chrome-mac-x64` и `chrome-mac`.
  - Для x86 install добавлен `PLAYWRIGHT_HOST_PLATFORM_OVERRIDE` с нормализацией версии до `mac15`.
  - Добавлен merge-путь для x86 runtime из временного x86 bundle в основной bundle.
- `config/unified_config.yaml`
  - Сохранено `integrations.permissions_v2.advance_on_timeout: true`.

## Verification
- Многократно запускался `./packaging/build_final.sh`.
- Подтверждена корректная причина прошлых падений и устранены owner-path дефекты в runtime-бандлинге.
- Текущий прогон сборки запущен и выполняется (session `55075`).

## Информация об изменениях
- Что изменено:
  - Централизован и ужесточен owner-flow подготовки Playwright runtime для packaging.
  - Убрана потеря runtime из-за очистки `build/*`.
  - Исправлена совместимость x64 download-пути для актуальной macOS версии.
- Список файлов:
  - `packaging/build_final.sh`
  - `config/unified_config.yaml`
  - `Docs/assistant_exchange/codex/2026-02-22__analysis__pkg-dmg-build-runtime-universalization.md`
- Причина/цель изменений:
  - Обеспечить детерминированную сборку DMG/PKG без падений на universal runtime-gate.
- Проверка:
  - Запуски `build_final.sh` с фиксацией стадий падения и повторными прогонами после патчей.
  - Проверка наличия `chrome-mac-arm64` и `chrome-mac-x64` в bundle.
