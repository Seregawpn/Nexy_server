# Single-owner для Gemini модели и удаление env example

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-19
- ID (INS-###): INS-N/A

## Diagnosis
Модель задавалась дублирующими переменными (`LANGCHAIN_MODEL`, `MEMORY_ANALYSIS_MODEL`) и частично fallback-строками в коде, что создавало конфликт owner-path.

## Root Cause
Несколько конфигурационных осей для одной сущности (модель LLM) → разные модули могли читать разные ключи → риск рассинхронизации text vs memory.

## Optimal Fix
- Введен единый owner: `GEMINI_PRIMARY_MODEL`.
- Text и Memory читают модель только через этот ключ в `unified_config.py`.
- В `config.env` удалены дубли (`LANGCHAIN_MODEL`, `MEMORY_ANALYSIS_MODEL`).
- Резерв сохранен как отдельный факт: `GEMINI_BACKUP_MODEL=gemini-3-flash-preview` (без второго runtime-path).
- Удален файл примера: `server/config.env.example`.

## Verification
- `rg` подтверждает единую ось `GEMINI_PRIMARY_MODEL` в runtime-конфиге.
- `python3 -m py_compile` для измененных Python-файлов — успешно.
- `test ! -f server/config.env.example` — файл удален.

## Информация об изменениях
- Что изменено:
  - centralization: single owner для model selection;
  - cleanup: удален env example;
  - устранено дублирование ключей модели.
- Файлы:
  - `config.env`
  - `server/config/unified_config.py`
  - `server/modules/text_processing/config.py`
  - `server/modules/text_processing/providers/langchain_gemini_provider.py`
  - `server/modules/memory_management/providers/memory_analyzer.py`
  - `server/config.env.example` (deleted)
- Причина/цель: один источник истины + отсутствие конфликтующих override-path.
- Проверка: `rg`, `py_compile`, file-exists check.

## Запрос/цель
Убрать дублирование/конфликты, оставить изменение модели в одном месте, удалить пример конфигурации.

## Контекст
- Каноны: `AGENTS.md`, `../Docs/ARCHITECTURE_OVERVIEW.md`, `server/Docs/ARCHITECTURE_OVERVIEW.md`.
- Ограничения: без реархитектуры, без второго пути принятия решения.

## Решения/выводы
- Source of Truth для модели: `GEMINI_PRIMARY_MODEL`.
- `gemini-3-flash-preview` сохранена как резервная запись для ручного переключения.

## Открытые вопросы
- Нет.

## Следующие шаги
- Перезапуск сервера и проверка startup логов модели text/memory.
