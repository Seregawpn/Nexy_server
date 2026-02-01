import os
from pathlib import Path
from typing import Optional, Tuple

from telethon.sync import TelegramClient
from telethon.sessions import StringSession

# Стандартный путь к сессии (в корне home, как попросил пользователь в чате, 
# или лучше скрытый файл. Используем скрытый для безопасности)
SESSION_FILE_PATH = Path.home() / ".telegram_mcp_session"

# Если пользователь захочет использовать API ID/Hash из переменных окружения
# Но для удобства можно зашить дефолтные (если это open source, лучше env)
# For now we assume user provides them or we load from .env
DEFAULT_API_ID = os.getenv("TELEGRAM_API_ID")
DEFAULT_API_HASH = os.getenv("TELEGRAM_API_HASH")

def get_session_path() -> Path:
    """Возвращает путь к файлу сессии."""
    return SESSION_FILE_PATH

def load_session() -> Optional[str]:
    """Загружает строку сессии из файла."""
    path = get_session_path()
    if not path.exists():
        return None
    try:
        return path.read_text().strip()
    except Exception:
        return None

def save_session(session_str: str):
    """Сохраняет строку сессии в файл."""
    path = get_session_path()
    # Ensure parent dir exists (it's home, so likely yes)
    # Set restrictive permissions
    path.write_text(session_str)
    os.chmod(path, 0o600)

def ensure_authorized(client: TelegramClient) -> bool:
    """Проверяет авторизацию клиента."""
    return client.is_user_authorized()
