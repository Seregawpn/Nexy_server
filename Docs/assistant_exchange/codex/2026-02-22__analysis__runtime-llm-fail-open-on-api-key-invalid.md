# Runtime LLM fail-open on API key invalid

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-22
- ID (INS-###): N/A

## Diagnosis
После стабилизации startup, runtime-запросы с `API_KEY_INVALID` всё ещё уходили в пустой LLM поток (`0 chunks`) и затем в fallback, который мог озвучивать обогащённый prompt вместо корректной деградации.

## Root Cause
Ошибка text-модуля проглатывалась в `_stream_module_results` → `_iter_processed_sentences` видел только `yielded_any=False` → включался fallback-разбор `enriched_text` (не owner-path для ошибок провайдера).

## Optimal Fix
- Для text path включён проброс исключений (`raise_errors=True`) из `_stream_module_results`.
- В `_iter_processed_sentences` добавлен единый fail-open ответ для runtime-ошибки LLM (без echo системного контекста).
- Лог первого сегмента сделан нейтральным (не утверждает, что это именно LLM sentence).

## Verification
- `python -m py_compile server/integrations/workflow_integrations/streaming_workflow_integration.py`
- Проверка diff: fallback теперь выбирается по `llm_runtime_error`, а не по echo `enriched_text`.

## Информация об изменениях
- Что изменено:
  - Добавлен `llm_runtime_error` guard в `_iter_processed_sentences`.
  - Добавлен параметр `raise_errors` в `_stream_module_results`.
  - Для `_stream_text_module` включен `raise_errors=True`.
  - Обновлен лог старта потока на нейтральный.
- Файлы:
  - `server/integrations/workflow_integrations/streaming_workflow_integration.py`
- Причина/цель:
  - Убрать silent-empty/ложный fallback при ошибках внешнего LLM провайдера.
- Проверка:
  - py_compile + ручная проверка кодовых веток и логики ветвления.

## Запрос/цель
Закрыть runtime-сценарий из логов: `API_KEY_INVALID` должен приводить к предсказуемому degraded response, а не к пустому/ложному LLM-потоку.

## Контекст
- Файлы: `server/integrations/workflow_integrations/streaming_workflow_integration.py`
- Документы: `AGENTS.md`, `server/Docs/ARCHITECTURE_OVERVIEW.md`, `../Docs/CODEX_PROMPT.md`, `../Docs/assistant_exchange/TEMPLATE.md`
- Ограничения: без реархитектуры, только в существующем owner-path workflow.

## Решения/выводы
- Source of Truth сохранен в `StreamingWorkflowIntegration` как owner runtime orchestration.
- Удален второй путь принятия решения (echo enriched_text при внешнем LLM-failure).

## Открытые вопросы
- Нужна ли локализация degraded-message под язык запроса пользователя.

## Следующие шаги
- Добавить unit/integration тест на сценарий `text_module.process` -> exception и ожидание fail-open текста.
