## Summary

- What changed:
- Why:

## Server Quality Checklist

- [ ] `bash server/scripts/full_quality_scan.sh` passed locally
- [ ] `bash server/scripts/prod_ready_check.sh` passed locally
- [ ] If feature flags were changed, `python3 server/scripts/verify_feature_flags.py` passed
- [ ] Docs updated when behavior/contracts changed (`server/Docs/*`)
- [ ] Added/updated regression tests for bug fixes

## Deployment Notes

- Risk level: low / medium / high
- Rollback plan:
