# Input Architecture V2 (PTT)

## 1. Owner and Layers

- **Source of Truth:** `InputProcessingIntegration` (`integration/integrations/input_processing_integration.py`)
- **Low-level adapter:** `QuartzKeyboardMonitor` / `KeyboardMonitor` (`modules/input_processing/keyboard/*`)
- **Mode switch owner:** `ModeManagementIntegration` через `mode.request`

## 2. Hard Rules

- Keyboard layer не управляет mode/session.
- Keyboard layer отправляет только edge-события: `PRESS`, `LONG_PRESS`, `SHORT_PRESS`, `RELEASE`.
- Все terminal-действия проходят только через coordinator path:
  1. `voice.recording_stop`
  2. wait `voice.mic_closed`
  3. `mode.request`
- Один `terminal stop` на один `press_id`.

## 3. State Machine (InputProcessingIntegration)

- `IDLE`
- `ARMED` (после `PRESS`)
- `RECORDING` (после `LONG_PRESS`)
- `STOPPING` (terminal stop path)
- `WAITING_GRPC` (после перехода в `PROCESSING`)

## 4. Canonical Flows

### Long press → processing
1. `PRESS` -> `ARMED`
2. `LONG_PRESS` -> `RECORDING` + `voice.recording_start` + `mode.request(LISTENING)`
3. `RELEASE` -> terminal stop -> `mode.request(PROCESSING)` -> `WAITING_GRPC`
4. `grpc.request_completed|failed` -> reset -> `IDLE`

### Short tap cancel
1. `PRESS` -> `ARMED`
2. `RELEASE` (below threshold) или `SHORT_PRESS` -> cancel path
3. `interrupt.request` + optional `grpc.request_cancel`
4. `keyboard.short_press` + `mode.request(SLEEPING)` -> reset -> `IDLE`

### Secure Input / tap disabled
1. health-check detects `tap_enabled=false`
2. forced terminal path (`_force_stop`)
3. `mode.request(SLEEPING)` -> reset -> `IDLE`

## 5. Integration Contract

- **Publishes:**
  - `keyboard.press`
  - `keyboard.short_press`
  - `voice.recording_start`
  - `voice.recording_stop`
  - `interrupt.request`
  - `grpc.request_cancel`
  - `mode.request`

- **Subscribes:**
  - `voice.recognition_*`
  - `grpc.request_*`
  - `playback.*`
  - `voice.mic_opened|closed`

## 6. Legacy Handling

- Legacy versions archived in:
  - `Docs/_archive/input_arch/input_processing_integration__legacy_2026-02-09.py`
  - `Docs/_archive/input_arch/quartz_monitor__snapshot_2026-02-09.py`

