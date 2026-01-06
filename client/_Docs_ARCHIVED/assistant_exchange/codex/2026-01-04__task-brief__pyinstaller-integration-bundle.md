# Task Brief

## Objective
Ensure integration modules are bundled in the PyInstaller app when client uses symlinked integration paths.

## Change
- `packaging/Nexy.spec`: replaced per-subdir integration datas with a single copy of `integration_backup` into `integration/` inside the bundle.

## Rationale
Symlinked `client/integration/*` paths were not reliably included in the bundle, causing `ModuleNotFoundError` for `integration.integrations.*` at runtime.

## Next Steps
- Rebuild with `./scripts/release_build.sh release` (or `local`) to produce a new .app.
- Validate runtime launch from `/Applications/Nexy.app/Contents/MacOS/Nexy`.
