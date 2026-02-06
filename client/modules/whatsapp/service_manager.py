
import asyncio
import json
import logging
import os
from pathlib import Path
import re
import shutil
from typing import Callable

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
        self.process: asyncio.subprocess.Process | None = None
        self.mcp_client: "StdioMcpClient | None" = None  # type: ignore[reportUndefinedVariable]
        self.qr_callback: Callable[[str], None] | None = None
        self.auth_callback: Callable[[], None] | None = None
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

    def _resolve_node_executable(self) -> str:
        """Resolve Node.js executable with fallbacks."""
        # 1. Try configured path
        node_path = self.config.node_path
        if os.path.exists(node_path):
            return node_path
            
        # 2. Try which 'node'
        which_node = shutil.which('node')
        if which_node:
            logger.info(f"Configured node path '{node_path}' not found, falling back to '{which_node}'")
            return which_node
            
        # 3. Try common locations
        common_paths = [
            "/opt/homebrew/bin/node",
            "/usr/local/bin/node",
            "/usr/bin/node"
        ]
        for path in common_paths:
            if os.path.exists(path):
                logger.info(f"Configured node path '{node_path}' not found, falling back to found '{path}'")
                return path
                
        # 4. Give up, return configured so error is clear
        return node_path

    async def start(self, qr_callback: Callable[[str], None] | None = None, auth_callback: Callable[[], None] | None = None, failure_callback: Callable[[], None] | None = None):
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
        self.failure_callback = failure_callback
        
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
                self._resolve_node_executable(),
                self._node_script,
                stdin=asyncio.subprocess.PIPE,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                env=env,
                cwd=str(self._root_dir / "Whatsapp/whatsapp-mcp-ready")
            )
            
            logger.info(f"WhatsApp Service started with PID {self.process.pid}")
            
            # Start output monitoring tasks (stdout has JSON logs with QR, stderr has errors)
            asyncio.create_task(self._monitor_output(self.process.stdout, 'stdout'))
            asyncio.create_task(self._monitor_output(self.process.stderr, 'stderr'))
            
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
                try:
                    await asyncio.wait_for(self.process.wait(), timeout=5.0)
                except (RuntimeError, ValueError) as e:
                    # Capture "attached to a different loop" error
                    if "attached to a different loop" in str(e):
                        logger.warning(f"⚠️ Loop mismatch during process wait/stop: {e}. continuing...")
                    else:
                        raise e
            except (asyncio.TimeoutError, ProcessLookupError):
                try:
                    self.process.kill()
                except ProcessLookupError:
                    pass
            except Exception as e:
                 logger.error(f"Error during stop: {e}")
                 # Ensure we don't block restart
            
            self.process = None
            logger.info("WhatsApp Service stopped")

    def clear_auth_cache(self):
        """
        Clear the WhatsApp authentication cache (auth_info directory).
        Used to reset the session if QR code cannot be generated.
        """
        try:
            # Assuming str path, convert to Path
            script_path = Path(self._node_script)
            # node_modules/@iflow-mcp/whatsapp-mcp-ts/build/index.js
            # auth_info is at: node_modules/@iflow-mcp/whatsapp-mcp-ts/auth_info
            
            # Go up from build/index.js to package root
            package_root = script_path.parent.parent
            auth_info_dir = package_root / "auth_info"
            
            if auth_info_dir.exists() and auth_info_dir.is_dir():
                logger.warning(f"🧹 Clearing WhatsApp auth cache at {auth_info_dir}")
                shutil.rmtree(auth_info_dir)
                logger.info("✅ Auth cache cleared successfully")
            else:
                logger.info(f"ℹ️ No auth cache found at {auth_info_dir} to clear")
                
        except Exception as e:
            logger.error(f"❌ Failed to clear auth cache: {e}")

    async def _monitor_output(self, stream, stream_name: str = 'output'):
        """Monitor stdout/stderr for logs and QR codes"""
        if not self.process or not stream:
            return
            
        try:
            while True:
                line = await stream.readline()
                if not line:
                    break
                
                decoded_line = line.decode('utf-8', errors='replace').strip()
                if not decoded_line:
                    continue
                    
                # Log stderr as debug info
                logger.debug(f"[WhatsApp Node] {decoded_line}")
                
                # Check for Auth Failure
                if "Auth failure" in decoded_line or "Authentication failure" in decoded_line or "Session closed" in decoded_line:
                    logger.warning("🚨 Detected WhatsApp Auth Failure in logs!")
                    if self.failure_callback:
                        self.failure_callback()
                
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
                        qr_url = f"https://quickchart.io/qr?text={encoded_qr}&dark=000000&light=ffffff&ecLevel=M&size=600&margin=0&format=svg"
                        logger.warning(f"🛑 QR Code detected from JSON (Size 1000): {qr_url}")
                        self.qr_callback(qr_url)
                        continue  # Skip legacy detection for this line
                            
                except json.JSONDecodeError:
                    pass
 
                # Check for legacy QR Code URL (quickchart.io)
                if "quickchart.io" in decoded_line and self.qr_callback:
                    # Extract URL
                    match = re.search(r'(https://quickchart\.io/qr\?[^ \n]+)', decoded_line)
                    if match:
                        qr_url = match.group(1)
                        # Force size to 1200
                            
                        # Robustly force size and margin
                        # Remove existing size/margin to avoid dupes
                        qr_url = re.sub(r'[&?]size=\d+', '', qr_url)
                        qr_url = re.sub(r'[&?]margin=\d+', '', qr_url)
                        
                        # Append our preferred params. Use & or ? depending on if ? exists
                        sep = '&' if '?' in qr_url else '?'
                        qr_url += f"{sep}size=1000&margin=0"
                            
                        logger.warning(f"🛑 QR Code detected (legacy, Size 1000): {qr_url}")
                        self.qr_callback(qr_url)
                        
        except Exception as e:
            logger.error(f"Error reading stderr: {e}")

