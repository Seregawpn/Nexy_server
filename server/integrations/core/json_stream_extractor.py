#!/usr/bin/env python3
"""
JsonStreamExtractor - Потоковое извлечение текста из JSON без ожидания завершения

Позволяет извлекать значение поля "text" по мере поступления символов,
обеспечивая низкую задержку для TTS.
"""

import re
import logging
from typing import Optional, Tuple
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)


@dataclass
class JsonStreamExtractor:
    """
    Потоковый экстрактор текста из JSON.
    
    Отслеживает буфер JSON и извлекает новые символы из поля "text"
    по мере их поступления, не дожидаясь закрытия JSON.
    
    Использование:
        extractor = JsonStreamExtractor()
        
        for chunk in llm_stream:
            new_text = extractor.feed(chunk)
            if new_text:
                await process_text_for_tts(new_text)
        
        # Финализация (получить остаток и флаг команды)
        remaining, has_command = extractor.finalize()
    """
    
    # Внутреннее состояние
    buffer: str = ""
    text_start_pos: int = -1  # Позиция начала значения "text" (после открывающей кавычки)
    text_extracted_pos: int = 0  # Сколько символов уже извлечено из text
    in_text_value: bool = False  # Находимся ли внутри значения поля "text"
    text_value_complete: bool = False  # Значение "text" полностью получено
    escape_next: bool = False  # Следующий символ экранирован
    
    # Паттерны для поиска начала поля "text"
    TEXT_FIELD_PATTERN: str = field(default=r'"text"\s*:\s*"', repr=False)
    
    def feed(self, chunk: str) -> str:
        """
        Добавляет новый chunk в буфер и возвращает новый извлечённый текст.
        
        Args:
            chunk: Новая порция данных от LLM
            
        Returns:
            Новый текст, извлечённый из поля "text" (может быть пустым)
        """
        if not chunk:
            return ""
        
        prev_buffer_len = len(self.buffer)
        self.buffer += chunk
        
        logger.info(f"🔍 [EXTRACTOR] feed: chunk_len={len(chunk)}, buffer_len={prev_buffer_len}→{len(self.buffer)}, in_text={self.in_text_value}, complete={self.text_value_complete}")
        
        # Если значение text уже полностью получено, ничего не извлекаем
        if self.text_value_complete:
            logger.debug(f"🔍 [EXTRACTOR] text_value_complete=True, возвращаем пустую строку")
            return ""
        
        # Если ещё не нашли начало поля "text", ищем его
        if not self.in_text_value:
            match = re.search(self.TEXT_FIELD_PATTERN, self.buffer)
            if match:
                self.text_start_pos = match.end()  # Позиция после открывающей кавычки
                self.text_extracted_pos = self.text_start_pos
                self.in_text_value = True
                logger.info(f"📍 [EXTRACTOR] НАЙДЕНО начало 'text' на позиции {self.text_start_pos}, buffer_snippet='{self.buffer[max(0,match.start()-10):match.end()+20]}'")
            else:
                # Показываем последние 50 символов буфера для диагностики
                logger.debug(f"🔍 [EXTRACTOR] Паттерн 'text' НЕ найден в буфере (len={len(self.buffer)}), tail='{self.buffer[-50:] if len(self.buffer) > 50 else self.buffer}'")
        
        # Если находимся внутри значения "text", извлекаем новые символы
        if self.in_text_value and not self.text_value_complete:
            result = self._extract_new_text()
            if result:
                logger.info(f"📤 [EXTRACTOR] Извлечено {len(result)} символов: '{result[:50]}...'")
            return result
        
        return ""
    
    def _extract_new_text(self) -> str:
        """Извлекает новые символы из значения поля text."""
        new_text = []
        i = self.text_extracted_pos
        
        while i < len(self.buffer):
            char = self.buffer[i]
            
            if self.escape_next:
                # Обрабатываем экранированный символ
                if char == 'n':
                    new_text.append('\n')
                elif char == 't':
                    new_text.append('\t')
                elif char == 'r':
                    new_text.append('\r')
                elif char == '"':
                    new_text.append('"')
                elif char == '\\':
                    new_text.append('\\')
                elif char == '/':
                    new_text.append('/')
                else:
                    # Неизвестная escape-последовательность — добавляем как есть
                    new_text.append(char)
                self.escape_next = False
                i += 1
                continue
            
            if char == '\\':
                # Следующий символ экранирован
                self.escape_next = True
                i += 1
                continue
            
            if char == '"':
                # Конец значения поля "text"
                self.text_value_complete = True
                self.in_text_value = False
                logger.debug(f"✅ Поле 'text' завершено на позиции {i}")
                break
            
            # Обычный символ
            new_text.append(char)
            i += 1
        
        self.text_extracted_pos = i
        result = ''.join(new_text)
        
        if result:
            logger.debug(f"📤 Извлечено {len(result)} новых символов из 'text'")
        
        return result
    
    def finalize(self) -> Tuple[str, bool]:
        """
        Финализирует извлечение и возвращает остаток.
        
        Returns:
            Tuple[remaining_text, has_command]:
                - remaining_text: Текст, который ещё не был извлечён
                - has_command: Есть ли в JSON поле "command"
        """
        remaining = ""
        
        # Если text не был завершён, извлекаем остаток
        if self.in_text_value and not self.text_value_complete:
            remaining = self._extract_new_text()
        
        # Проверяем наличие команды
        has_command = '"command"' in self.buffer and '"command": null' not in self.buffer
        
        return remaining, has_command
    
    def get_full_buffer(self) -> str:
        """Возвращает полный буфер для финального парсинга."""
        return self.buffer
    
    def reset(self):
        """Сбрасывает состояние экстрактора."""
        self.buffer = ""
        self.text_start_pos = -1
        self.text_extracted_pos = 0
        self.in_text_value = False
        self.text_value_complete = False
        self.escape_next = False
    
    def is_potential_json(self) -> bool:
        """Проверяет, похож ли буфер на JSON."""
        stripped = self.buffer.strip()
        return stripped.startswith('{') or stripped.startswith('```')


# Вспомогательная функция для использования без класса
def extract_text_streaming(buffer: str, last_extracted_pos: int = 0) -> Tuple[str, int, bool]:
    """
    Простая функция для потокового извлечения текста из JSON буфера.
    
    Args:
        buffer: Текущий JSON буфер
        last_extracted_pos: Позиция, до которой текст уже был извлечён
        
    Returns:
        Tuple[new_text, new_pos, is_complete]:
            - new_text: Новый извлечённый текст
            - new_pos: Новая позиция извлечения
            - is_complete: True если значение "text" полностью получено
    """
    # Ищем начало поля "text"
    text_pattern = r'"text"\s*:\s*"'
    match = re.search(text_pattern, buffer)
    
    if not match:
        return "", 0, False
    
    text_start = match.end()
    
    # Если last_extracted_pos меньше начала, начинаем с начала
    if last_extracted_pos < text_start:
        last_extracted_pos = text_start
    
    new_text = []
    i = last_extracted_pos
    escape_next = False
    is_complete = False
    
    while i < len(buffer):
        char = buffer[i]
        
        if escape_next:
            if char == 'n':
                new_text.append('\n')
            elif char == 't':
                new_text.append('\t')
            elif char == '"':
                new_text.append('"')
            elif char == '\\':
                new_text.append('\\')
            else:
                new_text.append(char)
            escape_next = False
            i += 1
            continue
        
        if char == '\\':
            escape_next = True
            i += 1
            continue
        
        if char == '"':
            is_complete = True
            break
        
        new_text.append(char)
        i += 1
    
    return ''.join(new_text), i, is_complete
