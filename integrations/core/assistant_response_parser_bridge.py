import re
from typing import Any, Callable, Dict, List


def extract_json_from_markdown(text: str) -> str:
    if not text:
        return ""

    text = str(text).strip()

    if text.startswith("```"):
        text = text[3:]
        text = text.lstrip()

        lowered = text.lower()
        if lowered.startswith("json"):
            text = text[4:]
        text = text.lstrip()

        while text.startswith(("\n", "\r")):
            text = text[1:]

        text = text.rstrip()
        if text.endswith("```"):
            text = text[:-3]
        text = text.strip()

    text_lower = text.lower()
    if text_lower.startswith("json") and len(text) > 4:
        after_json = text[4:].lstrip()
        if after_json.startswith("{") or after_json.startswith("\n{") or after_json.startswith("\r{"):
            text = after_json

    first_brace = text.find("{")
    last_brace = text.rfind("}")

    if first_brace != -1 and last_brace != -1 and first_brace < last_brace:
        json_candidate = text[first_brace:last_brace + 1].strip()
        json_candidate = re.sub(r"//.*?$", "", json_candidate, flags=re.MULTILINE)
        json_candidate = re.sub(r"/\*.*?\*/", "", json_candidate, flags=re.DOTALL)
        json_candidate = re.sub(r",\s*}", "}", json_candidate)
        json_candidate = re.sub(r",\s*]", "]", json_candidate)
        json_candidate = re.sub(r"\n\s*\n", "\n", json_candidate)
        json_candidate = re.sub(r"[ \t]+", " ", json_candidate)
        json_candidate = re.sub(r"\s*:\s*", ": ", json_candidate)
        json_candidate = re.sub(r"\s*,\s*", ", ", json_candidate)
        return json_candidate

    return text.strip()


def normalize_text_response(text_response: Any) -> str:
    if not isinstance(text_response, str):
        return ""
    return text_response.strip()


def normalize_action_args(
    *,
    command: Any,
    args: Any,
    normalize_browser_use_args: Callable[[Any], Dict[str, Any]],
    normalize_message_args: Callable[[Any], Dict[str, Any]],
) -> Dict[str, Any]:
    normalized_args = args if isinstance(args, dict) else args
    if command == "browser_use":
        return normalize_browser_use_args(normalized_args)
    if command in {"send_message", "send_whatsapp_message"}:
        return normalize_message_args(normalized_args)
    return normalized_args if isinstance(normalized_args, dict) else {}


def validate_action_payload(
    *,
    command: Any,
    args: Any,
    session_id: Any,
    allowed_commands: List[str],
) -> List[str]:
    validation_errors: List[str] = []

    if command not in allowed_commands:
        validation_errors.append(
            f"Команда '{command}' отключена или не разрешена. Allowed: {allowed_commands}"
        )

    if not session_id:
        validation_errors.append(
            "Отсутствует обязательное поле 'session_id' (не предоставлен ни в данных, ни в контексте)"
        )

    if not isinstance(args, dict):
        validation_errors.append("Поле 'args' должно быть словарём")
        return validation_errors

    if command == "open_app" and not args.get("app_name"):
        validation_errors.append("Для команды 'open_app' требуется поле 'args.app_name'")

    if command == "close_app" and not args.get("app_name"):
        validation_errors.append("Для команды 'close_app' требуется поле 'args.app_name'")

    if command == "browser_use" and not args.get("task"):
        validation_errors.append("Для команды 'browser_use' требуется поле 'args.task'")

    if command == "send_whatsapp_message":
        if not args.get("contact"):
            validation_errors.append("Для команды 'send_whatsapp_message' требуется поле 'args.contact'")
        if not args.get("message"):
            validation_errors.append("Для команды 'send_whatsapp_message' требуется поле 'args.message'")

    if command == "read_whatsapp_messages" and "contact" in args and not args.get("contact"):
        validation_errors.append(
            "Для команды 'read_whatsapp_messages' поле 'args.contact' не может быть пустым"
        )

    return validation_errors


def build_command_payload(*, session_id: str, command: Any, args: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "event": "mcp.command_request",
        "payload": {
            "session_id": session_id,
            "command": command,
            "args": args,
        },
    }
