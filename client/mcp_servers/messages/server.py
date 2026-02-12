#!/usr/bin/env python3
"""
MCP Server для работы с приложением Messages на macOS

Этот сервер предоставляет инструменты для:
- Поиска контактов
- Чтения сообщений
- Отправки сообщений
"""

import asyncio
import logging
import sys
from typing import Any

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import (
    TextContent,
    Tool,
)

# Импорт модуля работы с базой данных
import messages_db  # pyright: ignore[reportImplicitRelativeImport]

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stderr)  # Логи в stderr, чтобы не мешать протоколу
    ],
)
logger = logging.getLogger(__name__)

# Создание MCP сервера
server = Server("messages-mcp-server")


@server.list_tools()
async def list_tools() -> list[Tool]:
    """
    Возвращает список доступных инструментов.
    """
    logger.info("List tools requested")

    return [
        Tool(
            name="find_contact",
            description="Find a contact by phone number, email address, or name. Supports exact match for phone/email and partial match for names.",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Phone number (e.g., +1234567890), email address (e.g., user@example.com), or contact name (e.g., John Doe) to search for",
                    }
                },
                "required": ["query"],
            },
        ),
        Tool(
            name="read_messages",
            description="Read recent messages from a contact. You can search by phone number, email, or contact name. Returns the last N messages in chronological order.",
            inputSchema={
                "type": "object",
                "properties": {
                    "contact": {
                        "type": "string",
                        "description": "Phone number (e.g., +1234567890), email address (e.g., user@example.com), or contact name (e.g., John Doe) to read messages from",
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Maximum number of messages to return (default: 10, max: 50)",
                        "default": 10,
                        "minimum": 1,
                        "maximum": 50,
                    },
                },
                "required": ["contact"],
            },
        ),
        Tool(
            name="send_message",
            description="Send a message to a contact. You can specify contact by name, phone number, or email. The system will find the contact and send the message. If contact has multiple phone numbers, the system will automatically select the one with the most recent message, or you can specify it explicitly.",
            inputSchema={
                "type": "object",
                "properties": {
                    "contact": {
                        "type": "string",
                        "description": "Contact name (e.g., John Doe), phone number (e.g., +1234567890), or email address (e.g., user@example.com)",
                    },
                    "message": {"type": "string", "description": "Text of the message to send"},
                    "phone_number": {
                        "type": "string",
                        "description": "Optional: Specific phone number to use if contact has multiple numbers (e.g., +1234567890)",
                    },
                },
                "required": ["contact", "message"],
            },
        ),
    ]


@server.call_tool()
async def call_tool(
    name: str,
    arguments: dict[str, Any] | None,
) -> list[TextContent]:
    """
    Обрабатывает вызов инструмента.
    """
    logger.info(f"Tool call requested: {name} with arguments: {arguments}")

    if arguments is None:
        arguments = {}

    # Обработка инструмента find_contact
    if name == "find_contact":
        return await handle_find_contact(arguments)

    # Обработка инструмента read_messages
    if name == "read_messages":
        return await handle_read_messages(arguments)

    # Обработка инструмента send_message
    if name == "send_message":
        return await handle_send_message(arguments)

    # Неизвестный инструмент
    return [TextContent(type="text", text=f"Unknown tool: {name}")]


async def handle_find_contact(arguments: dict[str, Any]) -> list[TextContent]:
    """
    Обрабатывает запрос на поиск контакта.
    Поддерживает поиск по номеру телефона, email или имени.

    Args:
        arguments: Словарь с аргументами, должен содержать 'query'

    Returns:
        list[TextContent]: Список с результатами поиска
    """
    # Валидация аргументов
    query = arguments.get("query")
    if not query:
        return [TextContent(type="text", text="Error: 'query' parameter is required")]

    if not isinstance(query, str):
        return [TextContent(type="text", text="Error: 'query' must be a string")]

    # Подключение к базе данных
    conn = messages_db.connect_db()
    if not conn:
        return [
            TextContent(
                type="text",
                text="Error: Could not connect to Messages database. Please ensure Full Disk Access is granted.",
            )
        ]

    try:
        # Универсальный поиск (сначала по номеру/email, потом по имени)
        contacts = messages_db.find_contact(conn, query)

        if not contacts:
            return [
                TextContent(
                    type="text",
                    text=f"No contact found matching: {query}\n\nTry searching by:\n- Phone number (e.g., +1234567890)\n- Email address (e.g., user@example.com)\n- Contact name (e.g., John Doe)",
                )
            ]

        # Форматирование результатов
        if len(contacts) == 1:
            # Один контакт - детальная информация
            contact = contacts[0]
            info = messages_db.format_contact_info(contact)
            result_text = f"Found contact:\n\n{info}"
        else:
            # Несколько контактов - список
            result_lines = [f"Found {len(contacts)} contacts:"]
            for i, contact in enumerate(contacts, 1):
                display_name = contact.get("display_name")
                contact_id = contact.get("id", "Unknown")

                # Показываем имя, если есть, иначе ID
                if display_name:
                    result_lines.append(f"\n{i}. {display_name}")
                    result_lines.append(f"   ID: {contact_id}")
                else:
                    result_lines.append(f"\n{i}. {contact_id}")

                service = contact.get("service", "Unknown")
                service_name = "iMessage" if service == "iMessage" else service
                result_lines.append(f"   Service: {service_name}")
            result_text = "\n".join(result_lines)

        return [TextContent(type="text", text=result_text)]

    except Exception as e:
        logger.error(f"Error in find_contact: {e}", exc_info=True)
        return [TextContent(type="text", text=f"Error searching for contact: {str(e)}")]
    finally:
        conn.close()


