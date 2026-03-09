from datetime import datetime, timedelta

from integrations.workflow_integrations.memory_cache_bridge import (
    build_cache_write_entries,
    build_variant_key,
    get_cache_state,
    get_refresh_delay_sec,
)


class _MemoryModuleWithGate:
    def get_manager(self):
        class _Manager:
            def should_include_medium_term(self, user_input):
                return ("weather" not in (user_input or "").lower(), "heuristic")

        return _Manager()


def test_build_variant_key_respects_gate_bucket() -> None:
    module = _MemoryModuleWithGate()

    regular = build_variant_key(
        hardware_id="hw-1",
        memory_module=module,
        user_input="What is the weather today?",
        apply_medium_gate=True,
    )
    full = build_variant_key(
        hardware_id="hw-1",
        memory_module=module,
        user_input="Summarize my longer-term projects",
        apply_medium_gate=True,
    )
    all_bucket = build_variant_key(
        hardware_id="hw-1",
        memory_module=module,
        user_input=None,
        apply_medium_gate=False,
    )

    assert regular == ("hw-1", "no_medium")
    assert full == ("hw-1", "medium")
    assert all_bucket == ("hw-1", "all")


def test_get_cache_state_reports_stale_and_hard_expired() -> None:
    now = datetime.now()
    context, is_stale, is_hard_expired = get_cache_state(
        cache_entry={
            "context": {"short_term_context": "x"},
            "timestamp": now - timedelta(seconds=700),
        },
        now=now,
        cache_ttl=600,
        cache_hard_ttl=86400,
    )

    assert context == {"short_term_context": "x"}
    assert is_stale is True
    assert is_hard_expired is False


def test_build_cache_write_entries_keeps_medium_hidden_for_gated_bucket() -> None:
    module = object()
    now = datetime.now()

    entries = build_cache_write_entries(
        hardware_id="hw-fast",
        memory_module=module,
        memory_context={
            "short_term_context": "recent",
            "medium_term_context": "hidden",
            "factual_long_term_context": "fact",
        },
        now=now,
        apply_medium_gate=None,
        strip_medium_term=lambda ctx: {**ctx, "medium_term_context": ""},
    )

    assert entries[("hw-fast", "all")]["context"]["medium_term_context"] == "hidden"
    assert entries[("hw-fast", "no_medium")]["context"]["medium_term_context"] == ""


def test_get_refresh_delay_sec_never_returns_negative_value() -> None:
    assert get_refresh_delay_sec(cache_ttl=600, cache_refresh_before_expiry=30) == 570
    assert get_refresh_delay_sec(cache_ttl=10, cache_refresh_before_expiry=30) == 0
