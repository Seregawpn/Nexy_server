#!/usr/bin/env python3
import sys
from pathlib import Path

import pytest

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from api.webhooks import stripe_webhook as webhook_module


class _ReqStub:
    def __init__(self, headers: dict[str, str] | None = None):
        self.headers = headers or {}


class _CfgStub:
    stripe_webhook_secret = "whsec_cfg"


def test_collect_webhook_secrets_merges_sources(monkeypatch):
    monkeypatch.setenv("STRIPE_WEBHOOK_SECRETS", "whsec_shared_1,whsec_shared_2")
    monkeypatch.setenv("STRIPE_TEST_WEBHOOK_SECRET", "whsec_test")
    monkeypatch.setenv("STRIPE_LIVE_WEBHOOK_SECRET", "whsec_live")
    monkeypatch.setenv("STRIPE_WEBHOOK_SECRET_STAGING", "whsec_staging")

    req = _ReqStub(headers={"X-Nexy-Webhook-Source": "staging"})
    secrets = webhook_module._collect_webhook_secrets(config=_CfgStub(), request=req)

    assert secrets == (
        "whsec_staging",
        "whsec_cfg",
        "whsec_shared_1",
        "whsec_shared_2",
        "whsec_test",
        "whsec_live",
    )


@pytest.mark.asyncio
async def test_verify_and_construct_event_accepts_any_configured_secret(monkeypatch):
    class _FakeSigError(Exception):
        pass

    class _FakeWebhook:
        @staticmethod
        def construct_event(payload, sig_header, secret):
            if secret != "whsec_ok":
                raise _FakeSigError("bad signature")
            return {"id": "evt_ok", "type": "invoice.payment_succeeded"}

    class _FakeStripe:
        class error:  # noqa: D401 - compatibility shim for stripe_lib.error
            SignatureVerificationError = _FakeSigError

        Webhook = _FakeWebhook

    monkeypatch.setattr(webhook_module, "stripe_lib", _FakeStripe)

    event = await webhook_module._verify_and_construct_event(
        payload=b'{"id":"evt_ok"}',
        sig_header="t=1,v1=fake",
        webhook_secrets=("whsec_bad", "whsec_ok"),
    )
    assert event is not None
    assert event["id"] == "evt_ok"
