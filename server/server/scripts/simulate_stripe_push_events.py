import requests
import time
import json
import hmac
import hashlib

# Config
URL_BASE = "http://localhost:8080"
import os
WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET", "whsec_4930ebc7d487722e8f36a42192f7375a3592047035372a52d6cf3bd0974a665d")

def send_event(event_type, description, status="active"):
    unique_id = int(time.time() * 1000)
    
    # Construct payload based on event type
    data_object = {
        "id": f"sub_test_{unique_id}",
        "object": "subscription",
        "status": status,
        "metadata": {
            "hardware_id": "test_hw_id_manual" 
        },
        "current_period_end": int(time.time()) + 86400 * 30, # +30 days
        "cancel_at_period_end": False
    }
    
    payload = {
        "id": f"evt_test_{unique_id}",
        "object": "event",
        "type": event_type,
        "created": int(time.time()),
        "data": {
            "object": data_object
        }
    }
    
    # Specific adjustments for invoice events
    if event_type.startswith("invoice."):
        payload["data"]["object"] = {
            "id": f"in_test_{unique_id}",
            "object": "invoice",
            "subscription": f"sub_test_{unique_id}",
            "payment_intent": f"pi_test_{unique_id}",
            "amount_paid": 2000,
            "currency": "usd",
            "status": "paid" if event_type == "invoice.payment_succeeded" else "open",
            "metadata": {
                "hardware_id": "test_hw_id_manual"
            }
        }

    payload_str = json.dumps(payload)
    
    # Signature
    timestamp = int(time.time())
    signed_payload = f"{timestamp}.{payload_str}"
    signature = hmac.new(
        WEBHOOK_SECRET.encode(),
        signed_payload.encode(),
        hashlib.sha256
    ).hexdigest()
    
    headers = {
        "Stripe-Signature": f"t={timestamp},v1={signature}",
        "Content-Type": "application/json"
    }
    
    print(f"🔹 Simulating Push: {description} ({event_type})...")
    try:
        resp = requests.post(f"{URL_BASE}/webhook/stripe", data=payload_str, headers=headers, timeout=5)
        print(f"Server Response: {resp.status_code}")
        try:
             print(f"Body: {resp.json()}")
        except:
             print(f"Body: {resp.text}")
    except Exception as e:
        print(f"❌ Connection failed: {e}")
    print("-" * 50)

if __name__ == "__main__":
    # 1. Simulate Invoice Payment Succeeded (Renewal)
    send_event("invoice.payment_succeeded", "✅ Monthly Payment Succeeded (Active)")
    time.sleep(1)
    
    # 2. Simulate Payment Failed
    send_event("invoice.payment_failed", "❌ Payment Failed (Billing Problem)")
    time.sleep(1)
    
    # 3. Simulate Subscription Updated (Back to Active)
    send_event("customer.subscription.updated", "🔄 User updated card (Back to Active)", status="active")
    time.sleep(1)
    
    # 4. Simulate Subscription Cancelled
    send_event("customer.subscription.deleted", "🗑️ Subscription Cancelled", status="canceled")
