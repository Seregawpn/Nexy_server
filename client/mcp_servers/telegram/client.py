import logging
from typing import Any

from telethon import TelegramClient  # type: ignore
from telethon.sessions import StringSession  # type: ignore
from telethon.tl.types import Channel, Chat, User  # type: ignore

from .auth import DEFAULT_API_HASH, DEFAULT_API_ID, load_session

logger = logging.getLogger(__name__)

class TelegramWrapper:
    """Обертка над Telethon для упрощения операций."""
    
    def __init__(self):
        self.client: TelegramClient | None = None
        self._session_str = load_session()
        
    async def connect(self):
        """Подключается к Telegram используя сохраненную сессию."""
        if not self._session_str:
            raise ValueError("No session found. Please run setup_auth.py first.")
        
        # Используем StringSession для портативности
        # NOTE: API ID/HASH должны быть доступны. 
        # Если их нет в env, скрипт должен упасть или мы должны их пробросить.
        if not DEFAULT_API_ID or not DEFAULT_API_HASH:
             # Fallback для разработки/теста, но лучше требовать от юзера
             logger.warning("TELEGRAM_API_ID/HASH not set. Connection might fail if not embedded in session.")
             
        self.client = TelegramClient(
            StringSession(self._session_str),
            int(DEFAULT_API_ID or 0), 
            DEFAULT_API_HASH or "dummy"
        )
        if self.client:
            await self.client.connect()
        
        if self.client and not await self.client.is_user_authorized():
            raise PermissionError("Session invalid or unauthorized. Please re-run setup_auth.py.")
            
        logger.info("Connected to Telegram successfully.")

    async def disconnect(self):
        if self.client:
            await self.client.disconnect()

    async def get_dialogs(self, limit: int = 10) -> list[dict[str, Any]]:
        """Получает список диалогов."""
        if not self.client:
             raise RuntimeError("Client not connected")
             
        dialogs = []
        async for dialog in self.client.iter_dialogs(limit=limit):
            entity = dialog.entity
            name = dialog.name
            chat_id = dialog.id
            
            chat_type = "unknown"
            if isinstance(entity, User): chat_type = "user"
            elif isinstance(entity, Chat): chat_type = "group"
            elif isinstance(entity, Channel): chat_type = "channel"
            
            dialogs.append({
                "id": chat_id,
                "name": name,
                "type": chat_type,
                "unread_count": dialog.unread_count,
                 # "date": dialog.date.isoformat() if dialog.date else None
            })
        return dialogs

    async def get_messages(self, chat_id: int, limit: int = 10) -> list[dict[str, Any]]:
        """Получает сообщения из чата."""
        if not self.client:
             raise RuntimeError("Client not connected")

        messages = []
        # chat_id может быть int или username (str)
        # Telethon сам разберется, если передать int или entity
        async for message in self.client.iter_messages(chat_id, limit=limit):
            sender = await message.get_sender()
            sender_name = "Unknown"
            if sender:
                sender_name = getattr(sender, 'first_name', '') or getattr(sender, 'title', '')
                if getattr(sender, 'last_name', None):
                    sender_name += f" {sender.last_name}"
            
            messages.append({
                "id": message.id,
                "text": message.text or "",
                "sender_id": message.sender_id,
                "sender_name": sender_name.strip(),
                "date": message.date.isoformat(),
                "is_active": True # placeholder
            })
        return messages

    async def send_message(self, chat_id: Any, text: str) -> dict[str, Any]:
        """Отправляет сообщение."""
        if not self.client:
             raise RuntimeError("Client not connected")
             
        # Если chat_id похож на int в строке, конвертируем
        try:
            chat_id = int(chat_id)
        except (ValueError, TypeError):
            pass # Оставляем как есть (например username)

        sent = await self.client.send_message(chat_id, text)
        return {
            "id": sent.id,
            "chat_id": sent.chat_id,
            "date": sent.date.isoformat()
        }
