# Memory prompt single-source (config-only)

## Goal
Убрать дубли prompt-политики памяти и оставить один Source of Truth: `MemoryConfig.memory_analysis_prompt`.

## Changes
1. `server/server/modules/memory_management/providers/memory_analyzer.py`
- Удален встроенный `DEFAULT_ANALYSIS_PROMPT_TEMPLATE`.
- Убрана fallback-логика.
- `analysis_prompt_template` теперь обязателен; при пустом значении выбрасывается `ValueError`.

2. `server/server/modules/memory_management/core/memory_manager.py`
- Путь уже был централизован: prompt передается в `MemoryAnalyzer` из `MemoryConfig`.

3. `server/server/tests/test_memory_prompt_policy.py`
- Обновлены проверки: подтверждается отсутствие fallback-константы в provider и наличие требования config-driven prompt.

## Validation
- `python3 -m py_compile modules/memory_management/providers/memory_analyzer.py modules/memory_management/config.py modules/memory_management/core/memory_manager.py tests/test_memory_prompt_policy.py`
- `pytest -q tests/test_memory_prompt_policy.py tests/test_memory_single_call_smoke.py tests/test_memory_short_term_cleanup_scheduler.py`
- Result: `7 passed`

## Architecture gates
- Single Owner: yes (`MemoryConfig`)
- Zero Duplication: yes (provider fallback removed)
- Anti-Race: N/A (no shared-state changes)
- Flag lifecycle: unchanged
