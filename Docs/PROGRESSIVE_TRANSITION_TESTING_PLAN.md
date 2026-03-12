# Progressive Transition Testing Plan

Цель документа: зафиксировать пошаговый способ улучшения ассистента через transition-family coverage и difficulty levels без создания второго owner-path.

Связанные каноны:
- Gate процесса: `server/server/Docs/GOAL_STACK_TEST_GATE.md`
- Архитектура владельцев: `server/server/Docs/ARCHITECTURE_OVERVIEW.md`
- Flow контракт: `server/server/Docs/FLOW_INTERACTION_SPEC.md`

## 1. Scope

Этот документ не меняет runtime owners.

Он задает:
- как группировать risky запросы;
- в каком порядке их добавлять;
- как вести циклы `20/20`;
- когда править `prompts.py`, а когда `memory_management/config.py`.

## 2. Source of Truth

### 2.1 Coverage owner
- `server/server/tests/goal_stack_gate_registry.py`

### 2.2 Execution / continuity owner
- `server/server/config/prompts.py`

### 2.3 Lifecycle / post-state owner
- `server/server/modules/memory_management/config.py`

### 2.4 Deterministic projection
- `server/server/tests/test_memory_full_cycle_factual_e2e.py`

### 2.5 Live verification
- `server/server/scripts/run_live_goal_stack_matrix.py`

## 3. Core rule

Новые проблемы группируются не по категориям (`browser`, `messages`, `search`), а по типу перехода:

- `new_task`
- `clarification_needed`
- `slot_fill_after_clarification`
- `continuation`
- `replacement_with_correction`
- `cancel`
- `cancel_plus_pivot`
- `noisy_retarget_inside_active_task`
- `long_horizon_reference`
- `entity_role_disambiguation`

Категория используется только как вторая ось coverage.

## 4. Difficulty model

Каждый кейс должен иметь difficulty level.

### L1_basic_direct
- чистый прямой запрос
- один intent
- нет активного контекста

Примеры:
- `Open Safari`
- `Send a message to Sophia`
- `Find latest world news`

### L2_clarification_slot_fill
- assistant запросил один missing slot
- пользователь дал короткий прямой ответ

Примеры:
- `Open an app` -> `Safari`
- `Find news` -> `world politics`
- `Send a message to Sophia` -> `I am downstairs`

### L3_short_continuation
- есть active goal
- follow-up короткий и неполный
- intent сохраняется

Примеры:
- `Tell her I'll be late`
- `world headlines`
- `sleep music instead`

### L4_replacement_or_cancel
- старый task отменяется или заменяется
- в turn есть один correction signal

Примеры:
- `Actually open Telegram instead`
- `No, send a message to Sophia instead`
- `Forget that`

### L5_multi_signal_noisy
- шумный или сильно сжатый turn
- в одном turn несколько semantic signals

Примеры:
- `nah not safari actually telegram`
- `txt her im downstairs`
- `nah yt thunder ambi insted`

## 5. Required metadata for each case

Минимальный набор полей для registry case:

- `transition_family`
- `difficulty_level`
- `noise_profile`
- `context_depth`
- `signal_count`

### 5.1 Required expected outputs for each case

Для каждого кейса должны быть явно описаны 4 ожидаемых ответа системы:

- `memory_expected`
  - ожидаемый `goal_state`
  - ожидаемый `current_goal`

- `classifier_expected`
  - ожидаемый `category`
  - ожидаемый `route`

- `generator_expected`
  - ожидаемый `text`
  - ожидаемый `command`
  - ожидаемые `args`

- `full_cycle_expected`
  - итоговый execution outcome
  - итоговый post-state outcome

Это правило обязательное:
- не проверять только “общий ответ системы”;
- всегда локализовать expectation по owner-слою.

### 5.2 Case contract template

Для каждого нового campaign case использовать такой шаблон:

- `request`
- `transition_family`
- `difficulty_level`
- `category`
- `noise_profile`
- `context_depth`
- `signal_count`
- `memory_expected`
- `classifier_expected`
- `generator_expected`
- `full_cycle_expected`

Рекомендуемые значения:

### noise_profile
- `clean`
- `short`
- `pronoun`
- `noisy`
- `multi_signal`

### context_depth
- `0`
- `1`
- `2_plus`

## 6. Work order

Работа ведётся только по одной transition family за раз и только по одному уровню сложности за раз.

Строгий порядок уровней обязателен:

1. `L1_basic_direct`
2. `L2_clarification_slot_fill`
3. `L3_short_continuation`
4. `L4_replacement_or_cancel`
5. `L5_multi_signal_noisy`

Запрещено:
- переходить к следующему уровню, пока текущий не закрыт на `20/20`;
- смешивать в одном campaign кейсы из нескольких difficulty levels.

Только после закрытия уровня по одной family можно открывать следующий уровень для этой же family.

### 6.1 Family order

При фиксированном уровне сложности families проходятся в таком порядке:

