# Task Brief: English-only strict intent routing for Describe and WebSearch

## Goal
Ensure screenshot/describe and web-search style requests always return Text-only JSON, while Action JSON is used only for supported executable commands.

## Updated Source of Truth
- `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/server/server/config/prompts.py`

## What Changed
1. Describe block hardened:
- Added explicit examples for screenshot/visibility queries.
- Added explicit prohibition of Action JSON for describe/screenshot intents.
- Added explicit prohibition of invented commands (`describe_screen`, `screen_describe`).

2. WebSearch block hardened:
- Added explicit examples, including "find the latest football news".
- Added explicit prohibition of Action JSON for WebSearch intents.

3. Footer routing policy hardened:
- Ambiguous clarifier rewritten to English and aligned with supported routing.
- Added strict intent routing matrix:
  - Describe/screenshot -> Text-only JSON.
  - Web search/news/facts/prices/current events -> Text-only JSON.
  - Action JSON only for supported executable operations.
  - Non-matching intents -> Text-only JSON.
  - Never invent commands outside `allowed_commands`.
- Cleaned Action examples to supported commands only.

## Validation
- Prompt build sanity check passed.
- Tests passed: `server/server/tests/test_prompt_keywords.py` (3/3).
