# WhatsApp Gateway Compliance Review

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-01-29
- ID (INS-###): INS-UNKNOWN

## Diagnosis
WhatsApp интеграция добавлена, но решение обходится без DecisionEngine и канонического decision‑логирования; правило `decision: notify_user` в interaction_matrix не совместимо с текущим enum Decision.

## Root Cause
Новый gateway использует отдельный enum и ручную логику вместо стандартного DecisionEngine → несоответствие interaction_matrix и базовых типов → риск расхождений и отсутствия канонических логов.

## Optimal Fix
Выровнять WhatsApp gateway под DecisionEngine: расширить Decision enum (notify_user), использовать get_engine("decide_whatsapp_action"), логировать через log_decision (duration_ms), удалить GenericDecision.

## Verification
DoD: decision‑логи с duration_ms, interaction_matrix правила исполняются через engine, тесты gateway покрывают qr_required.

## Запрос/цель
Проверить заявленные архитектурные изменения WhatsApp и выявить несоответствия.

## Контекст
- Файлы: client/integration/core/gateways/whatsapp_gateways.py, client/integration/core/gateways/decision_engine.py, client/integration/core/gateways/types.py, client/config/interaction_matrix.yaml
- Документы: AGENTS.md, Docs/PROJECT_REQUIREMENTS.md, Docs/ARCHITECTURE_OVERVIEW.md
- Ограничения: без новой архитектуры, единый источник истины

## Решения/выводы
- Правило notify_user несовместимо с Decision enum и не исполняется через DecisionEngine.
- Логи WhatsApp gateway не соответствуют каноническому формату (нет duration_ms, логируется не всегда).

## Открытые вопросы
- Нужно ли официально расширять Decision enum под notify_user или заменить decision на существующий (degrade/abort)?

## Следующие шаги
- Согласовать решение по decision type и привести gateway к DecisionEngine + log_decision.
