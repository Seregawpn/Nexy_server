"""
Test initialization order of integrations in SimpleModuleCoordinator.

Ensures first_run_permissions is at position 3 and permission_restart at position 4.
See .cursorrules section 4 for the required order.
"""
import ast
import inspect
import pytest
from pathlib import Path


def extract_startup_order_from_code() -> list:
    """Extract startup_order list from SimpleModuleCoordinator.start() method."""
    coordinator_path = Path(__file__).parent.parent / "integration" / "core" / "simple_module_coordinator.py"
    
    with open(coordinator_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Parse AST to find startup_order assignment
    tree = ast.parse(content)
    
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "startup_order":
                    if isinstance(node.value, ast.List):
                        # Extract list elements
                        order = []
                        for elt in node.value.elts:
                            if isinstance(elt, ast.Constant):
                                order.append(elt.value)
                            elif isinstance(elt, ast.Str):  # Python < 3.8
                                order.append(elt.s)
                        return order
    
    return []


class TestInitOrder:
    """Test that integrations are initialized in the correct order."""
    
    def test_first_run_permissions_before_tray(self):
        """Test that first_run_permissions is initialized before tray."""
        startup_order = extract_startup_order_from_code()
        
        if not startup_order:
            pytest.skip("Could not extract startup_order from code")
        
        assert 'first_run_permissions' in startup_order, \
            "first_run_permissions must be in startup_order"
        assert 'tray' in startup_order, \
            "tray must be in startup_order"
        
        first_run_idx = startup_order.index('first_run_permissions')
        tray_idx = startup_order.index('tray')
        
        assert first_run_idx < tray_idx, \
            f"first_run_permissions (pos {first_run_idx}) must be before tray (pos {tray_idx})"
    
    def test_permission_restart_after_first_run_permissions(self):
        """Test that permission_restart is initialized immediately after first_run_permissions."""
        startup_order = extract_startup_order_from_code()
        
        if not startup_order:
            pytest.skip("Could not extract startup_order from code")
        
        assert 'first_run_permissions' in startup_order, \
            "first_run_permissions must be in startup_order"
        assert 'permission_restart' in startup_order, \
            "permission_restart must be in startup_order"
        
        first_run_idx = startup_order.index('first_run_permissions')
        perm_restart_idx = startup_order.index('permission_restart')
        
        assert perm_restart_idx == first_run_idx + 1, \
            f"permission_restart (pos {perm_restart_idx}) must be immediately after first_run_permissions (pos {first_run_idx})"
    
    def test_init_order_critical_positions(self):
        """Test critical positions in initialization order."""
        startup_order = extract_startup_order_from_code()
        
        if not startup_order:
            pytest.skip("Could not extract startup_order from code")
        
        # Expected positions (0-based)
        assert startup_order[0] == 'instance_manager', \
            f"instance_manager must be first (blocking), got {startup_order[0]}"
        assert startup_order[1] == 'hardware_id', \
            f"hardware_id must be second, got {startup_order[1]}"
        assert startup_order[2] == 'first_run_permissions', \
            f"first_run_permissions must be third (blocking), got {startup_order[2]}"
        assert startup_order[3] == 'permission_restart', \
            f"permission_restart must be fourth (immediately after first_run_permissions), got {startup_order[3]}"
        assert startup_order[4] == 'tray', \
            f"tray must be fifth (after permission_restart), got {startup_order[4]}"
    
    def test_startup_order_contains_all_required(self):
        """Test that startup_order contains all required integrations."""
        startup_order = extract_startup_order_from_code()
        
        if not startup_order:
            pytest.skip("Could not extract startup_order from code")
        
        required = [
            'instance_manager',
            'hardware_id',
            'first_run_permissions',
            'permission_restart',
            'tray',
        ]
        
        for integration in required:
            assert integration in startup_order, \
                f"{integration} must be in startup_order"

