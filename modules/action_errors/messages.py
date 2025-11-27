"""
Utility helpers for mapping action executor error codes to user-facing speech text.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional

DEFAULT_APP_PLACEHOLDER = "the requested application"


@dataclass(frozen=True)
class ActionErrorMessageTemplate:
    """Container for formatting user-facing speech text."""

    template: str

    def format(self, app_name: Optional[str]) -> str:
        name = (app_name or "").strip()
        return self.template.format(app=name or DEFAULT_APP_PLACEHOLDER)


class ActionErrorMessageResolver:
    """Maps executor error codes to consistent speech-friendly text."""

    def __init__(self) -> None:
        self._templates: Dict[str, ActionErrorMessageTemplate] = {
            "app_not_found": ActionErrorMessageTemplate(
                "The app {app} isn't installed on this Mac."
            ),
            "not_allowed": ActionErrorMessageTemplate(
                "Opening {app} is blocked by security settings."
            ),
            "disabled": ActionErrorMessageTemplate(
                "App launching is currently disabled. Please enable it in settings first."
            ),
            "executions_disabled": ActionErrorMessageTemplate(
                "App launching is currently disabled. Please enable it in settings first."
            ),
            "timeout": ActionErrorMessageTemplate(
                "I couldn't open {app} because the request timed out. Please try again."
            ),
            "command_failed": ActionErrorMessageTemplate(
                "I couldn't open {app} because of a system error. Please try again."
            ),
            "spawn_failed": ActionErrorMessageTemplate(
                "I couldn't open {app} because of a system error. Please try again."
            ),
            "binary_missing": ActionErrorMessageTemplate(
                "I couldn't open {app} because a required system tool is missing."
            ),
            "invalid_payload": ActionErrorMessageTemplate(
                "I couldn't understand which app to open. Please repeat the name."
            ),
            "unsupported_action": ActionErrorMessageTemplate(
                "This action isn't supported yet."
            ),
            "fallback": ActionErrorMessageTemplate(
                "I couldn't open {app}. Please try again."
            ),
        }

    def resolve(self, error_code: Optional[str], app_name: Optional[str]) -> str:
        template = self._templates.get(error_code or "")
        if template is None:
            template = self._templates["fallback"]
        return template.format(app_name)


resolver = ActionErrorMessageResolver()
