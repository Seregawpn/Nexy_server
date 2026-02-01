#!/usr/bin/env python3
"""
Verification script for WhatsApp Gateway Logic.
Tests that the DecisionEngine correctly processes WhatsApp status.
"""

import sys
import os
import unittest
from unittest.mock import MagicMock, patch

# Add client directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
client_dir = os.path.dirname(current_dir)
sys.path.insert(0, client_dir)

from integration.core.selectors import Snapshot, WhatsappStatus, PermissionStatus, DeviceStatus, NetworkStatus, AppMode
from integration.core.gateways.types import Decision
from integration.core.gateways.whatsapp_gateways import decide_whatsapp_action

class TestWhatsappGateway(unittest.TestCase):

    def create_snapshot(self, whatsapp_status: WhatsappStatus):
        return Snapshot(
            perm_mic=PermissionStatus.GRANTED,
            perm_screen=PermissionStatus.GRANTED,
            perm_accessibility=PermissionStatus.GRANTED,
            device_input=DeviceStatus.DEFAULT_OK,
            network=NetworkStatus.ONLINE,
            first_run=False,
            app_mode=AppMode.SLEEPING,
            restart_pending=False,
            update_in_progress=False,
            whatsapp_status=whatsapp_status
        )

    def test_qr_required_decision(self):
        """Test that QR_REQUIRED status results in NOTIFY_USER decision."""
        print("\nTesting QR_REQUIRED status...")
        snapshot = self.create_snapshot(WhatsappStatus.QR_REQUIRED)
        decision = decide_whatsapp_action(snapshot)
        print(f"Decision for QR_REQUIRED: {decision}")
        self.assertEqual(decision, Decision.NOTIFY_USER, "Should notify user when QR is required")

    def test_connected_decision(self):
        """Test that CONNECTED status results in default decision (START)."""
        print("\nTesting CONNECTED status...")
        snapshot = self.create_snapshot(WhatsappStatus.CONNECTED)
        decision = decide_whatsapp_action(snapshot)
        print(f"Decision for CONNECTED: {decision}")
        # Assuming default is START as per decision_engine.py if no rules match
        self.assertEqual(decision, Decision.START, "Should default to START when connected (no specific rule)")

    def test_disconnected_decision(self):
        """Test that DISCONNECTED status results in default decision (START)."""
        print("\nTesting DISCONNECTED status...")
        snapshot = self.create_snapshot(WhatsappStatus.DISCONNECTED)
        decision = decide_whatsapp_action(snapshot)
        print(f"Decision for DISCONNECTED: {decision}")
        self.assertEqual(decision, Decision.START, "Should default to START when disconnected")

if __name__ == "__main__":
    unittest.main()