1. `slot_fill_after_clarification`
2. `replacement_with_correction`
3. `cancel_plus_pivot`
4. `noisy_retarget_inside_active_task`
5. `long_horizon_reference`
6. `entity_role_disambiguation`

## 7. First campaign

Первая campaign family:
- `slot_fill_after_clarification`

Первый campaign level:
- `L1_basic_direct`

Почему первой:
- это базовый человеческий паттерн;
- он одинаково важен для `system_control`, `google_search`, `messages`, `whatsapp`, `browser`;
- если этот слой слабый, дальше будут сыпаться replacement/noisy cases.

Почему начинаем именно с `L1`:
- он проверяет базовую route integrity без шума и без сложного carry-over;
- если `L1` неустойчив, результаты `L2-L5` будут шумными и непригодными для локализации причин.

### Recommended first 20 for `L1_basic_direct`

- `4` кейса `system_control`
- `4` кейса `messages`
- `3` кейса `whatsapp`
- `3` кейса `browser`
- `3` кейса `google_search`
- `3` кейса `none/describe/capability`

Все `20` кейсов первого campaign должны быть только уровня `L1_basic_direct`.

## 8. Verification loop

Для каждой family и для каждого уровня сложности обязательный цикл:

1. Добавить/обновить `20` кейсов в registry.
2. Прогнать:
   - `memory-only`
   - `memory+classifier`
   - `deterministic full-cycle`
3. Довести deterministic до `20/20`.
4. Прогнать live subset тех же `20`.
5. Довести live до `20/20`.
6. Отметить текущий уровень как `closed`.
7. Только потом переходить к следующему уровню этой family.
8. Только после закрытия всех уровней family переходить к следующей family.

### 8.1 Owner verdict order

На каждом цикле verdict должен сниматься строго в таком порядке:

1. `memory-only`
2. `memory+classifier`
3. `deterministic full-cycle`
4. `live full-cycle`

Если `full-cycle` не зелёный, сначала определить:

- сломан `memory_expected`
- или сломан `classifier_expected`
- или сломан `generator_expected`

Только после этого вносить fix.

## 9. Fix rules

### 9.1 When to fix prompts
Правим только `server/server/config/prompts.py`, если:
- route неверный;
- short/noisy follow-up падает в `none`;
- replacement/cancel/continuation распознаны неверно;
- execution shape неверный.

### 9.2 When to fix memory
Правим только `server/server/modules/memory_management/config.py`, если:
- execution уже correct;
- после completed turn goal не очищается;
- после unfinished clarification goal исчезает слишком рано.

### 9.3 What is forbidden
- не переносить lifecycle в classifier;
- не добавлять parser/runtime fallback как primary path;
- не делать category-specific костыль раньше universal rule;
- не смешивать несколько transition families в одном первом `20-case` цикле.

## 10. Acceptance

Текущий уровень считается закрытым только если:

- deterministic:
  - `20/20`
- live:
  - `20/20`

и fail list пуст по:
- execution
- memory post-state

### 10.1 Level status

Для каждого уровня допустимы только 3 статуса:

- `open`
- `in_progress`
- `closed`

Правила:
- новый уровень открывается только если предыдущий `closed`;
- одновременно `in_progress` может быть только один уровень;
- `closed` ставится только после полного `20/20` по всем owner-слоям.

## 11. Reporting

После каждого level-campaign фиксировать:

- какой `transition_family` закрывали;
- какой `difficulty_level` закрывали;
- deterministic result;
- live result;
- owner слоя, который реально правили.

Использовать:
- `Docs/assistant_exchange/codex/`

## 12. Level Notes

Для каждого уровня сложности нужно фиксировать не только кейсы, но и operational notes.

### 12.1 Required sections per level

Для каждого `L1-L5` заполнять:

- `Level Goal`
- `What must work`
- `Critical nuances`
- `Common failure modes`
- `Owner expectations`
- `Exit criteria`

### 12.2 Level guidance

#### L1_basic_direct
- `Level Goal`
  - чистый прямой запрос без ambiguity
- `Critical nuances`
  - missing slot не должен ронять executable intent в `none`
  - app/site names — supporting signal, не owner route

#### L2_clarification_slot_fill
- `Level Goal`
  - short answer correctly closes one missing detail
- `Critical nuances`
  - short answer after clarification = supplied detail
  - один и тот же slot нельзя спрашивать повторно
  - если пришёл последний missing detail, нужно execute now

#### L3_short_continuation
- `Level Goal`
  - short follow-up keeps active task
- `Critical nuances`
  - short continuation не падает в `none`
  - pronoun follow-up reuse already known entity

#### L4_replacement_or_cancel
- `Level Goal`
  - replace/cancel semantics remain stable
- `Critical nuances`
  - replacement beats continuation
  - cancel without new task => `none`
  - old goal must not leak into new task

#### L5_multi_signal_noisy
- `Level Goal`
  - noisy and compressed human turns remain recoverable
- `Critical nuances`
  - typo/noise не должны ломать clear continuation
  - multiple correction signals can still resolve to one replacement
  - completed noisy follow-up must still cleanup goal correctly
