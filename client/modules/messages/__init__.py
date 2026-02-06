"""
Client-side Messages module for reading/sending messages and resolving contacts.
"""
from .contact_resolver import find_contacts_by_name, resolve_contact
from .messages_db import (
    check_db_access,
    connect_db,
    format_message_date,
    get_last_message,
    get_messages_by_contact,
)
from .send_message import send_message_to_contact, send_message_via_applescript

__all__ = [
    "find_contacts_by_name",
    "resolve_contact",
    "check_db_access",
    "connect_db",
    "format_message_date",
    "get_last_message",
    "get_messages_by_contact",
    "send_message_to_contact",
    "send_message_via_applescript",
]
