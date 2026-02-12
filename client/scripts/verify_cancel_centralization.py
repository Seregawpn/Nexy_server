#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INTEGRATIONS = ROOT / "integration" / "integrations"

ALLOWED_PLAYBACK_CANCELLED = {
    INTEGRATIONS / "speech_playback_integration.py",
}
ALLOWED_GRPC_REQUEST_CANCEL = {
    INTEGRATIONS / "interrupt_management_integration.py",
}


def _find_publishers(token: str) -> list[Path]:
    hits: list[Path] = []
    for path in INTEGRATIONS.glob("*.py"):
        try:
            text = path.read_text(encoding="utf-8")
        except Exception:
            continue
        if f'publish("{token}"' in text or f"publish('{token}'" in text:
            hits.append(path)
    return hits


def _validate(token: str, allowed: set[Path]) -> list[str]:
    errors: list[str] = []
    hits = _find_publishers(token)
    for path in hits:
        if path not in allowed:
            errors.append(f"{token} publisher not allowed: {path}")
    return errors


def main() -> int:
    errors: list[str] = []
    errors.extend(_validate("playback.cancelled", ALLOWED_PLAYBACK_CANCELLED))
    errors.extend(_validate("grpc.request_cancel", ALLOWED_GRPC_REQUEST_CANCEL))

    if errors:
        print("CANCEL_CENTRALIZATION_VIOLATIONS:")
        for err in errors:
            print(f"- {err}")
        return 1

    print("OK: cancel centralization verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
