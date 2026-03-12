# Prompt Catalog

Цель: зафиксировать текущий prompt owner-path по категориям и отдельный experimental prompt profile layer без поломки production.

## Source of Truth

- generation/system prompts: `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/server/server/config/prompts.py`
- runtime route prompt builder: `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/server/server/config/prompts.py::build_route_system_prompt`
- classifier prompt owner: `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/server/server/config/prompts.py::build_intent_classifier_prompt`
- experimental prompt overlays: `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/server/server/experimental/assistant_runtime_v2/prompts/experimental_v2/`

## Category Mapping

| Category | Runtime route | Prompt owner |
| --- | --- | --- |
| Simple Conversation | `none` | `PROMPT_FOOTER` + `PROMPT_UNIFIED_POLICY` + classifier `none category rules` |
| Capability / Meta | `capability` | `PROMPT_CAPABILITY` |
| Screen Description | `describe` | `PROMPT_DESCRIBE` |
| Messages | `messages` | `PROMPT_MESSAGES` |
| WhatsApp | `whatsapp` | `PROMPT_WHATSAPP` |
| System Control | `system_control` | `PROMPT_SYSTEM_CONTROL` |
| Browser | `browser` | `PROMPT_BROWSER` |
| Google Search / Factual | `google_search` | `PROMPT_WEB_SEARCH` |
| Payment / Subscription | `payment` | `PROMPT_PAYMENT` |

## Rules

- Production prompt owner остаётся в `config/prompts.py`.
- Experimental prompt profiles допустимы только как overlays, выбираемые через один selector.
- Default profile всегда `current`.
- Experimental profiles нельзя включать без явного selector.

## Testing Strategy

- classifier coverage: category rules в `build_intent_classifier_prompt()`
- generation coverage: route-specific prompt в `build_route_system_prompt(route, ...)`
- category baseline tests должны проверять, что route-specific prompt не подтягивает чужие action sections
