#!/usr/bin/env python3
"""
Модуль для работы с базой данных Messages на macOS

Этот модуль предоставляет функции для:
- Подключения к базе данных chat.db
- Чтения структуры базы данных
- Работы с контактами и сообщениями
"""

import logging
from pathlib import Path
import re
import sqlite3
from typing import Any

# Импортируем новый ContactResolver
try:
    from .contact_resolver import resolve_contact
except ImportError:
    # Если модуль не найден, используем простую функцию
    def resolve_contact(identifier, messages_conn=None):
        return {"display_label": identifier, "source": "fallback", "raw_identifier": identifier}


logger = logging.getLogger(__name__)

# Путь к базе данных Messages
MESSAGES_DB_PATH = Path.home() / "Library" / "Messages" / "chat.db"


def get_db_path() -> Path:
    """
    Возвращает путь к базе данных Messages.

    Returns:
        Path: Путь к файлу chat.db
    """
    return MESSAGES_DB_PATH


def check_db_access() -> tuple[bool, str | None]:
    """
    Проверяет доступность базы данных Messages.

    Returns:
        tuple[bool, Optional[str]]: (доступна, сообщение об ошибке)
    """
    db_path = get_db_path()

    # Проверка существования файла
    if not db_path.exists():
        error_msg = f"База данных не найдена: {db_path}"
        logger.error(error_msg)
        return False, error_msg

    # Проверка прав на чтение
    if not db_path.is_file():
        error_msg = f"Путь не является файлом: {db_path}"
        logger.error(error_msg)
        return False, error_msg

    # Попытка открыть файл
    try:
        with open(db_path, "rb"):
            pass
    except PermissionError:
        error_msg = "Нет прав доступа к базе данных. Требуется Full Disk Access."
        logger.error(error_msg)
        return False, error_msg
    except Exception as e:
        error_msg = f"Ошибка доступа к базе данных: {e}"
        logger.error(error_msg)
        return False, error_msg

    logger.info(f"База данных доступна: {db_path}")
    return True, None


def connect_db() -> sqlite3.Connection | None:
    """
    Подключается к базе данных Messages.

    Returns:
        Optional[sqlite3.Connection]: Соединение с БД или None при ошибке
    """
    # Проверка доступа
    accessible, error_msg = check_db_access()
    if not accessible:
        logger.error(f"Не удалось подключиться: {error_msg}")
        return None

    db_path = get_db_path()

    try:
        # Подключение в режиме только для чтения
        # Используем URI с флагом mode=ro для безопасности
        conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
        conn.row_factory = sqlite3.Row  # Для доступа к колонкам по имени
        logger.info("Успешное подключение к базе данных")
        return conn
    except sqlite3.Error as e:
        logger.error(f"Ошибка SQLite при подключении: {e}")
        return None
    except Exception as e:
        logger.error(f"Неожиданная ошибка при подключении: {e}")
        return None


