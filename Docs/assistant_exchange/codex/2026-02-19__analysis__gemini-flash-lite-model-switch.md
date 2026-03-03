# Переключение text+memory на gemini-flash-lite-latest

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-19
- ID (INS-###): INS-N/A

## Diagnosis
Основная модель текста и модель анализа памяти были рассинхронизированы по дефолтам, а в MemoryAnalyzer была локальная захардкоженная модель (второй owner-path).

## Root Cause
Нарушение single-owner конфигурации → MemoryAnalyzer игнорировал centralized `memory_analysis_model` → смена модели через env работала не полностью/нестабильно.

## Optimal Fix
Цель: централизовать выбор модели для text+memory через unified_config/env и оставить быстрый ручной rollback.

Architecture Fit: через текущий центр конфигурации (`config.env` + `server/config/unified_config.py`).

Source of Truth: `LANGCHAIN_MODEL` и `MEMORY_ANALYSIS_MODEL`.

План внедрения:
1. Переключить `LANGCHAIN_MODEL` и `MEMORY_ANALYSIS_MODEL` на `gemini-flash-lite-latest`.
2. Оставить `gemini-3-flash-preview` как резервное значение для ручного переключения (commented env строка, без нового runtime-path).
3. Синхронизировать дефолты в `unified_config.py/.yaml`, provider/config fallback-строки.
4. Убрать hardcode memory модели: передавать `memory_analysis_model` и `memory_analysis_temperature` из `MemoryConfig` в `MemoryAnalyzer`.

## Verification
- `rg` по измененным файлам подтверждает единые значения `gemini-flash-lite-latest`.
- `python3 -m py_compile` для измененных python-файлов проходит без ошибок.

## Информация об изменениях
- Что изменено:
  - основная модель и модель памяти переведены на `gemini-flash-lite-latest`;
  - `gemini-3-flash-preview` сохранена как резервная для ручного отката;
  - удален дублирующий hardcode модели в `MemoryAnalyzer`.
- Файлы:
  - `config.env`
  - `server/config.env.example`
  - `server/config/unified_config.py`
  - `server/config/unified_config.yaml`
  - `server/modules/text_processing/config.py`
  - `server/modules/text_processing/providers/langchain_gemini_provider.py`
  - `server/modules/memory_management/providers/memory_analyzer.py`
  - `server/modules/memory_management/core/memory_manager.py`
- Причина/цель: единый owner для model selection, без второго пути принятия решений.
- Проверка: `rg`, `py_compile`.

## Запрос/цель
Перевести память и основную модель на `gemini-flash-lite-latest`, не удаляя `gemini-3-flash-preview` и сохранив возможность быстрого переключения.

## Контекст
- Файлы: конфиг и runtime модули text/memory.
- Документы: `AGENTS.md`, `../Docs/ARCHITECTURE_OVERVIEW.md`, `server/Docs/ARCHITECTURE_OVERVIEW.md`, `../Docs/assistant_exchange/TEMPLATE.md`.
- Ограничения: без реархитектуры, без добавления второго runtime-owner path.

## Решения/выводы
- Owner оси model-selection сохранен централизованным.
- Дубликат устранен: hardcode в MemoryAnalyzer объединен с unified config path.

## Открытые вопросы
- Нет.

## Следующие шаги
- Перезапустить server runtime и проверить startup-лог с новыми model_name.
