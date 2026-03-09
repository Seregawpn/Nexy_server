#!/usr/bin/env python3
"""Fast docs presence gate for server CI."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _exists_any(candidates: list[str]) -> bool:
    return any((ROOT / candidate).exists() for candidate in candidates)


REQUIRED_SETS = {
    "AGENTS": ["AGENTS.md"],
    "Server Architecture": ["server/Docs/ARCHITECTURE_OVERVIEW.md"],
    "Server Deployment": ["server/Docs/SERVER_DEPLOYMENT_GUIDE.md"],
    "Release/Update Guide": ["server/Docs/RELEASE_AND_UPDATE_GUIDE.md"],
    "gRPC Proto": ["server/modules/grpc_service/streaming.proto"],
    # Root-docs may live one level above in monorepo layout.
    "Project Requirements": ["Docs/PROJECT_REQUIREMENTS.md", "../Docs/PROJECT_REQUIREMENTS.md"],
    "Assistant Coordination": ["Docs/ASSISTANT_COORDINATION_PROTOCOL.md", "../Docs/ASSISTANT_COORDINATION_PROTOCOL.md"],
    "Codex Prompt": ["Docs/CODEX_PROMPT.md", "../Docs/CODEX_PROMPT.md"],
    "Antigravity Prompt": ["Docs/ANTIGRAVITY_PROMPT.md", "../Docs/ANTIGRAVITY_PROMPT.md"],
    "Assistant Template": ["Docs/assistant_exchange/TEMPLATE.md", "../Docs/assistant_exchange/TEMPLATE.md"],
}


def main() -> int:
    missing: list[str] = []
    for label, candidates in REQUIRED_SETS.items():
        if not _exists_any(candidates):
            missing.append(f"{label}: one of {candidates}")

    if missing:
        print("[docs-gate] FAIL")
        for item in missing:
            print(f"  - {item}")
        return 1

    print("[docs-gate] OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
