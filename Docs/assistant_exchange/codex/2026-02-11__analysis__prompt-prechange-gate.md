# Prompt Pre-Change Gate

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-11
- ID (INS-###): N/A

## Diagnosis
Правила требовали архитектурного соответствия, но не содержали жесткого "gate" перед изменениями и не включали обязательную проверку feature flags.

## Root Cause
Неполный pre-change процесс в промптах -> ассистент мог начать правки до сверки документации/флагов -> появлялись дубли, конфликты и локальные обходы центра управления.

## Optimal Fix
Добавлен обязательный `Pre-Change Gate` в `AGENTS.md` и `Docs/CODEX_PROMPT.md`, плюс `Docs/FEATURE_FLAGS.md` включен в обязательные источники.

## Verification
Проверить наличие секции `1.1) Pre-Change Gate` и `Docs/FEATURE_FLAGS.md` в списках обязательных источников в обоих файлах.

## Запрос/цель
Усилить промпт, чтобы перед любыми изменениями выполнялась проверка архитектуры, документации и флагов.

## Контекст
- Файлы: `AGENTS.md`, `Docs/CODEX_PROMPT.md`
- Документы: `Docs/PROJECT_REQUIREMENTS.md`, `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/FEATURE_FLAGS.md`
- Ограничения: без реархитектуры

## Решения/выводы
- Созданы рабочие версии документов из `_archive` в `Docs/`: `CODEX_PROMPT.md`, `ANTIGRAVITY_PROMPT.md`, `ASSISTANT_COORDINATION_PROTOCOL.md`, `assistant_exchange/TEMPLATE.md`.
- Усилен процесс предотвращения дублирования и децентрализации перед code changes.

## Открытые вопросы
- Нужно ли аналогично усилить `Docs/ANTIGRAVITY_PROMPT.md` тем же `Pre-Change Gate`.

## Следующие шаги
- При следующем запросе выполнять Gate как обязательный шаг до любых правок.
