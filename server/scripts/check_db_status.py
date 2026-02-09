#!/usr/bin/env python3
import sys
import os
import logging
from pprint import pprint

# Setup path
current_dir = os.path.dirname(os.path.abspath(__file__))
server_root = os.path.dirname(os.path.dirname(current_dir))
server_app = os.path.join(server_root, 'server')
sys.path.append(server_app)

from modules.subscription.repository.subscription_repository import SubscriptionRepository

def check_status():
    print("🔍 Checking Subscription Status in DB...")
    repo = SubscriptionRepository()
    conn = repo._get_connection()
    try:
        with conn.cursor() as cur:
            # Get all subscriptions
            cur.execute("SELECT hardware_id, status, stripe_customer_id, updated_at FROM subscriptions")
            rows = cur.fetchall()
            
            if not rows:
                print("❌ No subscriptions found.")
                return False
                
            print(f"found {len(rows)} subscriptions:")
            has_paid = False
            for row in rows:
                print(f" - HardwareID: {row[0]}, Status: {row[1]}, CustomerID: {row[2]}, Updated: {row[3]}")
                if row[1] in ['paid', 'paid_trial']:
                    has_paid = True
            
            if has_paid:
                print("\n✅ SUCCESS: Found at least one 'paid' subscription!")
                return True
            else:
                print("\n⚠️ WARNING: No 'paid' subscriptions found yet.")
                return False
    finally:
        conn.close()

if __name__ == "__main__":
    check_status()
