# Gemini API key fallback runtime switch

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-22
- ID (INS-###): N/A

## Diagnosis
В сервере отсутствовал runtime fallback для Gemini API ключей: использовался только `GEMINI_API_KEY`, поэтому при `API_KEY_INVALID` автопереключения не было.

## Root Cause
Конфигурация (`TextProcessingConfig.from_env`) читала только один ключ, а `LangChainGeminiProvider` не имел key-switch логики → fallback manager работал для обработки/деградации, но не для ротации ключа.

## Optimal Fix
- Добавлен `GEMINI_FALLBACK_API_KEY` в конфигурацию text processing.
- Добавлен единый key-switch owner в `LangChainGeminiProvider`:
  - список ключей `[primary, fallback]`;
  - `asyncio.Lock` для anti-race при переключении;
  - switch при key-related ошибках (`API_KEY_INVALID`, `API key expired`, `PERMISSION_DENIED`);
  - однократный retry запроса на fallback ключе.
- В `config.env` fallback ключ переведен из комментария в runtime переменную.

## Verification
- `python -m py_compile` для измененных файлов — успешно.
- Проверка wiring с env:
  - `text_key_set=True`
  - `fallback_key_set=True`
  - `provider_has_fallback=True`

## Информация об изменениях
- Что изменено:
  - Расширен runtime-конфиг вторым ключом.
  - Добавлен безопасный механизм автопереключения ключа в провайдере.
  - Добавлены статус-поля по количеству/индексу активного ключа (без утечки секретов).
- Файлы:
  - `config.env`
  - `server/config/unified_config.py`
  - `server/modules/text_processing/config.py`
  - `server/modules/text_processing/providers/langchain_gemini_provider.py`
- Причина/цель:
  - Автоматически переживать сбой primary API key без ручной ротации и без второго owner-path.
- Проверка:
  - Компиляция + runtime wiring check через env.

## Запрос/цель
Настроить fallback Gemini API key на случай сбоя основного ключа.

## Контекст
- Файлы: `server/modules/text_processing/*`, `server/config/unified_config.py`, `config.env`
- Документы: `AGENTS.md`, `server/Docs/ARCHITECTURE_OVERVIEW.md`, `../Docs/CODEX_PROMPT.md`, `../Docs/assistant_exchange/TEMPLATE.md`
- Ограничения: без реархитектуры, один owner-path принятия решения.

## Решения/выводы
- Source of Truth по key-switch оставлен в `LangChainGeminiProvider`.
- Дубликаты и второй путь в workflow/coordinator не добавлялись.
- Anti-race закрыт lock'ом внутри провайдера.

## Открытые вопросы
- Нужен ли аналогичный key-fallback для `memory_management` (сейчас там все еще один ключ).

## Следующие шаги
- Добавить интеграционный тест: невалидный primary + валидный fallback => успешный ответ после одного switch.
