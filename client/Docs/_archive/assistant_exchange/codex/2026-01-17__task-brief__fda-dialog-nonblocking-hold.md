# FDA Dialog Nonblocking Hold

## Goal
Avoid perceived hang after FDA dialog by skipping the post-dialog hold.

## Changes
- Track whether FDA dialog was shown; skip hold sleep when dialog is displayed.

## Touchpoints
- `modules/permissions/first_run/activator.py`
