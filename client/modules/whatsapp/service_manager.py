
import asyncio
import logging
import os
import re
import shutil
import json
from typing import Optional, Callable
from pathlib import Path
from dataclasses import dataclass


from .config import WhatsappConfig
# from client.modules.mcp_action.connection.stdio_client import StdioMcpClient (Removed unused import)

logger = logging.getLogger(__name__)

class WhatsappServiceManager:
    """
    Manages the Whatsapp Node.js MCP Service.
    Handles process lifecycle, QR code detection, and MCP connection.
    """
    
    def __init__(self, config: WhatsappConfig):
        self.config = config
        self.process: Optional[asyncio.subprocess.Process] = None
        self.mcp_client: Optional[StdioMcpClient] = None
        self.qr_callback: Optional[Callable[[str], None]] = None
        self.auth_callback: Optional[Callable[[], None]] = None
        self._root_dir = Path(__file__).parent.parent.parent.parent # Fix_new
        self._node_script = self._resolve_script_path()
        
    def _resolve_script_path(self) -> str:
        """Resolve the absolute path to the Node.js script"""
        if self.config.service_script_path:
            return str(Path(self.config.service_script_path).resolve())
        
        # Default path inside "Whatsapp/whatsapp-mcp-ready/node_modules/..."
        default_path = self._root_dir / "Whatsapp/whatsapp-mcp-ready/node_modules/@iflow-mcp/whatsapp-mcp-ts/build/index.js"
        if not default_path.exists():
             logger.warning(f"Default WhatsApp script not found at {default_path}")
             # Check if we should fallback to looking for the package location differently
        return str(default_path)

    async def start(self, qr_callback: Optional[Callable[[str], None]] = None, auth_callback: Optional[Callable[[], None]] = None):
        """
        Start the Node.js service and initialize MCP client.
        """
        if not self.config.enabled:
            logger.info("WhatsApp module disabled, not starting service.")
            return

        if self.process:
            logger.warning("WhatsApp service already running.")
            return

        self.qr_callback = qr_callback
        self.auth_callback = auth_callback
        
        logger.info(f"Starting WhatsApp Service: {self._node_script}")
        
        # Prepare environment
        env = os.environ.copy()
        # Ensure PATH includes node
        
        try:
            # We use StdioMcpClient to manage the process and communication
            # But we need to intercept stderr for QR codes.
            # Unlike generic StdioMcpClient, we might need custom handling.
            # For now, let's try to use the generic client but maybe wrap the process creation if possible 
            # OR just run it manually here and pass streams to a client.
            
            # Since StdioMcpClient in this codebase might be designed to spawn the process itself,
            # let's look at how it works. If it's flexible, we use it.
            # If not, we might need to implement our own simple MCP handler or use the one logic.
            
            # Assuming we can instantiate StdioMcpClient with a command.
            # I'll create a tailored implementation here for simplicity and control over stderr.
            
            self.process = await asyncio.create_subprocess_exec(
                self.config.node_path,
                self._node_script,
                stdin=asyncio.subprocess.PIPE,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                env=env,
                cwd=str(self._root_dir / "Whatsapp/whatsapp-mcp-ready")
            )
            
            logger.info(f"WhatsApp Service started with PID {self.process.pid}")
            
            # Start stderr monitoring task
            asyncio.create_task(self._monitor_stderr())
            
            # Initialize MCP Client (wraps the streams)
            # We need a simple MCP client that can use existing streams. 
            # If StdioMcpClient strictly spawns, we might need a custom one or modify it.
            # For now, let's assume we need a custom minimal client class in mcp_client.py 
            # provided in the next step.
            
        except Exception as e:
            logger.error(f"Failed to start WhatsApp service: {e}")
            raise

    async def stop(self):
        """Stop the service"""
        if self.process:
            logger.info("Stopping WhatsApp Service...")
            try:
                self.process.terminate()
                await asyncio.wait_for(self.process.wait(), timeout=5.0)
            except (asyncio.TimeoutError, ProcessLookupError):
                try:
                    self.process.kill()
                except ProcessLookupError:
                    pass
            self.process = None
            logger.info("WhatsApp Service stopped")

    async def _monitor_stderr(self):
        """Monitor stderr for logs and QR codes"""
        if not self.process or not self.process.stderr:
            return
            
        try:
            while True:
                line = await self.process.stderr.readline()
                if not line:
                    break
                
                decoded_line = line.decode('utf-8', errors='replace').strip()
                if not decoded_line:
                    continue
                    
                # Log stderr as debug info
                logger.debug(f"[WhatsApp Node] {decoded_line}")
                
                # Try to parse JSON log
                try:
                    log_entry = json.loads(decoded_line)
                    msg = log_entry.get('msg', '')
                    
                    # Detect Auth Success
                    if "connected to WA" in msg or "Application setup complete" in msg:
                        if self.auth_callback:
                            self.auth_callback()

                    # Detect Raw QR Code Data
                    qr_data = log_entry.get('qrCodeData')
                    if qr_data and self.qr_callback:
                        # Construct quickchart URL
                        # URL encode is needed, but for simplicity let's rely on basic string, 
                        # or use urllib if needed. QR data usually safe chars but commas...
                        from urllib.parse import quote
                        encoded_qr = quote(qr_data)
                        qr_url = f"https://quickchart.io/qr?text={encoded_qr}&dark=000000&light=ffffff&ecLevel=M&size=600"
                        logger.info(f"QR Code detected from JSON: {qr_url}")
                        self.qr_callback(qr_url)
                            
                except json.JSONDecodeError:
                    pass
 
                # Check for legacy QR Code URL (quickchart.io)
                if "quickchart.io" in decoded_line and self.qr_callback:
                    # Extract URL
                    match = re.search(r'(https://quickchart\.io/qr\?[^ \n]+)', decoded_line)
                    if match:
                        qr_url = match.group(1)
                        logger.info(f"QR Code detected (legacy): {qr_url}")
                        self.qr_callback(qr_url)
                        
        except Exception as e:
            logger.error(f"Error reading stderr: {e}")

