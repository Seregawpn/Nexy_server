"""
Модуль для обработки ошибок MCP сервера Messages

Определяет специфичные типы ошибок для лучшей обработки и диагностики.
"""


class MessagesError(Exception):
    """Базовый класс для всех ошибок MCP сервера Messages"""

    pass


class ContactNotFoundError(MessagesError):
    """Ошибка: контакт не найден"""

    def __init__(self, contact: str, message: str | None = None):
        self.contact = contact
        if message is None:
            message = f"Contact '{contact}' not found"
        super().__init__(message)


class NoPhoneNumbersError(MessagesError):
    """Ошибка: у контакта нет номеров телефонов"""

    def __init__(self, contact: str, message: str | None = None):
        self.contact = contact
        if message is None:
            message = f"No phone numbers found for contact '{contact}'"
        super().__init__(message)


class MessageSendError(MessagesError):
    """Ошибка: не удалось отправить сообщение"""

    def __init__(self, phone_number: str, reason: str, message: str | None = None):
        self.phone_number = phone_number
        self.reason = reason
        if message is None:
            message = f"Failed to send message to {phone_number}: {reason}"
        super().__init__(message)


class DatabaseError(MessagesError):
    """Ошибка: проблема с базой данных"""

    def __init__(self, operation: str, reason: str, message: str | None = None):
        self.operation = operation
        self.reason = reason
        if message is None:
            message = f"Database error during {operation}: {reason}"
        super().__init__(message)


class PermissionError(MessagesError):
    """Ошибка: недостаточно разрешений"""

    def __init__(self, permission: str, message: str | None = None):
        self.permission = permission
        if message is None:
            message = f"Permission denied: {permission}. Please grant Full Disk Access."
        super().__init__(message)


class ContactResolverError(MessagesError):
    """Ошибка: проблема при резолвинге контакта"""

    def __init__(self, identifier: str, reason: str, message: str | None = None):
        self.identifier = identifier
        self.reason = reason
        if message is None:
            message = f"Failed to resolve contact '{identifier}': {reason}"
        super().__init__(message)
