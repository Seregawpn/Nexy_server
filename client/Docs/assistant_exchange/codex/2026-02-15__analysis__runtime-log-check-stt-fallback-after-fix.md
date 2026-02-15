# Runtime log check: STT fallback race after fix

Date checked: 2026-02-15

## Files
- /Users/sergiyzasorin/Library/Logs/Nexy/nexy.log
- /Users/sergiyzasorin/Library/Logs/Nexy/nexy-dev.log

## Result
- `nexy.log` last active entries are around 12:57 and still show old race pattern:
  - fallback `no_speech_after_release` before late STT completion,
  - then `terminal STT dedup` for completed.
- `nexy-dev.log` has fresh run (13:46+) and shows corrected behavior:
  - `Stop requested, processing FINAL audio chunk before exit` at 13:46:55,
  - `voice.recognition_completed` published at 13:46:58,
  - no fallback terminal and no terminal-dedup-for-completed in this run slice.

## Conclusion
Current run (13:46+) is correct and regression is not reproduced there.
