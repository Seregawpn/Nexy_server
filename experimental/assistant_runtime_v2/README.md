# Assistant Runtime V2

Изолированный experimental runtime для новой архитектуры ассистента.

Правила:

- routing в `v2` включается только через единый server feature flag;
- current runtime остаётся default owner-path;
- `v2` не создаёт второй owner для long-term memory или action execution;
- `v2` не делает локальный intent parsing/keyword routing;
- на текущем этапе `v2` владеет только thin lifecycle hook вокруг current streaming path.

Папка подготовлена для поэтапного переноса:

- `active_context.py` — runtime owner текущей незавершённой задачи;
- `task_lifecycle.py` — passive lifecycle observer поверх canonical stream outputs;
- `LEVEL_GATED_DEVELOPMENT_PLAN.md` — активный level-gated roadmap; единственный рабочий план продвижения по уровням;
- `CATEGORY_MATRIX.md` — category-based baseline contract для развития chat / describe / action flows;
- `server/server/tests/category_level_dataset_registry.py` — canonical quality dataset registry по категориям и уровням `1..5`;
- `server/server/scripts/run_category_level_campaign.py` — единый summary runner для полного quality campaign и срезов по category/level;
- `PROMPT_CATALOG.md` — category-to-prompt owner map поверх current prompt stack;
- `prompts/` — isolated experimental prompt profiles, selectable without touching production prompt stack;
- `runtime.py` — единая точка входа `v2`;
- далее сюда добавляются lifecycle/orchestration слои поверх existing classifier/generator/memory owners.
