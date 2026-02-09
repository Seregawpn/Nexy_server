
import unittest
import sys
import os
import logging
from unittest.mock import MagicMock

# Adjust path to find client modules
sys.path.append('/Users/sergiyzasorin/Fix_new/client')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("test_local_qr")

from modules.whatsapp.qr_viewer import QRViewer

class TestLocalQR(unittest.TestCase):
    
    def test_rendering(self):
        """Verify QRViewer generates Data URI from raw input"""
        print("\n🔎 Testing Local QR Generation...")
        
        viewer = QRViewer()
        
        # Mock input
        raw_qr = "raw:2@test-qr-data,Key1,Key2"
        
        # We can't easily capture the internal variable `image_src` without inspecting the HTML it generates
        # or checking logs. However, the display method opens a browser.
        # We can look at the logs (already setup) or better:
        # Refactor QRViewer to return the path or content? No, let's mock webbrowser.open
        # and checking the file content written.
        
        with unittest.mock.patch('webbrowser.open') as mock_open:
            with unittest.mock.patch('os.fdopen') as mock_fdopen:
                # We need to capture the write to the temp file
                mock_file = MagicMock()
                mock_fdopen.return_value.__enter__.return_value = mock_file
                
                # Mock tempfile.mkstemp to return a dummy path
                with unittest.mock.patch('tempfile.mkstemp', return_value=(123, "/tmp/dummy.html")):
                    
                    viewer.display(raw_qr)
                    
                    # Capture what was written
                    args, _ = mock_file.write.call_args
                    html_content = args[0]
                    
                    # Verify Data URI presence
                    if "data:image/svg+xml;base64," not in html_content:
                        self.fail("❌ SVG Data URI not found in generated HTML!")
                    
                    print("✅ SVG Data URI detected in HTML output")
                    
                    # Verify it's not empty
                    # Extract base64
                    import re
                    match = re.search(r'src="(data:image/svg\+xml;base64,[^"]+)"', html_content)
                    if match:
                        data_uri = match.group(1)
                        print(f"   Generated URI length: {len(data_uri)}")
                    else:
                        self.fail("❌ Could not extract src attribute")

if __name__ == '__main__':
    unittest.main()
