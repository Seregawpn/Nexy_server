# Task Brief: Disable Browser and Remove Nexy Chromium Runtime

## Context
Запрос: удалить браузер/Chrome для тестирования и исключить запуск browser automation в клиенте.

## Changes
1. Отключен browser feature в клиентском конфиге:
   - `features.browser.enabled: false`
   - `features.browser_use.enabled: false`
   - `browser_use.enabled: false`
2. Удален локальный Chromium runtime Nexy:
   - `~/Library/Application Support/Nexy-Dev/ms-playwright`
3. Проверено, что системный `Google Chrome.app` в `/Applications` и `~/Applications` не найден.

## Verification
- Проверка конфига через `rg` по `config/unified_config.yaml`.
- Проверка удаления runtime: директория `~/Library/Application Support/Nexy-Dev/ms-playwright` отсутствует.

## Информация об изменениях
- Что изменено:
  - Browser отключен флагами (централизованно через конфиг).
  - Удален runtime Chromium для Nexy-Dev.
- Список файлов:
  - `config/unified_config.yaml`
- Причина/цель изменений:
  - Полностью выключить browser-функционал для тестирования и убрать локальный browser runtime.
- Проверка:
  - Конфиг обновлен.
  - Runtime директория удалена.
