# AVAudioEngine Restart Backoff

Goal: reduce AVAudioEngine restart spam and add backoff/guarding.

## Changes
- Added restart backoff, in-progress guard, and warn rate-limit to AVAudioEngine recovery.

## Files
- `modules/speech_playback/core/avf_player.py`
