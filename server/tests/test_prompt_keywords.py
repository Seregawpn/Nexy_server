import os
import sys
from pathlib import Path

import yaml

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from config import prompts


def _reset_keyword_cache() -> None:
    prompts._KEYWORD_CACHE = {}
    prompts._KEYWORD_CACHE_PATH = ""


def test_load_prompt_keywords_from_yaml(monkeypatch, tmp_path):
    data = {
        "system_control": ["Open", "Close"],
        "messages": ["Read Messages"],
        "web_search": ["Price"],
    }
    path = tmp_path / "intent_keywords.yaml"
    path.write_text(yaml.safe_dump(data), encoding="utf-8")

    monkeypatch.setenv("PROMPT_KEYWORDS_PATH", str(path))
    _reset_keyword_cache()

    keywords = prompts.load_prompt_keywords()

    assert keywords["system_control"] == ["open", "close"]
    assert "read messages" in keywords["messages"]
    assert keywords["web_search"] == ["price"]


def test_load_prompt_keywords_fallback(monkeypatch):
    monkeypatch.setenv("PROMPT_KEYWORDS_PATH", "/tmp/does_not_exist.yaml")
    _reset_keyword_cache()

    keywords = prompts.load_prompt_keywords()

    assert "open" in keywords["system_control"]


def test_resolve_prompt_sections(monkeypatch, tmp_path):
    data = {
        "system_control": ["open"],
        "messages": ["read messages"],
        "web_search": ["price"],
    }
    path = tmp_path / "intent_keywords.yaml"
    path.write_text(yaml.safe_dump(data), encoding="utf-8")

    monkeypatch.setenv("PROMPT_KEYWORDS_PATH", str(path))
    _reset_keyword_cache()

    result = prompts.resolve_prompt_sections("Please open Safari and read messages about price.")

    assert result["system_control"] is True
    assert result["messages"] is True
    assert result["web_search"] is True
    assert result["whatsapp"] is False
    assert result["browser"] is False
    assert result["payment"] is False
    assert result["describe"] is False


def test_resolve_prompt_sections_weather_english(monkeypatch):
    monkeypatch.setenv("PROMPT_KEYWORDS_PATH", "/tmp/does_not_exist.yaml")
    _reset_keyword_cache()

    for text in [
        "What is the weather in Montreal today?",
        "Will it rain in Montreal now?",
        "What's the temperature outside in Montreal?",
        "Current humidity and wind in Montreal",
    ]:
        result = prompts.resolve_prompt_sections(text)
        assert result["web_search"] is True, text


def test_system_prompt_contains_short_chat_history_policy():
    prompt_text = prompts.build_system_prompt(web_search_enabled=True)
    assert "short chat history" in prompt_text
    assert "Do not ask again for details that are already present" in prompt_text


def test_system_prompt_contract_session_id_and_websearch_length_rules():
    prompt_text = prompts.build_system_prompt(web_search_enabled=True, browser_enabled=True, messages_enabled=True)
    assert "{\"session_id\": \"<from request>\", \"text\": \"Hello\"}" in prompt_text
    assert "Up to 3 short factual sentences total" in prompt_text
    assert "First sentence must answer the question directly" in prompt_text


def test_system_prompt_has_no_forced_browser_for_any_open_website_phrase():
    prompt_text = prompts.build_system_prompt(web_search_enabled=True, browser_enabled=True)
    assert "ALWAYS a browser_use command" not in prompt_text
    assert "interactive website task" in prompt_text


def test_system_prompt_is_english_only_for_messages_examples():
    prompt_text = prompts.build_system_prompt(messages_enabled=True)
    assert "напиши" not in prompt_text
    assert "найди контакт" not in prompt_text
