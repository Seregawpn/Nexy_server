## Task
Разобрать остановку packaging и определить точную причину `notary Invalid`, затем предложить/внести исправление.

## Diagnosis
Сборка останавливается на stapler после `notarytool status: Invalid`.

## Root Cause
По `xcrun notarytool log 44d7c994-59b0-427f-a9b2-239cb144ad01 --keychain-profile nexy-notary` Apple вернул critical errors:
- неподписанные `libEGL.dylib`, `libvk_swiftshader.dylib`, `libGLESv2.dylib`, `libwidevinecdm.dylib`
- отсутствует secure timestamp
Пути: внутри `Contents/Resources/playwright-browsers/.../Google Chrome for Testing.app/...` (arm64 и x64).

## Changes
- `scripts/sign_all_binaries.sh`
  - убрано исключение `| grep -v "/Google Chrome for Testing.app/"` из owner-прохода подписи Mach-O;
  - теперь dylib внутри nested Chromium app подписываются пофайлово (с `--timestamp`) до финального `--deep` подписи nested app.

## Verification
- Получен официальный notary log с точными причинами `Invalid`.
- Локально исправлен owner-path подписи проблемного дерева файлов.

## Информация об изменениях
- Что изменено:
  - устранено исключение, из-за которого часть Playwright Chromium dylib не попадала в подпись.
- Список файлов:
  - `scripts/sign_all_binaries.sh`
  - `Docs/assistant_exchange/codex/2026-02-22__analysis__notary-invalid-unsigned-playwright-dylibs.md`
- Причина/цель изменений:
  - убрать блокер notarization (`Archive contains critical validation errors`).
- Проверка:
  - анализ notary log, затем патч owner-скрипта подписи.
