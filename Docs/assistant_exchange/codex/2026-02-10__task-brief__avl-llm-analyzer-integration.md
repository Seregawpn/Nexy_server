# AVL LLM analyzer integration

Date: 2026-02-10
Type: task-brief

## Goal
Switch AVL from deterministic decisioning to LLM-based screenshot analysis, with safe fallback.

## Changes
- Replaced analyzer implementation:
  - `/Users/sergiyzasorin/Fix_new/Whatsapp_test/src/whatsapp_test/avl/analyzer.py`
  - added:
    - `DeterministicAnalyzer`
    - `LlmAnalyzer` (OpenAI `responses` API + screenshot image as base64)
    - `build_analyzer(model, force_deterministic)`
  - fallback to deterministic on missing key / API / parsing errors.
- Updated AVL entrypoint:
  - `/Users/sergiyzasorin/Fix_new/Whatsapp_test/src/whatsapp_test/avl_main.py`
  - new args:
    - `--llm-model`
    - `--deterministic`
- Updated coordinator typing to analyzer-agnostic:
  - `/Users/sergiyzasorin/Fix_new/Whatsapp_test/src/whatsapp_test/avl/coordinator.py`
- Updated docs:
  - `/Users/sergiyzasorin/Fix_new/Whatsapp_test/README.md`
  - added `OPENAI_API_KEY` usage and deterministic mode example.

## Validation
- `python3 /Users/sergiyzasorin/Fix_new/Whatsapp_test/main_avl.py --help` passed
- `python3 -m py_compile` for updated AVL modules passed

