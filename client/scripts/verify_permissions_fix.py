#!/usr/bin/env python3
"""
Verification script for TCC Permissions Fixes.

This script imports the actual application modules to verify:
1. Safety: status_checker.check_accessibility_status() should NOT crash.
2. Functionality: activator.activate_accessibility() should trigger the native system dialog.

Usage:
    python3 scripts/verify_permissions_fix.py
"""

import sys
import os
import asyncio
import logging

# Configure path to find client modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(name)s: %(message)s')
logger = logging.getLogger("PermissionsVerifier")

async def verify_status_check():
    print("\n" + "="*60)
    print("TEST 1: Status Checker Safety (CRASH TEST)")
    print("="*60)
    print("Objective: Ensure check_accessibility_status() does NOT crash the app on macOS Sequoia.")
    
    try:
        from modules.permissions.first_run.status_checker import check_accessibility_status, PermissionStatus
        print("✅ Module imported successfully")
        
        print("⏳ Running check_accessibility_status()...")
        status = check_accessibility_status()
        print(f"✅ Result: {status}")
        
        if isinstance(status, PermissionStatus):
            print("✅ Status Check: PASSED (No Crash)")
            return True
        else:
            print("❌ Status Check: FAILED (Invalid result type)")
            return False
            
    except Exception as e:
        print(f"❌ Status Check FAILED with error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def verify_activation():
    print("\n" + "="*60)
    print("TEST 2: Activator Functionality (DIALOG TEST)")
    print("="*60)
    print("Objective: Ensure activate_accessibility() calls the native API correctly.")
    
    try:
        from modules.permissions.first_run.activator import activate_accessibility
        print("✅ Module imported successfully")
        
        print("⏳ Calling activate_accessibility()...")
        print("   -> If permission is missing: You should see 'Nexy would like to control this computer...'")
        print("   -> If permission is granted: It should return True immediately.")
        
        result = await activate_accessibility()
        print(f"✅ Result: {result}")
        
        if result:
            print("✅ Activator: PASSED (Execution successful)")
            return True
        else:
            print("❌ Activator: FAILED (Returned False)")
            return False
            
    except Exception as e:
        print(f"❌ Activator FAILED with error: {e}")
        return False

async def main():
    print("🚀 STARTING PERMISSIONS FIX VERIFICATION")
    
    # Test 1: Status Checker
    checker_passed = await verify_status_check()
    if not checker_passed:
        print("\n❌ CRITICAL ERROR: Application still crashing or failing status check.")
        sys.exit(1)
        
    # Test 2: Activator
    activator_passed = await verify_activation()
    
    print("\n" + "="*60)
    print("VERIFICATION SUMMARY")
    print("="*60)
    print(f"1. Status Check (Crash Fix):   {'✅ PASS' if checker_passed else '❌ FAIL'}")
    print(f"2. Activator (Native Dialog):  {'✅ PASS' if activator_passed else '❌ FAIL'}")
    
    if checker_passed and activator_passed:
        print("\n✅ SUCCESS: The fixes are working correctly.")
        print("You can now rebuild the application.")
        sys.exit(0)
    else:
        print("\n⚠️ FAILURE: Some checks failed.")
        sys.exit(1)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nCancelled.")
    except Exception as e:
        print(f"\n❌ Unhandled exception: {e}")
        sys.exit(1)
