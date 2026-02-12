"""
ContactResolver - модуль для получения имени контакта при обработке сообщения

Архитектура:
1. Кэширование для производительности
2. Многоуровневая система получения имени:
   - Messages.display_name (если пользователь задал имя чату)
   - AddressBook SQLite (локальная база контактов)
   - Contacts.framework через AppleScript (системные контакты)
   - Fallback на identifier

Использование:
    contact = resolve_contact(identifier="+14388554334")
    # Returns: {"display_label": "John Doe", "first_name": "John", ...}
"""

import json
import logging
from pathlib import Path
import re
import sqlite3
import subprocess
import time
from typing import Any

logger = logging.getLogger(__name__)

# Кэш для результатов резолвинга по номеру/email
_CONTACT_CACHE: dict[str, dict[str, Any]] = {}

# Кэш для результатов поиска по имени (с TTL)
_CONTACT_NAME_CACHE: dict[str, tuple[list[dict[str, Any]], float]] = {}
_CACHE_TTL = 300  # 5 минут в секундах

# Путь к базе данных контактов
CONTACTS_DB_PATH = (
    Path.home() / "Library" / "Application Support" / "AddressBook" / "AddressBook-v22.abcddb"
)


def normalize_identifier(identifier: str) -> str:
    """
    Нормализует идентификатор для поиска в кэше и базе данных.

    Args:
        identifier: Номер телефона или email

    Returns:
        str: Нормализованный идентификатор
    """
    # Для email - просто lowercase
    if "@" in identifier:
        return identifier.lower().strip()

    # Для телефона - оставляем только цифры (для сравнения)
    # Но сохраняем оригинальный формат для отображения
    return identifier.strip()


def normalize_phone_for_search(phone: str) -> str:
    """
    Нормализует телефонный номер для поиска (только цифры).

    Args:
        phone: Номер телефона

    Returns:
        str: Только цифры
    """
    return re.sub(r"\D", "", phone)


