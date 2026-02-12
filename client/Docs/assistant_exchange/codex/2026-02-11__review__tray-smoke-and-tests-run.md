# Tray smoke and tests run

## Метаданные
- Ассистент: codex
- Тип: review
- Дата: 2026-02-11
- ID (INS-###): N/A

## Diagnosis
Выполнен прогон тестов и runtime smoke для tray/quit-пути после централизации tray icon update.

## Root Cause
Проверялась стабильность после изменений single-writer/stale-guard в tray icon pipeline.

## Optimal Fix
Не применялось в этой задаче (только верификация).

## Verification
- `pytest -q tests/test_tray_quit_dispatch.py` -> `4 passed`
- `pytest -q tests/test_coordinator_shutdown_user_initiated.py tests/test_user_quit_ack.py` -> `3 passed`
- `python3 main.py` (с escalated perms для доступа к `~/Library`) -> startup прошел до инициализации tray/integrations, остановлен вручную `SIGINT`, process exit `0`
- `pytest -q tests/test_tray_quit_dispatch.py tests/verify_menu_quit_fix.py` -> `verify_menu_quit_fix.py` вызывает `rumps.quit_application` и аварийно завершает интерпретатор (`Fatal Python error: Aborted`) в headless/pytest окружении.

## Pre-Change Gate Evidence (обязательно)
- Прочитанные документы: N/A (код не менялся, только прогон).
- Source of Truth: N/A.
- Дублирование: none.
- Feature Flags check: none.
- Race check: none.

## Запрос/цель
Прогнать предложенные проверки и smoke runtime.

## Контекст
- Файлы тестов:
  - `tests/test_tray_quit_dispatch.py`
  - `tests/verify_menu_quit_fix.py`
  - `tests/test_coordinator_shutdown_user_initiated.py`
  - `tests/test_user_quit_ack.py`

## Решения/выводы
- Базовые tray/coordinator quit тесты проходят.
- Runtime startup проходит.
- Один legacy тест не пригоден для headless pytest из-за прямого вызова `rumps.quit_application`.

## Найденные проблемы (если review)
- Статус: **ЧАСТИЧНОЕ**
- `tests/verify_menu_quit_fix.py` не стабилен в CI/headless окружении (процесс abort на `rumps.quit_application`).

## Открытые вопросы
- Перевести `verify_menu_quit_fix.py` на mock `rumps.quit_application` или пометить как manual-only?

## Следующие шаги
- Добавить маркер для GUI-only теста (`@pytest.mark.gui`) или мокнуть quit API.
