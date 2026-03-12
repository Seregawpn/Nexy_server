# Experimental Prompt Profiles

Этот каталог содержит изолированные prompt profiles для безопасных экспериментов.

Правила:

- `current` production prompt stack остаётся в `server/server/config/prompts.py`
- experimental profiles подключаются только через selector
- default profile: `current`
- активный profile задаётся env-переменной `NEXY_PROMPT_PROFILE`

Доступные profiles:

- `experimental_v2`

Назначение:

- тестировать новую prompt-логику по категориям без изменения production prompt stack
- сравнивать `current` vs `experimental_v2` через dataset/campaign loop

Role-based base inside `experimental_v2`:

- `classifier/`
- `generator/`
- `memory/`
- `orchestrator/`

Это не отдельные runtime owners, а изолированная prompt-база для role-specific hardening.
