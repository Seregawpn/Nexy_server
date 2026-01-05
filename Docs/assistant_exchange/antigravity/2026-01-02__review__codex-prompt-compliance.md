# Review: CODEX_PROMPT.md на соответствие формату ответа и обязательным источникам

1) Diagnosis

Формат ответа и обязательные источники в `Docs/CODEX_PROMPT.md` в целом соответствуют правилам, но отчет ранее содержал неверный факт о отсутствии `Docs/ANTIGRAVITY_PROMPT.md`.

2) Root Cause

Неполная сверка источников → ошибочный вывод о несоответствии → риск ложных замечаний в review.

3) Optimal Fix (PRIMARY)

Goal: дать корректное заключение по соответствию и убрать ложные несоответствия

Architecture Fit:

Where it belongs: review-документ для проверки формата

Source of Truth: `AGENTS.md`, `Docs/CODEX_PROMPT.md`

Breaks architecture: no

Implementation Plan:

1. Проверить раздел "Обязательные источники" в `Docs/CODEX_PROMPT.md`.
2. Подтвердить наличие `Docs/ANTIGRAVITY_PROMPT.md` и других обязательных ссылок.
3. Зафиксировать только реальные расхождения, если они есть.

Code Touchpoints:

Docs/CODEX_PROMPT.md

Concurrency Guard (if needed):

n/a

What to remove / merge:

n/a

4) Alternative (ONLY if needed)

Если review не нужен, можно ссылаться только на `AGENTS.md` как источник правил.

5) Conflict & Risk Check (обязательный)
Duplication risk: low
Race risk: low
New state introduced: no
Centralized: yes
Breaks architecture: no

6) Verification (DoD)

Steps:

1. Сверить список источников в `Docs/CODEX_PROMPT.md` с `AGENTS.md`.
2. Проверить, что формат ответа в `Docs/CODEX_PROMPT.md` соответствует разделу 2 `AGENTS.md`.

Expected behavior/logs:

- В review указаны только фактические расхождения.

Regression checks:

- Убедиться, что `Docs/CODEX_PROMPT.md` содержит ссылки: `Docs/PROJECT_REQUIREMENTS.md`, `Docs/ARCHITECTURE_OVERVIEW.md`, `Docs/ASSISTANT_COORDINATION_PROTOCOL.md`, `Docs/ANTIGRAVITY_PROMPT.md`, `Docs/CODEX_PROMPT.md`, `Docs/assistant_exchange/TEMPLATE.md`.

Criteria: “стало проще/стабильнее” (конкретно)

- Review не содержит ложных замечаний и соответствует формату.
