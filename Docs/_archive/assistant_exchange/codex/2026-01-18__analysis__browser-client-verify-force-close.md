# Browser Client Verify (Force Close)

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-18
- ID (INS-###): INS-005

## Diagnosis
Повторная верификация завершилась успешно при включенном `VERIFY_FORCE_CLOSE=1` и явном выходе из скрипта.

## Root Cause
Без принудительного выхода verify зависал из-за фоновых задач browser_use при `keep_browser_open=true`.

## Optimal Fix
Оставить прод‑поведение без закрытия браузера, но завершать verify через флаг `VERIFY_FORCE_CLOSE` с `os._exit(0)`.

## Verification
Запуск `.venv/bin/python -X faulthandler client/scripts/verify_browser_client.py` с `GEMINI_API_KEY` и `VERIFY_FORCE_CLOSE=1` завершился успешно.

## Запрос/цель
Повторить verify после правок и убедиться, что скрипт завершает работу.

## Контекст
- Файлы: client/scripts/verify_browser_client.py, client/modules/browser_use/module.py
- Документы: Docs/ARCHITECTURE_OVERVIEW.md

## Решения/выводы
- Verify проходит и завершает процесс.

## Открытые вопросы
- Нужен ли отдельный verify‑режим без LLM (offline)?

## Следующие шаги
- При необходимости убрать os._exit после подтверждения поведения в CI.
