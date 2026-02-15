"""
Startup order contract tests.

Single source of truth: IntegrationFactory.get_startup_order/STARTUP_ORDER.
"""

from integration.core.integration_factory import IntegrationFactory


def test_tray_immediately_after_instance_manager() -> None:
    order = IntegrationFactory.STARTUP_ORDER
    assert "instance_manager" in order
    assert "tray" in order
    assert order.index("tray") == order.index("instance_manager") + 1


def test_permission_restart_after_first_run_permissions() -> None:
    order = IntegrationFactory.STARTUP_ORDER
    assert "first_run_permissions" in order
    assert "permission_restart" in order
    assert order.index("permission_restart") == order.index("first_run_permissions") + 1


def test_startup_order_contains_required_integrations() -> None:
    order = IntegrationFactory.STARTUP_ORDER
    required = [
        "instance_manager",
        "tray",
        "hardware_id",
        "first_run_permissions",
        "permission_restart",
    ]
    for integration in required:
        assert integration in order


def test_get_startup_order_filters_by_available_only() -> None:
    available = {"instance_manager", "tray", "hardware_id"}
    selected = IntegrationFactory.get_startup_order(
        restrict_to_permissions=True,
        available=available,
    )
    assert selected == ["instance_manager", "tray", "hardware_id"]


def test_get_startup_order_ignores_permissions_only_flag() -> None:
    available = set(IntegrationFactory.STARTUP_ORDER)
    selected_true = IntegrationFactory.get_startup_order(
        restrict_to_permissions=True,
        available=available,
    )
    selected_false = IntegrationFactory.get_startup_order(
        restrict_to_permissions=False,
        available=available,
    )
    assert selected_true == selected_false == IntegrationFactory.STARTUP_ORDER

