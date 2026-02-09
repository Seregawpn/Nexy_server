import requests
import time
import stripe
import json

# Config
BASE_URL = "http://localhost:8097" # Using 8097 based on simulate_stripe_e2e.py config
# Wait, simulate_stripe_e2e.py had HTTP_PORT = 8097 but server config usually is 8080.
# Let's check config.env again. It said HTTP_PORT=auto (default 8080).
# simulate_stripe_e2e.py sets env["HTTP_PORT"] = str(HTTP_PORT) # 8097
# So the script was trying to start on 8097.
# IF the user started the server manually, it's likely on 8080.
# I should try 8080.

URLS = ["http://localhost:8080", "http://127.0.0.1:8080"]
WEBHOOK_SECRET = "whsec_test_secret_simulation"
# Need to check if config.env has this secret. 
# The user's config.env has STRIPE_WEBHOOK_SECRET=whsec_hTTXARzepf6XsWUJin2m7H3Iwb8Xtn97

REAL_SECRET = "whsec_4930ebc7d487722e8f36a42192f7375a3592047035372a52d6cf3bd0974a665d"

def send_webhook():
    unique_id = int(time.time())
    payload = {
        "id": f"evt_test_manual_verify_{unique_id}",
        "object": "event",
        "type": "checkout.session.completed", # Use a valid event type
        # Or "invoice.payment_succeeded"
        "data": {
            "object": {
                "id": "cs_test_manual_1",
                "client_reference_id": "test_hw_id_manual", # Use a recognizable HWID
                "subscription": "sub_test_manual",
                "customer": "cus_test_manual",
                "metadata": {
                    "hardware_id": "test_hw_id_manual"
                }
            }
        }
    }
    payload_str = json.dumps(payload)
    timestamp = int(time.time())
    
    # Manual signature generation
    import hmac
    import hashlib
    
    timestamp = int(time.time())
    signed_payload = f"{timestamp}.{payload_str}"
    signature = hmac.new(
        REAL_SECRET.encode(),
        signed_payload.encode(),
        hashlib.sha256
    ).hexdigest()
    
    # Format: t=timestamp,v1=signature
    signature_header = f"t={timestamp},v1={signature}"
    
    headers = {
        "Stripe-Signature": signature_header,
        "Content-Type": "application/json"
    }
    
    for base in URLS:
        try:
            print(f"Trying {base}/webhook/stripe...")
            resp = requests.post(f"{base}/webhook/stripe", data=payload_str, headers=headers, timeout=5)
            print(f"Response: {resp.status_code}")
            print(resp.text)
            if resp.status_code == 200:
                print("✅ Success!")
                return
        except Exception as e:
            print(f"Failed to connect to {base}: {e}")

if __name__ == "__main__":
    send_webhook()
