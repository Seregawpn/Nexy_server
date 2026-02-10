# AVL switch OpenAI -> Gemini

Date: 2026-02-10
Type: task-brief

## Goal
Replace OpenAI-based AVL analyzer with Gemini.

## Changes
- Updated `/Users/sergiyzasorin/Fix_new/Whatsapp_test/src/whatsapp_test/avl/analyzer.py`
  - API switched to Gemini `generateContent` endpoint
  - key source switched from `OPENAI_API_KEY` to `GEMINI_API_KEY`
  - request format updated to Gemini (`system_instruction`, `contents.parts.inline_data`)
  - robust JSON extraction added for model text output
  - deterministic fallback preserved on API/parse failures
- Updated `/Users/sergiyzasorin/Fix_new/Whatsapp_test/src/whatsapp_test/avl_main.py`
  - default model changed to `gemini-2.0-flash`
  - help text updated to Gemini
- Updated `/Users/sergiyzasorin/Fix_new/Whatsapp_test/README.md`
  - docs switched to Gemini env var and model examples

## Validation
- `python3 -m py_compile` passed for updated modules
- `python3 /Users/sergiyzasorin/Fix_new/Whatsapp_test/main_avl.py --help` passed

