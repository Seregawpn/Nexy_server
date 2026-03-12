from config.prompts import (
    PROMPT_PROFILE_ENV_VAR,
    build_intent_classifier_prompt,
    build_route_system_prompt,
)


def test_current_prompt_profile_is_default(monkeypatch):
    monkeypatch.delenv(PROMPT_PROFILE_ENV_VAR, raising=False)

    prompt = build_route_system_prompt("messages")

    assert "[Experimental Prompt Profile:" not in prompt


def test_experimental_prompt_profile_overlays_classifier(monkeypatch):
    monkeypatch.setenv(PROMPT_PROFILE_ENV_VAR, "experimental_v2")

    prompt = build_intent_classifier_prompt()

    assert "[Experimental Prompt Profile: experimental_v2 / classifier]" in prompt
    assert "Route by current user intent first" in prompt


def test_experimental_prompt_profile_overlays_route_section(monkeypatch):
    monkeypatch.setenv(PROMPT_PROFILE_ENV_VAR, "experimental_v2")

    prompt = build_route_system_prompt("messages")

    assert "[Experimental Prompt Profile: experimental_v2 / messages]" in prompt
    assert "On pivot from another task into messaging" in prompt
    assert "[Experimental Prompt Profile: experimental_v2 / header]" in prompt
