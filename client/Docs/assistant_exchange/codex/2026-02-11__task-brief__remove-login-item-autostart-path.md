# Remove Login Item Autostart Path

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-11

## Diagnosis
В модуле автозапуска оставался альтернативный `login_item` путь, который не использовался runtime-интеграцией и создавал дублирующую точку запуска.

## Root Cause
Исторический код Login Items не был удален после перехода к единому owner через LaunchAgent.

## Changes
- Удален файл `modules/autostart_manager/macos/login_item.py`.
- В `modules/autostart_manager/core/types.py` и `modules/autostart_manager/core/config.py` поле `method` ограничено типом `Literal["launch_agent"]`.
- Обновлены актуальные описания: `modules/autostart_manager/README.md`, `Docs/ARCHITECTURE_OVERVIEW.md` (без Login Items).

## Verification
- `rg` по активному коду/докам: ссылок на `login_item` не осталось.
- `python3 -m py_compile` для затронутых модулей — ok.
