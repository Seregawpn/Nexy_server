#!/usr/bin/env python3
import sys
import os
import argparse

# Add server directory to python path
current_dir = os.path.dirname(os.path.abspath(__file__))
server_dir = os.path.join(current_dir, 'server')
sys.path.append(server_dir)

from server.modules.subscription.repository.subscription_repository import SubscriptionRepository

HARDWARE_ID = "E03D2455-8EF1-5270-AA03-13B5771C7CB2"

def _parse_args():
    parser = argparse.ArgumentParser(description="Manual subscription activation (destructive admin utility).")
    parser.add_argument(
        "--allow-update",
        action="store_true",
        help="Required flag to allow manual DB status update."
    )
    parser.add_argument(
        "--hardware-id",
        default=HARDWARE_ID,
        help="Target hardware_id."
    )
    parser.add_argument(
        "--email",
        default="test@example.com",
        help="Email to write into subscription row."
    )
    return parser.parse_args()


def _require_confirmation(args):
    if not args.allow_update:
        raise RuntimeError("Blocked: pass --allow-update to run this admin mutation.")

    confirm_token = os.getenv("NEXY_CONFIRM_DESTRUCTIVE", "")
    if confirm_token != "YES":
        raise RuntimeError("Blocked: set NEXY_CONFIRM_DESTRUCTIVE=YES.")

    env_name = os.getenv("NEXY_ENV", "").lower()
    if env_name == "production":
        raise RuntimeError("Blocked in production environment (NEXY_ENV=production).")


def main():
    args = _parse_args()
    _require_confirmation(args)
    hardware_id = args.hardware_id
    email = args.email

    print(f"Connecting to DB and updating for hardware_id: {hardware_id}...")
    
    try:
        repo = SubscriptionRepository()
        
        # Check current
        sub = repo.get_subscription(hardware_id)
        print(f"Current subscription state: {sub}")
        
        # Update
        print(f"Updating status to 'paid', stripe_status to 'active', and email to '{email}'...")
        repo.update_subscription(
            hardware_id, 
            status='paid', 
            stripe_status='active',
            email=email
        )
        
        # Verify
        sub = repo.get_subscription(hardware_id)
        print(f"New subscription state: {sub}")
        print("✅ Subscription manually activated!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
