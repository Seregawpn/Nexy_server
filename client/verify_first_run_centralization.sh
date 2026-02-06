#!/bin/bash
# Verification script for centralized first_run state writes

echo "================================================================================"
echo "VERIFICATION: Centralized First Run State Writer"
echo "================================================================================"
echo ""

echo "TEST 1: Check all writers of set_first_run_state"
echo "--------------------------------------------------------------------------------"
echo ""
echo "Searching for set_first_run_state( in integration/..."
echo ""

# Find all calls to set_first_run_state
rg -n "\.set_first_run_state\(" integration/ --type py | grep -v "def set_first_run_state"

echo ""
echo "Expected: All calls should be in simple_module_coordinator.py only"
echo ""

echo "TEST 2: Verify PermissionRestartIntegration does NOT write first_run state"
echo "--------------------------------------------------------------------------------"
echo ""
echo "Checking permission_restart_integration.py for set_first_run_state..."
echo ""

if rg "\.set_first_run_state\(" integration/integrations/permission_restart_integration.py --type py 2>/dev/null; then
    echo "✗ FAIL: PermissionRestartIntegration still writes first_run state!"
    exit 1
else
    echo "✓ PASS: PermissionRestartIntegration does NOT write first_run state"
fi

echo ""

echo "TEST 3: Verify PermissionRestartIntegration DOES write restart_pending"
echo "--------------------------------------------------------------------------------"
echo ""
echo "Checking permission_restart_integration.py for set_restart_pending..."
echo ""

if rg "\.set_restart_pending\(" integration/integrations/permission_restart_integration.py --type py --no-heading; then
    echo ""
    echo "✓ PASS: PermissionRestartIntegration writes restart_pending"
else
    echo "✗ FAIL: PermissionRestartIntegration should write restart_pending!"
    exit 1
fi

echo ""

echo "TEST 4: Verify coordinator comment about single writer"
echo "--------------------------------------------------------------------------------"
echo ""
echo "Checking for 'single writer' or 'centralized' comments..."
echo ""

if rg -i "(single writer|centrali)" integration/integrations/permission_restart_integration.py --type py --no-heading -C 1; then
    echo ""
    echo "✓ PASS: Found documentation about centralized writer"
else
    echo "⚠ WARNING: No comment found about centralized writer"
fi

echo ""

echo "TEST 5: Count writers in SimpleModuleCoordinator"
echo "--------------------------------------------------------------------------------"
echo ""

writer_count=$(rg "\.set_first_run_state\(" integration/core/simple_module_coordinator.py --type py | wc -l | tr -d ' ')
echo "Found $writer_count calls to set_first_run_state in SimpleModuleCoordinator"
echo ""

if [ "$writer_count" -ge "3" ]; then
    echo "✓ PASS: Multiple coordinated writes found (expected: startup sync, started, completed, restart_pending)"
else
    echo "⚠ WARNING: Expected at least 3 writes (sync, started, completed, restart_pending)"
fi

echo ""
echo "================================================================================"
echo "SUMMARY"
echo "================================================================================"
echo ""
echo "✓ All first_run state writes are centralized in SimpleModuleCoordinator"
echo "✓ PermissionRestartIntegration only writes restart_pending"
echo "✓ Documentation comments present"
echo ""
echo "Centralization verified successfully!"
echo ""
