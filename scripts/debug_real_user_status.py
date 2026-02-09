import asyncio
import os
import sys
import psycopg2
from psycopg2.extras import RealDictCursor
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    print("🚀 Debugging Real User Status (Direct Mode)...")
    
    # Path to server/server/config.env
    # Current script is in server/scripts/debug_real_user_status.py
    # we need server/server/config.env
    config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "server", "config.env")
    print(f"Loading config from: {config_path}")
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            for line in f:
                if '=' in line and not line.startswith('#'):
                    k, v = line.strip().split('=', 1)
                    os.environ[k] = v
    
    # DB Connection
    db_url = os.getenv('DATABASE_URL')
    if not db_url:
        host = os.getenv('DB_HOST', 'localhost')
        port = os.getenv('DB_PORT', '5432')
        name = os.getenv('DB_NAME', 'voice_assistant_db')
        user = os.getenv('DB_USER', 'postgres')
        password = os.getenv('DB_PASSWORD', '')
        db_url = f"postgresql://{user}:{password}@{host}:{port}/{name}"
    
    hardware_id = "manual-test-uuid-1234"
    
    print(f"🔍 Checking DB for hardware_id: {hardware_id}")
    
    try:
        conn = psycopg2.connect(db_url)
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM subscriptions WHERE hardware_id = %s", (hardware_id,))
            sub = cur.fetchone()
            
            if not sub:
                print("❌ No subscription record found in local DB!")
            else:
                print("✅ Found Local DB Record:")
                # Convert datetime objects to string for printing
                safe_sub = {k: str(v) if isinstance(v, datetime) else v for k,v in sub.items()}
                print(f"   Status: {safe_sub.get('status')}")
                print(f"   Stripe Customer ID: {safe_sub.get('stripe_customer_id')}")
                print(f"   Stripe Subscription ID: {safe_sub.get('stripe_subscription_id')}")
                print(f"   Email: {safe_sub.get('email')}")
                print(f"   Created At: {safe_sub.get('created_at')}")
                
                cid = safe_sub.get('stripe_customer_id')
                
    except Exception as e:
        print(f"❌ DB Error: {e}")
        return

    # Stripe Check
    if cid:
        print(f"\n🌍 Querying Stripe for Customer: {cid}...")
        try:
            import stripe
            stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
            if not stripe.api_key:
                print("❌ STRIPE_SECRET_KEY not found in env")
                return
            
            print(f"🔑 Using API Key: {stripe.api_key[:7]}...") # Show prefix to confirm Live/Test

            customer = stripe.Customer.retrieve(cid, expand=['subscriptions'])
            print(f"   Email: {customer.email}")
            print(f"   Created: {customer.created}")
            print(f"   Livemode: {customer.livemode}")
            
            subs = customer.subscriptions.data
            if not subs:
                print("   ⚠️  No active subscriptions found in Stripe for this customer.")
            else:
                for s in subs:
                    print(f"   ✅ Active Subscription: {s.id} | Status: {s.status}")
                    print(f"      Current Period End: {s.current_period_end}")
                    print(f"      Items: {[i.price.id for i in s.items.data]}")
        except Exception as e:
            print(f"❌ Stripe Error: {e}")
    else:
        print("❌ No Stripe Customer ID in local DB record.")

if __name__ == "__main__":
    asyncio.run(main())
