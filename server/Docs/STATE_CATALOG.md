# STATE_CATALOG

Owner: Tech Lead клиента
Source of truth: This document consolidates cross-domain state axes.

## Client Axes
- Permission.mic: granted | denied | prompt_blocked
- Permission.screen: granted | denied
- Permission.accessibility: granted | denied
- Device.input: default_ok | busy
- Network: online | offline
- FirstRun: true | false
- appMode: IDLE | LISTENING | PROCESSING | SPEAKING

## Server Axes (updated 21 Jan 2026)

| Axis | Owner | Values |
|------|-------|--------|
| Session.registry | `SessionRegistry` | active | expired | interrupted |
| Interrupt.global_flag | `GlobalFlagProvider` | true | false |
| Interrupt.hardware_id | `GlobalFlagProvider` | string | null |
| Backpressure.state | `BackpressureManager` | accepting | rejecting |

**Source of Truth:**
- `SessionRegistry` (`modules/session_management/core/session_registry.py`) — единственный владелец session state
- `GlobalFlagProvider` (`modules/interrupt_handling/providers/global_flag_provider.py`) — единственный владелец interrupt flags

## Ownership
- Who writes/reads each axis, and from where

## Metrics
- decision_rate{type}
- stream_open_success_rate
- tcc_prompt_duration_ms
- session_count{status}
- interrupt_rate{hardware_id}