async def handle_read_messages(arguments: dict[str, Any]) -> list[TextContent]:
    """
    Обрабатывает запрос на чтение сообщений.
    Поддерживает поиск по номеру телефона, email или имени контакта.

    Args:
        arguments: Словарь с аргументами, должен содержать 'contact' и опционально 'limit'

    Returns:
        list[TextContent]: Список с результатами чтения сообщений
    """
    # Валидация аргументов
    contact = arguments.get("contact")

    # Специальный случай: "последнее сообщение" без указания контакта
    if not contact or contact.lower() == "last" or contact.lower() == "последнее":
        # Получаем последнее сообщение из всех чатов
        conn = messages_db.connect_db()
        if not conn:
            return [
                TextContent(
                    type="text",
                    text="Error: Could not connect to Messages database. Please ensure Full Disk Access is granted.",
                )
            ]

        try:
            last_message = messages_db.get_last_message(conn)

            if not last_message:
                return [TextContent(type="text", text="No messages found in database.")]

            # Получаем имя контакта
            contact_id = last_message.get("contact_id")
            import contact_resolver  # pyright: ignore[reportImplicitRelativeImport]

            contact_info = contact_resolver.resolve_contact(
                str(contact_id or ""), messages_conn=conn
            )
            contact_name = contact_info.get("display_label", contact_id)

            # Форматируем сообщение
            formatted_text = messages_db.format_messages(  # pyright: ignore[reportArgumentType]
                [last_message],
                str(contact_name or "Unknown"),
                group_by_date=True,
                show_chat_info=False,
                messages_conn=conn,
            )

            # Убираем заголовок "Last X messages" и добавляем свой
            lines = formatted_text.split("\n")
            if lines and "Last" in lines[0]:
                lines = lines[2:]  # Пропускаем заголовок и пустую строку

            # Формируем результат с информацией о контакте
            result_text = f"💬 Последнее сообщение от {contact_name}"
            if contact_id != contact_name:
                result_text += f" ({contact_id})"
            result_text += ":\n\n"
            result_text += "\n".join(lines)

            return [TextContent(type="text", text=result_text)]
        except Exception as e:
            logger.error(f"Error getting last message: {e}", exc_info=True)
            return [TextContent(type="text", text=f"Error getting last message: {str(e)}")]
        finally:
            conn.close()

    if not isinstance(contact, str):
        return [TextContent(type="text", text="Error: 'contact' must be a string")]

    # Получаем limit (по умолчанию 10, максимум 50)
    limit = arguments.get("limit", 10)
    if not isinstance(limit, int):
        limit = 10
    if limit < 1:
        limit = 1
    if limit > 50:
        limit = 50

    # Подключение к базе данных
    conn = messages_db.connect_db()
    if not conn:
        return [
            TextContent(
                type="text",
                text="Error: Could not connect to Messages database. Please ensure Full Disk Access is granted.",
            )
        ]

    try:
        # Определяем, что передано: номер/email или имя
        # Если содержит @ или начинается с +, считаем это номером/email
        is_phone_or_email = (
            contact.startswith("+")
            or "@" in contact
            or contact.replace(" ", "").replace("-", "").replace("(", "").replace(")", "").isdigit()
        )

        contact_id = contact
        contact_name = None
        found_contacts = []

        if not is_phone_or_email:
            # Это похоже на имя - ищем контакт через несколько источников
            logger.info(f"Searching for contact by name: {contact}")

            # 1. Ищем в базе Messages
            found_contacts = messages_db.find_contact(conn, contact)

            # 2. Ищем через Swift helper в системных контактах
            import contact_resolver  # pyright: ignore[reportImplicitRelativeImport]

            swift_contacts = contact_resolver.find_contacts_by_name(contact)

            # Объединяем результаты
            all_contacts = []
            contact_ids_seen = set()

            # Добавляем контакты из базы Messages
            for cont in found_contacts:
                cont_id = cont.get("id")
                if cont_id and cont_id not in contact_ids_seen:
                    all_contacts.append(
                        {
                            "id": cont_id,
                            "name": cont.get("display_name") or cont_id,
                            "source": "messages_db",
                            "phones": [cont_id] if not "@" in cont_id else [],
                            "emails": [cont_id] if "@" in cont_id else [],
                        }
                    )
                    contact_ids_seen.add(cont_id)

            # Добавляем контакты из системных контактов (Swift helper)
            for swift_cont in swift_contacts:
                phones = swift_cont.get("phones", [])
                emails = swift_cont.get("emails", [])

                # Для каждого телефона/email создаем запись
                for phone in phones:
                    if phone and phone not in contact_ids_seen:
                        all_contacts.append(
                            {
                                "id": phone,
                                "name": swift_cont.get("display_label", contact),
                                "source": "system_contacts",
                                "phones": [phone],
                                "emails": [],
                            }
                        )
                        contact_ids_seen.add(phone)

                for email in emails:
                    if email and email not in contact_ids_seen:
                        all_contacts.append(
                            {
                                "id": email,
                                "name": swift_cont.get("display_label", contact),
                                "source": "system_contacts",
                                "phones": [],
                                "emails": [email],
                            }
                        )
                        contact_ids_seen.add(email)

            if not all_contacts:
                return [
                    TextContent(
                        type="text",
                        text=f"Contact not found: '{contact}'\n\nTry searching by:\n- Phone number (e.g., +1234567890)\n- Email address (e.g., user@example.com)\n- Contact name (e.g., John Doe)\n\nOr use find_contact first to find the correct contact.",
                    )
                ]

            if len(all_contacts) == 1:
                # Один контакт найден - используем его ID
                found_contact = all_contacts[0]
                contact_id = found_contact.get("id")
                contact_name = found_contact.get("name")
                logger.info(f"Found contact: {contact_name} ({contact_id})")
            else:
                # Несколько контактов найдено - получаем сообщения от всех
                logger.info(f"Found {len(all_contacts)} contacts matching '{contact}'")

                # Собираем сообщения от всех найденных контактов
                all_messages = []
                for cont in all_contacts:
                    cont_id = cont.get("id")
                    cont_name = cont.get("name")

                    # Получаем сообщения для этого контакта
                    cont_messages = messages_db.get_messages_by_contact(conn, cont_id, limit=limit)

                    if cont_messages:
                        # Добавляем информацию о контакте к каждому сообщению
                        for msg in cont_messages:
                            msg["contact_name"] = cont_name
                            msg["contact_id"] = cont_id
                            all_messages.append(msg)

                if not all_messages:
                    # Формируем список контактов
                    result_lines = [
                        f"Found {len(all_contacts)} contacts matching '{contact}', but no messages found:"
                    ]
                    for i, cont in enumerate(all_contacts, 1):
                        name = cont.get("name", "Unknown")
                        cont_id = cont.get("id", "Unknown")
                        result_lines.append(f"\n{i}. {name}")
                        result_lines.append(f"   ID: {cont_id}")

                    return [TextContent(type="text", text="\n".join(result_lines))]

                # Сортируем сообщения по дате (новые первыми)
                all_messages.sort(key=lambda x: x.get("date", 0), reverse=True)

                # Берем только limit самых новых
                all_messages = all_messages[:limit]

                # Форматируем сообщения от всех контактов
                result_lines = [f"Found {len(all_contacts)} contacts matching '{contact}':"]
                for i, cont in enumerate(all_contacts, 1):
                    name = cont.get("name", "Unknown")
                    cont_id = cont.get("id", "Unknown")
                    result_lines.append(f"\n{i}. {name} ({cont_id})")

                result_lines.append(f"\n{'=' * 70}")
                result_lines.append(f"Last {len(all_messages)} messages from all contacts:")
                result_lines.append("")

                # Группируем сообщения по контактам
                from collections import defaultdict

                messages_by_contact = defaultdict(list)
                for msg in all_messages:
                    contact_name = msg.get("contact_name", "Unknown")
                    messages_by_contact[contact_name].append(msg)

                # Форматируем для каждого контакта
                for contact_name, msgs in messages_by_contact.items():
                    result_lines.append(f"💬 Messages from {contact_name}:")
                    formatted = messages_db.format_messages(
                        msgs,
                        contact_name,
                        group_by_date=True,
                        show_chat_info=False,
                        messages_conn=conn,
                    )
                    # Убираем заголовок "Last X messages"
                    lines = formatted.split("\n")
                    if lines and "Last" in lines[0]:
                        lines = lines[2:]  # Пропускаем заголовок и пустую строку
                    result_lines.extend(lines)
                    result_lines.append("")

                return [TextContent(type="text", text="\n".join(result_lines))]

        # Получение сообщений по ID контакта
        messages = messages_db.get_messages_by_contact(conn, contact_id, limit)

        if not messages:
            # Сообщений нет
            if contact_name:
                return [
                    TextContent(
                        type="text", text=f"No messages found with {contact_name} ({contact_id})"
                    )
                ]
            else:
                # Пробуем получить имя контакта
                contacts = messages_db.find_contact_exact(conn, contact_id)
                if contacts:
                    contact_name = contacts[0].get("display_name") or contact_id
                    return [
                        TextContent(
                            type="text",
                            text=f"No messages found with {contact_name} ({contact_id})",
                        )
                    ]
                else:
                    return [TextContent(type="text", text=f"No messages found with {contact_id}")]

        # Получаем имя контакта через новый ContactResolver
        import contact_resolver  # pyright: ignore[reportImplicitRelativeImport]

        contact_info = contact_resolver.resolve_contact(contact_id, messages_conn=conn)
        contact_name = contact_info.get("display_label")

        # Если resolver вернул identifier, значит имя не найдено - используем None
        if contact_name == contact_id:
            contact_name = None

        # ⚠️ CRITICAL: Проверяем, что в сообщениях есть реальный текст
        for i, msg in enumerate(messages[:3]):  # Проверяем первые 3 сообщения
            msg_text = msg.get("text", "")
            logger.info(
                f"[MCP Messages] Message #{i + 1} text (first 100 chars): {msg_text[:100] if msg_text else '(empty)'}"
            )
            if not msg_text or msg_text.strip() == "":
                attributed_body = msg.get("attributed_body")
                logger.info(
                    f"[MCP Messages] Message #{i + 1} has empty text, attributed_body present: {attributed_body is not None}"
                )
                if attributed_body:
                    # Пытаемся извлечь текст из attributedBody
                    extracted = messages_db.extract_text_from_attributed_body(attributed_body)
                    if extracted:
                        logger.info(
                            f"[MCP Messages] Message #{i + 1} extracted from attributedBody (first 100 chars): {extracted[:100]}"
                        )

        # Форматируем сообщения с улучшенным форматированием
        formatted_text = messages_db.format_messages(  # pyright: ignore[reportArgumentType]
            messages,
            str(contact_name or "Unknown"),
            group_by_date=True,  # Группировка по датам
            show_chat_info=True,  # Показывать информацию о чате
            messages_conn=conn,  # Передаем соединение для resolver
        )

        # ⚠️ CRITICAL: Логируем отформатированный текст для отладки
        logger.info(f"[MCP Messages] Formatted text (first 500 chars): {formatted_text[:500]}")
        logger.info(f"[MCP Messages] Formatted text length: {len(formatted_text)}")

        # ⚠️ CRITICAL: Упрощаем формат для LLM - оставляем только текст сообщений
        # Это нужно, чтобы LLM видел только реальный текст сообщений, а не технические детали
        lines = formatted_text.split("\n")
        simplified_lines = []
        in_messages_section = False

        for line in lines:
            # Пропускаем заголовки чата и метаданные
            if (
                line.startswith("💬")
                or line.startswith("Service:")
                or line.startswith("Last ")
                and "messages:" in line
            ):
                continue

            # Начинаем собирать сообщения после заголовка даты или сразу с сообщения
            if line.startswith("📅") or (
                ":" in line and ("[" in line or line.strip().startswith("You:"))
            ):
                in_messages_section = True

            if in_messages_section:
                simplified_lines.append(line)

        # Если упрощение не дало результатов, используем оригинальный текст
        if not simplified_lines or len(simplified_lines) < 2:
            simplified_text = formatted_text
            logger.warning(f"[MCP Messages] Simplification failed, using original text")
        else:
            simplified_text = "\n".join(simplified_lines)
            logger.info(
                f"[MCP Messages] Simplified text (first 500 chars): {simplified_text[:500]}"
            )

        return [TextContent(type="text", text=simplified_text)]

    except Exception as e:
        logger.error(f"Error in read_messages: {e}", exc_info=True)
        return [TextContent(type="text", text=f"Error reading messages: {str(e)}")]
    finally:
        conn.close()


