## Task
Upload only client-side changes to GitHub for version 1.6.0.37 scope.

## Scope
- Repository root: `/Users/sergiyzasorin/Fix_new/downloads/Nexy_v1.6.1.27`
- Included: `client/**`
- Excluded: `server/**`, `Docs/**` outside `client/`

## Actions
1. Created branch `release/v1.6.0.37` from current HEAD.
2. Staged only `client` changes via `git add -A .` from `client/`.
3. Verified staged paths contain only `client/...`.
4. Committed and pushed branch to `origin`.

## Result
Client-only changes were uploaded without server-side files.
