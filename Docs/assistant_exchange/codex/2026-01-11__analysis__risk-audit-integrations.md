# Risk Audit: Integrations

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-11
- ID (INS-###): INS-005

## Diagnosis
В интеграциях есть несколько пересекающихся источников истины (session_id, события режима) и разрозненные контракты событий, что создаёт потенциальные гонки, несогласованность и потерю событий.

## Root Cause
Нет строгого единого владельца session_id и события смены режима → разные интеграции записывают состояние и реагируют на неиспользуемые события → out-of-order обновления, пропуски обработчиков и ложные отмены.

## Optimal Fix
Цель: единый владелец session_id и единый канал режима, уменьшение гонок и ложных отмен.

## Verification
Проверка событий: session_id стабилен в одной цепочке, события режима приходят всем подписчикам, нет ложных отмен и зависших микрофонов.

## Запрос/цель
Определить опасные точки и конфликтные места в логике интеграций и модулей.

## Контекст
- Файлы: integration/integrations/input_processing_integration.py, integration/integrations/voice_recognition_integration.py, integration/integrations/speech_playback_integration.py, integration/core/selectors.py
- Документы: Docs/ARCHITECTURE_OVERVIEW.md, Docs/PROJECT_REQUIREMENTS.md
- Ограничения: без реархитектуры, сохранить текущую архитектуру и SoT

## Решения/выводы
- Multiple writers для session_id (input_processing, voice_recognition, speech_playback) создают риск отката session_id на старое значение при поздних чанках/коллбеках.
- input_processing подписан на mode.switch, но событие нигде не публикуется → обработчик режима не вызывается.
- Контракт событий нарушен: keyboard.press публикует data.timestamp как session_id (строка вместо числа).
- GoogleSRController коллбеки зависят от event_bus._loop; при отсутствии loop результат распознавания теряется.
- Дублирующие interrupt.request/grpc.request_cancel из разных веток увеличивают риск ложных отмен и race.

## Найденные проблемы (если review)
- N/A

## Открытые вопросы
- Нужен ли отдельный режим mode.switch или следует везде использовать app.mode_changed как единственный канал?
- Должен ли только InputProcessingIntegration писать session_id в ApplicationStateManager?

## Следующие шаги
- Зафиксировать владельца session_id и запретить запись из voice_recognition/speech_playback.
- Унифицировать события режима (app.mode_changed) или добавить публикацию mode.switch в ModeManagementIntegration.
- Исправить payload keyboard.press: отдельное поле session_id и корректный timestamp.
- Добавить безопасную публикацию событий из потоков (threadsafe publish) для GoogleSRController.
