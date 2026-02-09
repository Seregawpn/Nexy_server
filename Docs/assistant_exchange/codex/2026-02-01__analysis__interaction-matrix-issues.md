# Interaction Matrix Issues

## Метаданные
- Ассистент: codex
- Тип: analysis
- Дата: 2026-02-01
- ID (INS-###): N/A (CRM_INSTRUCTION_REGISTRY.md not found)

## Diagnosis
В interaction_matrix.yaml есть правила, которые никогда не срабатывают или дублируются из‑за несоответствия predicate-имен и отсутствующих осей в Snapshot.

## Root Cause
Несинхронизированы источники истины: interaction_matrix.yaml содержит новые оси/правила, но predicates/ Snapshot/ selectors не обновлены → правила не матчятся → дефолтные решения маскируют ошибки.

## Optimal Fix
Синхронизировать имена predicate и набор осей между interaction_matrix.yaml, Snapshot и predicates; убрать дублирующие/ошибочные правила или добавить недостающие предикаты, если оси действительно поддерживаются.

## Verification
DoD: правила без неизвестных predicate; нет дублей по одному gateway; поведение совпадает с описанием.

## Запрос/цель
Проверить interaction_matrix.yaml на дубли/конфликты/гонки и зафиксировать проблемы.

## Контекст
- Файлы: client/config/interaction_matrix.yaml, client/integration/core/gateways/predicates.py, client/integration/core/selectors.py
- Документы: Docs/PROJECT_REQUIREMENTS.md, Docs/ARCHITECTURE_OVERVIEW.md

## Решения/выводы
- Обнаружены «мертвые» правила (unknown predicate) и дубликат в decide_permission_restart_safety.
- Обнаружена смысловая коллизия: правило про update launch привязано к неверному gateway/decision.

## Открытые вопросы
- Являются ли оси full_disk_access/subscription/browser реальными и где их Source of Truth?

## Следующие шаги
- Согласовать, какие оси реально поддерживаются, затем синхронизировать predicates/Snapshot/interaction_matrix.
