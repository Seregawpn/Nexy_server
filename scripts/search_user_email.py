import asyncio
import os
import sys
import psycopg2
from psycopg2.extras import RealDictCursor
import stripe
import logging

async def main():
    target_email = "Seregawpn@gmail.com"
    print(f"# 🔍 Searching for `{target_email}`\n")

    # Load centralized config owner (server/server/config/unified_config.py -> server/config.env)
    project_server_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, os.path.join(project_server_root, "server"))
    from config.unified_config import get_config  # pylint: disable=import-outside-toplevel

    subscription_cfg = get_config().subscription
    active_mode = subscription_cfg.stripe_mode

    # Parse config.env only for DB params and optional secondary Stripe checks.
    config_path = os.path.join(project_server_root, "config.env")
    env_vars = {}
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line.lstrip().startswith('#'):
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

    # Active mode from centralized config
    check_stripe(subscription_cfg.stripe_secret_key, f"Active Config / {active_mode.upper()}")

    # Optional secondary mode check from mode-specific keys
    if active_mode == "test":
        check_stripe(env_vars.get("STRIPE_LIVE_SECRET_KEY"), "LIVE MODE")
    else:
        check_stripe(env_vars.get("STRIPE_TEST_SECRET_KEY"), "TEST MODE")

if __name__ == "__main__":
    asyncio.run(main())
