# STT interim -> gRPC early send analysis

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-18
- ID (INS-###): N/A

## Diagnosis
`voice.recognition_completed` может приходить в промежуточном режиме (`interim=true`) при удержании PTT, но gRPC-слой отправляет запрос сразу на первое такое событие.
Это создает ранний старт обработки и риск потери хвоста фразы при длинном удержании.

## Root Cause
Арх-нарушение отсутствует (событийный owner-path сохранен), но есть контрактный разрыв: STT публикует interim/final в одном событии, а gRPC owner не фильтрует interim.
Механизм: первый partial text попадает в `_sessions[sid]["text"]` и запускает `_maybe_send`; последующие части не переотправляются, пока inflight активен.
Эффект: ранняя отправка и субъективно "ушла только первая часть".

## Optimal Fix
- Владелец решения: `GrpcClientIntegration` (single owner входа в gRPC send).
- Правило: `_on_voice_completed` должен игнорировать `interim=true` и отправлять только terminal STT (или буферизовать latest interim до terminal).
- Не добавлять новый owner-path в Input/Voice; только уточнить контракт потребления в gRPC.

## Verification
- Удерживать PTT 5-8с, говорить длинную фразу.
- Проверить, что `TRACE phase=grpc.start` появляется только после release/terminal STT.
- Проверить отсутствие ранних `grpc.request_started` при `interim=true`.

## Информация об изменениях
- Что изменено: Изменения не вносились.
- Файлы: Нет.
- Причина/цель: Диагностика текущего поведения передачи текста.
- Проверка: Анализ runtime логов + сверка owner-path в integration коде.

## Запрос/цель
Подтвердить, отправляется ли распознанный текст частями до завершения речи и почему может теряться хвост длинной фразы.

## Контекст
- Файлы: client/integration/integrations/voice_recognition_integration.py, client/integration/integrations/grpc_client_integration.py, client/integration/integrations/input_processing_integration.py, client/integration/workflows/processing_workflow.py
- Документы: Docs/PROJECT_REQUIREMENTS.md, Docs/ARCHITECTURE_OVERVIEW.md, Docs/ASSISTANT_COORDINATION_PROTOCOL.md, Docs/ANTIGRAVITY_PROMPT.md, Docs/CODEX_PROMPT.md, Docs/assistant_exchange/TEMPLATE.md
- Ограничения: Без реархитектуры, только owner-path совместимые изменения.

## Решения/выводы
- Да, в текущей реализации ранняя отправка до окончания речи действительно возможна.
- Причина не в EventBus/Mode owner-цепочке, а в несогласованности consumer-контракта `interim`.
- Primary fix должен жить в gRPC integration и не трогать source-of-truth режимов/сессий.

## Открытые вопросы
- Нужна ли поддержка streaming-to-server по interim вообще, или только terminal STT?

## Следующие шаги
- Внести фильтр `interim` в gRPC consumer и добавить контрактный тест "long hold -> one grpc start on terminal".
