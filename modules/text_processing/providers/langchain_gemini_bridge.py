from __future__ import annotations

from typing import Any, Callable, Optional, Union


def extract_runtime_memory_context(raw_text: str) -> tuple[str, str]:
    """
    Split enriched text into runtime memory context and pure user input.
    Expected input format:
        MEMORY_CONTEXT:
        ...

        USER_INPUT:
        ...
    """
    text = str(raw_text or "")
    memory_marker = "MEMORY_CONTEXT:"
    user_marker = "USER_INPUT:"

    memory_pos = text.find(memory_marker)
    user_pos = text.find(user_marker)
    if memory_pos == -1 or user_pos == -1 or memory_pos > user_pos:
        return "", text

    after_memory = text[memory_pos + len(memory_marker):]
    memory_block, sep, user_block = after_memory.partition(user_marker)
    if not sep:
        return "", text

    runtime_memory_context = memory_block.strip()
    user_input = user_block.strip() or text
    return runtime_memory_context, user_input


def build_runtime_system_prompt(
    *,
    route: Optional[str],
    system_prompt_override: Optional[str],
    runtime_memory_context: Optional[str],
    resolve_system_prompt: Callable[[Optional[str], Optional[str]], str],
) -> str:
    try:
        system_prompt = resolve_system_prompt(
            route=route,
            system_prompt_override=system_prompt_override,
        )
    except TypeError:
        system_prompt = resolve_system_prompt(route, system_prompt_override)
    if runtime_memory_context:
        if system_prompt:
            system_prompt = (
                f"{system_prompt}\n\n"
                f"[Runtime Memory Context]\n{runtime_memory_context}"
            )
        else:
            system_prompt = f"[Runtime Memory Context]\n{runtime_memory_context}"
    return system_prompt


def build_text_user_content(
    *,
    clean_user_input: str,
    session_id: Optional[str],
) -> str:
    if session_id:
        return f"{clean_user_input}\n\n[System Context: session_id={session_id}]"
    return clean_user_input


def build_image_user_content(
    *,
    clean_user_input: str,
    session_id: Optional[str],
    image_mime_type: str,
    image_b64: str,
) -> list[dict[str, Any]]:
    return [
        {
            "type": "text",
            "text": build_text_user_content(
                clean_user_input=clean_user_input,
                session_id=session_id,
            ),
        },
        {
            "type": "image_url",
            "image_url": {
                "url": f"data:{image_mime_type};base64,{image_b64}"
            },
        },
    ]


def record_usage_if_available(
    *,
    token_usage_tracker: Any,
    accumulated_usage: Optional[dict[str, Any]],
    hardware_id: Optional[str],
    session_id: Optional[str],
    model_name: str,
) -> None:
    if not token_usage_tracker or not accumulated_usage:
        return

    target_id = hardware_id or "unknown"
    token_usage_tracker.record_usage(
        hardware_id=target_id,
        source="main_llm",
        input_tokens=accumulated_usage.get("input_tokens", 0),
        output_tokens=accumulated_usage.get("output_tokens", 0),
        session_id=session_id,
        model_name=model_name,
    )


def normalize_runtime_generation_inputs(
    *,
    user_input: str,
    runtime_memory_context: Optional[str],
) -> tuple[str, str, bool]:
    clean_user_input = user_input
    context = runtime_memory_context
    legacy_used = False
    if context is None:
        context, clean_user_input = extract_runtime_memory_context(user_input)
        legacy_used = bool(context)
    return clean_user_input, context or "", legacy_used
