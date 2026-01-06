# Release Deployment Checklist

**Registry ID:** INS-007

## Pre-Flight
- [x] Verify Git Status clean
- [x] Check version number in `main.py`
- [ ] Run unit tests

## Build
- [ ] Run `build_final.sh`
- [ ] Verify `.app` signature

## Post-Build
- [ ] Upload to Staging
- [ ] Notify QA
