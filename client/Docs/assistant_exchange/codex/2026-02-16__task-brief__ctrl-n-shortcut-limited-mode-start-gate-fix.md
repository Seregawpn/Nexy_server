# Task Brief: Ctrl+N shortcut limited-mode startup gate fix

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-16
- ID (INS-###): N/A

## Diagnosis
Shortcut `Ctrl+N` не срабатывал, потому что `InputProcessingIntegration` не стартовал в `limited_mode`.

## Root Cause
В `SimpleModuleCoordinator.start()` действовал общий gate `first_run_permissions.are_all_granted` для `input`/`voice_recognition`.
При `limited_mode` (например, `screen_capture=fail`) gate блокировал `input`, и keyboard monitor не запускался, поэтому `keyboard.short_press` не генерировался.

## Optimal Fix
- Source of Truth: startup gate в `SimpleModuleCoordinator`.
- Изменение:
  - Убрано применение строгого `all granted` gate для `input` и `voice_recognition`.
  - Строгий gate оставлен только для `screenshot_capture` и `voiceover_ducking`.
  - Для `input/voice_recognition` используются их собственные runtime-gates и деградация в `limited_mode`.

## Verification
- `python3 -m py_compile integration/core/simple_module_coordinator.py` -> OK
- После перезапуска приложения проверить в логе:
  - нет `Skipping input start because permissions are not granted`
  - есть запуск keyboard monitor (`INPUT`/`Quartz` события)
  - при `Ctrl+N` появляются `QUARTZ_DECISION ... target_combo_activation` и `keyboard.short_press`

## Информация об изменениях
- Что изменено:
  - Скорректирован startup permission-gate для модулей в `SimpleModuleCoordinator`.
- Файлы:
  - `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/integration/core/simple_module_coordinator.py`
- Причина/цель:
  - Восстановить работу `Ctrl+N` в `limited_mode`, не ломая архитектуру owner-гейтов.
- Проверка:
  - Синтаксическая проверка Python файла и проверка diff.

