# Task Brief: Remove Dormant AudioDeviceMonitor Duplicate

Date: 2026-02-11

## Context
В `voice_recognition` существовал второй монитор input-устройств:
- `core/audio_route_monitor.py` (runtime owner, используется через GoogleSRController)
- `core/audio_device_monitor.py` (неиспользуемый дубликат)

Дубликат повышал риск расхождения поведения и возвращения второго пути ownership.

## Change
Файл удален:
- `modules/voice_recognition/core/audio_device_monitor.py`

Проверка ссылок:
- Runtime-ссылок на `AudioDeviceMonitor` не было.

## Verification
- `PYTHONPATH=. pytest -q tests/test_unified_config_avfoundation_flags.py tests/test_voice_route_manager_gate.py tests/test_interrupt_playback.py -k "grpc_cancel or interrupt_idempotently or avfoundation or route_reconcile"` → `7 passed, 19 deselected`
- `rg -n "audio_device_monitor|AudioDeviceMonitor" modules integration tests` → нет совпадений

## Outcome
- У input-device monitoring остался один runtime-owner: `AudioRouteMonitor`.
- Снижен риск повторного появления второго параллельного мониторинга.
