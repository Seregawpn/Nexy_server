from pathlib import Path


PROMPT_ROOT = (
    Path(__file__).resolve().parent.parent
    / "experimental"
    / "assistant_runtime_v2"
    / "prompts"
    / "experimental_v2"
)


def test_experimental_prompt_role_base_has_expected_roles():
    roles = sorted(path.name for path in PROMPT_ROOT.iterdir() if path.is_dir())

    assert roles == ["classifier", "generator", "memory", "orchestrator"]


def test_experimental_prompt_role_base_has_required_files():
    required = {
        "classifier": {"core.md", "noisy.md", "pivot.md"},
        "generator": {"answer.md", "clarify.md", "continue.md", "replace_cancel.md"},
        "memory": {"priority.md", "current_goal.md", "stale_guard.md"},
        "orchestrator": {"lifecycle.md", "replace_cancel.md", "execution_readiness.md"},
    }

    for role, expected_files in required.items():
        actual = {path.name for path in (PROMPT_ROOT / role).iterdir() if path.is_file()}
        assert expected_files.issubset(actual), role
