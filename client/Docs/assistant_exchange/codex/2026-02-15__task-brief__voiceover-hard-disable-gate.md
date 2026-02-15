# VoiceOver hard-disable gate in IntegrationFactory

## Context
Пользователь попросил убрать влияние VoiceOver-функционала Nexy и исключить конфликты при запуске/работе вместе с системным VoiceOver.

## Problem
`accessibility.voiceover_control.enabled=false` был в конфиге, но `VoiceOverDuckingIntegration` все равно создавался в `IntegrationFactory`.
Это создавало лишний runtime path и риск побочных взаимодействий.

## Change
Файл: `integration/core/integration_factory.py`

- Добавлен жесткий feature-gate по `voiceover_control.enabled`.
- При `enabled=true`: интеграция регистрируется как раньше.
- При `enabled=false`: интеграция не создается, пишется явный лог disabled.

## Architecture fit
- Owner создания интеграций: `IntegrationFactory` (централизованный source of truth).
- Новые дубли/локальные флаги не добавлялись.

## Verification
- `PYTHONPATH=. .venv/bin/python -m unittest discover -s tests -p 'test_quartz_monitor_chord_logic.py'` -> OK
- `PYTHONPATH=. .venv/bin/python -m unittest discover -s tests -p 'test_coordinator_critical_subscriptions.py'` -> failed (missing `pytest` in current venv)

## Expected runtime impact
- VoiceOver-specific Nexy path полностью выключается при `enabled=false`.
- Уменьшен риск конфликтов в VoiceOver-ветке без влияния на owner hotkey path (`quartz_monitor`).
