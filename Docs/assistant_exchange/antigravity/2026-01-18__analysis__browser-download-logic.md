# Browser Download Logic Analysis

## Context
User asked how logic decides whether to download a browser on the client side, and the criteria/requirements.

## Findings
- No client-side download logic found in this server repository.
- Server-side browser automation uses the browser_use module; on init it runs `python -m playwright install chromium` when browser_use is available.
- The module treats install completion under ~2 seconds as "already installed"; longer indicates a download in progress.
- If browser_use is not installed, the module runs in stub mode and does not attempt downloads.

## References
- server/modules/browser_use/module.py
- server/Docs/ARCHITECTURE_OVERVIEW.md
