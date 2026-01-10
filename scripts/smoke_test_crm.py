#!/usr/bin/env python3
"""
CRM Smoke Test - Verify Core Protections
1. HTTP 409 Conflict Detection
2. Atomic Writes (Backup creation)
3. Audit Log Append
"""

import json
import requests
import os
import time

SERVER_URL = "http://localhost:8000"
API_URL = f"{SERVER_URL}/api"
JSON_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Docs", "PROJECT_KANBAN.json")
BACKUP_PATH = JSON_PATH + ".bak"
AUDIT_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Docs", "CRM_AUDIT_LOG.ndjson")

def test_conflict_flow():
    print("\n--- Test 1: HTTP 409 Conflict Flow ---")
    
    # 1. Get current data (Revision A)
    try:
        res = requests.get(f"{API_URL}/data")
        data = res.json()
        rev_a = data.get('meta', {}).get('revision', 0)
        print(f"[INFO] Current Revision: {rev_a}")
    except Exception as e:
        print(f"[ERROR] Server not running? {e}")
        return False

    # Simulate Assistant 1 saving (Success)
    print("[INFO] Assistant 1 attempting save...")
    payload_1 = data.copy()
    payload_1['meta']['revision'] = rev_a # Sending current revision
    # Add a dummy change
    if 'smoke_test' not in payload_1.get('meta', {}):
        payload_1['meta']['smoke_test'] = 0
    payload_1['meta']['smoke_test'] += 1
    
    res_1 = requests.post(f"{API_URL}/save", json=payload_1)
    if res_1.status_code == 200:
        print(f"[PASS] Assistant 1 save successful. New revision should be {rev_a + 1}")
    else:
        print(f"[FAIL] Assistant 1 save failed: {res_1.status_code} {res_1.text}")
        return False

    # Simulate Assistant 2 saving with OLD revision (Fail)
    print(f"[INFO] Assistant 2 attempting save with OLD revision {rev_a}...")
    payload_2 = data.copy()
    payload_2['meta']['revision'] = rev_a # STALE revision!
    
    res_2 = requests.post(f"{API_URL}/save", json=payload_2)
    
    if res_2.status_code == 409:
        print(f"[PASS] Assistant 2 correctly blocked with 409.")
        print(f"       Response: {res_2.text}")
    else:
        print(f"[FAIL] Assistant 2 should have failed with 409, got {res_2.status_code}")
        return False
        
    return True

def test_atomic_backup():
    print("\n--- Test 2: Atomic Write & Backup ---")
    
    # Check if backup file exists (it should have been created by Test 1)
    if os.path.exists(BACKUP_PATH):
        print(f"[PASS] Backup file exists at {BACKUP_PATH}")
        # Validate content
        try:
            with open(BACKUP_PATH, 'r') as f:
                json.load(f)
            print("[PASS] Backup file is valid JSON")
        except:
            print("[FAIL] Backup file is corrupted")
            return False
    else:
        print("[FAIL] Backup file not found")
        return False
        
    return True

def test_audit_log():
    print("\n--- Test 3: Audit Log ---")
    
    if os.path.exists(AUDIT_PATH):
        print(f"[PASS] Audit log exists at {AUDIT_PATH}")
        # Read last lines
        with open(AUDIT_PATH, 'r') as f:
            lines = f.readlines()
            if lines:
                last_line = lines[-1]
                entry = json.loads(last_line)
                print(f"[INFO] Last audit entry: {entry['action']} at {entry['timestamp']}")
                if entry['action'] in ['save', 'save_conflict']:
                    print("[PASS] verified 'save' or 'save_conflict' action in log")
                else:
                    print(f"[WARN] Unexpected last action: {entry['action']}")
            else:
                print("[FAIL] Audit log is empty")
                return False
    else:
        print("[FAIL] Audit log not found")
        return False

    return True

if __name__ == "__main__":
    success = True
    success &= test_conflict_flow()
    success &= test_atomic_backup()
    success &= test_audit_log()
    
    if success:
        print("\n✅ SMOKE TEST PASSED")
    else:
        print("\n❌ SMOKE TEST FAILED")
