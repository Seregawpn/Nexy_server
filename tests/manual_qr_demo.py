
import sys
import os
import logging
import time
import asyncio

# Adjust path to find client modules
sys.path.append('/Users/sergiyzasorin/Fix_new/client')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("manual_demo")

from modules.whatsapp.qr_viewer import QRViewer

def main():
    print("----------------------------------------------------------------")
    print("   🚀 STARTING MANUAL QR DEMO")
    print("----------------------------------------------------------------")
    print("1. Initializing QR Viewer...")
    viewer = QRViewer()
    
    # Simulate a raw QR code string coming from Node.js (Longer data for density check)
    sample_qr_data = "raw:2@Sample-QR-Data-For-Demonstration-Of-New-Sizing-Logic,User:Sergiy,Device:MacBookPro,Session:Valid,Timestamp:1234567890,Key:LongerKeyStringToForceMoreModules"
    
    print(f"2. Simulating incoming QR data: {sample_qr_data[:20]}...")
    
    print("3. Generating Local SVG and Opening Window...")
    # This should open the default web browser with the centered, SVG-rendered QR Code
    viewer.display(sample_qr_data)
    
    print("----------------------------------------------------------------")
    print("   ✅ WINDOW SHOULD BE OPEN NOW")
    print("   Check your browser.")
    print("----------------------------------------------------------------")

if __name__ == '__main__':
    main()
