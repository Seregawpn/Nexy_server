
import sys
import os
import time
import requests
import stripe
import json

# Config
BASE_URL = "http://localhost:8080"
# Key from config.env (must match what server loaded)
WEBHOOK_SECRET = "whsec_hTTXARzepf6XsWUJin2m7H3Iwb8Xtn97"

# Using stripe library from venv
        signature = stripe.WebhookSignature.generate_header(
            payload_str,
            WEBHOOK_SECRET,
            timestamp=timestamp
        )
        
        print("Sending valid webhook...")
        resp = requests.post(f"{BASE_URL}/webhook/stripe", data=payload_str, headers=headers)
        print(f"Response: {resp.status_code}")
        
        if resp.status_code == 200:
            print("✅ Valid webhook processed (200 OK)")
            return True
        else:
            print(f"❌ Failed: Valid webhook. Got {resp.status_code}")
            print(resp.text)
            return False

    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    success = run_test()
    sys.exit(0 if success else 1)
