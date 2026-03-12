# Assistant Runtime V2 Level-Gated Development Plan

Цель документа: зафиксировать один активный план развития без дублей между категориями, уровнями, fronts и owner-paths.

## Source of Truth

- active quality gate: `server/server/tests/category_level_dataset_registry.py`
- live run: `server/server/scripts/run_live_category_level_campaign.py`
- observed evaluation: `server/server/scripts/run_category_level_campaign.py`
- route owner: `server/server/modules/text_processing/core/text_processor.py`
- prompt owner: `server/server/config/prompts.py`
- lifecycle owner: `server/server/modules/memory_management/core/memory_manager.py`

## Working Mode

1. Активен только один уровень за раз.
2. Активный уровень гоняется по всем категориям одновременно.
3. После прогона выбирается только один top failure class.
4. Один change-set меняет только один owner-layer.
5. Следующий уровень открывается только после green текущего уровня.

## Active Gate Now

- active level: `Level 1`
- active campaign: `level1_30`
- current status: `29/30`
- remaining defect:
  - case: `google_search_l1_03`
  - conflict: route is correct (`google_search`), but runtime keeps pending lifecycle:
    - observed `behavior=clarify`
    - observed `goal_state=keep`
    - expected `behavior=answer`
    - expected `goal_state=empty`
- active semantic/lifecycle focus:
  - keep `context > keyword` as the semantic rule
  - do not add category-specific lifecycle hacks
  - close the remaining `Level 1` defect only through the active semantic/lifecycle owners

## Level Order

1. `Level 1` — direct complete requests
2. `Level 2` — missing required detail / clarify
3. `Level 3` — continuation / follow-up / keep
4. `Level 4` — noisy / typo / fragment recovery
5. `Level 5` — ambiguity / replace / cancel / competing intent

## Category Coverage Per Level

На каждом уровне одновременно проверяются все категории:

- `none`
- `capability`
- `describe`
- `messages`
- `whatsapp`
- `system_control`
- `browser`
- `google_search`
- `payment`

## Owner Rules

### 1. Semantic owner

- `route` и semantic boundary меняются только в:
  - `server/server/modules/text_processing/core/text_processor.py`
  - `server/server/config/prompts.py`

Нельзя:
- дублировать route decision в bridge/tests/fronts
- вводить category-specific keyword hacks как primary mechanism

### 2. Lifecycle owner

- `goal_state/current_goal` меняются только в:
  - `server/server/modules/memory_management/core/memory_manager.py`

Нельзя:
- писать final lifecycle rules в prompts
- писать lifecycle overrides в bridge/tests

### 3. Prompt/front owner rules

- production/runtime prompt owner:
  - `server/server/config/prompts.py`
- runtime sandbox prompt owner:
  - top-level overlays under `server/server/experimental/assistant_runtime_v2/prompts/experimental_v2/*.md`
- role-based prompt fronts:
  - `experimental_v2/classifier|generator|memory|orchestrator/*`
  - spec only, not runtime owners

Нельзя:
- подключать role-based fronts в runtime до появления одного centralized resolver
- одновременно использовать несколько active prompt paths

## Semantic Priority Policy

Для любого уровня и любой категории:

1. explicit cancel/replace
2. explicit current intent
3. continuation of same unfinished task
4. old context
5. keywords only as fallback

Правило:
- смысл текущей реплики важнее ключевых слов и старого контекста

## Lifecycle Priority Policy

Для любого уровня и любой категории:

1. `replaces_old_task` -> `replace/new set`
2. `task_completed` -> `empty`
3. `waiting_for_user` -> `set`
4. `continues_same_task` -> `keep`
5. fallback -> `empty`

Правило:
- категория сама по себе не определяет `goal_state`
- `goal_state` зависит только от состояния задачи

## Change Process

Для каждого активного уровня:

1. Прогнать live campaign
2. Прогнать observed evaluation
3. Получить:
   - `ok_cases`
   - `failed_cases`
   - `failure_type`
   - `owner`
4. Выбрать top-1 failure class
5. Изменить только один owner-layer
6. Перепрогнать тот же уровень
7. Повторять до green

## Current Plan

### Step 1. Close `Level 1`

- не открывать `L2-L5`
- закрыть remaining `google_search_l1_03`
- сохранить единый semantic contract:
  - `context > keyword`
  - lexical hints are fallback only
- привести remaining defect к одному owner-driven решению:
  - semantic owner decides `answer vs clarify`
  - lifecycle owner decides `empty vs set/keep`

### Step 2. Open `Level 2`

После `Level 1 = 30/30`:

- active gate -> `Level 2`
- focus:
  - missing detail
  - clarify correctness
  - correct `set`

### Step 3. Open `Level 3`

- continuation
- follow-up
- correct `keep`
- pivot vs continuation boundary

### Step 4. Open `Level 4`

- noisy input
- typo recovery
- fragment recovery
- context-over-keyword validation

### Step 5. Open `Level 5`

- ambiguity
- replace/cancel
- competing intents
- no wrong action

## Parallel Non-Active Track

- latency track remains secondary
- no latency fix is active unless it blocks the active level gate
- current latency work stays observational until correctness gates are green

## Forbidden While Executing This Plan

- parallel active fixes across multiple levels
- runtime wiring of role-based prompt fronts
- new lifecycle owners outside `MemoryManager`
- new semantic owners outside `TextProcessor/prompts.py`
- category-specific hacks as a substitute for universal semantic/lifecycle rules

## Definition of Progress

Прогресс считается реальным только если:

- текущий активный уровень даёт меньше `failed_cases`, чем до change-set
- owner failure concentration уменьшается
- не появляется новый duplicate owner-path
- green текущего уровня подтверждён повторным live run
