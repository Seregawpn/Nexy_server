# Task Brief — Hotkey sequenced implementation plan

## Context
Пользователь запросил подробный поэтапный план внедрения с акцентом на:
- удаление дублей;
- предотвращение гонок;
- централизацию ownership;
- корректные точки взаимодействия;
- обязательное тестирование.

## Deliverable
Создан документ:
- `Docs/HOTKEY_IMPLEMENTATION_PLAN.md`

## Что включает план
- Архитектурный контракт и Source of Truth.
- Жёсткие anti-duplication/anti-race инварианты.
- Этапы 0..6 с exit criteria по каждому этапу.
- Матрицу тестирования и обязательные лог-проверки.
- Правила внедрения (изменения только в owner-слое текущего этапа).

## Architecture fit
- План не добавляет новые owner-слои.
- Централизация сохранена: suppression owner + lifecycle owner + mode owner.
