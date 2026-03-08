# Goal Stack Test Gate

## Purpose

Canonical verification gate for strong changes in:
- prompts;
- memory lifecycle semantics;
- classifier routing;
- generator payload/output;
- provider path behavior for messages / WhatsApp / browser / search / system control.

This gate validates the single-owner stack:
- memory owns `goal_state/current_goal`;
- classifier owns `category/route`;
- generator owns final payload/text;
- live run confirms product truth on the real model/tool path.

## Source of Truth

- Canonical registry: `server/server/tests/goal_stack_gate_registry.py`
- Deterministic suites:
  - `server/server/tests/test_memory_basic_goal_matrix.py`
  - `server/server/tests/test_classifier_current_goal_lifecycle_matrix.py`
  - `server/server/tests/test_memory_full_cycle_factual_e2e.py`
- Live runner:
  - `server/server/scripts/run_live_goal_stack_matrix.py`

## Required Run Order

1. `memory-only`
2. `memory + classifier`
3. `full-cycle deterministic`
4. `live 20-case`

Next layer is allowed only after the previous one is green.

## Canonical 20-Case Contract

- Total: `20`
- Stable core: `16`
- Rotatable high-risk cases: `4`
- Dirty/noisy recoverable inputs: `4`
- Paired continuity cases: `>=10`

Coverage must include:
- `new_task`
- `clarification`
- `continuation`
- `pronoun_continuation`
- `same_turn_completion`
- `cancel`
- `replace`
- `no_task`

Category coverage must include:
- `messages`
- `whatsapp`
- `browser`
- `google_search`
- `system_control`
- `describe`
- `capability`
- `none`

## Fail Labeling

Every fail must be labeled with one primary owner only:
- `memory`
- `classifier`
- `generator`
- `live`

Interpretation rules:
- wrong `goal_state/current_goal` => `memory`
- right lifecycle but wrong route => `classifier`
- right route but wrong action payload/text => `generator`
- right deterministic behavior but wrong real provider/tool outcome => `live`

Do not mix owners in one verdict.

## Pairing Rule

Paired continuity cases must use the same logical context:
- same `hardware_id`
- same active task chain
- second turn validates continuation, completion, replace, or cancel

## Dirty Input Rule

Dirty inputs must be recoverable voice-like noise, not random garbage.

Allowed dirty shapes:
- clipped phrase
- malformed word
- dropped filler words
- short fragmented continuation
- STT-like letter/spacing noise

## Trigger Rule

Run the full gate after any strong change touching:
- prompt contracts;
- memory analyzer policy;
- routing/classifier behavior;
- generator payload behavior;
- live provider path;
- acceptance logic in matrix runner.
