# Streaming Latency Analysis

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-02
- ID (INS-###): N/A (CRM_INSTRUCTION_REGISTRY.md not found)

## Diagnosis
- Основная задержка до первого ответа возникает на этапе LLM (первый chunk ~21.7s), а не на gRPC/памяти/аудио.
- Мониторинг gRPC фиксирует «медленный ответ», но это следствие LLM-латентности, а не отдельный блок в StreamAudio.

## Root Cause
- Причина: высокая латентность LangChain Gemini при запросе с системным промптом + скриншотом.
- Механизм: первый streaming chunk от LLM приходит только спустя ~20s → задержка озвучки и всей цепочки.
- Эффект: end-to-end 10–25s на ответ при простых командах.

## Optimal Fix
- Цель: снизить time-to-first-token/first-chunk и стабилизировать p95 StreamAudio.
- Место в архитектуре: server text_processing (конфиг и провайдер) + workflow интеграция (решение о включении скриншота).
- Source of Truth: unified_config.py / env для LLM и tools, StreamingWorkflowIntegration для состава входных данных.
- План внедрения:
  1) Включить быстрый LLM профиль: LANGCHAIN_MODEL=gemini-2.5-flash (или более быстрый flash), TEXT_PROCESSING_TEMPERATURE=0.2–0.4, TEXT_PROCESSING_MAX_TOKENS=512–1024.
  2) Отключить tools для default чата (TEXT_PROCESSING_TOOLS=) и WEB_SEARCH_ENABLED=false, если поиск не нужен.
  3) Добавить в StreamingWorkflowIntegration дешёвый pre-filter скриншота: не передавать screenshot для коротких системных команд (open/close) или при отсутствии явного «описать/что на экране».
  4) Включить пер-стейдж метрики: time-to-first-chunk, time-to-first-audio, llm_total_time (уже есть) + корреляция с model/tools/screenshot.

## Verification
- DoD: p95 StreamAudio ≤ 1000–1500ms на простых командах без скриншота; time-to-first-chunk ≤ 1500ms.
- Шаги: сравнить запросы с/без скриншота; сравнить модель 3-flash-preview vs 2.5-flash; оценить эффект отключения tools.
- Ожидаемое поведение: падение time-to-first-chunk, исчезновение warning «Медленный ответ».

## Запрос/цель
- Найти причины задержек 10–15s и предложить архитектурно совместимые пути ускорения.

## Контекст
- Файлы: server/server/integrations/workflow_integrations/streaming_workflow_integration.py, server/server/modules/text_processing/providers/langchain_gemini_provider.py, server/server/config/unified_config.py, server/server/config/prompts.py
- Документы: Docs/ARCHITECTURE_OVERVIEW.md, Docs/PROJECT_REQUIREMENTS.md
- Ограничения: решения об action принимает LLM; без ввода второго источника истины.

## Решения/выводы
- Латентность почти полностью в LLM; TTS и gRPC не являются основными узкими местами.
- Быстрый эффект дают конфиг-изменения (модель/tools) и отключение скриншота там, где он не нужен.

## Открытые вопросы
- Какие интенты обязаны всегда получать screenshot?
- Можно ли использовать другой (быстрее) LLM без нарушения продуктовых требований?

## Следующие шаги
- Согласовать критерии «когда нужен screenshot» и применить фильтр в StreamingWorkflowIntegration.
- Прогнать A/B с отключенным google_search tool и быстрым flash-моделем.
