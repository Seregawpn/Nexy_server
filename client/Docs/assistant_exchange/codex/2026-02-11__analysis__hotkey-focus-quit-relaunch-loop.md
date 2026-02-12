# Hotkey/Focus/Quit Relaunch Loop Analysis

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-11
- ID (INS-###): N/A

## Diagnosis
- Симптом пользователя (Spotlight/Alfred закрывается, Quit приводит к повторному запуску) соответствует гонке в quit-path и внешнему autostart-подъему.
- Клавиатурный монитор не подавляет `Cmd+Space` (observe-only, suppression только для `Ctrl+N`-ветки).

## Root Cause
- Причина: `TrayController._on_quit_clicked` публикует `quit_clicked` асинхронно и сразу завершает app.
- Механизм: при быстром выходе `USER_QUIT_INTENT`/`app.shutdown` могут не успеть отработать, `suspend_current_session` не вызывается вовремя.
- Эффект: LaunchAgent снова поднимает приложение, пользователь видит loop и срыв фокуса.

## Optimal Fix
- Закреплен единый owner quit-цепочки: `tray.quit_clicked -> TrayControllerIntegration -> USER_QUIT_INTENT/app.shutdown`.
- В `TrayController` добавлено короткое ожидание доставки quit-события (`future.result(timeout=0.5)`) до `tray_menu.quit()`.
- Добавлен регрессионный тест на dispatch-before-quit и timeout-path без падения.

## Verification
- `pytest -q tests/test_tray_quit_dispatch.py`
- Результат: `2 passed`

## Запрос/цель
- Проверить loop при горячих клавишах/фокусе и убрать причину повторного старта после Quit без реархитектуры.

## Контекст
- Файлы: `modules/tray_controller/core/tray_controller.py`, `tests/test_tray_quit_dispatch.py`, `modules/input_processing/keyboard/mac/quartz_monitor.py`
- Документы: `Docs/PROJECT_REQUIREMENTS.md`, `Docs/ARCHITECTURE_OVERVIEW.md`, `../Docs/_archive/ASSISTANT_COORDINATION_PROTOCOL.md`, `../Docs/_archive/CODEX_PROMPT.md`, `../Docs/_archive/ANTIGRAVITY_PROMPT.md`, `../Docs/_archive/assistant_exchange/TEMPLATE.md`
- Ограничения: без добавления новых владельцев состояния и обхода coordinator/event bus.

## Решения/выводы
- Дубликат владельцев не вводился; fix локализован в существующем tray path.
- Основной риск пользовательского loop снижен через устранение гонки dispatch/quit.

## Открытые вопросы
- Есть ли на машине пользователя сторонний/legacy LaunchAgent вне штатного `com.nexy.assistant` (нужна быстрая проверка окружения).

## Следующие шаги
- Прогнать ручной сценарий: `Quit` из трея -> убедиться, что relaunch не происходит.
- Снять фрагмент логов с маркерами `QUIT_ACK` и autostart suspend для подтверждения на среде пользователя.
