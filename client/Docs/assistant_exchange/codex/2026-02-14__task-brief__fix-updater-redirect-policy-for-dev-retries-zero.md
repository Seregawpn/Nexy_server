# Fix updater redirect policy for dev retries=0

## Problem
- Update download failed with:
  - `too many redirects` on GitHub URL.
- Root cause:
  - `UpdateHTTPClient` used `Retry(total=retries, redirect=5)`.
  - In development profile `retries=0`, so redirects were effectively blocked.

## Change
- File: `modules/updater/net.py`
- Updated retry policy to decouple redirects from retry count:
  - `total=None`
  - `connect/read/status/other = retries`
  - `redirect=10`
  - explicit `allowed_methods` for safe methods

## Why this is correct
- Keeps zero retry behavior for transient failures when configured (`retries=0`).
- Still allows normal HTTP redirect chains (GitHub releases CDN redirects) required for artifact download.

## Validation
- `python3 -m py_compile modules/updater/net.py modules/updater/updater.py integration/integrations/updater_integration.py` passed.

## Expected behavior
- On next app start with update available:
  - `update_started` should proceed past first 302 redirect.
  - If no other issues, download progresses instead of immediate redirect failure.
