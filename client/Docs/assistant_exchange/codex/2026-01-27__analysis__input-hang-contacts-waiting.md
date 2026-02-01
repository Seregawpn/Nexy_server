# Analysis — “Hang” after Input

## Finding
`~/Library/Logs/Nexy/nexy.log` shows the pipeline moved from `screen_capture` to `contacts` at 13:42:38 and then repeatedly logged `CONTACTS_PROBER Not determined` with `state=waiting_user`. No evidence of an `input_monitoring` step in this window.

## Conclusion
The flow is not hung after Input; it is blocked on Contacts dialog not being granted (or not shown). With AUTO_DIALOG now blocking, the pipeline waits indefinitely while Contacts remains NOT_DETERMINED.

## Next options
- Re-enable Settings fallback for Contacts after a timeout (e.g., waiting_long).
- Or keep strict blocking and require user action on Contacts dialog.
