"""
Модуль для отправки сообщений через Messages на macOS

Использует AppleScript для отправки сообщений через приложение Messages.
"""

import logging
import subprocess
from typing import Any

logger = logging.getLogger(__name__)


def _find_similar_contacts(query: str) -> list[dict]:
    """
    Поиск похожих контактов по частичному совпадению имени.
    
    Args:
        query: Искомое имя (частичное)
        
    Returns:
        Список похожих контактов
    """
    from modules.messages.contact_resolver import find_contacts_by_name
    
    query_lower = query.lower().strip()
    if len(query_lower) < 2:
        return []
    
    # Попробуем найти контакты, начинающиеся с первых букв запроса
    # или содержащие запрос как подстроку
    similar = []
    
    # Стратегия 1: Поиск по первым 2-3 буквам
    for prefix_len in [3, 2]:
        if len(query_lower) >= prefix_len:
            prefix = query_lower[:prefix_len]
            # find_contacts_by_name ищет по partial match
            matches = find_contacts_by_name(prefix)
            for m in matches:
                label = (m.get('display_label') or m.get('first_name') or '').lower()
                # Проверяем, что имя начинается с префикса или содержит его
                if label.startswith(prefix) or query_lower in label or prefix in label:
                    if m not in similar:
                        similar.append(m)
            if similar:
                break
    
    # Стратегия 2: Если ничего не нашли, пробуем различные варианты написания
    if not similar and len(query_lower) >= 3:
        # Попробуем убрать последнюю букву (опечатка в окончании)
        alt_query = query_lower[:-1]
        matches = find_contacts_by_name(alt_query)
        for m in matches:
            if m not in similar:
                similar.append(m)
    
    return similar[:5]  # Максимум 5 предложений


