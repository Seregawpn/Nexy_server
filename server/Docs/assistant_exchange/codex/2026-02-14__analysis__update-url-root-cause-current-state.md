# Update URL root cause (current state)

## What was verified
- Client enforces HTTPS in updater network layer:
  - `../client/modules/updater/net.py:76`
  - `../client/modules/updater/net.py:224`
- Local server manifest currently contains wrong artifact metadata:
  - `server/updates/manifests/manifest.json`
  - `artifact.url` points to `https://20.151.51.172/updates/appcast.xml` (feed URL, not DMG/PKG)
  - `artifact.type` is `txt`
  - `artifact.size` is `33`

## Implication
- Even if URL is HTTPS, update payload source is malformed (points to appcast feed instead of package artifact).
- The observed runtime error `URL должен использовать HTTPS...` means production appcast currently emits a non-HTTPS enclosure URL in the latest run.

## Conclusion
Primary issue is release publication data (manifest/appcast source of truth), not client update orchestration.
