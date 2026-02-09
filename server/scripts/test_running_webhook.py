#!/usr/bin/env python3
import hashlib
import hmac
import json
import sys
import time

import requests

BASE_URL = "http://localhost:8080"
WEBHOOK_SECRET = "whsec_hTTXARzepf6XsWUJin2m7H3Iwb8Xtn97"


def _build_signature_header(payload: str, secret: str, timestamp: int) -> str:
    signed_payload = f"{timestamp}.{payload}".encode("utf-8")
    signature = hmac.new(secret.encode("utf-8"), signed_payload, hashlib.sha256).hexdigest()
    return f"t={timestamp},v1={signature}"


def run_test() -> bool:
    try:
        payload = {
            "id": f"evt_manual_{int(time.time())}",
            "object": "event",
            "type": "checkout.session.completed",
            "created": int(time.time()),
            "data": {
                "object": {
                    "id": "cs_manual_test",
                    "object": "checkout.session",
                    "mode": "subscription",
                    "payment_status": "paid",
                    "customer": "cus_manual_test",
                    "subscription": "sub_manual_test",
                    "metadata": {"hardware_id": "test_hw_id_manual"},
                }
            },
        }
        payload_str = json.dumps(payload)
        timestamp = int(time.time())
        signature_header = _build_signature_header(payload_str, WEBHOOK_SECRET, timestamp)
        headers = {
            "Content-Type": "application/json",
            "Stripe-Signature": signature_header,
        }

        print("Sending webhook request...")
        resp = requests.post(
            f"{BASE_URL}/webhook/stripe",
            data=payload_str.encode("utf-8"),
            headers=headers,
            timeout=10,
        )
        print(f"Response: {resp.status_code}")
        print(resp.text)
        return resp.status_code == 200
    except Exception as exc:
        print(f"Webhook test failed: {exc}")
        return False


if __name__ == "__main__":
    raise SystemExit(0 if run_test() else 1)
