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
    from server.server.config.prompts import resolve_prompt_sections, build_system_prompt
    from google import genai
except ImportError:
    # Fallback for different path structure
    try:
        sys.path.insert(0, str(project_root / "server"))
        from server.config.prompts import resolve_prompt_sections, build_system_prompt
        from google import genai
    except ImportError as e:
        print(f"Import Error: {e}")
        sys.exit(1)

# Load API Key
API_KEY = os.getenv("GEMINI_API_KEY", "")
# try:
#     config_path = project_root / "config.env"
# ... (commented out or removed for this direct test to ensure it works)

MODEL = "gemini-3-flash-preview"

async def test_case(client, name, text):
    print(f"\n{'-'*60}")
    print(f"TEST: {name}")
    print(f"INPUT: {text}")
    
    # 1. Resolve Intent
    sections = resolve_prompt_sections(text)
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
        web_search_enabled=sections["web_search"]
    )
    
    # Check if a specific section was actually added
    print("PROMPT SECTIONS INCLUDED:")
    if "**MESSAGES ACTIONS" in system_prompt: print(" - MESSAGES present")
    if "**WHATSAPP ACTIONS" in system_prompt: print(" - WHATSAPP present")
    if "Browser Automation Intent" in system_prompt: print(" - BROWSER present")
    if "Descriptor Intent" in system_prompt or "Describe Intent" in system_prompt: print(" - DESCRIBE present")
    if "WebSearch Intent" in system_prompt: print(" - WEB_SEARCH present")
    
    # 3. Call Gemini (Standard Generation)
    print("\nSending to Gemini...")
    try:
        # Enable Google Search if intent requires it
        tools = []
        if sections.get("web_search"):
            tools = [{"google_search": {}}]
            print(" - TOOLS: [google_search] enabled")

        # Use standard generate_content instead of live.connect for testing intent logic
        response = await client.aio.models.generate_content(
            model=MODEL,
            contents=[text],
            config={
                "system_instruction": system_prompt,
                "response_mime_type": "application/json", # Enforce JSON
                "tools": tools,
            }
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
