# Unify All Cues Including Error

## Request
Сделать одинаковыми все аудио-сигналы, включая ошибку.

## Changes
- `integration/integrations/signal_integration.py`
  - `LISTEN_START`, `DONE`, `ERROR`, `CANCEL` теперь используют один профиль:
    - `tone_hz=880`
    - `duration_ms=120`
    - `volume=0.22`
- `modules/signals/config/types.py`
  - Резервные дефолты для `LISTEN_START`, `DONE`, `ERROR`, `CANCEL` также выровнены к тем же параметрам.

## Validation
```bash
PYTHONPATH=. pytest -q \
  tests/test_signal_integration_cancel_done_suppression.py \
  tests/test_interrupt_playback.py \
  tests/test_processing_workflow_session_guard.py
```

Result: `22 passed`.
