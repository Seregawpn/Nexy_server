# Task Brief: Full Version Centralization (Runtime + Scripts)

## Goal
- Довести использование версии до одного источника (`VERSION`) без числовых fallback в runtime логике.

## Applied Changes
- Runtime config fallbacks:
  - `server/config/unified_config.py`
    - removed hardcoded fallback version
    - fallback chain: `VERSION` -> `SERVER_VERSION` -> `0.0.0.0` (technical)
  - `server/modules/update/config.py`
    - removed hardcoded fallback version
    - fallback chain: `VERSION` -> `SERVER_VERSION` -> `0.0.0.0`

- Update appcast fallback:
  - `server/modules/update/providers/update_server_provider.py`
    - `sparkle:shortVersionString` fallback now uses `self.config.default_version` (not `1.0.0`)

- Version updater hardening:
  - `server/scripts/update_version.py`
    - no longer injects hardcoded `SERVER_VERSION` defaults into code
    - now also updates local `server/updates/manifests/manifest.json`

- Module metadata version dedup:
  - added `server/modules/_version.py` helper reading `VERSION` (fallback: env, then `0.0.0.0`)
  - replaced static `__version__ = '1.0.0'` in:
    - `server/modules/session_management/__init__.py`
    - `server/modules/update/__init__.py`
    - `server/modules/database/__init__.py`
    - `server/modules/text_processing/__init__.py`
    - `server/modules/audio_generation/__init__.py`

- Script default cleanup:
  - `server/scripts/fix_version_mismatch.sh`
    - default `CLIENT_VERSION` now from `VERSION` (or argument), no `1.0.0`

## Synced to Current Version
- Ran `python3 server/scripts/update_version.py <current VERSION>` to sync:
  - `server/config/unified_config.yaml`
  - `server/config.env.example`
  - `server/config/unified_config.py`
  - `server/updates/manifests/manifest.json`

## Verification
- Shell checks: `bash -n` passed for updated `.sh`.
- Python checks: `python3 -m py_compile` passed for updated `.py`.
- No remaining hardcoded app runtime versions in active code paths except template value in `config.env.example` (managed by `update_version.py`).

