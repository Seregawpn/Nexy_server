# Documentation Audit

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-03
- ID (INS-###): INS-005

## Diagnosis
В основной документации есть рассинхрон с фактическими путями, конфигами и статусами подписок; ссылки на ряд документов ведут в отсутствующие файлы.

## Root Cause
Документы частично перенесены в `Docs/_archive` без обновления ссылок и путей → ссылки и конфиг‑пути в описании фич устарели → риск неверной настройки и неверных ожиданий.

## Optimal Fix
Сделать единый проход обновления ссылок и описаний фич‑флагов/статусов подписок, опираясь на текущие конфиги и source‑of‑truth модули.

## Verification
Проверить, что все ссылки из ключевых docs разрешаются, а пути конфигов и статусов совпадают с кодом.

## Запрос/цель
Аудит документации на актуальность и выявление необходимых правок.

## Контекст
- Файлы: `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/FEATURE_FLAGS.md`, `Docs/SYSTEM_CONCEPT.md`, `Docs/PAYMENT_FLOW_EXPLAINED.md`, `server/server/modules/subscription/*`, `server/server/config.env`, `client/config/unified_config.yaml`
- Документы: `Docs/_archive/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/_archive/CODEX_PROMPT.md`, `Docs/_archive/ANTIGRAVITY_PROMPT.md`, `Docs/_archive/assistant_exchange/TEMPLATE.md`
- Ограничения: без изменения API контрактов.

## Решения/выводы
- Обязательные docs из `Docs/Antigravity/*` и `Docs/Codex/*` отсутствуют в активной директории и доступны только в `_archive`.
- В `Docs/FEATURE_FLAGS.md` пути клиентских флагов не совпадают с `client/config/unified_config.yaml`.
- В `Docs/PAYMENT_FLOW_EXPLAINED.md` статусы и логика расходятся с текущими `subscription_types.py` и `state_machine.py`.
- В `Docs/ARCHITECTURE_OVERVIEW.md` и ряде docs ссылки на ключевые файлы невалидны.

## Открытые вопросы
- Нужно ли восстанавливать архивные документы в `Docs/` или обновлять ссылки на `_archive`?

## Следующие шаги
- Согласовать, какие документы считаются каноничными (active vs archive) и обновить ссылки/описания.
