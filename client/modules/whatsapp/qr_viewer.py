import io
import logging
import os
import sys
import webbrowser

logger = logging.getLogger(__name__)

# Add vendored libs to path
try:
    libs_path = os.path.join(os.path.dirname(__file__), "libs")
    if libs_path not in sys.path:
        sys.path.append(libs_path)

    import qrcode  # type: ignore
    from qrcode.image.svg import SvgPathImage  # type: ignore
except ImportError as e:
    logger.error(f"Failed to import local qrcode library: {e}")
    qrcode = None


class QRViewer:
    """
    Handles the display of the WhatsApp QR Code.
    Supports both legacy URLs and local SVG generation.
    """

    def display(self, qr_content: str):
        """
        Display the QR code in a centered HTML page.
        Args:
            qr_content: Can be a URL (legacy) or "raw:<data>" string
        """
        logger.info(f"Display request for QR content (start): {qr_content[:30]}...")

        image_src = ""

        # 1. Handle Raw Data (Local Generation)
        if qr_content.startswith("raw:") and qrcode:
            try:
                raw_data = qr_content[4:]  # Strip "raw:"
                logger.info("Generatng local SVG for QR code...")

                # Generate SVG in memory
                img = qrcode.make(raw_data, image_factory=SvgPathImage)

                # Serialize to string
                stream = io.BytesIO()
                img.save(stream)
                svg_data = stream.getvalue().decode("utf-8")

                # Create Data URI
                # Only need the <svg... part, but qrcode output usually full XML.
                # Embedding directly as data URI is safest:
                import base64

                b64_svg = base64.b64encode(svg_data.encode("utf-8")).decode("utf-8")
                image_src = f"data:image/svg+xml;base64,{b64_svg}"
                logger.info("✅ Generated local SVG Data URI")

            except Exception as e:
                logger.error(f"Failed to generate local QR: {e}")
                # Fallback? No fallback for raw data if gen fails.

        # 2. Handle Legacy URL
        elif qr_content.startswith("http"):
            image_src = qr_content

        if not image_src:
            logger.error("Could not determine image source for QR code")
            return

        # Create a temporary HTML file to ensure centering
        try:
            import tempfile

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
                        padding: 2rem;
                        border-radius: 1.5rem;
                        box-shadow: 0 10px 40px rgba(0,0,0,0.12);
                        
                        /* Layout inside card */
                        display: flex;
                        flex-direction: column;
                        align_items: center;
                        gap: 1.5rem;
                    }}
                    img {{
                        /* Responsive sizing: fits within 85% of the viewport */
                        width: auto;
                        height: auto;
                        max-width: 85vmin;
                        max-height: 85vmin;
                        min-width: 400px;
                        min-height: 400px;
                        
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
                    <img src="{image_src}" alt="WhatsApp QR Code">
                </div>
            </body>
            </html>
            """

            # Write to temp file
            fd, path = tempfile.mkstemp(suffix=".html", prefix="nexy_whatsapp_qr_")
            with os.fdopen(fd, "w") as tmp:
                tmp.write(html_content)

            logger.info(f"Opening centered QR view at: file://{path}")
            webbrowser.open(f"file://{path}")

        except Exception as e:
            logger.error(f"Failed to open HTML viewer: {e}")
            # Fallback to direct URL (only if URL)
            if image_src.startswith("http"):
                try:
                    webbrowser.open(image_src)
                except Exception as e2:
                    logger.warning(f"Could not open browser: {e2}")

    def close(self):
        """Close the QR viewer (no-op for browser-based viewer)."""
        pass
