# Packaging Readiness Checklist

Дата: `YYYY-MM-DD`  
Исполнитель: `<name>`  
Версия: `<app_version>`

## Gates

- [ ] `./scripts/pre_build_gate.sh --skip-tests`
- [ ] `REQUIRE_BASEDPYRIGHT_IN_SCAN=true ./scripts/problem_scan_gate.sh`
- [ ] `python3 scripts/verify_packaging_readiness.py`

## Build

- [ ] `./packaging/build_final.sh` завершен успешно
- [ ] `dist/Nexy.app` существует
- [ ] `dist/Nexy.pkg` существует
- [ ] `dist/Nexy.dmg` существует

## Artifact Validation

- [ ] `codesign --verify --deep --strict dist/Nexy.app`
- [ ] `xcrun stapler validate dist/Nexy.app`
- [ ] `pkgutil --check-signature dist/Nexy.pkg`
- [ ] `xcrun stapler validate dist/Nexy.pkg`
- [ ] `python3 scripts/validate_release_bundle.py dist/Nexy.app dist/Nexy.pkg`

## Logs

- [ ] `dist/packaging_verification.log` без ошибок
- [ ] build/preflight логи приложены к задаче/PR

## Итог

- [ ] Ready for release
- [ ] Not ready (описать причины)
