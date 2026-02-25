#!/usr/bin/env python3
import os
import stripe

TEST_KEY = os.getenv("STRIPE_TEST_SECRET_KEY", "").strip()
SESSION_ID = os.getenv("STRIPE_SESSION_ID", "").strip()

def verify_session():
    if not TEST_KEY:
        print("❌ Missing STRIPE_TEST_SECRET_KEY")
        return
    if not SESSION_ID:
        print("❌ Missing STRIPE_SESSION_ID")
        return

    stripe.api_key = TEST_KEY
    
    print(f"Querying Stripe for Session ID: {SESSION_ID}")
    try:
        session = stripe.checkout.Session.retrieve(SESSION_ID)
        print("\n✅ Session Found!")
        print(f"Status: {session.status}")
        print(f"Payment Status: {session.payment_status}")
        print(f"Customer Email: {session.customer_details.email if session.customer_details else 'N/A'}")
        print(f"Amount Total: {session.amount_total}")
        
        if session.payment_status == 'paid':
            print("\n🎉 Payment was successful on Stripe side!")
        else:
            print(f"\n⚠️ Payment not paid. Status: {session.payment_status}")
            
    except Exception as e:
        print(f"\n❌ Error querying Stripe: {e}")

if __name__ == "__main__":
    verify_session()