async def handle_send_message(arguments: dict[str, Any]) -> list[TextContent]:
    """
    Обрабатывает запрос на отправку сообщения.
    Поддерживает поиск контакта по имени, номеру телефона или email.

    Args:
        arguments: Словарь с аргументами, должен содержать 'contact' и 'message'

    Returns:
        list[TextContent]: Список с результатами отправки сообщения
    """
    # Валидация аргументов
    contact = arguments.get("contact")
    message_text = arguments.get("message")

    if not contact:
        return [TextContent(type="text", text="Error: 'contact' parameter is required")]

    if not message_text:
        return [TextContent(type="text", text="Error: 'message' parameter is required")]

    if not isinstance(contact, str) or not isinstance(message_text, str):
        return [TextContent(type="text", text="Error: 'contact' and 'message' must be strings")]

    try:
        # Импортируем модуль отправки сообщений
        import contact_resolver  # pyright: ignore[reportImplicitRelativeImport]
        from errors import (  # pyright: ignore[reportImplicitRelativeImport]
            ContactNotFoundError,
            MessageSendError,
            NoPhoneNumbersError,
        )
        import send_message  # pyright: ignore[reportImplicitRelativeImport]

        # Определяем, что передано: номер/email или имя
        is_phone_or_email = (
            contact.startswith("+")
            or "@" in contact
            or contact.replace(" ", "").replace("-", "").replace("(", "").replace(")", "").isdigit()
        )

        if is_phone_or_email:
            # Прямая отправка по номеру/email
            logger.info(f"Sending message to {contact}")
            result = send_message.send_message_alternative(contact, message_text)

            if result.get("success"):
                return [
                    TextContent(
                        type="text",
                        text=f"✅ Message sent successfully to {contact}\n\nMessage: {message_text}",
                    )
                ]
            else:
                return [
                    TextContent(
                        type="text",
                        text=f"❌ Failed to send message to {contact}\n\nError: {result.get('message', 'Unknown error')}",
                    )
                ]
        else:
            # Поиск контакта по имени
            logger.info(f"Searching for contact '{contact}' to send message")

            # Находим контакты через Swift helper
            contacts = contact_resolver.find_contacts_by_name(contact)

            if not contacts:
                raise ContactNotFoundError(
                    contact,
                    f"Contact '{contact}' not found. Try searching by:\n- Phone number (e.g., +1234567890)\n- Email address (e.g., user@example.com)\n- Contact name (e.g., John Doe)",
                )

            # Получаем номера телефонов
            phone_numbers = []
            contact_names = []
            for cont in contacts:
                phones = cont.get("phones", [])
                phone_numbers.extend(phones)
                contact_names.append(cont.get("display_label", contact))

            if not phone_numbers:
                raise NoPhoneNumbersError(
                    contact, f"No phone numbers found for contact '{contact}'"
                )

            # Умный выбор номера при нескольких номерах
            if len(phone_numbers) > 1:
                # Проверяем, указан ли номер явно
                specified_phone = arguments.get("phone_number")
                if specified_phone and specified_phone in phone_numbers:
                    phone_number = specified_phone
                    logger.info(f"Используется указанный номер: {phone_number}")
                else:
                    # Умный выбор: номер с последним сообщением
                    import messages_db  # pyright: ignore[reportImplicitRelativeImport]

                    conn = messages_db.connect_db()
                    if conn:
                        try:
                            phone_number = messages_db.get_phone_with_last_message(
                                conn, phone_numbers
                            )
                            if phone_number:
                                logger.info(
                                    f"Выбран номер с последним сообщением: {phone_number} из {phone_numbers}"
                                )
                            else:
                                phone_number = phone_numbers[0]
                                logger.warning(
                                    f"Не удалось выбрать номер, используем первый: {phone_number}"
                                )
                        finally:
                            conn.close()
                    else:
                        phone_number = phone_numbers[0]
                        logger.warning(
                            f"Не удалось подключиться к БД, используем первый номер: {phone_number}"
                        )
            else:
                phone_number = phone_numbers[0]

            contact_display_name = contact_names[0] if contact_names else contact

            # Отправляем сообщение
            logger.info(f"Sending message to {contact_display_name} ({phone_number})")
            result = send_message.send_message_alternative(phone_number, message_text)

            if result.get("success"):
                response_text = f"✅ Message sent successfully to {contact_display_name} ({phone_number})\n\nMessage: {message_text}"

                if len(phone_numbers) > 1:
                    response_text += f"\n\nNote: Found {len(phone_numbers)} phone numbers for this contact. Selected number with last message: {phone_number}"
                    response_text += f"\nOther numbers: {', '.join(phone_numbers)}"

                return [TextContent(type="text", text=response_text)]
            else:
                error_msg = result.get("message", "Unknown error")
                raise MessageSendError(
                    phone_number,
                    error_msg,
                    f"Failed to send message to {contact_display_name} ({phone_number})\n\nError: {error_msg}",
                )

    except (ContactNotFoundError, NoPhoneNumbersError, MessageSendError) as e:
        logger.error(f"Error in send_message: {e}", exc_info=True)
        return [TextContent(type="text", text=f"❌ {str(e)}")]
    except Exception as e:
        logger.error(f"Unexpected error in send_message: {e}", exc_info=True)
        return [TextContent(type="text", text=f"Error sending message: {str(e)}")]


async def main():
    """
    Главная функция для запуска сервера.
    """
    logger.info("Starting MCP server for Messages...")

    # Запуск сервера через stdio
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
    except Exception as e:
        logger.error(f"Server error: {e}", exc_info=True)
        sys.exit(1)
