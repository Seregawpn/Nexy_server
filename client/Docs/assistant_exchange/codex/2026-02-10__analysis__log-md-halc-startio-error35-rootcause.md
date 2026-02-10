# Analysis: log.md HALC StartIO error 35

## Context
- Checked `log.md` for repeated `HALC_ProxyIOContext::_StartIO ... error 35`.
- Correlated with current audio/input owners and event paths.

## Findings
1. `log.md` shows bursty `PauseIO/ResumeIO` loops around each error window (22:05:27, 22:05:41, 22:08:14, 22:08:24).
2. In code, `InputProcessingIntegration` can publish interrupt preempt and then immediately proceed to arm/start recording in the same user action path.
3. There are still two internal stop entry paths in Input owner:
   - keyboard local stop path (`_terminal_stop` from keyboard handlers)
   - external interrupt owner path (`_on_interrupt_request` -> `_terminal_stop`)
4. `InterruptManagementIntegration` dedups only `grpc.request_cancel` publish, but still routes duplicate speech_stop through coordinator and `mode.request` path.

## Architecture risk
- Source-of-truth is intended to be centralized owner chain:
  `interrupt.request -> InterruptManagementIntegration -> grpc.request_cancel/mode.request` and input owner for terminal mic stop.
- Current timing allows near-concurrent stop/start transitions at audio boundary, causing CoreAudio StartIO contention.

## Recommended fix set
1. Add a serialized transition guard in Input owner (`asyncio.Lock`) for stop/start lifecycle.
2. Introduce a single internal entry for speech stop in Input owner, and route both keyboard/external sources through it.
3. Add an idempotent gate for start/resume in Input owner: do not emit `voice.recording_start` if already in `RECORDING/STOPPING` or start in flight.
4. For preempt-before-start path, wait for terminal stop barrier (`mic_closed` or bounded timeout) before emitting new `voice.recording_start`.
5. Optional cleanup: in Interrupt owner, extend dedup to skip duplicate coordinator handling for speech_stop within dedup window.

## Verification focus
- No repeated `HALC_ProxyIOContext::_StartIO ... error 35` during rapid press/interrupt cycles.
- Exactly one `voice.recording_start` per press cycle.
- Exactly one terminal `voice.recording_stop` per cycle.
- No extra `mode.request` churn for duplicate `speech_stop`.
