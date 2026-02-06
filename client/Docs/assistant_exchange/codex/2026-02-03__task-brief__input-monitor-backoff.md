# Input Monitor Backoff & Log Throttling

Goal: reduce CGEventTap deactivation spam and add recovery backoff.

## Changes
- Added backoff to CGEventTap recovery attempts.
- Rate-limited deactivation warnings.
- Removed stacktrace spam from deactivation logs.

## Files
- `modules/input_processing/keyboard/mac/quartz_monitor.py`
