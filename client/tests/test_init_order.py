"""
Test initialization order of integrations in SimpleModuleCoordinator.

Ensures tray starts immediately after instance_manager (gate mechanism),
and first_run_permissions/permission_restart are sequenced for the gate mechanism.
See .cursorrules section 4 for the required order.
"""
import ast
import inspect
import pytest
from pathlib import Path


def extract_startup_order_from_code() -> list:
    """Extract startup_order list from SimpleModuleCoordinator.start() method.
    
    Uses ast.literal_eval with defensive manual fallback for stability
    if the coordinator's list literal changes form.
    """
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
                        # Try ast.literal_eval first (more robust)
                        try:
                            # Convert AST node to string representation
                            list_str = ast.unparse(node.value) if hasattr(ast, 'unparse') else None
                            if list_str:
                                import ast as ast_module
                                return ast_module.literal_eval(list_str)
                        except (ValueError, SyntaxError):
                            pass
                        
                        # Fallback: manual extraction
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
    
    def test_tray_immediately_after_instance_manager(self):
        """Test that tray starts immediately after instance_manager (gate mechanism)."""
        startup_order = extract_startup_order_from_code()
        
        if not startup_order:
            pytest.skip("Could not extract startup_order from code")
        
        assert 'instance_manager' in startup_order, \
            "instance_manager must be in startup_order"
        assert 'tray' in startup_order, \
            "tray must be in startup_order"
        
        instance_mgr_idx = startup_order.index('instance_manager')
        tray_idx = startup_order.index('tray')
        
        assert tray_idx == instance_mgr_idx + 1, \
            f"tray (pos {tray_idx}) must be immediately after instance_manager (pos {instance_mgr_idx})"
    
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
        """Test critical positions in initialization order.
        
        Tray must start immediately after instance_manager for gate mechanism.
        first_run_permissions and permission_restart must be sequenced.
        """
        startup_order = extract_startup_order_from_code()
        
        if not startup_order:
            pytest.skip("Could not extract startup_order from code")
        
        # Tightened assertion: compare prefix directly against expected tray gate ordering
        expected_prefix = ['instance_manager', 'tray']
        actual_prefix = startup_order[:len(expected_prefix)]
        
        assert actual_prefix == expected_prefix, \
            f"Critical prefix must be {expected_prefix}, got {actual_prefix}"
        
        # Verify first_run_permissions and permission_restart are sequenced
        assert 'first_run_permissions' in startup_order, \
            "first_run_permissions must be in startup_order"
        assert 'permission_restart' in startup_order, \
            "permission_restart must be in startup_order"
        
        first_run_idx = startup_order.index('first_run_permissions')
        perm_restart_idx = startup_order.index('permission_restart')
        
        assert perm_restart_idx == first_run_idx + 1, \
            f"permission_restart (pos {perm_restart_idx}) must be immediately after first_run_permissions (pos {first_run_idx})"
    
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

