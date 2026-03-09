from __future__ import annotations

from datetime import datetime, timedelta
from typing import Any, Callable, Optional, Tuple


def resolve_gate_bucket(
    *,
    memory_module: Any,
    user_input: Optional[str],
    apply_medium_gate: bool,
) -> str:
    if not apply_medium_gate:
        return "all"
    manager = None
    getter = getattr(memory_module, "get_manager", None)
    if callable(getter):
        manager = getter()
    gate_fn = getattr(manager, "should_include_medium_term", None)
    if callable(gate_fn):
        try:
            include_medium, _ = gate_fn(user_input)
            return "medium" if include_medium else "no_medium"
        except Exception:
            return "no_medium"
    return "no_medium"


def build_variant_key(
    *,
    hardware_id: str,
    memory_module: Any,
    user_input: Optional[str],
    apply_medium_gate: bool,
) -> Tuple[str, str]:
    return (
        str(hardware_id),
        resolve_gate_bucket(
            memory_module=memory_module,
            user_input=user_input,
            apply_medium_gate=apply_medium_gate,
        ),
    )


def get_cache_state(
    *,
    cache_entry: Optional[dict[str, Any]],
    now: datetime,
    cache_ttl: int,
    cache_hard_ttl: int,
) -> tuple[Optional[dict[str, Any]], bool, bool]:
    if not cache_entry:
        return None, False, False
    cache_time = cache_entry.get("timestamp")
    context = cache_entry.get("context")
    if not cache_time:
        return context, False, False

    cache_age = now - cache_time
    age_seconds = cache_age.total_seconds()
    is_stale = age_seconds > cache_ttl
    is_hard_expired = age_seconds > cache_hard_ttl
    return context, is_stale, is_hard_expired


def is_cache_hard_expired(
    *,
    cache_entry: Optional[dict[str, Any]],
    now: datetime,
    cache_hard_ttl: int,
) -> bool:
    if not cache_entry:
        return True
    cache_time = cache_entry.get("timestamp")
    if not cache_time:
        return False
    return (now - cache_time) > timedelta(seconds=cache_hard_ttl)


def build_cache_write_entries(
    *,
    hardware_id: str,
    memory_module: Any,
    memory_context: dict[str, Any],
    now: datetime,
    apply_medium_gate: Optional[bool],
    strip_medium_term: Callable[[dict[str, Any]], dict[str, Any]],
) -> dict[Tuple[str, str], dict[str, Any]]:
    if apply_medium_gate is None:
        return {
            build_variant_key(
                hardware_id=hardware_id,
                memory_module=memory_module,
                user_input=None,
                apply_medium_gate=False,
            ): {"context": dict(memory_context), "timestamp": now},
            build_variant_key(
                hardware_id=hardware_id,
                memory_module=memory_module,
                user_input=None,
                apply_medium_gate=True,
            ): {"context": strip_medium_term(memory_context), "timestamp": now},
        }

    return {
        build_variant_key(
            hardware_id=hardware_id,
            memory_module=memory_module,
            user_input=None,
            apply_medium_gate=apply_medium_gate,
        ): {"context": memory_context, "timestamp": now}
    }


def get_refresh_delay_sec(*, cache_ttl: int, cache_refresh_before_expiry: int) -> int:
    return max(0, cache_ttl - cache_refresh_before_expiry)
