# Embedded Gemini API Key Fallback (Experiment)

## Task
По запросу пользователя добавить возможность вшитого API-ключа в код для browser-use, чтобы запуск не зависел от env/credentials.

## Architecture Fit
- Owner сохранен: `BrowserUseModule._create_llm`.
- Второй owner-path не добавлялся: mode/session/event flow не изменен.

## Implementation
- Добавлены константы-кандидаты:
  - `EMBEDDED_GEMINI_API_KEY`
  - `EMBEDDED_GEMINI_API_KEY_FALLBACK`
- В `_create_llm` добавлен fallback на эти константы только если ключ не найден в:
  1. environment
  2. secure credentials
  3. config

## Risks
- Security risk высокий: ключ в коде может утечь через git/build artifacts.
- Оставлено как временный эксперимент.

## Verification
- Выполнено: `python3 -m py_compile modules/browser_automation/module.py` (ok)

## Информация об изменениях
- что изменено:
  - Добавлен code-fallback для Gemini API key в `BrowserUseModule`.
  - Добавлено предупреждение в лог при использовании встроенного ключа.
- список файлов:
  - `modules/browser_automation/module.py`
  - `Docs/assistant_exchange/codex/2026-02-21__task-brief__embedded-gemini-api-key-fallback.md`
- причина/цель изменений:
  - Временный эксперимент для принудительного включения browser-use API без внешнего credentials-файла.
- проверка (что выполнено для валидации):
  - Синтаксическая проверка Python-модуля через `py_compile`.
