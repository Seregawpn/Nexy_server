# Production Release Step-by-Step Manual And Rules

## Метаданные
- Ассистент: codex
- Тип: task-brief
- Дата: 2026-02-17
- ID (INS-###): N/A

## Diagnosis
В запросе требовался явный пошаговый release manual и закрепление этого процесса в правилах проекта.

## Root Cause
Релизный процесс был понятен технически, но не был формально зафиксирован как обязательный step-by-step в active rules.

## Optimal Fix
Добавлен канонический раздел в client release guide:
- `9. Пошаговый Production Release (обязательно)` в
  `client/Docs/RELEASE_VERSIONING_AND_PUBLISHING.md`

В правилах зафиксирован mandatory gate:
- `AGENTS.md`: новый раздел `10) Release Manual Gate (обязательно)`
- `client/AGENTS.md`: ссылка на обязательный runbook и правило про production assets через owner-flow.

## Verification
- Проверены маркеры новых секций через `rg`.
- Правила и manual синхронизированы по единому owner-flow.

## Информация об изменениях
- Что изменено:
  - Добавлен step-by-step production release manual.
  - Обновлены root/client rules для обязательного следования manual.
- Файлы:
  - `AGENTS.md`
  - `client/AGENTS.md`
  - `client/Docs/RELEASE_VERSIONING_AND_PUBLISHING.md`
- Причина/цель:
  - Сделать release-процесс однозначным и обязательным по правилам.
- Проверка:
  - grep-проверка наличия новых секций и owner-формулировок.

## Запрос/цель
Сделать пошаговый manual и отредактировать правила проекта.

## Контекст
- Packaging owner: `client/packaging/build_final.sh`.
- Production artifacts owner: `Seregawpn/Nexy_production`.

## Решения/выводы
- В active rules теперь закреплен единый обязательный release manual.

## Открытые вопросы
- Нет.

## Следующие шаги
- Выполнять релизы только по разделу 9 в `client/Docs/RELEASE_VERSIONING_AND_PUBLISHING.md`.
