import asyncio
import os
import sys

# Setup server path
current_dir = os.path.dirname(os.path.abspath(__file__))
# /Users/sergiyzasorin/Fix_new/server
server_dir = os.path.dirname(current_dir) 
# /Users/sergiyzasorin/Fix_new/server/server
server_inner_dir = os.path.join(server_dir, "server")

sys.path.insert(0, server_dir)
sys.path.insert(0, server_inner_dir)

from server.modules.subscription.subscription_module import initialize_subscription_module, get_subscription_module
from server.config.unified_config import get_config

async def main():
    print("🚀 Injecting Test Subscription...")
    
    # Load config to ensure DB connection params are available
    get_config()
    
    # Initialize module (connecting to DB)
    module = await initialize_subscription_module()
    if not module:
        print("❌ Failed to initialize module")
        return

    hardware_id = "manual-test-uuid-1234"
    repo = module._repository
    
    # Check existing
    existing = repo.get_subscription(hardware_id)
    if existing:
        print(f"ℹ️ Found existing subscription: {existing}")
    
    # Upsert dummy subscription with a fake customer_id
    # We use a fake customer ID 'cus_test123' just to trick the logic into trying to open portal.
    # HOWEVER, Stripe API will reject 'cus_test123'. 
    # So this only verifies that our backend CORRECTLY calls Stripe.
    # To actually open the Stripe Portal, we need a REAL customer ID associated with the API Key.
    
    # Since we can't easily generate a real customer ID without calling Stripe API, 
    # we will rely on checkout flow first? No, user wants to see portal.
    
    # Better approach:
    # Use 'create_customer' from StripeService if available?
    
    stripe_service = module._stripe_service
    # Ensure API key is set for raw stripe calls
    import stripe
    stripe.api_key = stripe_service.api_key

    try:
        print("Creating real test customer in Stripe...")
        # Use wrapper method
        customer_data = stripe_service.create_customer(
            hardware_id=hardware_id,
            email="sergiy@test.com"
        )
        real_customer_id = customer_data['customer_id']
        print(f"✅ Created Stripe Customer: {real_customer_id}")

        # Create a Test Card Payment Method
        print("Attaching test card...")
        payment_method = stripe.PaymentMethod.create(
            type="card",
            card={"token": "tok_visa"}, # Use test token
        )
        
        # Attach to customer
        stripe.PaymentMethod.attach(
            payment_method.id,
            customer=real_customer_id,
        )
        
        # Set as default
        stripe.Customer.modify(
            real_customer_id,
            invoice_settings={"default_payment_method": payment_method.id},
        )
        print(f"✅ Attached PaymentMethod: {payment_method.id}")

        # Create a Subscription
        # We need a price ID. If not in env, create a test one.
        # Create a Subscription
        # Always create a fresh test price to avoid "No such price" errors from Live ID
        print("Creating test price...")
        product = stripe.Product.create(name="Nexy Premium Test")
        price = stripe.Price.create(
            unit_amount=2000,
            currency="usd",
            recurring={"interval": "month"},
            product=product.id,
        )
        price_id = price.id
        subscription = stripe.Subscription.create(
            customer=real_customer_id,
            items=[{"price": price_id}],
            metadata={"hardware_id": hardware_id}
        )
        real_subscription_id = subscription.id
        print(f"✅ Created Subscription: {real_subscription_id}")
        
        # Now save this to our DB
        print("Saving to local DB...")
        success = repo.create_or_update_subscription(
            hardware_id=hardware_id,
            status="paid", 
            stripe_customer_id=real_customer_id,
            stripe_subscription_id=real_subscription_id,
            email="sergiy@test.com"
        )
        if success:
            print("✅ DB Updated (UPSERT success).")
        else:
            print("❌ DB Update failed.")
        
    except Exception as e:
        print(f"❌ Error talking to Stripe: {e}")

if __name__ == "__main__":
    asyncio.run(main())
