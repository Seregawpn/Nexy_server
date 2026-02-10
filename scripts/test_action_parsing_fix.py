
import json
import sys

def _normalize_action_payload(parsed):
    if not isinstance(parsed, dict):
        return None

    command = parsed.get("command")
    if isinstance(command, str) and command.strip():
        args = parsed.get("args")
        if not isinstance(args, dict):
            args = {}
        return {
            "command": command.strip(),
            "args": args,
        }
    return None

def test_parsing():
    # Server sends this format:
    server_json = """
    {
      "event": "mcp.command_request",
      "payload": {
        "session_id": "abc-123",
        "command": "send_whatsapp_message",
        "args": {
          "contact": "Mom",
          "message": "Hello"
        }
      }
    }
    """
    
    print(f"Experiment: Testing Action Parsing Logic Fix")
    print(f"Server sends JSON: {server_json}")
    
    parsed_payload = json.loads(server_json)
    
    # 1. Simulate OLD Logic (Direct parsing)
    old_result = _normalize_action_payload(parsed_payload)
    print(f"\n[OLD LOGIC] Result: {old_result}")
    if old_result is None:
        print("Analysis: OLD logic failed because 'command' isn't at the top level.")
    
    # 2. Simulate NEW Logic (Unwrapping)
    print("\n[NEW LOGIC] Applying fix...")
    
    # Unwrap mcp.command_request wrapper if present
    if isinstance(parsed_payload, dict) and parsed_payload.get("event") == "mcp.command_request":
        parsed_payload = parsed_payload.get("payload", parsed_payload)
        print("Debug: Unwrapped 'mcp.command_request', inner payload extracted.")
        
    new_result = _normalize_action_payload(parsed_payload)
    print(f"Result: {new_result}")
    
    if new_result and new_result['command'] == 'send_whatsapp_message':
        print("\n✅ VERIFICATION SUCCESS: Command 'send_whatsapp_message' was correctly extracted!")
        sys.exit(0)
    else:
        print("\n❌ VERIFICATION FAILURE: Command extraction still failing.")
        sys.exit(1)

if __name__ == "__main__":
    test_parsing()
