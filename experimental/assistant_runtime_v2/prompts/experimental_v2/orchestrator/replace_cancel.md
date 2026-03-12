Orchestrator replace/cancel rules:
- Replace is atomic: old goal out, new goal in.
- Cancel is terminal: old goal out, no continuation.
- Do not emit `keep` when the route has pivoted to a new task and the new task needs clarification.
