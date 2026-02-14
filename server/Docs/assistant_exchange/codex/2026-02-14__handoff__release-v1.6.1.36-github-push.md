# Release Handoff: v1.6.1.36 GitHub Push

## Scope
- Publish current `release/v1.6.1.36` workspace state to GitHub.
- Keep runtime configuration source as current `config.env`.
- Attempt dependency refresh to latest via `server/requirements.txt`.

## Done
- Verified branch/version alignment:
  - Branch: `release/v1.6.1.36`
  - `VERSION`: `1.6.1.36`
  - Manifest: `1.6.1.36`
- Attempted dependency update with current env:
  - Command: `source config.env && source .venv/bin/activate && pip install --upgrade -r server/requirements.txt`
  - Result: network resolution to package index unavailable in current environment.
  - Local environment remains at currently installed package set in `.venv`.
- Prepared code/doc changes for commit while excluding binary artifacts in `release_inbox/`.

## Constraints
- `release_inbox/` contains large build artifacts (`Nexy.dmg`, `Nexy.pkg`) and must not be committed into code repository.
- Dependency upgrades to "latest" require external network access to package index.

## Follow-up (when network is available)
1. Re-run:
   - `source config.env`
   - `source .venv/bin/activate`
   - `pip install --upgrade -r server/requirements.txt`
2. Validate with:
   - `pip list --outdated`
3. Commit only intentional dependency/lockfile changes.
