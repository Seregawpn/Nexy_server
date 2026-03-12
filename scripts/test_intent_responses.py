#!/usr/bin/env python3
import sys
import os
import asyncio
import json
from pathlib import Path

# Add server to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

try:
    from server.server.modules.text_processing.core.text_processor import TextProcessor
    from server.server.config.prompts import build_system_prompt
    from server.server.config.unified_config import get_config
    from google import genai
except ImportError:
    # Fallback for different path structure
    try:
        sys.path.insert(0, str(project_root / "server"))
        from server.modules.text_processing.core.text_processor import TextProcessor
        from server.config.prompts import build_system_prompt
        from server.config.unified_config import get_config
        from google import genai
    except ImportError as e:
        print(f"Import Error: {e}")
        sys.exit(1)

# Load API Key
API_KEY = os.getenv("GEMINI_API_KEY", "")
CFG = get_config()
MODEL = CFG.text_processing.langchain_model
_TP = TextProcessor(config={})

async def test_case(client, name, text):
    print(f"\n{'-'*60}")
    print(f"TEST: {name}")
    print(f"INPUT: {text}")
    
    # 1. Resolve Intent
    route, _ = await _TP._resolve_route_and_reason(intent_text=text)
    sections = {
        "system_control": route == "system_control",
        "describe": route == "describe",
        "messages": route == "messages",
        "whatsapp": route == "whatsapp",
        "browser": route == "browser",
        "payment": route == "payment",
        "google_search": route == "google_search",
        "capability": route == "capability",
        "primary_route": route,
    }
    print(f"INTENTS: {json.dumps(sections, indent=2)}")
    
    # 2. Build System Prompt
    # Force enable features to see if Intent logic includes the section
    system_prompt = build_system_prompt(
        system_control_enabled=sections["system_control"],
        describe_enabled=sections["describe"],
        messages_enabled=sections["messages"], 
        whatsapp_enabled=sections["whatsapp"], 
        browser_enabled=sections["browser"],   
        payment_enabled=sections["payment"],   
        google_search_enabled=sections["google_search"]
    )
    
    # Check if a specific section was actually added
    print("PROMPT SECTIONS INCLUDED:")
    if "**MESSAGES ACTIONS" in system_prompt: print(" - MESSAGES present")
    if "**WHATSAPP ACTIONS" in system_prompt: print(" - WHATSAPP present")
    if "Browser Automation Intent" in system_prompt: print(" - BROWSER present")
    if "Descriptor Intent" in system_prompt or "Describe Intent" in system_prompt: print(" - DESCRIBE present")
    if "Google Search Intent" in system_prompt: print(" - GOOGLE_SEARCH present")
    
    # 3. Call Gemini (Standard Generation)
    print("\nSending to Gemini...")
    try:
        # Enable Google Search if intent requires it
        tools = []
        if sections.get("google_search"):
            tools = [{"google_search": {}}]
            print(" - TOOLS: [google_search] enabled")

        # Use standard generate_content instead of live.connect for testing intent logic.
        # IMPORTANT: do not force JSON mime when Google Search tool is enabled,
        # otherwise Gemini may return 400 INVALID_ARGUMENT.
        request_config = {
            "system_instruction": system_prompt,
            "tools": tools,
        }
        if not tools:
            request_config["response_mime_type"] = "application/json"

        response = await client.aio.models.generate_content(
            model=MODEL,
            contents=[text],
            config=request_config,
        )
        
        print(f"\nRAW RESPONSE:\n{response.text}")
        
    except Exception as e:
        print(f"API ERROR: {e}")

async def main():
    print(f"Running Intent Tests with model: {MODEL}")
    if not API_KEY:
        print("GEMINI_API_KEY is not set")
        return
    try:
        client = genai.Client(api_key=API_KEY)
    except Exception as e:
        print(f"Failed to create Client: {e}")
        return

    tests = [
        ("General Request", "What is the capital of France?"),
        ("Screenshot Request", "What is on the screen?"),
        ("Message Request", "Send message to brother I'll be late"),
        ("Search Request", "Search for the latest iphone news and provide a detailed summary with at least 3 distinct topics"),
        #("Browser Request", "Open youtube.com") # Optional
    ]
    
    for name, text in tests:
        await test_case(client, name, text)
        await asyncio.sleep(2) # Avoid rate limits

if __name__ == "__main__":
    asyncio.run(main())
