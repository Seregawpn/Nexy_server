# PTT Focus Loss And Mic Not Activating

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-05
- ID (INS-###): <не указан>

## Diagnosis
После смены фокуса PTT-комбинация перестаёт доходить до input_processing, микрофон не открывается, слышны системные клики (NSBeep).

## Root Cause
Secure Input / keyThief в foreground приложении блокирует Quartz CGEventTap, из-за чего LONG_PRESS не генерируется и запись не стартует.

## Optimal Fix
Добавить обработку отключения CGEventTap (kCGEventTapDisabledByUserInput/Timeout) с восстановлением и деградацией PTT (ptt_available=false + suppress-beep handler).

## Verification
Проверить сценарий с фокусом на secure input: PTT не работает → лог о tap disabled. После выхода из secure input → восстановление CGEventTap и работа PTT.

## Запрос/цель
Объяснить причину и предложить минимальный фикс в рамках текущей архитектуры.

## Контекст
- Файлы: integration/integrations/input_processing_integration.py, modules/input_processing/keyboard/mac/quartz_monitor.py
- Документы: Docs/ARCHITECTURE_OVERVIEW.md, Docs/PROJECT_REQUIREMENTS.md
- Логи: log.md (WindowServer keyThief/deferring rules)

## Решения/выводы
- PTT зависит от Quartz CGEventTap, который может блокироваться secure input в foreground.
- Нужен health-check + восстановление tap и UX-логирование деградации.

## Открытые вопросы
- Есть ли централизованное событие app focus/secure input для уведомления UI?

## Следующие шаги
- Если подтвердим reproducible secure input case, внести изменения в QuartzKeyboardMonitor и InputProcessingIntegration.
