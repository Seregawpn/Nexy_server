"""
WhatsApp Client Module
"""
from .config import WhatsappConfig
from .mcp_client import (
    AmbiguousContactError,
    ContactNotFoundError,
    SimilarContactsFoundError,
    WhatsAppConnectionError,
    WhatsappMCPClient,
    WhatsAppNotAuthenticatedError,
    WhatsAppTimeoutError,
)
from .qr_viewer import QRViewer
from .service_manager import WhatsappServiceManager

__all__ = [
    'WhatsappServiceManager',
    'QRViewer',
    'WhatsappMCPClient',
    'WhatsappConfig',
    'AmbiguousContactError',
    'ContactNotFoundError',
    'SimilarContactsFoundError',
    'WhatsAppConnectionError',
    'WhatsAppNotAuthenticatedError',
    'WhatsAppTimeoutError',
]
