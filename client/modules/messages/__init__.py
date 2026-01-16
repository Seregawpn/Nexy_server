"""
Client-side Messages module for reading/sending messages and resolving contacts.
"""
from .messages_db import (
    check_db_access,
    connect_db,
    get_last_message,
    get_messages_by_contact,
    format_message_date
)
from .send_message import send_message_to_contact, send_message_via_applescript
from .contact_resolver import resolve_contact, find_contacts_by_name
