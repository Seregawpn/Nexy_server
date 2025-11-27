from modules.action_errors.messages import (
    DEFAULT_APP_PLACEHOLDER,
    ActionErrorMessageResolver,
    resolver,
)


def test_resolver_returns_specific_message_for_known_code():
    message = resolver.resolve("app_not_found", "Slack")
    assert "Slack" in message
    assert "isn't installed" in message


def test_resolver_falls_back_to_placeholder_when_app_missing():
    message = resolver.resolve("app_not_found", None)
    assert DEFAULT_APP_PLACEHOLDER in message


def test_resolver_handles_unknown_code_with_fallback():
    message = resolver.resolve("unknown_error", "Safari")
    assert message == "I couldn't open Safari. Please try again."


def test_custom_resolver_allows_override_templates():
    custom = ActionErrorMessageResolver()
    message = custom.resolve("binary_missing", "Xcode")
    assert "system tool is missing" in message
