#!/usr/bin/env python3
import stripe
import sys

# Using the TEST key found in config.env comments because the session ID is cs_test_...
TEST_KEY = "sk_test_51SfCTCGo52EfFi5Vz4gnYlHWLnkJfqj2uAfXookkeRM08o3H3BvijyQHg9yPlLKIHugjOMeXVFrdG2r36n0wHNjw00e9sZwIDi"
SESSION_ID = "cs_test_a1T4aLCCzMIVHo9AHAp9ZTSNRs7cUfmCqBI4We2Ksr9DKBMlHSfFN3iork"

def verify_session():
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
