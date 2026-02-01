
import logging
import webbrowser
import platform

logger = logging.getLogger(__name__)

class QRViewer:
    """
    Handles the display of the WhatsApp QR Code.
    """
    
    def display(self, qr_url: str):
        """
        Display the QR code.
        For now, this logs the URL and attempts to open it in the default browser.
        """
        logger.info(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        logger.info(f"WHATSAPP AUTHENTICATION REQUIRED")
        logger.info(f"Please scan the QR code at this URL:")
        logger.info(f"{qr_url}")
        logger.info(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        
        # Optionally open in browser
        try:
            webbrowser.open(qr_url)
        except Exception as e:
            logger.warning(f"Could not open browser automatically: {e}")

