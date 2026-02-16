#!/usr/bin/env python3
import sys
import os
import time
import argparse
from datetime import datetime

# Add server directory to python path
current_dir = os.path.dirname(os.path.abspath(__file__))
server_dir = os.path.join(current_dir, 'server')
sys.path.append(server_dir)

from server.modules.subscription.repository.subscription_repository import SubscriptionRepository

HARDWARE_ID = "IDEMPOTENCY_TEST_UUID"

def _parse_args():
    parser = argparse.ArgumentParser(description="Verify idempotency guards (uses destructive reset for test hardware_id).")
    parser.add_argument(
        "--allow-reset",
        action="store_true",
        help="Required flag to allow reset (DELETE) of the test subscription row."
    )
    return parser.parse_args()


def _require_reset_confirmation(args):
    if not args.allow_reset:
        raise RuntimeError("Blocked: pass --allow-reset to permit DELETE reset for test row.")

    confirm_token = os.getenv("NEXY_CONFIRM_DESTRUCTIVE", "")
    if confirm_token != "YES":
        raise RuntimeError("Blocked: set NEXY_CONFIRM_DESTRUCTIVE=YES.")

    env_name = os.getenv("NEXY_ENV", "").lower()
    if env_name == "production":
        raise RuntimeError("Blocked in production environment (NEXY_ENV=production).")

def main():
    args = _parse_args()
    _require_reset_confirmation(args)

    print(f"🔬 Testing Idempotency Guards for {HARDWARE_ID}...")
    
    repo = SubscriptionRepository()
    
    # 1. Reset
    conn = repo._get_connection()
    with conn.cursor() as cur:
        cur.execute("DELETE FROM subscriptions WHERE hardware_id = %s", (HARDWARE_ID,))
        conn.commit()
    conn.close()
    
    repo.create_subscription(HARDWARE_ID, status='initial')
    print("✅ Created initial subscription")
    
    # 2. Test Idempotency (Same Event ID)
    event_id = "evt_duplicate_test"
    now = datetime.now()
    
    print("\n--- Test 1: Duplicate Event ---")
    
    # First write
    print("1. Writing event 'evt_duplicate_test' (status=paid)...")
    repo.update_subscription(
        HARDWARE_ID,
        status='paid',
        last_stripe_event_id=event_id,
        last_stripe_event_at=now
    )
    
    sub = repo.get_subscription(HARDWARE_ID)
    print(f"   State: status={sub['status']}, event={sub['last_stripe_event_id']}")
    assert sub['status'] == 'paid'
    
    # Second write (different status, same event ID) -> Should be IGNORED
    print("2. Writing SAME event 'evt_duplicate_test' with status='failed'...")
    repo.update_subscription(
        HARDWARE_ID,
        status='failed',
        last_stripe_event_id=event_id,
        last_stripe_event_at=now
    )
    
    sub = repo.get_subscription(HARDWARE_ID)
    print(f"   State: status={sub['status']}, event={sub['last_stripe_event_id']}")
    
    if sub['status'] == 'paid':
        print("✅ SUCCESS: Update was ignored (Idempotency)")
    else:
        print(f"❌ FAILED: Status changed to {sub['status']}")
        
    # 3. Test Ordering (Older Event)
    print("\n--- Test 2: Out of Order Event ---")
    
    # New event (newer time)
    newer_event_id = "evt_newer"
    newer_time = datetime.fromtimestamp(now.timestamp() + 100)
    
    print(f"1. Writing NEWER event '{newer_event_id}' (status=active)...")
    repo.update_subscription(
        HARDWARE_ID,
        status='active',
        last_stripe_event_id=newer_event_id,
        last_stripe_event_at=newer_time
    )
    
    sub = repo.get_subscription(HARDWARE_ID)
    assert sub['status'] == 'active'
    
    # Old event (older time) -> Should be IGNORED
    older_event_id = "evt_older"
    older_time = datetime.fromtimestamp(now.timestamp() - 100)
    
    print(f"2. Writing OLDER event '{older_event_id}' (status=scammed)...")
    repo.update_subscription(
        HARDWARE_ID,
        status='scammed',
        last_stripe_event_id=older_event_id,
        last_stripe_event_at=older_time
    )
    
    sub = repo.get_subscription(HARDWARE_ID)
    print(f"   State: status={sub['status']}, event={sub['last_stripe_event_id']}")
    
    if sub['status'] == 'active':
        print("✅ SUCCESS: Update was ignored (Ordering)")
    else:
        print(f"❌ FAILED: Status changed to {sub['status']}")

    # 4. Test Email overwriting protection
    print("\n--- Test 3: Email Safety ---")
    
    print("1. Setting email to 'valid@email.com'...")
    repo.update_subscription(HARDWARE_ID, email='valid@email.com')
    
    sub = repo.get_subscription(HARDWARE_ID)
    assert sub['email'] == 'valid@email.com'
    
    print("2. Sending update with email=None...")
    repo.update_subscription(HARDWARE_ID, email=None)
    
    sub = repo.get_subscription(HARDWARE_ID)
    print(f"   State: email={sub['email']}")
    
    if sub['email'] == 'valid@email.com':
        print("✅ SUCCESS: Email was preserved")
    else:
        print(f"❌ FAILED: Email changed to {sub['email']}")

if __name__ == "__main__":
    main()
