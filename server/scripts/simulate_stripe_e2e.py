#!/usr/bin/env python3
import sys
import os
import time
import subprocess
import requests
import stripe
import json
from pathlib import Path

# Config
HTTP_PORT = 8097
HOST = "localhost"
BASE_URL = f"http://{HOST}:{HTTP_PORT}"
WEBHOOK_SECRET = "whsec_test_secret_simulation"
GRPC_PORT = "50060"

def run_simulation():
    server_process = None
    try:
        print("🚀 Starting Stripe E2E Simulation...")
        
        # Paths
        server_dir = Path(__file__).parent.parent
        main_py = server_dir / "main.py"
        # Path determined from previous checks
        venv_site_packages = "/Users/sergiyzasorin/Fix_new/v1.0.6 Payment/mvp_tests/venv/lib/python3.13/site-packages"
        
        # Environment
        env = os.environ.copy()
        env["HTTP_PORT"] = str(HTTP_PORT)
        env["GRPC_PORT"] = GRPC_PORT
        env["SUBSCRIPTION_ENABLED"] = "true"
        env["STRIPE_MODE"] = "test"
        env["STRIPE_TEST_WEBHOOK_SECRET"] = WEBHOOK_SECRET
        
        # Use current python interpreter (system python)
        venv_python = sys.executable
        
        print(f"Starting server process using {venv_python}...")
        server_process = subprocess.Popen(
            [venv_python, str(main_py)],
            cwd=str(server_dir),
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Wait for startup
        print("Waiting for server startup (10s)...")
        start_time = time.time()
        connected = False
        while time.time() - start_time < 20:
             try:
                 requests.get(f"{BASE_URL}/health", timeout=1)
                 connected = True
                 break
             except:
                 time.sleep(1)
        
        if not connected:
             print("❌ Server failed to start")
             # Read stderr
             try:
                 out, err = server_process.communicate(timeout=1)
                 print(f"STDERR: {err}\nSTDOUT: {out}")
             except:
                 pass
             return False

        print("✅ Server started")
        
        # 1. Valid Request
        payload = {
            "id": "evt_test_simulated_1",
            "object": "event",
            "type": "checkout.session.completed",
            "data": {
                "object": {
                    "id": "cs_test_123",
                    "client_reference_id": "hw_test_e2e_sim",
                    "subscription": "sub_test_123",
                    "customer": "cus_test_123"
                }
            }
        }
        payload_str = json.dumps(payload)
        timestamp = int(time.time())
        signature = stripe.WebhookSignature.generate_header(
            payload_str,
            WEBHOOK_SECRET,
            timestamp=timestamp
        )
        
        headers = {
            "Stripe-Signature": signature,
            "Content-Type": "application/json"
        }
        
        print("Sending valid webhook...")
        resp = requests.post(f"{BASE_URL}/webhook/stripe", data=payload_str, headers=headers)
        print(f"Response: {resp.status_code}")
        
        if resp.status_code != 200:
            print(f"❌ Failed: Valid webhook check. Got {resp.status_code}, expected 200")
            print(resp.text)
            return False
            
        print("✅ Valid webhook processed (200 OK)")

        # 2. Idempotency (Duplicate)
        print("Sending duplicate webhook...")
        resp = requests.post(f"{BASE_URL}/webhook/stripe", data=payload_str, headers=headers)
        if resp.status_code == 200:
            print("✅ Duplicate webhook processed (200 OK - Idempotent)")
        else:
            print(f"❌ Idempotency check failed. Got {resp.status_code}")
            return False

        # 3. Invalid Signature
        print("Sending invalid signature...")
        headers["Stripe-Signature"] = "t=123,v1=invalid_sig"
        resp = requests.post(f"{BASE_URL}/webhook/stripe", data=payload_str, headers=headers)
        
        # The updated code returns None from verify -> 400 Bad Request
        if resp.status_code == 400:
            print("✅ Invalid signature rejected (400 Bad Request)")
        else:
             print(f"❌ Invalid signature check failed. Got {resp.status_code}")
             return False

        return True

    except Exception as e:
        print(f"❌ Error during simulation: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        if server_process:
            print("Stopping server...")
            server_process.terminate()
            try:
                server_process.wait(timeout=5)
            except:
                server_process.kill()

if __name__ == "__main__":
    success = run_simulation()
    sys.exit(0 if success else 1)
