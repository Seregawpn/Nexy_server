import asyncio
import os
import psycopg2
from psycopg2.extras import RealDictCursor
import stripe
import logging

async def main():
    target_email = "Seregawpn@gmail.com"
    print(f"# 🔍 Searching for `{target_email}`\n")
    
    # 1. Parse config.env to get KEYS (both Live and Test)
    config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "server", "config.env")
    env_vars = {}
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line.lstrip().startswith('#'):
                     # Try to extract hidden keys
                     clean = line.lstrip().lstrip('#').strip()
                     if '=' in clean:
                         k, v = clean.split('=', 1)
                         if k.strip() in ['STRIPE_SECRET_KEY']:
                              env_vars[f"HIDDEN_{k.strip()}"] = v.strip()
                     continue
                
                if '=' in line:
                    k, v = line.split('=', 1)
                    env_vars[k] = v

    # DB Connection
    db_url = env_vars.get('DATABASE_URL')
    if not db_url:
        host = env_vars.get('DB_HOST', 'localhost')
        port = env_vars.get('DB_PORT', '5432')
        name = env_vars.get('DB_NAME', 'voice_assistant_db')
        user = env_vars.get('DB_USER', 'postgres')
        password = env_vars.get('DB_PASSWORD', '')
        db_url = f"postgresql://{user}:{password}@{host}:{port}/{name}"

    print("## 1. Local Database")
    try:
        conn = psycopg2.connect(db_url)
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT * FROM subscriptions WHERE email ILIKE %s", (target_email,))
            rows = cur.fetchall()
            if rows:
                for row in rows:
                    print(f"- ✅ Found: HW_ID=`{row['hardware_id']}` | Status=`{row['status']}`")
            else:
                print("- ❌ Not found in local DB")
    except Exception as e:
        print(f"- ⚠️ DB Error: {e}")

    # Stripe Search Helper
    def check_stripe(key, env_name):
        print(f"\n## 2. Stripe ({env_name})")
        if not key:
            print("- ❌ No API Key found")
            return
        
        try:
            stripe.api_key = key
            # List customers by email
            customers = stripe.Customer.list(email=target_email, limit=5, expand=['data.subscriptions'])
            if not customers.data:
                print(f"- ❌ No customers found with this email.")
            else:
                for c in customers.data:
                    print(f"- ✅ **Customer Found**: `{c.id}`")
                    print(f"  - Created: {c.created}")
                    print(f"  - Metadata: {c.metadata}")
                    if c.subscriptions.data:
                        for s in c.subscriptions.data:
                            print(f"  - 🟢 **Active Subscription**: `{s.id}` (Status: {s.status})")
                    else:
                        print(f"  - ⚪ No active subscriptions")
        except Exception as e:
            print(f"- ⚠️ Stripe Error: {e}")

    # Check TEST (Active)
    check_stripe(env_vars.get('STRIPE_SECRET_KEY'), "Active Config / TEST")
    
    # Check LIVE (Hidden/Commented) we need to find the sk_live key
    # It might be in env_vars under 'STRIPE_SECRET_KEY' if live is active, 
    # OR under 'HIDDEN_STRIPE_SECRET_KEY' if we parsed it from comments.
    
    live_key = None
    if env_vars.get('STRIPE_SECRET_KEY', '').startswith('sk_live'):
        live_key = env_vars.get('STRIPE_SECRET_KEY')
    elif env_vars.get('HIDDEN_STRIPE_SECRET_KEY', '').startswith('sk_live'):
        live_key = env_vars.get('HIDDEN_STRIPE_SECRET_KEY')
    
    # Try to find hardcoded fallback if parsing failed? 
    # No, assuming parsing worked.
    
    if live_key:
         check_stripe(live_key, "LIVE MODE")
    else:
         print("\n## 2b. Stripe (LIVE)")
         print("- ⚠️ Could not locate LIVE key to check.")

if __name__ == "__main__":
    asyncio.run(main())
