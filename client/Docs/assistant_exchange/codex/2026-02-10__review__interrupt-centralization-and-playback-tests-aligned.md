# Interrupt centralization + playback tests alignment

## Scope
- Централизация cancel-path для short press / preempt.
- Синхронизация playback tests с текущим guard-контрактом (`had_audio`).

## Code changes
- Removed duplicate short-press cancel subscription in gRPC integration:
  - `integration/integrations/grpc_client_integration.py`
  - убрана подписка `keyboard.short_press -> _on_interrupt`
- Removed duplicate short-press subscription in ListeningWorkflow:
  - `integration/workflows/listening_workflow.py`
  - оставлен только `interrupt.request -> _on_interrupt_request`
- Tests aligned with playback cancel contract:
  - `tests/test_interrupt_playback.py`
  - `../tests/test_playback_full_interrupt.py`

## Contract kept
- Единый owner-path отмены:
  - `interrupt.request` (publisher: Input/others)
  - `grpc.request_cancel` (publisher: InterruptManagementIntegration)
  - `playback.cancelled` (publisher: SpeechPlaybackIntegration)
- `cancelled_sessions` mark only if `had_audio_for_session=True`.

## Validation
- `python3 -m py_compile` (changed runtime files + local test): OK
- `PYTHONPATH=. pytest -q tests/test_interrupt_playback.py`: 6 passed
- `PYTHONPATH=. pytest -q ../tests/test_playback_full_interrupt.py`: 3 passed
- `PYTHONPATH=. pytest -q ../tests/test_no_timeouts_no_duplicates.py`: 3 passed

## Notes
- Pytest emitted cache warnings for `.pytest_cache` outside writable scope; test outcomes unaffected.
