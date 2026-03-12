from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]
SERVER_ROOT = ROOT / "server"
sys.path.insert(0, str(SERVER_ROOT))

from scripts.run_live_goal_stack_matrix import FullCycleCase, _full_cycle_passes


def test_full_cycle_acceptance_ignores_missing_route_telemetry_when_product_output_is_correct():
    case = FullCycleCase(
        "search-direct",
        "hw-1",
        "Find latest world news",
        "google_search",
        None,
        ["world", "news"],
        "clear",
    )

    assert _full_cycle_passes(
        case,
        command=None,
        text="Here are the latest world news headlines.",
        actual_state="clear",
    )


def test_full_cycle_acceptance_still_requires_expected_command_when_action_case():
    case = FullCycleCase(
        "open-safari",
        "hw-2",
        "Open Safari",
        "system_control",
        "open_app",
        ["opening", "safari"],
        "clear",
    )

    assert not _full_cycle_passes(
        case,
        command=None,
        text="Opening Safari.",
        actual_state="clear",
    )
