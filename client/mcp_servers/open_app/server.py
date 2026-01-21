#!/usr/bin/env python3
"""
MCP Server для открытия приложений на macOS.
"""

import logging
import sys
import subprocess
from pathlib import Path
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

server = Server("open-app-mcp-server")


@server.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="open_app",
            description="Open an application by name (e.g., Safari) or by full path.",
            inputSchema={
                "type": "object",
                "properties": {
                    "app_name": {
                        "type": "string",
                        "description": "Application name (e.g., Safari).",
                    },
                    "app_path": {
                        "type": "string",
                        "description": "Full path to the application bundle.",
                    },
                },
            },
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict[str, Any] | None) -> list[TextContent]:
    if name != "open_app":
        return [TextContent(type="text", text=f"❌ Unknown tool: {name}")]

    args = arguments or {}
    app_name = args.get("app_name")
    app_path = args.get("app_path")

    if not app_name and not app_path:
        return [TextContent(type="text", text="❌ Missing app_name or app_path for open_app")]

    try:
        if app_path:
            if not Path(app_path).exists():
                return [TextContent(type="text", text=f"❌ App path not found: {app_path}")]
            # app_path гарантированно не None здесь
            subprocess.run(["/usr/bin/open", str(app_path)], check=True)
        else:
            # app_name гарантированно не None здесь (проверено выше)
            if not app_name:
                return [TextContent(type="text", text="❌ Missing app_name for open_app")]
            subprocess.run(["/usr/bin/open", "-a", str(app_name)], check=True)
        return [TextContent(type="text", text=f"✅ Opened {app_path or app_name}")]
    except Exception as exc:
        logger.error("open_app failed: %s", exc)
        return [TextContent(type="text", text=f"❌ open_app failed: {exc}")]


async def main() -> None:
    async with stdio_server() as (read, write):
        await server.run(read, write, server.create_initialization_options())


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
