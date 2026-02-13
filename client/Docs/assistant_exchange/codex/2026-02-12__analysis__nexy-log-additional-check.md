# Additional nexy.log check (2026-02-12)

## Scope
- Source: `~/Library/Logs/Nexy/nexy.log`
- Focus: quit/restart loops, legacy/v2 restart conflicts, duplicated first-run restart events.

## Findings
1. Historical entries (older runs) contain legacy coordinator subscription/dispatch for `permissions.first_run_restart_pending` together with V2 freeze warnings.
2. In recent runs (around `2026-02-12 10:49`), logs still show informational V2 freeze warning from `permission_restart_integration`, but no new legacy restart-pending dispatch in the same window.
3. Quit behavior sample:
   - `2026-02-12 10:12:40` — `Quit requested via tray menu` and `quit() called`.
   - next recorded start is `2026-02-12 10:33:08` (no immediate auto-reopen loop in that segment).
4. Expected one-time first-run restart remains visible at `2026-02-12 10:10:10` (`Restart requested ... permission_activation`) with process handoff.

## Conclusion
- Current observed behavior is consistent with architecture intent:
  - no immediate quit->auto-reopen loop in latest checked segment,
  - no active evidence of V2 + legacy restart-owner conflict in newest startup window,
  - historical noisy lines remain in the same log file and can confuse diagnosis.

## Recommendation
- Rotate/clear log between validation sessions to isolate only fresh run evidence.
