import asyncio
import os
import psycopg2
from psycopg2.extras import RealDictCursor
import logging

async def main():
    print("# 📊 User Data Audit\n")
    
    # Load Config (manual)
    config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "server", "config.env")
    env_vars = {}
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            for line in f:
                if '=' in line and not line.startswith('#'):
                    k, v = line.strip().split('=', 1)
                    env_vars[k] = v
                    os.environ[k] = v
    
    db_url = os.getenv('DATABASE_URL')
    if not db_url:
        host = os.getenv('DB_HOST', 'localhost')
        port = os.getenv('DB_PORT', '5432')
        name = os.getenv('DB_NAME', 'voice_assistant_db')
        user = os.getenv('DB_USER', 'postgres')
        password = os.getenv('DB_PASSWORD', '')
        db_url = f"postgresql://{user}:{password}@{host}:{port}/{name}"

    # IDs to check
    targets = [
        ("Real User", "E03D2455-8EF1-5270-AA03-13B5771C7CB2"),
        ("Test User", "manual-test-uuid-1234")
    ]

    try:
        conn = psycopg2.connect(db_url)
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            for label, hw_id in targets:
                print(f"## Checking {label} (`{hw_id[:8]}...`)")
                cur.execute("SELECT * FROM subscriptions WHERE hardware_id = %s", (hw_id,))
                sub = cur.fetchone()
                
                if not sub:
                    print("- ❌ **ID in DB**: NO")
                    print("- ❌ **Email**: N/A")
                    print("- ❌ **Stripe Linked**: N/A")
                    print("- ❌ **Payment Status**: N/A")
                else:
                    print("- ✅ **ID in DB**: YES")
                    
                    email = sub.get('email')
                    if email:
                        print(f"- ✅ **Email**: YES (`{email}`)")
                    else:
                        print("- ❌ **Email**: NO (None)")
                        
                    cust_id = sub.get('stripe_customer_id')
                    if cust_id:
                        print(f"- ✅ **Stripe Linked**: YES (`{cust_id}`)")
                    else:
                        print("- ❌ **Stripe Linked**: NO")
                        
                    status = sub.get('status')
                    print(f"- ℹ️  **DB Status**: {status}")
                    
                    # Check connection to current Payment System (Test Mode check)
                    is_live_id = cust_id and not cust_id.startswith('cus_test') # Heuristic
                    current_mode = "TEST" if os.getenv('STRIPE_SECRET_KEY','').startswith('sk_test') else "LIVE"
                    
                    print(f"- ℹ️  **Payment System Mode**: {current_mode}")
                    
                    if current_mode == "TEST" and cust_id:
                        # Try to query if it's a test ID
                        try:
                            import stripe
                            stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
                            c = stripe.Customer.retrieve(cust_id)
                            has_subs = c.subscriptions.total_count > 0 if c.subscriptions else False
                            print(f"- ✅ **Payment Verified (Stripe)**: {'YES' if has_subs else 'NO (No Active Subs)'}")
                        except Exception as e:
                             print(f"- ⚠️  **Payment Verification Failed**: {str(e).splitlines()[0]}")
                             if "No such customer" in str(e):
                                 print("  -> Likely mismatched modes (Live ID vs Test Key)")

                print("")
                
    except Exception as e:
        print(f"❌ Database Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
