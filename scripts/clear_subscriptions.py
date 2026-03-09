#!/usr/bin/env python3
import sys
import os
import logging

# Setup path to import modules
current_dir = os.path.dirname(os.path.abspath(__file__))
server_root = os.path.dirname(os.path.dirname(current_dir)) # Fix_new/server
server_app = os.path.join(server_root, 'server') # Fix_new/server/server
sys.path.append(server_app)

from modules.subscription.repository.subscription_repository import SubscriptionRepository

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ClearSubscriptions")

def clear_data():
    print("🧹 Clearing subscription data...")
    repo = SubscriptionRepository()
    conn = repo._get_connection()
    try:
        with conn.cursor() as cur:
            # 1. Clear payments
            cur.execute("DELETE FROM payments")
            payments_count = cur.rowcount
            print(f"   - Deleted {payments_count} payments")

            # 2. Clear subscription events
            cur.execute("DELETE FROM subscription_events")
            events_count = cur.rowcount
            print(f"   - Deleted {events_count} subscription events")

            # 3. Clear subscriptions
            cur.execute("DELETE FROM subscriptions")
            subs_count = cur.rowcount
            print(f"   - Deleted {subs_count} subscriptions")
            
            conn.commit()
            print("✅ Database cleared successfully.")
            return True
    except Exception as e:
        print(f"❌ Error clearing database: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

if __name__ == "__main__":
    confirm = input("⚠️  Are you sure you want to DELETE ALL subscription data? (y/N): ")
    if confirm.lower() == 'y':
        success = clear_data()
        sys.exit(0 if success else 1)
    else:
        print("Cancelled.")
        sys.exit(0)
