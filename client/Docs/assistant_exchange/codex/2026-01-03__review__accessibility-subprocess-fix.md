# Review: Accessibility subprocess fix

## Summary
Verified that accessibility status check uses `/usr/bin/python3` (not `sys.executable`) to avoid spawning new Nexy instances and includes a 2s cache.

## Observations
- Correct imports for `AXIsProcessTrustedWithOptions` and `kAXTrustedCheckOptionPrompt`.
- Return mapping: true→GRANTED, false→DENIED, ImportError→DENIED, failure→DENIED, timeout→NOT_DETERMINED.

## Risk
- If `/usr/bin/python3` lacks PyObjC, result is DENIED, which may suppress re‑prompting; intended to avoid loops but should be validated in QA.
