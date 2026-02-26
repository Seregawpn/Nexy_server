
import sys
import os
import json
import logging
import re
from typing import Dict, Any

# Add server directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

from server.config.unified_config import UnifiedServerConfig
from server.config.prompts import build_system_prompt
from server.integrations.core.assistant_response_parser import AssistantResponseParser

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger("TestPromptSystem")


def _extract_allowed_commands(prompt: str) -> list[str]:
    match = re.search(r"MUST be exactly one of:\s*([^\n]+)", prompt)
    if not match:
        return []
    raw = match.group(1).strip()
    if raw == "none":
        return []
    return [item.strip() for item in raw.split(",") if item.strip()]

def test_prompt_building():
    logger.info("="*50)
    logger.info("TEST 1: Dynamic Prompt Building")
    logger.info("="*50)

    # Scenerio 1: WhatsApp Enabled
    logger.info("--- Scenario 1: WhatsApp Enabled ---")
    prompt_wa = build_system_prompt(whatsapp_enabled=True, browser_enabled=False)
    
    if "send_whatsapp_message" in prompt_wa:
        logger.info("✅ 'send_whatsapp_message' found in prompt")
    else:
        logger.error("❌ 'send_whatsapp_message' NOT found in prompt")

    if "WHATSAPP ACTIONS" in prompt_wa:
        logger.info("✅ WhatsApp Instructions found")
    else:
        logger.error("❌ WhatsApp Instructions NOT found")

    wa_allowed = _extract_allowed_commands(prompt_wa)
    if "browser_use" not in wa_allowed:
        logger.info("✅ 'browser_use' correctly ABSENT (disabled)")
    else:
        logger.error("❌ 'browser_use' wrongfully PRESENT in allowed commands")

    # Scenario 2: Browser and Payment Enabled
    logger.info("\n--- Scenario 2: Browser & Payment Enabled, WhatsApp Disabled ---")
    prompt_browser = build_system_prompt(whatsapp_enabled=False, browser_enabled=True, payment_enabled=True)
    
    browser_allowed = _extract_allowed_commands(prompt_browser)
    if "browser_use" in browser_allowed:
        logger.info("✅ 'browser_use' found in prompt")
    else:
        logger.error("❌ 'browser_use' NOT found in allowed commands")
        
    if "manage_subscription" in prompt_browser:
        logger.info("✅ 'manage_subscription' found in prompt")
    else:
        logger.error("❌ 'manage_subscription' NOT found in prompt")

    if "send_whatsapp_message" not in browser_allowed:
        logger.info("✅ 'send_whatsapp_message' correctly ABSENT")
    else:
        logger.error("❌ 'send_whatsapp_message' wrongfully PRESENT in allowed commands")

    # Scenario 3: All Enabled (Priorities)
    logger.info("\\n--- Scenario 3: All Features Enabled (Checking Priorities) ---")
    prompt_all = build_system_prompt(whatsapp_enabled=True, browser_enabled=True, payment_enabled=True)
    
    # Check if priorities exist inside the priority section
    priority_start = prompt_all.find("[Processing Priority]")
    if priority_start != -1:
        priority_section = prompt_all[priority_start:]
        
        wa_index = priority_section.find("WhatsApp Actions")
        browser_index = priority_section.find("Browser Automation")
        system_index = priority_section.find("System Actions")
        
        # WhatsApp should be first, then Browser, then System
        if wa_index != -1 and browser_index != -1 and system_index != -1:
            if wa_index < browser_index < system_index:
                 logger.info("✅ Priority Order Correct: WhatsApp < Browser < System")
            else:
                 logger.error(f"❌ Priority Order INCORRECT inside section: WA={wa_index}, Browser={browser_index}, System={system_index}")
        else:
            logger.error("❌ One of the priority items is missing in the section")
    else:
        logger.error("❌ Priority section missing")


def test_response_parsing():
    logger.info("\\n\\n" + "="*50)
    logger.info("TEST 2: Response Parsing (Simulating LLM Output)")
    logger.info("="*50)
    
    parser = AssistantResponseParser()

    # Case 1: WhatsApp Send
    wa_json = {
        "session_id": "test-session-123",
        "command": "send_whatsapp_message",
        "args": {
            "contact": "Mom",
            "message": "Hello!"
        },
        "text": "Sending message to Mom."
    }
    
    try:
        logger.info("\\nParsing WhatsApp Command...")
        parsed = parser.parse(json.dumps(wa_json))
        
        if parsed.command_payload and parsed.command_payload['payload']['command'] == "send_whatsapp_message":
             contact = parsed.command_payload['payload']['args'].get("contact")
             if contact == "Mom":
                 logger.info("✅ WhatsApp command parsed successfully")
             else:
                 logger.error(f"❌ Wrong contact: {contact}")
        else:
             logger.error(f"❌ Failed to parse match. Text: {parsed.text_response}")
    except Exception as e:
        logger.error(f"❌ Exception parsing WhatsApp: {e}")

    # Case 2: Browser Use
    browser_json = {
        "session_id": "test-session-123",
        "command": "browser_use",
        "args": {
            "task": "Open YouTube"
        },
        "text": "Opening YouTube."
    }
    
    try:
        logger.info("\\nParsing Browser Command...")
        parsed = parser.parse(json.dumps(browser_json))
        if parsed.command_payload and parsed.command_payload['payload']['command'] == "browser_use":
             task = parsed.command_payload['payload']['args'].get("task")
             if task == "Open YouTube":
                 logger.info("✅ Browser command parsed successfully")
             else:
                 logger.error(f"❌ Wrong task: {task}")
        else:
             logger.error(f"❌ Failed to parse match. Text: {parsed.text_response}")
    except Exception as e:
        logger.error(f"❌ Exception parsing Browser: {e}")

    # Case 3: Read Messages
    msg_json = {
        "session_id": "test-session-123",
        "command": "read_messages",
        "args": {
            "contact": "John",
            "limit": 5
        },
        "text": "Reading messages."
    }
    try:
        logger.info("\\nParsing Read Messages Command...")
        parsed = parser.parse(json.dumps(msg_json))
        if parsed.command_payload and parsed.command_payload['payload']['command'] == "read_messages":
             limit = parsed.command_payload['payload']['args'].get("limit")
             if limit == 5:
                 logger.info("✅ Read Messages command parsed successfully")
             else:
                 logger.error(f"❌ Wrong limit: {limit}")
        else:
             logger.error(f"❌ Failed to parse match. Text: {parsed.text_response}")
    except Exception as e:
        logger.error(f"❌ Exception parsing Read Messages: {e}")


if __name__ == "__main__":
    test_prompt_building()
    test_response_parsing()