def send_message_via_applescript(phone_number: str, message_text: str, service: str = "iMessage") -> dict[str, Any]:
    """
    Отправляет сообщение через AppleScript.
    
    Args:
        phone_number: Номер телефона получателя
        message_text: Текст сообщения
        service: Тип сервиса ("iMessage" или "SMS")
        
    Returns:
        Dict: Результат отправки
        {
            "success": bool,
            "message": str,
            "phone_number": str
        }
    """
    try:
        # AppleScript для отправки сообщения
        # Используем Messages.app через AppleScript
        applescript = f'''
        tell application "Messages"
            set targetService to id of 1st account whose service type = "{service}"
            set targetBuddy to participant "{phone_number}" of account id targetService
            send "{message_text}" to targetBuddy
        end tell
        '''
        
        result = subprocess.run(
            ['osascript', '-e', applescript],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0:
            logger.info(f"Сообщение отправлено на {phone_number}")
            return {
                "success": True,
                "message": f"Message sent to {phone_number}",
                "phone_number": phone_number
            }
        else:
            error = result.stderr.strip()
            logger.error(f"Ошибка отправки сообщения: {error}")
            return {
                "success": False,
                "message": f"Failed to send message: {error}",
                "phone_number": phone_number
            }
            
    except subprocess.TimeoutExpired:
        logger.error("Таймаут при отправке сообщения")
        return {
            "success": False,
            "message": "Timeout while sending message",
            "phone_number": phone_number
        }
    except Exception as e:
        logger.error(f"Ошибка отправки сообщения: {e}")
        return {
            "success": False,
            "message": f"Error: {str(e)}",
            "phone_number": phone_number
        }


def send_message_alternative(phone_number: str, message_text: str) -> dict[str, Any]:
    """
    Альтернативный способ отправки через AppleScript (более простой).
    
    Args:
        phone_number: Номер телефона получателя
        message_text: Текст сообщения
        
    Returns:
        Dict: Результат отправки
    """
    try:
        # Экранируем специальные символы в сообщении для AppleScript
        escaped_message = message_text.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')
        
        # Более надежный способ - используем iMessage account
        applescript = f'''
        tell application "Messages"
            set targetService to id of 1st account whose service type = iMessage
            set targetBuddy to participant "{phone_number}" of account id targetService
            send "{escaped_message}" to targetBuddy
        end tell
        '''
        
        result = subprocess.run(
            ['osascript', '-e', applescript],
            capture_output=True,
            text=True,
            timeout=15
        )
        
        if result.returncode == 0:
            logger.info(f"Message sent successfully to {phone_number}")
            return {
                "success": True,
                "message": f"Message sent to {phone_number}",
                "phone_number": phone_number
            }
        else:
            error_msg = result.stderr.strip() or result.stdout.strip()
            logger.error(f"Failed to send message to {phone_number}: {error_msg}")
            
            # Пробуем альтернативный способ (без указания service type)
            try:
                applescript2 = f'''
                tell application "Messages"
                    set targetBuddy to participant "{phone_number}" of account 1
                    send "{escaped_message}" to targetBuddy
                end tell
                '''
                
                result2 = subprocess.run(
                    ['osascript', '-e', applescript2],
                    capture_output=True,
                    text=True,
                    timeout=15
                )
                
                if result2.returncode == 0:
                    logger.info(f"Message sent successfully to {phone_number} (alternative method)")
                    return {
                        "success": True,
                        "message": f"Message sent to {phone_number}",
                        "phone_number": phone_number
                    }
            except Exception as e2:
                logger.error(f"Alternative method also failed: {e2}")
            
            return {
                "success": False,
                "message": f"Failed: {error_msg}",
                "phone_number": phone_number
            }
            
    except subprocess.TimeoutExpired:
        logger.error(f"Timeout while sending message to {phone_number}")
        return {
            "success": False,
            "message": "Timeout while sending message",
            "phone_number": phone_number
        }
    except Exception as e:
        logger.error(f"Error sending message to {phone_number}: {e}")
        return {
            "success": False,
            "message": f"Error: {str(e)}",
            "phone_number": phone_number
        }


def send_message_to_contact(contact_name: str, message_text: str) -> dict[str, Any]:
    """
    Отправляет сообщение контакту по имени.
    Находит контакт, получает номер, отправляет сообщение.
    
    Args:
        contact_name: Имя контакта
        message_text: Текст сообщения
        
    Returns:
        Dict: Результат отправки
    """
    # Импортируем здесь, чтобы избежать циклических импортов
    from modules.messages.contact_resolver import find_contacts_by_name
    
    # Шаг 1: Найти контакты по имени
    contacts = find_contacts_by_name(contact_name)
    
    if not contacts:
        # Fuzzy search: try to find similar contacts
        similar_contacts = _find_similar_contacts(contact_name)
        if similar_contacts:
            suggestions = [c.get('display_label', c.get('first_name', 'Unknown')) for c in similar_contacts[:5]]
            return {
                "success": False,
                "error_code": "similar_contacts_found",
                "message": f"Contact '{contact_name}' not found. Did you mean: {', '.join(suggestions)}?",
                "contact_name": contact_name,
                "suggestions": suggestions
            }
        return {
            "success": False,
            "error_code": "contact_not_found",
            "message": f"Contact '{contact_name}' not found",
            "contact_name": contact_name
        }
    
    # Шаг 3: Проверка на неоднозначность
    if len(contacts) > 1:
        names = [c.get('display_label', c.get('first_name', 'Unknown')) for c in contacts]
        return {
            "success": False,
            "error_code": "ambiguous_contact",
            "message": f"Multiple contacts found: {', '.join(names)}",
            "choices": names,
            "contact_name": contact_name
        }

    # Шаг 4: Если один контакт, но несколько номеров — используем первый (или все?)
    # Текущая логика: берем все номера первого контакта
    # Но если мы нашли UNIQUE contacts > 1, мы уже вышли выше.
    # Значит здесь contacts[0] единственный.
    phone_numbers = contacts[0].get("phones", [])
    
    if not phone_numbers:
         return {
            "success": False,
            "error_code": "no_phone_number",
            "message": f"No phone numbers found for contact '{contact_name}'",
            "contact_name": contact_name
        }
        
    if len(phone_numbers) > 1:
        logger.warning(f"Multiple phone numbers found for '{contact_name}': {phone_numbers}. Using first: {phone_numbers[0]}")
    
    phone_number = phone_numbers[0]
    
    # Шаг 5: Отправить сообщение
    result = send_message_alternative(phone_number, message_text)
    result["contact_name"] = contact_name
    result["phone_numbers_found"] = phone_numbers
    
    return result

