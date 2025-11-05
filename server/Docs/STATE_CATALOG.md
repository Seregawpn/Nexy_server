# STATE_CATALOG

Owner: Tech Lead клиента
Source of truth: This document consolidates cross-domain state axes.

## Axes
- Permission.mic: granted | denied | prompt_blocked
- Permission.screen: granted | denied
- Permission.accessibility: granted | denied
- Device.input: default_ok | busy
- Network: online | offline
- FirstRun: true | false
- appMode: IDLE | LISTENING | PROCESSING | SPEAKING

## Ownership
- Who writes/reads each axis, and from where

## Metrics
- decision_rate{type}
- stream_open_success_rate
- tcc_prompt_duration_ms
