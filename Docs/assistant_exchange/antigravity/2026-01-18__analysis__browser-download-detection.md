# Browser Download Detection Logic

## Question
User asked what the current logic uses to decide whether the browser is already downloaded or not.

## Answer
- Detection is a timing heuristic inside browser_use: it runs `python -m playwright install chromium` and waits up to 2 seconds.
- If the command finishes within 2 seconds, it assumes Chromium was already installed.
- If it exceeds 2 seconds, it assumes download/installation is in progress and logs "Browser not found. downloading...".

## Source
- server/modules/browser_use/module.py
