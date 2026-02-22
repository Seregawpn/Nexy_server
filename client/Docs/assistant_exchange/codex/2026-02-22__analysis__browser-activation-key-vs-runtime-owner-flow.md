# Analysis: browser activation keys vs browser runtime packaging

## Context
User sees browser activation asking for keys and proposes removing bundled browser runtime from package.

## Findings
- Key request is not a browser binary activation key. It is Gemini API key requirement for local browser-use LLM path.
- Browser runtime installation at user machine is currently intentionally disabled in runtime code.
- Therefore: removing bundled runtime without re-enabling runtime installer will hard-break browser feature.

## Evidence
- LLM key gate:
  - `modules/browser_automation/module.py` (`_create_llm`): raises
    `GEMINI_API_KEY not configured ...` when no key found.
- Runtime install disabled:
  - `modules/browser_automation/module.py`: `_ensure_browser_installed()` immediately raises
    `runtime_browser_install_disabled_use_prebundled_runtime`.
  - `_get_or_start_install_task()` also immediately raises same runtime-disabled error.
- Packaging currently expects pre-bundled runtime:
  - `packaging/build_final.sh` validates and bundles `playwright-browsers` into app.

## Conclusion
- Current failure perceived as “browser activation key” is primarily LLM API key provisioning issue.
- Browser runtime packaging and LLM key are two different axes; changing one does not fix the other.

## Recommended owner-flow
1. Keep single owner in `BrowserUseModule` for readiness (runtime + LLM).
2. Decide product mode explicitly:
   - Pre-bundled runtime mode (current packaging policy), or
   - User-machine runtime install mode (requires re-enabling installer code paths).
3. For key UX: replace ad-hoc runtime failure with explicit preflight reason and guided action.

## Verification
- No code changes in this analysis step.

## Информация об изменениях
- Изменения не вносились.
- Список файлов: отсутствует.
- Причина/цель изменений: определить истинную причину сбоя browser activation и owner-path решения.
- Проверка: прочитаны runtime/packaging модули и сопоставлены error paths.
