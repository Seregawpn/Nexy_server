# AVL API key configuration options

Date: 2026-02-10
Type: task-brief

## Goal
Allow user to provide Gemini API key via explicit configuration options.

## Changes
- Updated `/Users/sergiyzasorin/Fix_new/Whatsapp_test/src/whatsapp_test/avl_main.py`
  - Added CLI options:
    - `--api-key`
    - `--api-key-env` (default `GEMINI_API_KEY`)
    - `--config-env` (default `config.env`)
  - Added key resolution priority:
    1) `--api-key`
    2) env var from `--api-key-env`
    3) key from env-style file `--config-env`
- Updated `/Users/sergiyzasorin/Fix_new/Whatsapp_test/src/whatsapp_test/avl/analyzer.py`
  - `build_analyzer(..., api_key=...)` now accepts externally resolved key.
- Added `/Users/sergiyzasorin/Fix_new/Whatsapp_test/config.env.example`
- Updated `/Users/sergiyzasorin/Fix_new/Whatsapp_test/README.md`
  - documented config file setup and key source priority.

## Validation
- `python3 /Users/sergiyzasorin/Fix_new/Whatsapp_test/main_avl.py --help` passed
- `python3 -m py_compile` passed for updated modules