def get_name_from_messages_db(conn: sqlite3.Connection, identifier: str) -> dict[str, Any] | None:
    """
    Шаг 1: Получение имени из Messages (chat.display_name)

    Args:
        conn: Соединение с базой данных Messages
        identifier: Номер телефона или email

    Returns:
        Optional[Dict]: Информация о контакте или None
    """
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT DISTINCT c.display_name
            FROM chat c
            JOIN chat_handle_join chj ON chj.chat_id = c.ROWID
            JOIN handle h ON h.ROWID = chj.handle_id
            WHERE (h.id = ? OR h.uncanonicalized_id = ?)
            AND c.display_name IS NOT NULL
            AND c.display_name != ''
            LIMIT 1
        """,
            (identifier, identifier),
        )

        result = cursor.fetchone()
        if result and result[0]:
            display_name = result[0].strip()
            if display_name:
                logger.info(f"Имя найдено в Messages DB: {display_name}")
                return {
                    "display_label": display_name,
                    "first_name": None,
                    "last_name": None,
                    "source": "messages",
                    "raw_identifier": identifier,
                }
    except Exception as e:
        logger.error(f"Ошибка получения имени из Messages DB: {e}")

    return None


def get_name_from_addressbook_sqlite(identifier: str) -> dict[str, Any] | None:
    """
    Шаг 2A: Получение имени из AddressBook SQLite (локальная база)

    Args:
        identifier: Номер телефона или email

    Returns:
        Optional[Dict]: Информация о контакте или None
    """
    if not CONTACTS_DB_PATH.exists():
        return None

    try:
        conn = sqlite3.connect(str(CONTACTS_DB_PATH))
        cursor = conn.cursor()

        # Нормализуем для поиска
        if "@" in identifier:
            # Email поиск
            cursor.execute(
                """
                SELECT ZOWNER
                FROM ZABCDEMAILADDRESS
                WHERE ZADDRESS LIKE ?
                LIMIT 1
            """,
                (f"%{identifier}%",),
            )
        else:
            # Телефонный поиск
            normalized_digits = normalize_phone_for_search(identifier)

            # Ищем по полному номеру и по последним цифрам
            cursor.execute(
                """
                SELECT DISTINCT ZOWNER, ZFULLNUMBER
                FROM ZABCDPHONENUMBER
                WHERE REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(ZFULLNUMBER, ' ', ''), '-', ''), '(', ''), ')', ''), '+', ''), '.', '') LIKE ?
                   OR REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(ZFULLNUMBER, ' ', ''), '-', ''), '(', ''), ')', ''), '+', ''), '.', '') LIKE ?
                LIMIT 1
            """,
                (f"%{normalized_digits}%", f"%{normalized_digits[-10:]}%"),
            )

        result = cursor.fetchone()
        if result:
            owner_id = result[0]

            # Получаем имя контакта
            cursor.execute(
                """
                SELECT ZFIRSTNAME, ZLASTNAME, ZNICKNAME, ZMIDDLENAME, ZORGANIZATION
                FROM ZABCDRECORD
                WHERE Z_PK = ?
            """,
                (owner_id,),
            )

            name_result = cursor.fetchone()
            if name_result:
                first, last, nick, middle, org = name_result
                name_parts = [p for p in [first, middle, last, nick, org] if p]

                if name_parts:
                    display_label = " ".join(name_parts).strip()
                    if display_label:
                        logger.info(f"Имя найдено в AddressBook SQLite: {display_label}")
                        conn.close()
                        return {
                            "display_label": display_label,
                            "first_name": first,
                            "last_name": last,
                            "middle_name": middle,
                            "nickname": nick,
                            "organization": org,
                            "source": "contacts",
                            "raw_identifier": identifier,
                        }

        conn.close()
    except sqlite3.OperationalError as e:
        if "database is locked" not in str(e):
            logger.error(f"Ошибка доступа к AddressBook: {e}")
    except Exception as e:
        logger.error(f"Ошибка получения имени из AddressBook: {e}")

    return None


def get_name_from_contacts_framework(identifier: str) -> dict[str, Any] | None:
    """
    Шаг 2B: Получение имени через Contacts.framework (Swift helper)

    Это правильный способ, который работает с iCloud/Google контактами.
    Использует Swift helper для доступа к Contacts.framework.

    Args:
        identifier: Номер телефона или email

    Returns:
        Optional[Dict]: Информация о контакте или None
    """
    # Путь к Swift helper
    # Путь к Swift helper
    helper_path = Path(__file__).parent / "bin" / "contacts_helper"

    if not helper_path.exists():
        # Fallback на AppleScript, если Swift helper не найден
        logger.warning("Swift helper не найден, используем AppleScript")
        return get_name_from_contacts_framework_applescript(identifier)

    try:
        result = subprocess.run(
            [str(helper_path), identifier], capture_output=True, text=True, timeout=5
        )

        if result.returncode == 0:
            output = result.stdout.strip()
            if output and output != "{}":
                try:
                    contact_data = json.loads(output)

                    # Проверяем на ошибку
                    if "error" in contact_data:
                        logger.warning(f"Swift helper вернул ошибку: {contact_data['error']}")
                        return None

                    # Проверяем, что есть имя
                    display_label = contact_data.get("display_label")
                    if display_label:
                        logger.info(
                            f"Имя найдено через Contacts.framework (Swift): {display_label}"
                        )
                        return contact_data
                except json.JSONDecodeError as e:
                    logger.error(f"Ошибка парсинга JSON от Swift helper: {e}")
        else:
            error = result.stderr.strip()
            if error:
                logger.warning(f"Swift helper вернул ошибку: {error}")
    except subprocess.TimeoutExpired:
        logger.warning("Таймаут при получении имени через Contacts.framework (Swift)")
    except FileNotFoundError:
        logger.warning("Swift helper не найден, используем AppleScript")
        return get_name_from_contacts_framework_applescript(identifier)
    except Exception as e:
        logger.error(f"Ошибка получения имени через Contacts.framework (Swift): {e}")

    return None


def get_name_from_contacts_framework_applescript(identifier: str) -> dict[str, Any] | None:
    """
    Fallback: Получение имени через Contacts.framework (AppleScript)

    Используется, если Swift helper недоступен.

    Args:
        identifier: Номер телефона или email

    Returns:
        Optional[Dict]: Информация о контакте или None
    """
    try:
        # AppleScript для поиска контакта
        if "@" in identifier:
            # Поиск по email
            applescript = f'''
            tell application "Contacts"
                try
                    set contactList to (every person)
                    repeat with aPerson in contactList
                        set emailList to emails of aPerson
                        repeat with anEmail in emailList
                            set emailValue to value of anEmail as string
                            if emailValue contains "{identifier}" then
                                set contactName to name of aPerson
                                set firstName to first name of aPerson
                                set lastName to last name of aPerson
                                return contactName & "|" & firstName & "|" & lastName
                            end if
                        end repeat
                    end repeat
                    return ""
                on error
                    return ""
                end try
            end tell
            '''
        else:
            # Поиск по телефону
            applescript = f'''
            tell application "Contacts"
                try
                    set contactList to (every person)
                    repeat with aPerson in contactList
                        set phoneList to phones of aPerson
                        repeat with aPhone in phoneList
                            set phoneValue to value of aPhone as string
                            if phoneValue contains "{identifier}" or phoneValue contains "{identifier.replace("+", "")}" then
                                set contactName to name of aPerson
                                set firstName to first name of aPerson
                                set lastName to last name of aPerson
                                return contactName & "|" & firstName & "|" & lastName
                            end if
                        end repeat
                    end repeat
                    return ""
                on error
                    return ""
                end try
            end tell
            '''

        result = subprocess.run(
            ["osascript", "-e", applescript], capture_output=True, text=True, timeout=10
        )

        if result.returncode == 0:
            output = result.stdout.strip()
            if output and output != "":
                parts = output.split("|")
                if len(parts) >= 3:
                    full_name = parts[0]
                    first_name = parts[1] if parts[1] != "missing value" else None
                    last_name = parts[2] if parts[2] != "missing value" else None

                    if full_name and full_name != "missing value":
                        logger.info(
                            f"Имя найдено через Contacts.framework (AppleScript): {full_name}"
                        )
                        return {
                            "display_label": full_name,
                            "first_name": first_name,
                            "last_name": last_name,
                            "source": "contacts",
                            "raw_identifier": identifier,
                        }
    except subprocess.TimeoutExpired:
        logger.warning("Таймаут при получении имени через Contacts.framework (AppleScript)")
    except Exception as e:
        logger.error(f"Ошибка получения имени через Contacts.framework (AppleScript): {e}")

    return None


def find_contacts_by_name(name: str) -> list[dict[str, Any]]:
    """
    Находит все контакты с указанным именем через Swift helper.
    Использует кэширование с TTL для ускорения повторных запросов.

    Args:
        name: Имя для поиска

    Returns:
        List[Dict]: Список контактов с именами и номерами телефонов
    """
    # Нормализуем имя для кэша
    cache_key = name.lower().strip()
    current_time = time.time()

    # Проверка кэша
    if cache_key in _CONTACT_NAME_CACHE:
        contacts, cached_time = _CONTACT_NAME_CACHE[cache_key]
        if current_time - cached_time < _CACHE_TTL:
            logger.info(
                f"Использован кэш для поиска по имени '{name}' (возраст: {int(current_time - cached_time)}с)"
            )
            return contacts
        else:
            # Кэш устарел, удаляем
            logger.debug(f"Кэш для '{name}' устарел, обновляем")
            del _CONTACT_NAME_CACHE[cache_key]

    # Поиск через Swift helper
    # Поиск через Swift helper
    helper_path = Path(__file__).parent / "bin" / "find_contacts_by_name_swift"

    if not helper_path.exists():
        logger.warning("Swift helper для поиска по имени не найден")
        return []

    try:
        result = subprocess.run(
            [str(helper_path), name], capture_output=True, text=True, timeout=10
        )

        if result.returncode == 0:
            output = result.stdout.strip()
            if output and output != "[]":
                try:
                    contacts = json.loads(output)
                    if isinstance(contacts, list):
                        logger.info(f"Найдено контактов по имени '{name}': {len(contacts)}")
                        # Сохраняем в кэш
                        _CONTACT_NAME_CACHE[cache_key] = (contacts, current_time)
                        return contacts
                except json.JSONDecodeError as e:
                    logger.error(f"Ошибка парсинга JSON: {e}")
    except subprocess.TimeoutExpired:
        logger.warning("Таймаут при поиске контактов по имени")
    except Exception as e:
        logger.error(f"Ошибка поиска контактов по имени: {e}")

    # Сохраняем пустой результат в кэш, чтобы не искать повторно
    _CONTACT_NAME_CACHE[cache_key] = ([], current_time)
    return []


def resolve_contact(
    identifier: str, messages_conn: sqlite3.Connection | None = None
) -> dict[str, Any]:
    """
    Главная функция для получения информации о контакте.

    Проверяет все источники в порядке приоритета:
    1. Кэш
    2. Messages.display_name
    3. AddressBook SQLite
    4. Contacts.framework
    5. Fallback на identifier

    Args:
        identifier: Номер телефона или email
        messages_conn: Соединение с базой данных Messages (опционально)

    Returns:
        Dict: Информация о контакте
        {
            "display_label": "John Doe",  # Имя для отображения
            "first_name": "John",
            "last_name": "Doe",
            "source": "contacts",  # "messages" | "contacts" | "fallback"
            "raw_identifier": "+14388554334"
        }
    """
    # Нормализуем для кэша
    norm = normalize_identifier(identifier)

    # Шаг 0: Проверка кэша
    if norm in _CONTACT_CACHE:
        logger.debug(f"Имя найдено в кэше для {identifier}")
        return _CONTACT_CACHE[norm]

    # Шаг 1: Messages.display_name
    if messages_conn:
        contact = get_name_from_messages_db(messages_conn, identifier)
        if contact:
            _CONTACT_CACHE[norm] = contact
            return contact

    # Шаг 2A: AddressBook SQLite
    contact = get_name_from_addressbook_sqlite(identifier)
    if contact:
        _CONTACT_CACHE[norm] = contact
        return contact

    # Шаг 2B: Contacts.framework (правильный способ)
    contact = get_name_from_contacts_framework(identifier)
    if contact:
        _CONTACT_CACHE[norm] = contact
        return contact

    # Шаг 3: Fallback - используем identifier
    contact = {
        "display_label": identifier,
        "first_name": None,
        "last_name": None,
        "source": "fallback",
        "raw_identifier": identifier,
    }

    _CONTACT_CACHE[norm] = contact
    logger.info(f"Имя не найдено для {identifier}, используется fallback")
    return contact


def clear_cache() -> int:
    """
    Очищает кэш контактов (и резолвинга, и поиска по имени).

    Returns:
        int: Количество удаленных записей
    """
    global _CONTACT_CACHE, _CONTACT_NAME_CACHE
    count = len(_CONTACT_CACHE) + len(_CONTACT_NAME_CACHE)
    _CONTACT_CACHE.clear()
    _CONTACT_NAME_CACHE.clear()
    logger.info(f"Кэш очищен: удалено {count} записей")
    return count


def clear_contact_cache() -> int:
    """
    Алиас для clear_cache() для обратной совместимости.

    Returns:
        int: Количество удаленных записей
    """
    return clear_cache()


def clear_expired_cache() -> int:
    """
    Очищает устаревшие записи из кэша поиска по имени (TTL истек).

    Returns:
        int: Количество удаленных записей
    """
    global _CONTACT_NAME_CACHE
    current_time = time.time()
    expired_keys = [
        key
        for key, (_, cached_time) in _CONTACT_NAME_CACHE.items()
        if current_time - cached_time >= _CACHE_TTL
    ]

    for key in expired_keys:
        del _CONTACT_NAME_CACHE[key]

    if expired_keys:
        logger.info(f"Очищено устаревших записей из кэша: {len(expired_keys)}")

    return len(expired_keys)


def get_cache_size() -> int:
    """Возвращает общий размер кэша (резолвинг + поиск по имени)"""
    return len(_CONTACT_CACHE) + len(_CONTACT_NAME_CACHE)
