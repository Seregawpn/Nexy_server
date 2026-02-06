
import logging
import webbrowser

logger = logging.getLogger(__name__)

class QRViewer:
    """
    Handles the display of the WhatsApp QR Code.
    """
    
    def display(self, qr_url: str):
        """
        Display the QR code in a centered HTML page.
        """
        logger.info(f"Generated QR URL: {qr_url}")
        
        # Create a temporary HTML file to ensure centering
        try:
            import tempfile
            import os
            
            html_content = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>WhatsApp Login</title>
                <style>
                    html, body {{
                        height: 100vh;
                        width: 100vw;
                        margin: 0;
                        padding: 0;
                        overflow: hidden;
                    }}
                    body {{
                        display: grid;
                        place-items: center;
                        background-color: #f0f2f5;
                        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
                    }}
                    .container {{
                        text-align: center;
                        background: white;
                        padding: 2.5rem;
                        border-radius: 1.5rem;
                        box-shadow: 0 10px 40px rgba(0,0,0,0.12);
                        
                        /* Layout inside card */
                        display: flex;
                        flex-direction: column;
                        align_items: center;
                        gap: 1.5rem;
                    }}
                    img {{
                        /* Responsive sizing: fits within 75% of the viewport */
                        width: auto;
                        height: auto;
                        max-width: 75vmin;
                        max-height: 75vmin;
                        min-width: 250px;
                        min-height: 250px;
                        
                        /* Clean rendering */
                        display: block;
                    }}
                    h1 {{
                        font-size: 1.8rem;
                        color: #111b21;
                        margin: 0;
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Scan to Connect</h1>
                    <img src="{qr_url}" alt="WhatsApp QR Code">
                </div>
            </body>
            </html>
            """
            
            # Write to temp file
            fd, path = tempfile.mkstemp(suffix=".html", prefix="nexy_whatsapp_qr_")
            with os.fdopen(fd, 'w') as tmp:
                tmp.write(html_content)
                
            logger.info(f"Opening centered QR view at: file://{path}")
            webbrowser.open(f"file://{path}")
            
        except Exception as e:
            logger.error(f"Failed to open HTML viewer: {e}")
            # Fallback to direct URL
            try:
                webbrowser.open(qr_url)
            except Exception as e2:
                logger.warning(f"Could not open browser: {e2}")

    def close(self):
        """Close the QR viewer (no-op for browser-based viewer)."""
        pass

