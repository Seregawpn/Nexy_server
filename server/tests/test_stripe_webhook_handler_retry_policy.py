#!/usr/bin/env python3
import json
import sys
from pathlib import Path
from unittest.mock import AsyncMock

import pytest

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from api.webhooks import stripe_webhook as webhook_module


class _ReqStub:
    def __init__(self, payload: bytes, headers: dict[str, str] | None = None):
        self._payload = payload
        self.headers = headers or {}

    async def read(self) -> bytes:
        return self._payload


class _SubscriptionConfigStub:
    stripe_webhook_secret = "whsec_test"

    @staticmethod
    def is_active() -> bool:
        return True


class _ConfigStub:
    subscription = _SubscriptionConfigStub()


@pytest.mark.asyncio
async def test_webhook_returns_500_when_internal_processing_fails(monkeypatch):
    payload = b'{"id":"evt_test","type":"invoice.payment_succeeded","data":{"object":{}}}'
    request = _ReqStub(payload=payload, headers={"Stripe-Signature": "test"})

    monkeypatch.setattr("config.unified_config.get_config", lambda: _ConfigStub())
    monkeypatch.setattr("modules.subscription.get_subscription_module", lambda: None)
    monkeypatch.setattr(
        webhook_module,
        "_verify_and_construct_event",
        AsyncMock(
            return_value=json.loads(payload.decode("utf-8"))
        ),
    )
    monkeypatch.setattr(webhook_module, "_check_idempotency", AsyncMock(return_value=False))
    monkeypatch.setattr(
        webhook_module,
        "_process_event",
        AsyncMock(side_effect=RuntimeError("boom")),
    )

    response = await webhook_module.stripe_webhook_handler(request)  # type: ignore[arg-type]

    assert response.status == 500
