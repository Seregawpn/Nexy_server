Diagnosis: gRPC request not sent because voice.recognition_completed carries session_id=None after selectors filter non-uuid4 session_id stored in ApplicationStateManager.

Root cause: InputProcessingIntegration generates session_id from timestamp/monotonic float and stores it in state_manager; selectors.get_current_session_id returns None for non-uuid4; VoiceRecognitionIntegration publishes completion with session_id=None; GrpcClientIntegration ignores event with missing session_id.

Primary fix: Generate uuid4 session_id at PTT LONG_PRESS start in InputProcessingIntegration and store as string in ApplicationStateManager; remove float conversions and update local session_id fields to Optional[str].

Notes: Required docs (Docs/ASSISTANT_COORDINATION_PROTOCOL.md, Docs/ANTIGRAVITY_PROMPT.md, Docs/CODEX_PROMPT.md, Docs/assistant_exchange/TEMPLATE.md) not found in this workspace.
