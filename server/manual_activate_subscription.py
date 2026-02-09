#!/usr/bin/env python3
import sys
import os

# Add server directory to python path
current_dir = os.path.dirname(os.path.abspath(__file__))
server_dir = os.path.join(current_dir, 'server')
sys.path.append(server_dir)

from server.modules.subscription.repository.subscription_repository import SubscriptionRepository

HARDWARE_ID = "E03D2455-8EF1-5270-AA03-13B5771C7CB2"

def main():
    print(f"Connecting to DB and updating for hardware_id: {HARDWARE_ID}...")
    
    try:
        repo = SubscriptionRepository()
        
        # Check current
        sub = repo.get_subscription(HARDWARE_ID)
        print(f"Current subscription state: {sub}")
        
        # Update
        print("Updating status to 'paid', stripe_status to 'active', and email to 'test@example.com'...")
        repo.update_subscription(
            HARDWARE_ID, 
            status='paid', 
            stripe_status='active',
            email='test@example.com'
        )
        
        # Verify
        sub = repo.get_subscription(HARDWARE_ID)
        print(f"New subscription state: {sub}")
        print("✅ Subscription manually activated!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
