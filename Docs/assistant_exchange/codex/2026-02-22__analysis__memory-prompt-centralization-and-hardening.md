# Memory prompt: centralization and hardening

## Task
Проверить актуальность prompt для memory analyzer и актуализировать при необходимости.

## Diagnosis
- Prompt для извлечения памяти был дублирован и слишком общий.
- Риск: запись шумного short-term контента (служебные детали, неконкретные формулировки).

## Changes
1. Updated canonical memory prompt in:
- `server/server/modules/memory_management/config.py`

2. Centralized ownership of prompt:
- `MemoryManager` теперь передает `analysis_prompt_template=self.config.memory_analysis_prompt` в `MemoryAnalyzer`.
- Файл: `server/server/modules/memory_management/core/memory_manager.py`

3. Kept safe fallback in analyzer:
- Добавлен `DEFAULT_ANALYSIS_PROMPT_TEMPLATE` и optional constructor arg `analysis_prompt_template`.
- Файл: `server/server/modules/memory_management/providers/memory_analyzer.py`

## Prompt policy update (summary)
- SHORT_TERM: только активный контекст и незакрытое намерение, 1-2 коротких предложения, без service/tool/json/debug артефактов.
- LONG_TERM: только стабильные предпочтения/факты пользователя.
- Явный запрет на временные/эпизодические детали в long-term.
- Формат ответа analyzer сохранен: `SHORT_TERM:` / `LONG_TERM:`.

## Validation
- `python3 -m py_compile modules/memory_management/config.py modules/memory_management/providers/memory_analyzer.py modules/memory_management/core/memory_manager.py`
- `pytest -q tests/test_memory_single_call_smoke.py tests/test_memory_short_term_cleanup_scheduler.py`
- Result: `5 passed`

## Architecture gates
- Single owner: yes (MemoryConfig prompt).
- Duplication reduced: yes.
- Race impact: none.
- Long-term memory behavior unchanged except stricter extraction policy.
