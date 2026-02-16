# Runtime Analysis: shortcut / browser install / updater visibility

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-16
- ID (INS-###): N/A

## Diagnosis
В текущем запуске подтверждены: падение browser-setup внутри bundled Playwright Node, а update-flow корректно отрабатывает как `no_updates_available`, поэтому визуального апдейта нет.
По shortcut в последнем запуске нет событий `keyboard.press/keyboard.short_press`, поэтому проблема на входе capture, а не в обработчиках.

## Root Cause
- Browser install: frozen Playwright driver запускается, но завершается `FatalProcessOutOfMemory` → install Chromium прерывается → показывается `Browser setup failed`.
- Updater: манифест успешно получен с версией `1.6.1.40`, равной текущей → публикуется `updater.update_skipped` → уведомления intentionally disabled.
- Shortcut: в этом конкретном запуске подписчики на `keyboard.short_press` зарегистрированы, но сами события не приходят → источник в слое глобального key-capture/runtime permissions session.

## Optimal Fix
- Для browser-ошибки: зафиксировать runtime path для Playwright и выполнить install в стабильном окружении без запуска bundled `node` из read-only app bundle (или гарантировать совместимый node бинарь в bundle).
- Для updater: поведение корректное, fix не требуется; при необходимости включать отдельное UI-уведомление о `no_updates_available`.
- Для shortcut: воспроизвести с live-tail логом и проверить приход `QUARTZ_DECISION`/`keyboard.short_press` в реальном времени, чтобы локализовать capture-layer.

## Verification
- Лог-файл: `/Users/sergiyzasorin/Library/Logs/Nexy/nexy.log`
- Подтвержденные сигнатуры:
  - Browser fail: `Playwright install stderr ... FatalProcessOutOfMemory` + `Browser setup failed`.
  - Updater skip: `XML манифест распарсен: версия 1.6.1.40` + `Update skipped ... no_updates_available`.
  - Shortcut: есть `subscribe keyboard.short_press`, но в последнем запуске нет dispatch-событий на нажатие.

## Информация об изменениях
- Изменения не вносились.

