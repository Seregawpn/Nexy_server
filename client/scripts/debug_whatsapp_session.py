#!/usr/bin/env python3
"""
Debug script to inspect current WhatsApp session.
Lists recent chats to verify account identity.
"""
import asyncio
import json
import logging
import os
import sys

# Setup path
current_dir = os.path.dirname(os.path.abspath(__file__))
client_dir = os.path.dirname(current_dir) # .../client
sys.path.insert(0, client_dir)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("DebugWhatsApp")

# Correct imports relative to client_dir
from modules.whatsapp import WhatsappConfig, WhatsappMCPClient, WhatsappServiceManager

# Assuming config is in client/config
# But verify unified_config_loader location. 
# If it's in client/config/unified_config_loader.py, then 'from config.unified_config_loader' works
try:
    from config.unified_config_loader import UnifiedConfigLoader
except ImportError:
    # Fallback if config structure is different or complicated
    UnifiedConfigLoader = None
    print("Warning: Could not import UnifiedConfigLoader. Using defaults.")

async def main():
    print("🚀 Debugging WhatsApp Session...")
    
    # Load Config
    config = WhatsappConfig.from_env()
    config.enabled = True # Force enable
    
    if UnifiedConfigLoader:
        try:
            loader = UnifiedConfigLoader.get_instance()
            whatsapp_cfg = loader.get_whatsapp_config()
            if 'node_path' in whatsapp_cfg:
                config.node_path = whatsapp_cfg['node_path']
        except Exception as e:
            print(f"Config load error: {e}")

    config.node_path = "/opt/homebrew/bin/node" # Force correct path OVERRIDE
    print(f"Node path: {config.node_path}")
    
    manager = WhatsappServiceManager(config)
    client = WhatsappMCPClient(manager)
    
    try:
        print("Starting service...")
        await manager.start(
            qr_callback=lambda url: print(f"⚠️ QR REQUIRED: {url}"),
            auth_callback=lambda: print("✅ Authenticated!")
        )
        await client.start()
        
        # Wait for connection to fully establish and HISTORY SYNC to happen
        print("Waiting for History Sync (15 seconds)...")
        await asyncio.sleep(15)
        
        # List Chats
        print("\n--- Listing Recent Chats ---")
        try:
            result = await client.call_tool("list_chats", {"limit": 5})
            
            if isinstance(result, dict) and 'content' in result:
                for item in result['content']:
                    if item.get('type') == 'text':
                        text = item.get('text', '')
                        try:
                            chats = json.loads(text)
                            if chats:
                                # debug first chat
                                # print(f"DEBUG: First Chat: {json.dumps(chats[0], indent=2)}")
                                pass
                                
                            for chat in chats:
                                print(f"Raw Chat Data: {json.dumps(chat, indent=2)}")
                                name = chat.get('name', 'Unknown')
                                jid = chat.get('jid') 
                                jid = chat.get('id', {}).get('_serialized', '??') if isinstance(chat.get('id'), dict) else chat.get('id')
                                
                                last_msg_preview = chat.get('last_message_preview', '')
                                print(f"🔹 Chat: {name} ({jid})")
                                print(f"   Last: {last_msg_preview[:50]}...")
                        except json.JSONDecodeError:
                             print(f"Raw Output: {text}")
            else:
                print(f"Raw Result: {result}")
                
        except Exception as e:
            print(f"Error listing chats: {e}")

        # List tools to confirm capabilities
        print("\n--- Available Tools ---")
        tools = await client.list_tools()
        if isinstance(tools, dict) and 'tools' in tools:
             # Standard MCP format { tools: [...] }
             tool_list = tools['tools']
        elif isinstance(tools, list):
             tool_list = tools
        else:
             print(f"DEBUG: Unknown tools format: {tools}")
             tool_list = []

        for tool in tool_list:
             # MCP Tool object usually has name, description, inputSchema
             # Or it's a dict
             if isinstance(tool, dict):
                 name = tool.get('name', 'Unknown')
                 desc = tool.get('description', 'No description')
             else:
                 name = getattr(tool, 'name', 'Unknown')
                 desc = getattr(tool, 'description', 'No description')
                 
             print(f"Tool: {name} - {desc}")
        
        print("\n--- Listing Contacts (if possible) ---")
        # Try to see if there is a tool for contacts
        has_contacts_tool = any(getattr(t, 'name', '') == 'get_contacts' for t in tools)
         
        if has_contacts_tool:
             print("Found 'get_contacts'. calling it...")
             # get_contacts might not take args or take limit
             contacts = await client.call_tool("get_contacts", {})
             print(f"Contacts result type: {type(contacts)}")
             # Process result...
        else:
             print("No 'get_contacts' tool found. Checking 'search_contacts'...")
             print("\n--- Searching for 'Peter' ---")
             try:
                search_res = await client.call_tool("search_contacts", {"query": "Peter"})
                print(f"Search Result: {search_res}")
             except Exception as e:
                print(f"Search failed: {e}")
            
    except Exception as e:
        print(f"Fatal Error: {e}")
        
    finally:
        print("\nStopping...")
        await client.stop()
        await manager.stop()

if __name__ == "__main__":
    asyncio.run(main())
