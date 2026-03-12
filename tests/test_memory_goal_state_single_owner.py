from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SERVER_ROOT = ROOT / "server"


def test_goal_state_is_not_used_outside_memory_owner_path_in_production_code():
    allowed_prod_roots = {
        SERVER_ROOT / "modules" / "memory_management",
    }
    excluded_roots = {
        SERVER_ROOT / "tests",
        SERVER_ROOT / "scripts",
    }

    offenders: list[str] = []
    for path in SERVER_ROOT.rglob("*.py"):
        if any(root in path.parents for root in excluded_roots):
            continue
        if any(root in path.parents or path == root for root in allowed_prod_roots):
            continue
        text = path.read_text(encoding="utf-8")
        if "goal_state" in text:
            offenders.append(str(path))

    assert offenders == [], (
        "goal_state must stay owned only by memory modules; "
        f"unexpected production usages: {offenders}"
    )