def get_tables(conn: sqlite3.Connection) -> list[str]:
    """
    Возвращает список всех таблиц в базе данных.

    Args:
        conn: Соединение с базой данных

    Returns:
        list[str]: Список имен таблиц
    """
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT name 
            FROM sqlite_master 
            WHERE type='table' 
            ORDER BY name
        """)
        tables = [row[0] for row in cursor.fetchall()]
        logger.info(f"Найдено таблиц: {len(tables)}")
        return tables
    except sqlite3.Error as e:
        logger.error(f"Ошибка при получении списка таблиц: {e}")
        return []


def get_table_schema(conn: sqlite3.Connection, table_name: str) -> list[dict[str, Any]]:
    """
    Возвращает схему таблицы (список колонок с их типами).

    Args:
        conn: Соединение с базой данных
        table_name: Имя таблицы

    Returns:
        list[dict]: Список словарей с информацией о колонках
        Каждый словарь содержит: name, type, notnull, default_value, pk
    """
    try:
        cursor = conn.cursor()
        cursor.execute(f"PRAGMA table_info({table_name})")

        columns = []
        for row in cursor.fetchall():
            columns.append(
                {
                    "name": row[1],  # cid, name, type, notnull, dflt_value, pk
                    "type": row[2],
                    "notnull": bool(row[3]),
                    "default_value": row[4],
                    "pk": bool(row[5]),
                }
            )

        logger.info(f"Схема таблицы '{table_name}': {len(columns)} колонок")
        return columns
    except sqlite3.Error as e:
        logger.error(f"Ошибка при получении схемы таблицы '{table_name}': {e}")
        return []


def test_connection() -> dict[str, Any]:
    """
    Тестирует подключение к базе данных и возвращает информацию о ней.

    Returns:
        dict: Словарь с результатами теста
    """
    result = {
        "success": False,
        "db_path": str(get_db_path()),
        "accessible": False,
        "tables": [],
        "error": None,
    }

    # Проверка доступа
    accessible, error_msg = check_db_access()
    result["accessible"] = accessible

    if not accessible:
        result["error"] = error_msg
        return result

    # Подключение
    conn = connect_db()
    if not conn:
        result["error"] = "Не удалось подключиться к базе данных"
        return result

    try:
        # Получение списка таблиц
        tables = get_tables(conn)
        result["tables"] = tables

        # Проверка наличия ключевых таблиц
        key_tables = ["handle", "chat", "message", "chat_handle_join", "chat_message_join"]
        missing_tables = [t for t in key_tables if t not in tables]

        if missing_tables:
            result["warning"] = f"Отсутствуют ключевые таблицы: {missing_tables}"
        else:
            result["success"] = True

        logger.info("Тест подключения завершен успешно")

    except Exception as e:
        result["error"] = f"Ошибка при тестировании: {e}"
        logger.error(f"Ошибка при тестировании: {e}")
    finally:
        conn.close()

    return result


def find_contact_exact(conn: sqlite3.Connection, query: str) -> list[dict[str, Any]]:
    """
    Находит контакт по точному совпадению номера телефона или email.

    Args:
        conn: Соединение с базой данных
        query: Номер телефона или email для поиска

    Returns:
        List[Dict[str, Any]]: Список найденных контактов
        Каждый контакт содержит: ROWID, id, service, uncanonicalized_id, display_name
    """
    try:
        cursor = conn.cursor()

        # Поиск по точному совпадению в id или uncanonicalized_id
        # Также получаем display_name из связанного чата
        cursor.execute(
            """
            SELECT DISTINCT
                h.ROWID,
                h.id,
                h.service,
                h.uncanonicalized_id,
                h.country,
                c.display_name
            FROM handle h
            LEFT JOIN chat_handle_join chj ON h.ROWID = chj.handle_id
            LEFT JOIN chat c ON chj.chat_id = c.ROWID
            WHERE h.id = ? OR h.uncanonicalized_id = ?
            LIMIT 10
        """,
            (query, query),
        )

        contacts = []
        for row in cursor.fetchall():
            contact_data = {
                "ROWID": row[0],
                "id": row[1],
                "service": row[2],
                "uncanonicalized_id": row[3],
                "country": row[4],
                "display_name": row[5],
            }

            # Если display_name пустое, пробуем получить имя из других источников
            if not contact_data.get("display_name"):
                try:
                    contact_info = resolve_contact(contact_data["id"], messages_conn=conn)
                    if (
                        contact_info.get("display_label")
                        and contact_info.get("display_label") != contact_data["id"]
                    ):
                        contact_data["display_name"] = contact_info["display_label"]
                        logger.info(
                            f"Имя получено из {contact_info.get('source')}: {contact_info.get('display_label')}"
                        )
                except Exception as e:
                    logger.warning(f"Не удалось получить имя из альтернативных источников: {e}")

            contacts.append(contact_data)

        logger.info(f"Найдено контактов для '{query}': {len(contacts)}")
        return contacts

    except sqlite3.Error as e:
        logger.error(f"Ошибка SQLite при поиске контакта: {e}")
        return []
    except Exception as e:
        logger.error(f"Неожиданная ошибка при поиске контакта: {e}")
        return []


def find_contact_by_name(conn: sqlite3.Connection, name: str) -> list[dict[str, Any]]:
    """
    Находит контакты по имени (поиск в display_name).

    Args:
        conn: Соединение с базой данных
        name: Имя для поиска (частичное совпадение)

    Returns:
        List[Dict[str, Any]]: Список найденных контактов
        Каждый контакт содержит: ROWID, id, service, display_name
    """
    try:
        cursor = conn.cursor()

        # Поиск по имени в display_name (частичное совпадение, нечувствительно к регистру)
        cursor.execute(
            """
            SELECT DISTINCT
                h.ROWID,
                h.id,
                h.service,
                h.uncanonicalized_id,
                h.country,
                c.display_name
            FROM handle h
            JOIN chat_handle_join chj ON h.ROWID = chj.handle_id
            JOIN chat c ON chj.chat_id = c.ROWID
            WHERE c.display_name LIKE ? COLLATE NOCASE
            ORDER BY c.display_name
            LIMIT 20
        """,
            (f"%{name}%",),
        )

        contacts = []
        for row in cursor.fetchall():
            contacts.append(
                {
                    "ROWID": row[0],
                    "id": row[1],
                    "service": row[2],
                    "uncanonicalized_id": row[3],
                    "country": row[4],
                    "display_name": row[5],
                }
            )

        logger.info(f"Найдено контактов по имени '{name}': {len(contacts)}")
        return contacts

    except sqlite3.Error as e:
        logger.error(f"Ошибка SQLite при поиске контакта по имени: {e}")
        return []
    except Exception as e:
        logger.error(f"Неожиданная ошибка при поиске контакта по имени: {e}")
        return []


def find_contact(conn: sqlite3.Connection, query: str) -> list[dict[str, Any]]:
    """
    Универсальная функция поиска контакта.
    Пытается найти по номеру/email, если не найдено - ищет по имени.

    Args:
        conn: Соединение с базой данных
        query: Номер телефона, email или имя для поиска

    Returns:
        List[Dict[str, Any]]: Список найденных контактов
    """
    # Сначала пробуем точный поиск по номеру/email
    contacts = find_contact_exact(conn, query)

    # Если не найдено, пробуем поиск по имени
    if not contacts:
        contacts = find_contact_by_name(conn, query)

    return contacts


def format_contact_info(contact: dict[str, Any]) -> str:
    """
    Форматирует информацию о контакте для вывода.

    Args:
        contact: Словарь с информацией о контакте

    Returns:
        str: Отформатированная строка с информацией о контакте
    """
    lines = []

    # Имя контакта (если есть)
    display_name = contact.get("display_name")
    if display_name:
        lines.append(f"Name: {display_name}")

    # ID контакта
    contact_id = contact.get("id", "Unknown")
    lines.append(f"ID: {contact_id}")

    # Сервис
    service = contact.get("service", "Unknown")
    service_name = "iMessage" if service == "iMessage" else service
    lines.append(f"Service: {service_name}")

    # Uncanonicalized ID (если отличается от id)
    uncanonicalized = contact.get("uncanonicalized_id")
    if uncanonicalized and uncanonicalized != contact_id:
        lines.append(f"Original ID: {uncanonicalized}")

    # Страна (если есть)
    country = contact.get("country")
    if country:
        lines.append(f"Country: {country}")

    return "\n".join(lines)


def get_last_message(conn: sqlite3.Connection) -> dict[str, Any] | None:
    """
    Получает последнее сообщение из всех чатов.

    Args:
        conn: Соединение с базой данных

    Returns:
        Optional[Dict[str, Any]]: Последнее сообщение или None
        Сообщение содержит: ROWID, text, date, is_from_me, handle_id, contact_id, display_name
    """
    try:
        cursor = conn.cursor()

        # SQL запрос для получения последнего сообщения из всех чатов
        cursor.execute("""
            SELECT 
                m.ROWID,
                m.text,
                m.attributedBody,
                m.date,
                m.is_from_me,
                m.handle_id,
                h.id as contact_id,
                c.display_name,
                c.chat_identifier,
                c.service_name,
                c.room_name
            FROM message m
            JOIN chat_message_join cmj ON m.ROWID = cmj.message_id
            JOIN chat_handle_join chj ON cmj.chat_id = chj.chat_id
            JOIN handle h ON chj.handle_id = h.ROWID
            LEFT JOIN chat c ON cmj.chat_id = c.ROWID
            ORDER BY m.date DESC
            LIMIT 1
        """)

        row = cursor.fetchone()
        if not row:
            return None

        # Извлечение текста
        text = row[1]  # text field
        attributed_body = row[2]  # attributedBody field

        # ⚠️ CRITICAL: Если текста нет, пробуем извлечь из attributedBody
        if not text and attributed_body:
            extracted_text = extract_text_from_attributed_body(attributed_body)
            if extracted_text:
                text = extracted_text
                logger.debug(
                    f"Extracted text from attributedBody in get_last_message: {text[:50]}..."
                )

        message = {
            "ROWID": row[0],
            "text": text or "",
            "attributed_body": attributed_body,  # Сохраняем для повторной попытки в format_messages
            "date": row[3],
            "is_from_me": bool(row[4]),
            "handle_id": row[5],
            "contact_id": row[6],
            "display_name": row[7],
            "chat_identifier": row[8],
            "service_name": row[9],
            "room_name": row[10],
        }

        logger.info(f"Найдено последнее сообщение от {message['contact_id']}")
        return message

    except sqlite3.Error as e:
        logger.error(f"Ошибка SQLite при получении последнего сообщения: {e}")
        return None
    except Exception as e:
        logger.error(f"Неожиданная ошибка при получении последнего сообщения: {e}")
        return None


def get_phone_with_last_message(conn: sqlite3.Connection, phone_numbers: list[str]) -> str | None:
    """
    Определяет номер телефона, от которого было последнее сообщение.
    Используется для умного выбора номера при нескольких номерах у контакта.

    Args:
        conn: Соединение с базой данных
        phone_numbers: Список номеров телефонов для проверки

    Returns:
        Optional[str]: Номер телефона с последним сообщением или None
    """
    if not phone_numbers:
        return None

    try:
        cursor = conn.cursor()

        # Создаем плейсхолдеры для IN запроса
        placeholders = ",".join(["?" for _ in phone_numbers])

        # SQL запрос для получения последнего сообщения от любого из номеров
        cursor.execute(
            f"""
            SELECT 
                h.id as contact_id,
                MAX(m.date) as last_message_date
            FROM message m
            JOIN chat_message_join cmj ON m.ROWID = cmj.message_id
            JOIN chat_handle_join chj ON cmj.chat_id = chj.chat_id
            JOIN handle h ON chj.handle_id = h.ROWID
            WHERE (h.id IN ({placeholders}) OR h.uncanonicalized_id IN ({placeholders}))
            GROUP BY h.id
            ORDER BY last_message_date DESC
            LIMIT 1
        """,
            phone_numbers + phone_numbers,
        )

        row = cursor.fetchone()
        if row and row[0]:
            selected_phone = row[0]
            logger.info(f"Выбран номер с последним сообщением: {selected_phone}")
            return selected_phone

        # Если сообщений нет, возвращаем первый номер
        logger.info(f"Сообщений не найдено, используем первый номер: {phone_numbers[0]}")
        return phone_numbers[0]

    except sqlite3.Error as e:
        logger.error(f"Ошибка SQLite при выборе номера: {e}")
        return phone_numbers[0] if phone_numbers else None
    except Exception as e:
        logger.error(f"Неожиданная ошибка при выборе номера: {e}")
        return phone_numbers[0] if phone_numbers else None


def get_messages_by_contact(
    conn: sqlite3.Connection, contact_id: str, limit: int = 10
) -> list[dict[str, Any]]:
    """
    Получает последние сообщения из чата с контактом.

    Args:
        conn: Соединение с базой данных
        contact_id: Номер телефона или email контакта
        limit: Максимальное количество сообщений (по умолчанию 10)

    Returns:
        List[Dict[str, Any]]: Список сообщений
        Каждое сообщение содержит: ROWID, text, date, is_from_me, handle_id, contact_id, display_name
    """
    try:
        cursor = conn.cursor()

        # SQL запрос для получения сообщений
        # Связываем message -> chat_message_join -> chat -> chat_handle_join -> handle
        cursor.execute(
            """
            SELECT 
                m.ROWID,
                m.text,
                m.attributedBody,
                m.date,
                m.is_from_me,
                m.handle_id,
                h.id as contact_id,
                c.display_name,
                c.chat_identifier,
                c.service_name,
                c.room_name
            FROM message m
            JOIN chat_message_join cmj ON m.ROWID = cmj.message_id
            JOIN chat_handle_join chj ON cmj.chat_id = chj.chat_id
            JOIN handle h ON chj.handle_id = h.ROWID
            LEFT JOIN chat c ON cmj.chat_id = c.ROWID
            WHERE (h.id = ? OR h.uncanonicalized_id = ?)
            ORDER BY m.date DESC
            LIMIT ?
        """,
            (contact_id, contact_id, limit),
        )

        messages = []
        for row in cursor.fetchall():
            # Извлекаем текст - сначала из text, если нет - из attributedBody
            text = row[1]  # text field
            attributed_body = row[2]  # attributedBody field

            # ⚠️ CRITICAL: Если текста нет, пробуем извлечь из attributedBody
            # Это важно для медиа-сообщений, которые могут содержать текст в attributedBody
            if not text and attributed_body:
                extracted_text = extract_text_from_attributed_body(attributed_body)
                if extracted_text:
                    text = extracted_text
                    logger.debug(f"Extracted text from attributedBody: {text[:50]}...")

            # ⚠️ CRITICAL: Сохраняем attributedBody для последующего извлечения в format_messages
            # Это позволяет повторно попытаться извлечь текст, если первая попытка не удалась
            messages.append(
                {
                    "ROWID": row[0],
                    "text": text or "",  # Может быть пустым, если не удалось извлечь
                    "attributed_body": attributed_body,  # Сохраняем для повторной попытки
                    "date": row[3],  # Unix timestamp в наносекундах
                    "is_from_me": bool(row[4]),
                    "handle_id": row[5],
                    "contact_id": row[6],
                    "display_name": row[7],
                    "chat_identifier": row[8],
                    "service_name": row[9],
                    "room_name": row[10],  # Для групповых чатов
                }
            )

        logger.info(f"Найдено сообщений для контакта '{contact_id}': {len(messages)}")
        return messages

    except sqlite3.Error as e:
        logger.error(f"Ошибка SQLite при получении сообщений: {e}")
        return []
    except Exception as e:
        logger.error(f"Неожиданная ошибка при получении сообщений: {e}")
        return []


def format_message_date(timestamp_ns: int) -> str:
    """
    Форматирует дату из наносекунд в читаемый формат.

    Args:
        timestamp_ns: Unix timestamp в наносекундах

    Returns:
        str: Отформатированная дата и время (YYYY-MM-DD HH:MM:SS)
    """
    try:
        # Конвертируем из наносекунд в секунды
        timestamp_seconds = timestamp_ns / 1_000_000_000

        from datetime import datetime

        dt = datetime.fromtimestamp(timestamp_seconds)
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    except (ValueError, OSError) as e:
        logger.error(f"Ошибка форматирования даты: {e}")
        return "Unknown date"


def format_message_date_nice(timestamp_ns: int) -> tuple[str, str]:
    """
    Форматирует дату в красивый формат с отдельной датой и временем.

    Args:
        timestamp_ns: Unix timestamp в наносекундах

    Returns:
        tuple[str, str]: (дата, время) - например ("2024-01-15", "14:30")
    """
    try:
        timestamp_seconds = timestamp_ns / 1_000_000_000
        from datetime import datetime

        dt = datetime.fromtimestamp(timestamp_seconds)
        date_str = dt.strftime("%Y-%m-%d")
        time_str = dt.strftime("%H:%M")
        return date_str, time_str
    except (ValueError, OSError) as e:
        logger.error(f"Ошибка форматирования даты: {e}")
        return "Unknown", "date"


def extract_text_from_attributed_body(attributed_body: bytes) -> str | None:
    """
    Извлекает текст из attributedBody (NSKeyedArchiver формат).

    В macOS Messages, даже медиа-сообщения могут содержать текст в attributedBody.
    Эта функция пытается извлечь читаемый текст различными методами.

    Args:
        attributed_body: Бинарные данные attributedBody

    Returns:
        Optional[str]: Извлеченный текст или None
    """
    if not attributed_body:
        return None

    try:
        # Декодируем как UTF-8 с игнорированием ошибок
        decoded = attributed_body.decode("utf-8", errors="ignore")

        # ⚠️ DEBUG: Логируем первые 200 символов для отладки
        logger.debug(f"AttributedBody decoded (first 200 chars): {decoded[:200]}")

        # Метод 0: Прямой поиск читаемого текста (самый простой)
        # Ищем последовательности из 2+ слов, разделенных пробелами
        # Это часто работает для простых текстовых сообщений
        pattern0 = r"\b([a-zA-Zа-яА-ЯёЁ]{2,}(?:\s+[a-zA-Zа-яА-ЯёЁ]{2,}){1,})\b"
        matches0 = re.findall(pattern0, decoded)
        if matches0:
            valid_phrases = []
            for phrase in matches0:
                phrase_clean = phrase.strip()
                # Фильтруем технические термины
                if (
                    len(phrase_clean) > 4
                    and not phrase_clean.lower().startswith("ns")
                    and "streamtyped" not in phrase_clean.lower()
                    and "streamtype" not in phrase_clean.lower()
                    and "attribute" not in phrase_clean.lower()
                    and "dictionary" not in phrase_clean.lower()
                ):
                    valid_phrases.append(phrase_clean)

            if valid_phrases:
                text = max(valid_phrases, key=len)
                logger.info(f"Extracted text via method 0 (direct): {text[:100]}...")
                return text

        # Метод 0.5: Поиск отдельных слов после "+" в формате NSKeyedArchiver
        # Формат: +[байт_длины][текст][маркер]
        # Ищем паттерн: +[байт][текст_из_букв][нечитаемый_символ]
        pattern0_5 = r"\+\x07([A-Za-zа-яА-ЯёЁ]{3,})[\x00-\x1f]"
        matches0_5 = re.findall(pattern0_5, decoded)
        if matches0_5:
            for match in matches0_5:
                if (
                    len(match) >= 3
                    and "streamtyped" not in match.lower()
                    and not match.startswith("NS")
                ):
                    logger.info(
                        f"Extracted text via method 0.5 (NSKeyedArchiver format): {match[:100]}..."
                    )
                    return match

        # Метод 0.6: Более гибкий поиск - ищем текст после "+" с любым байтом длины
        # Паттерн: +[байт_0x01-0x20][текст_из_букв][нечитаемый_символ]
        pattern0_6 = r"\+[\x01-\x20]([A-Za-zа-яА-ЯёЁ]{2,})[\x00-\x1fNS]"
        matches0_6 = re.findall(pattern0_6, decoded)
        if matches0_6:
            for match in matches0_6:
                if (
                    len(match) >= 2
                    and "streamtyped" not in match.lower()
                    and not match.startswith("NS")
                ):
                    logger.info(
                        f"Extracted text via method 0.6 (flexible NSKeyedArchiver): {match[:100]}..."
                    )
                    return match

        # Метод 1: Ищем текст после "+" в формате NSString
        # В NSKeyedArchiver текст часто идет после "+" и перед служебными символами
        # ⚠️ CRITICAL: Улучшенный паттерн - ищем текст после "+" до любого нечитаемого символа
        # Паттерн: +[читаемый_текст][нечитаемый_символ или конец]
        pattern1 = r"\+([a-zA-Zа-яА-ЯёЁ][a-zA-Zа-яА-ЯёЁ\s\.,!?;:\-\(\)\[\]@#\$%&\*\+\=\<\>\/\\0-9]{0,}?)(?:[^\w\s\.,!?;:\-\(\)\[\]@#\$%&\*\+\=\<\>\/\\]|NS|iI|$)"
        matches = re.findall(pattern1, decoded)
        if matches:
            # Фильтруем - убираем служебные строки
            valid_texts = []
            for match in matches:
                # Убираем служебные маркеры и невидимые символы
                cleaned = re.sub(r"[^\w\s\.,!?;:\-\(\)\[\]@#\$%&\*\+\=\<\>\/\\]", "", match)
                cleaned = cleaned.strip()

                # Проверяем, что это не служебная строка
                # ⚠️ CRITICAL: Разрешаем короткие тексты (минимум 2 символа)
                if (
                    len(cleaned) >= 2
                    and not cleaned.startswith("NS")
                    and not cleaned.startswith("kIM")
                    and not cleaned.startswith("__")
                    and "streamtyped" not in cleaned.lower()
                    and "streamtype" not in cleaned.lower()
                    and "Attribute" not in cleaned
                    and "Dictionary" not in cleaned
                    and "Number" not in cleaned
                    and "Value" not in cleaned
                    and
                    # Проверяем, что это не только технические символы
                    len(re.findall(r"[a-zA-Zа-яА-ЯёЁ]", cleaned)) >= 1
                ):  # Минимум 1 буква
                    valid_texts.append(cleaned)

            if valid_texts:
                # Берем самую длинную валидную строку
                text = max(valid_texts, key=len)
                if len(text) >= 2:
                    logger.info(f"Extracted text via method 1: {text[:100]}...")
                    return text

        # Метод 1.5: Более простой паттерн - ищем текст между "+" и следующими техническими маркерами
        # Паттерн: +[текст][технический_маркер]
        pattern1_5 = r"\+([a-zA-Zа-яА-ЯёЁ][a-zA-Zа-яА-ЯёЁ\s\.,!?;:\-\(\)\[\]@#\$%&\*\+\=\<\>\/\\]{0,}?)(?:[\x00-\x1f]|NS|iI|kIM|__)"
        matches = re.findall(pattern1_5, decoded)
        if matches:
            valid_texts = []
            for match in matches:
                cleaned = match.strip()
                if (
                    len(cleaned) >= 2
                    and not cleaned.startswith("NS")
                    and "streamtyped" not in cleaned.lower()
                    and len(re.findall(r"[a-zA-Zа-яА-ЯёЁ]", cleaned)) >= 1
                ):
                    valid_texts.append(cleaned)

            if valid_texts:
                text = max(valid_texts, key=len)
                logger.info(f"Extracted text via method 1.5: {text[:100]}...")
                return text

        # Метод 2: Ищем читаемые фразы (слова с пробелами)
        # Ищем последовательности из 2+ слов
        pattern2 = r"\b([a-zA-Zа-яА-ЯёЁ]{2,}(?:\s+[a-zA-Zа-яА-ЯёЁ]{2,}){1,})\b"
        matches = re.findall(pattern2, decoded)
        if matches:
            # Фильтруем служебные строки
            valid_phrases = []
            for phrase in matches:
                phrase_clean = phrase.strip()
                if (
                    len(phrase_clean) > 5
                    and not phrase_clean.startswith("NS")
                    and not phrase_clean.startswith("kIM")
                    and "Attribute" not in phrase_clean
                    and "Dictionary" not in phrase_clean
                ):
                    valid_phrases.append(phrase_clean)

            if valid_phrases:
                # Берем самую длинную фразу
                text = max(valid_phrases, key=len)
                logger.debug(f"Extracted text via method 2: {text[:100]}...")
                return text

        # Метод 3: Ищем участки с читаемым текстом между служебными маркерами
        # Ищем последовательности символов, которые выглядят как текст
        # Паттерн: ищем участки с буквами, цифрами, пробелами и пунктуацией
        pattern3 = r"[a-zA-Zа-яА-ЯёЁ0-9\s\.,!?;:\-\(\)\[\]@#\$%&\*\+\=\<\>\/\\]{10,}"
        matches = re.findall(pattern3, decoded)
        if matches:
            valid_texts = []
            technical_terms = [
                "streamtyped",
                "streamtype",
                "NSKeyedArchiver",
                "NSArchiver",
                "NSAttributedString",
            ]
            for match in matches:
                # Фильтруем служебные строки и технические термины
                match_lower = match.lower()
                if (
                    len(match.strip()) > 10
                    and not match.strip().startswith("NS")
                    and not any(term in match_lower for term in technical_terms)
                    and not "Attribute" in match
                    and not "Dictionary" in match
                    and
                    # Проверяем, что есть хотя бы несколько букв
                    len(re.findall(r"[a-zA-Zа-яА-ЯёЁ]", match)) > 5
                ):
                    valid_texts.append(match.strip())

            if valid_texts:
                # Берем самую длинную валидную строку
                text = max(valid_texts, key=len)
                logger.debug(f"Extracted text via method 3: {text[:100]}...")
                return text

        # Метод 4: Простое извлечение - ищем участки с читаемым текстом
        # Разбиваем на слова и собираем в фразы
        words = re.findall(r"\b[a-zA-Zа-яА-ЯёЁ]{3,}\b", decoded)
        # Фильтруем служебные слова и технические термины
        technical_words = [
            "NSString",
            "NSObject",
            "NSDictionary",
            "NSNumber",
            "NSValue",
            "NSAttributedString",
            "kIMMessagePartAttributeName",
            "streamtyped",
            "streamtype",
            "stream",
            "typed",
            "type",
            "NSKeyedArchiver",
            "NSArchiver",
            "NSData",
            "NSMutable",
            "kIM",
            "IM",
            "Message",
            "Attribute",
            "Dictionary",
            "Number",
            "Value",
            "Object",
            "String",
            "Data",
            "Archiver",
        ]
        filtered_words = [
            w for w in words if w not in technical_words and not w.lower().startswith("ns")
        ]
        if len(filtered_words) > 2:
            # Объединяем слова в текст (берем первые 20 слов)
            text = " ".join(filtered_words[:20])
            logger.debug(f"Extracted text via method 4: {text[:100]}...")
            return text.strip()

        # Метод 5: Попытка найти любые читаемые слова (последняя попытка)
        # Ищем любые слова длиной 4+ символов, которые не являются техническими
        words = re.findall(r"\b[a-zA-Zа-яА-ЯёЁ]{4,}\b", decoded)
        technical_words_lower = [
            w.lower()
            for w in [
                "NSString",
                "NSObject",
                "NSDictionary",
                "NSNumber",
                "NSValue",
                "NSAttributedString",
                "kIMMessagePartAttributeName",
                "streamtyped",
                "streamtype",
                "stream",
                "typed",
                "type",
                "NSKeyedArchiver",
                "NSArchiver",
                "NSData",
                "NSMutable",
                "kIM",
                "IM",
                "Message",
                "Attribute",
                "Dictionary",
                "Number",
                "Value",
                "Object",
                "String",
                "Data",
                "Archiver",
            ]
        ]
        filtered_words = [
            w
            for w in words
            if w.lower() not in technical_words_lower and not w.lower().startswith("ns")
        ]

        if len(filtered_words) >= 2:
            # Объединяем слова в текст (берем первые 30 слов)
            text = " ".join(filtered_words[:30])
            logger.info(f"Extracted text via method 5 (fallback): {text[:100]}...")
            return text.strip()

        logger.warning(
            f"Could not extract text from attributedBody using any method. Decoded preview: {decoded[:100]}"
        )
        return None

    except Exception as e:
        logger.error(f"Ошибка извлечения текста из attributedBody: {e}", exc_info=True)
        return None


def format_date_header(date_str: str) -> str:
    """
    Форматирует заголовок даты для группировки сообщений.

    Args:
        date_str: Дата в формате YYYY-MM-DD

    Returns:
        str: Отформатированный заголовок даты
    """
    try:
        from datetime import datetime

        dt = datetime.strptime(date_str, "%Y-%m-%d")
        today = datetime.now().date()
        msg_date = dt.date()

        # Определяем относительную дату
        if msg_date == today:
            return "Today"
        elif msg_date == today.replace(day=today.day - 1):
            return "Yesterday"
        else:
            # Форматируем как "Monday, January 15, 2024"
            return dt.strftime("%A, %B %d, %Y")
    except Exception:
        return date_str


def format_messages(
    messages: list[dict[str, Any]],
    contact_name: str | None = None,
    group_by_date: bool = True,
    show_chat_info: bool = True,
    messages_conn: sqlite3.Connection | None = None,
) -> str:
    """
    Форматирует список сообщений для вывода с улучшенным форматированием.

    Args:
        messages: Список сообщений
        contact_name: Имя контакта (опционально)
        group_by_date: Группировать сообщения по датам (по умолчанию True)

    Returns:
        str: Отформатированный текст с сообщениями
    """
    if not messages:
        return "No messages found."

    lines = []

    # Информация о чате (если есть)
    if show_chat_info and messages:
        first_msg = messages[0]
        room_name = first_msg.get("room_name")
        service_name = first_msg.get("service_name")

        if room_name:
            # Групповой чат
            lines.append(f"💬 Group Chat: {room_name}")
        elif contact_name:
            lines.append(f"💬 Chat with {contact_name}")
        else:
            contact_id = messages[0].get("contact_id", "Unknown")
            lines.append(f"💬 Chat with {contact_id}")

        if service_name:
            service_display = "iMessage" if service_name == "iMessage" else service_name
            lines.append(f"   Service: {service_display}")

        lines.append("")  # Пустая строка

    # Заголовок
    lines.append(f"Last {len(messages)} messages:")
    lines.append("")  # Пустая строка

    if group_by_date:
        # Группировка по датам
        from collections import defaultdict

        messages_by_date = defaultdict(list)

        # Переворачиваем для хронологического порядка
        for msg in reversed(messages):
            date_str, time_str = format_message_date_nice(msg.get("date", 0))
            messages_by_date[date_str].append((time_str, msg))

        # Сортируем даты
        sorted_dates = sorted(messages_by_date.keys())

        # Форматируем каждую дату
        for date_str in sorted_dates:
            # Заголовок даты
            date_header = format_date_header(date_str)
            lines.append(f"📅 {date_header}")
            lines.append("")

            # Сообщения за эту дату
            for time_str, msg in messages_by_date[date_str]:
                # Направление и отправитель
                is_from_me = msg.get("is_from_me", False)
                sender = (
                    "You"
                    if is_from_me
                    else (msg.get("display_name") or msg.get("contact_id", "Contact"))
                )

                # Текст сообщения
                text = msg.get("text")

                # ⚠️ CRITICAL: Если текста нет, пытаемся извлечь из attributedBody
                # Это важно для медиа-сообщений, которые могут содержать текст
                if not text or text.strip() == "":
                    attributed_body = msg.get("attributed_body")
                    if attributed_body:
                        extracted_text = extract_text_from_attributed_body(attributed_body)
                        if extracted_text and extracted_text.strip():
                            # ⚠️ CRITICAL: Фильтруем технические термины из извлеченного текста
                            technical_terms = [
                                "streamtyped",
                                "streamtype",
                                "nsstring",
                                "nsobject",
                                "nsdictionary",
                            ]
                            extracted_lower = extracted_text.lower()
                            if not any(term in extracted_lower for term in technical_terms):
                                text = extracted_text
                                logger.info(
                                    f"[MCP Messages] Extracted text from attributedBody in format_messages: {text[:100]}..."
                                )
                            else:
                                logger.warning(
                                    f"[MCP Messages] Extracted text contains technical terms, skipping: {extracted_text[:100]}..."
                                )
                                text = None

                # Если после всех попыток текст все еще пустой, показываем "[Media message]"
                if not text or text.strip() == "":
                    text = "[Media message]"
                else:
                    # Обрезаем слишком длинные сообщения
                    if len(text) > 200:
                        text = text[:200] + "..."

                # Форматируем строку
                lines.append(f"  [{time_str}] {sender}: {text}")

            lines.append("")  # Пустая строка между датами
    else:
        # Простое форматирование без группировки
        for msg in reversed(messages):
            date_str = format_message_date(msg.get("date", 0))
            is_from_me = msg.get("is_from_me", False)
            sender = (
                "You"
                if is_from_me
                else (msg.get("display_name") or msg.get("contact_id", "Contact"))
            )
            text = msg.get("text")

            # ⚠️ CRITICAL: Если текста нет, пытаемся извлечь из attributedBody
            # Это важно для медиа-сообщений, которые могут содержать текст
            if not text or text.strip() == "":
                attributed_body = msg.get("attributed_body")
                if attributed_body:
                    extracted_text = extract_text_from_attributed_body(attributed_body)
                    if extracted_text and extracted_text.strip():
                        text = extracted_text
                        logger.debug(
                            f"Extracted text from attributedBody in format_messages (simple): {text[:50]}..."
                        )

            # Если после всех попыток текст все еще пустой, показываем "[Media message]"
            if not text or text.strip() == "":
                text = "[Media message]"
            else:
                # Обрезаем слишком длинные сообщения
                if len(text) > 200:
                    text = text[:200] + "..."
            lines.append(f"[{date_str}] {sender}: {text}")

    # Убираем последнюю пустую строку
    if lines and lines[-1] == "":
        lines.pop()

    return "\n".join(lines)


if __name__ == "__main__":
    # Настройка логирования для тестирования
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Тест подключения
    print("=" * 60)
    print("Тест подключения к базе данных Messages")
    print("=" * 60)

    result = test_connection()

    print(f"\nПуть к БД: {result['db_path']}")
    print(f"Доступна: {'✅ Да' if result['accessible'] else '❌ Нет'}")

    if result["error"]:
        print(f"Ошибка: {result['error']}")
    else:
        print(f"\nНайдено таблиц: {len(result['tables'])}")
        if result["tables"]:
            print("\nСписок таблиц:")
            for table in result["tables"][:10]:  # Показываем первые 10
                print(f"  - {table}")
            if len(result["tables"]) > 10:
                print(f"  ... и еще {len(result['tables']) - 10} таблиц")

        if result.get("success"):
            print("\n✅ Тест пройден успешно!")
        elif result.get("warning"):
            print(f"\n⚠️  Предупреждение: {result['warning']}")
