#!/usr/bin/env python3
"""
MCP Server для закрытия приложений на macOS.
"""

import logging
import sys
import subprocess
from typing import Any

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stderr)],
)
logger = logging.getLogger(__name__)

server = Server("close-app-mcp-server")


@server.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="close_app",
            description="Quit an application by name (e.g., Safari).",
            inputSchema={
                "type": "object",
                "properties": {
                    "app_name": {
                        "type": "string",
                        "description": "Application name (e.g., Safari).",
                    }
                },
                "required": ["app_name"],
            },
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict[str, Any] | None) -> list[TextContent]:
    if name != "close_app":
        return [TextContent(type="text", text=f"❌ Unknown tool: {name}")]

    args = arguments or {}
    app_name = args.get("app_name")
    if not app_name:
        return [TextContent(type="text", text="❌ Missing app_name for close_app")]

    script = f'tell application "{app_name}" to quit'
    try:
        subprocess.run(["/usr/bin/osascript", "-e", script], check=True)
        return [TextContent(type="text", text=f"✅ Closed {app_name}")]
    except Exception as exc:
        logger.error("close_app failed: %s", exc)
        return [TextContent(type="text", text=f"❌ close_app failed: {exc}")]


async def main() -> None:
    async with stdio_server() as (read, write):
        await server.run(read, write, server.create_initialization_options())


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
