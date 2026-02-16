# Task Brief: browser install start TTS text update

## Change
Updated browser installation start TTS text in:
- `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27/client/modules/browser_automation/module.py`

New text:
`Browser installation has started. I will let you know when it is finished. After that, you will be able to use browser use.`

Applied to both start-announcement paths:
- immediate install start path
- timeout fallback announcement path

## Verification
- `python3 -m py_compile modules/browser_automation/module.py` passed.
