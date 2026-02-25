#!/usr/bin/env python3
"""
Smoke test для проверки инициализации SubscriptionModule и Webhook.
Запускает сервер в отдельном процессе, проверяет endpoints, затем убивает процесс.
"""

import sys
import os
import time
import subprocess
import requests
import signal
from pathlib import Path

# Config
HTTP_PORT = 8090
HOST = "localhost"
BASE_URL = f"http://{HOST}:{HTTP_PORT}"

def run_smoke_test():
    server_process = None
    try:
        print("🚀 Starting Server Smoke Test...")
        
        # Paths
        server_dir = Path(__file__).parent.parent
        main_py = server_dir / "main.py"
        
        # Environment
        env = os.environ.copy()
        env["HTTP_PORT"] = str(HTTP_PORT)
        # Use custom GRPC port to avoid conflicts
        env["GRPC_PORT"] = "50056" 
        # Включаем subscription module явно
        env["SUBSCRIPTION_ENABLED"] = "true"
        # Для теста можно использовать mock ключи, если они не заданы в .env
        if "STRIPE_SECRET_KEY" not in env:
            env["STRIPE_SECRET_KEY"] = "sk_test_mock"
        if "STRIPE_WEBHOOK_SECRET" not in env:
            env["STRIPE_WEBHOOK_SECRET"] = "whsec_mock"
            
        print(f"Starting server process: python3 {main_py}")
        server_process = subprocess.Popen(
            ["python3", str(main_py)],
            cwd=str(server_dir),
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Wait for startup
        print("Waiting for server startup (10s)...")
        # Poll /health endpoint
        start_time = time.time()
        connected = False
        while time.time() - start_time < 20:
            try:
                resp = requests.get(f"{BASE_URL}/health", timeout=1)
                if resp.status_code == 200:
                    connected = True
                    print("✅ /health check passed")
                    break
            except requests.ConnectionError:
                time.sleep(1)
                
        if not connected:
            print("❌ Server failed to start or /health not accessible")
            # Try to read stderr
            try:
                outs, errs = server_process.communicate(timeout=1)
                print(f"Server STDERR:\n{errs}")
            except:
                pass
            return False
            
        # Test Subscription Endpoints
        print("Checking /webhook/stripe access...")
        try:
            # Expecting 400 because of missing signature header or invalid signature
            resp = requests.post(f"{BASE_URL}/webhook/stripe", json={}, timeout=2)
            print(f"Response code: {resp.status_code}")
            print(f"Response text: {resp.text}")
            
            if resp.status_code == 400:
                print("✅ /webhook/stripe returned 400 (Expected Bad Request/Invalid Signature)")
            else:
                print(f"❌ /webhook/stripe returned unexpected code: {resp.status_code}")
                return False
                
        except Exception as e:
            print(f"❌ Error accessing webhook: {e}")
            return False
            
        # Optional: Check /status if it exposes module info (usually it doesn't expose internal modules list explicitly unless modified)
        
        print("\n✅ smoke test passed!")
        return True
        
    except Exception as e:
        print(f"\n❌ Test failed with exception: {e}")
        return False
        
    finally:
        if server_process:
            print("Stopping server process...")
            server_process.terminate()
            try:
                server_process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                server_process.kill()
            print("Server stopped.")

if __name__ == "__main__":
    success = run_smoke_test()
    sys.exit(0 if success else 1)
