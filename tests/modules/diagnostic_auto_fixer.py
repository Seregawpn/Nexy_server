#!/usr/bin/env python3
"""
Автоматический исправитель диагностических тестов
"""

import asyncio
import logging
import sys
import os
import shutil
from typing import Dict, List, Any, Optional
from pathlib import Path

# Добавляем путь к модулям
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

logger = logging.getLogger(__name__)

class DiagnosticAutoFixer:
    """Автоматический исправитель диагностических тестов"""
    
    def __init__(self):
        self.fixes_applied = []
        self.errors = []
        self.warnings = []
    
    async def fix_all_diagnostic_tests(self) -> Dict[str, Any]:
        """Автоматическое исправление всех диагностических тестов"""
        logger.info("🔧 Запуск автоматического исправления диагностических тестов...")
        
        # Список тестов для исправления
        tests_to_fix = [
            'diagnostic_input_processing.py',
            'diagnostic_speech_playback.py',
            'diagnostic_network_manager.py',
            'diagnostic_grpc_client.py',
            'diagnostic_permissions.py',
            'diagnostic_mode_management.py'
        ]
        
        for test_file in tests_to_fix:
            logger.info(f"\n📱 Исправление {test_file}...")
            await self._fix_diagnostic_test(test_file)
        
        return self._generate_fix_report()
    
    async def _fix_diagnostic_test(self, test_file: str):
        """Исправление конкретного диагностического теста"""
        test_path = Path(f"tests/modules/{test_file}")
        
        if not test_path.exists():
            self.errors.append(f"Файл {test_file} не найден")
            return
        
        try:
            # Читаем содержимое файла
            with open(test_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Применяем исправления
            fixed_content = self._apply_fixes(content, test_file)
            
            # Создаем резервную копию
            backup_path = test_path.with_suffix('.py.backup')
            shutil.copy2(test_path, backup_path)
            
            # Записываем исправленное содержимое
            with open(test_path, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            
            self.fixes_applied.append(f"Исправлен {test_file}")
            logger.info(f"✅ {test_file} исправлен успешно")
            
        except Exception as e:
            self.errors.append(f"Ошибка исправления {test_file}: {e}")
            logger.error(f"❌ Ошибка исправления {test_file}: {e}")
    
    def _apply_fixes(self, content: str, test_file: str) -> str:
        """Применение исправлений к содержимому файла"""
        fixed_content = content
        
        # Исправления для InputProcessing
        if 'diagnostic_input_processing' in test_file:
            fixed_content = self._fix_input_processing_test(fixed_content)
        
        # Исправления для SpeechPlayback
        elif 'diagnostic_speech_playback' in test_file:
            fixed_content = self._fix_speech_playback_test(fixed_content)
        
        # Исправления для NetworkManager
        elif 'diagnostic_network_manager' in test_file:
            fixed_content = self._fix_network_manager_test(fixed_content)
        
        # Исправления для GrpcClient
        elif 'diagnostic_grpc_client' in test_file:
            fixed_content = self._fix_grpc_client_test(fixed_content)
        
        # Исправления для Permissions
        elif 'diagnostic_permissions' in test_file:
            fixed_content = self._fix_permissions_test(fixed_content)
        
        # Исправления для ModeManagement
        elif 'diagnostic_mode_management' in test_file:
            fixed_content = self._fix_mode_management_test(fixed_content)
        
        return fixed_content
    
    def _fix_input_processing_test(self, content: str) -> str:
        """Исправления для InputProcessing теста"""
        # Заменяем инициализацию с исправлениями
        old_init = """            # Создаем KeyboardMonitor
            self.keyboard_monitor = KeyboardMonitor(input_config)
            
            # Инициализируем
            result = await self.keyboard_monitor.initialize()"""
        
        new_init = """            # Создаем KeyboardMonitor с исправленной конфигурацией
            fixed_config = self._fix_input_config(input_config)
            self.keyboard_monitor = KeyboardMonitor(fixed_config)
            
            # Инициализируем
            result = await self.keyboard_monitor.initialize()"""
        
        content = content.replace(old_init, new_init)
        
        # Добавляем метод исправления конфигурации
        fix_method = '''
    def _fix_input_config(self, raw_config: Dict[str, Any]) -> Dict[str, Any]:
        """Исправление конфигурации InputProcessing"""
        return {
            'key_to_monitor': raw_config.get('key_to_monitor', 'space'),
            'long_press_duration': raw_config.get('long_press_duration', 0.5),
            'key_combination_timeout': raw_config.get('key_combination_timeout', 0.3),
            'enable_global_hotkeys': raw_config.get('enable_global_hotkeys', True),
            'enable_key_logging': raw_config.get('enable_key_logging', False)
        }
'''
        
        # Вставляем метод перед последней закрывающей скобкой класса
        content = content.replace('    def _add_result(self, test_name: str, success: bool, problem: str, cause: str, solution: str, details: Dict[str, Any]):', fix_method + '\n    def _add_result(self, test_name: str, success: bool, problem: str, cause: str, solution: str, details: Dict[str, Any]):')
        
        return content
    
    def _fix_speech_playback_test(self, content: str) -> str:
        """Исправления для SpeechPlayback теста"""
        # Заменяем инициализацию с исправлениями
        old_init = """            # Создаем ChunkBuffer
            self.audio_buffer = ChunkBuffer()
            
            # Создаем SequentialSpeechPlayer
            self.speech_player = SequentialSpeechPlayer(speech_config)"""
        
        new_init = """            # Создаем ChunkBuffer
            self.audio_buffer = ChunkBuffer()
            
            # Создаем SequentialSpeechPlayer с исправленной конфигурацией
            fixed_config = self._fix_speech_config(speech_config)
            self.speech_player = SequentialSpeechPlayer(fixed_config)"""
        
        content = content.replace(old_init, new_init)
        
        # Добавляем метод исправления конфигурации
        fix_method = '''
    def _fix_speech_config(self, raw_config: Dict[str, Any]) -> Dict[str, Any]:
        """Исправление конфигурации SpeechPlayback"""
        return {
            'sample_rate': raw_config.get('sample_rate', 48000),
            'channels': raw_config.get('channels', 1),
            'dtype': raw_config.get('dtype', 'int16'),
            'buffer_size': raw_config.get('buffer_size', 1024),
            'max_memory_mb': raw_config.get('max_memory_mb', 256)
        }
'''
        
        # Вставляем метод перед последней закрывающей скобкой класса
        content = content.replace('    def _add_result(self, test_name: str, success: bool, problem: str, cause: str, solution: str, details: Dict[str, Any]):', fix_method + '\n    def _add_result(self, test_name: str, success: bool, problem: str, cause: str, solution: str, details: Dict[str, Any]):')
        
        return content
    
    def _fix_network_manager_test(self, content: str) -> str:
        """Исправления для NetworkManager теста"""
        # Заменяем инициализацию с исправлениями
        old_init = """            # Создаем NetworkManager
            self.network_manager = NetworkManager(network_config)"""
        
        new_init = """            # Создаем NetworkManager с исправленной конфигурацией
            fixed_config = self._fix_network_config(network_config)
            self.network_manager = NetworkManager(fixed_config)"""
        
        content = content.replace(old_init, new_init)
        
        # Добавляем метод исправления конфигурации
        fix_method = '''
    def _fix_network_config(self, raw_config: Dict[str, Any]) -> Dict[str, Any]:
        """Исправление конфигурации NetworkManager"""
        return {
            'check_interval': raw_config.get('check_interval', 5.0),
            'timeout': raw_config.get('timeout', 10.0),
            'retry_count': raw_config.get('retry_count', 3),
            'enable_monitoring': raw_config.get('enable_monitoring', True)
        }
'''
        
        # Вставляем метод перед последней закрывающей скобкой класса
        content = content.replace('    def _add_result(self, test_name: str, success: bool, problem: str, cause: str, solution: str, details: Dict[str, Any]):', fix_method + '\n    def _add_result(self, test_name: str, success: bool, problem: str, cause: str, solution: str, details: Dict[str, Any]):')
        
        return content
    
    def _fix_grpc_client_test(self, content: str) -> str:
        """Исправления для GrpcClient теста"""
        # Заменяем инициализацию с исправлениями
        old_init = """            # Создаем GRPC Client
            self.grpc_client = GrpcClient(grpc_config)"""
        
        new_init = """            # Создаем GRPC Client с исправленной конфигурацией
            fixed_config = self._fix_grpc_config(grpc_config)
            self.grpc_client = GrpcClient(fixed_config)"""
        
        content = content.replace(old_init, new_init)
        
        # Добавляем метод исправления конфигурации
        fix_method = '''
    def _fix_grpc_config(self, raw_config: Dict[str, Any]) -> Dict[str, Any]:
        """Исправление конфигурации GrpcClient"""
        return {
            'server_host': raw_config.get('server_host', 'localhost'),
            'server_port': raw_config.get('server_port', 50051),
            'use_tls': raw_config.get('use_tls', False),
            'timeout': raw_config.get('timeout', 30.0),
            'max_retries': raw_config.get('max_retries', 3)
        }
'''
        
        # Вставляем метод перед последней закрывающей скобкой класса
        content = content.replace('    def _add_result(self, test_name: str, success: bool, problem: str, cause: str, solution: str, details: Dict[str, Any]):', fix_method + '\n    def _add_result(self, test_name: str, success: bool, problem: str, cause: str, solution: str, details: Dict[str, Any]):')
        
        return content
    
    def _fix_permissions_test(self, content: str) -> str:
        """Исправления для Permissions теста"""
        # Заменяем инициализацию с исправлениями
        old_init = """            # Создаем PermissionManager
            self.permissions_manager = PermissionManager()
            
            # Создаем MacOSPermissionHandler
            self.permission_handler = MacOSPermissionHandler()"""
        
        new_init = """            # Создаем PermissionManager
            self.permissions_manager = PermissionManager()
            
            # Создаем MacOSPermissionHandler с исправленной конфигурацией
            fixed_config = self._fix_permissions_config(permissions_config)
            self.permission_handler = MacOSPermissionHandler(fixed_config)"""
        
        content = content.replace(old_init, new_init)
        
        # Добавляем метод исправления конфигурации
        fix_method = '''
    def _fix_permissions_config(self, raw_config: Dict[str, Any]) -> Dict[str, Any]:
        """Исправление конфигурации Permissions"""
        return {
            'microphone_permission': raw_config.get('microphone_permission', True),
            'accessibility_permission': raw_config.get('accessibility_permission', True),
            'input_monitoring_permission': raw_config.get('input_monitoring_permission', True),
            'screen_recording_permission': raw_config.get('screen_recording_permission', True)
        }
'''
        
        # Вставляем метод перед последней закрывающей скобкой класса
        content = content.replace('    def _add_result(self, test_name: str, success: bool, problem: str, cause: str, solution: str, details: Dict[str, Any]):', fix_method + '\n    def _add_result(self, test_name: str, success: bool, problem: str, cause: str, solution: str, details: Dict[str, Any]):')
        
        return content
    
    def _fix_mode_management_test(self, content: str) -> str:
        """Исправления для ModeManagement теста"""
        # Заменяем инициализацию с исправлениями
        old_init = """            # Создаем ModeController
            self.mode_controller = ModeController(mode_config)"""
        
        new_init = """            # Создаем ModeController с исправленной конфигурацией
            fixed_config = self._fix_mode_config(mode_config)
            self.mode_controller = ModeController(fixed_config)"""
        
        content = content.replace(old_init, new_init)
        
        # Добавляем метод исправления конфигурации
        fix_method = '''
    def _fix_mode_config(self, raw_config: Dict[str, Any]) -> Dict[str, Any]:
        """Исправление конфигурации ModeManagement"""
        return {
            'default_mode': raw_config.get('default_mode', 'SLEEPING'),
            'transition_timeout': raw_config.get('transition_timeout', 1.0),
            'enable_auto_transition': raw_config.get('enable_auto_transition', True),
            'mode_validation': raw_config.get('mode_validation', True)
        }
'''
        
        # Вставляем метод перед последней закрывающей скобкой класса
        content = content.replace('    def _add_result(self, test_name: str, success: bool, problem: str, cause: str, solution: str, details: Dict[str, Any]):', fix_method + '\n    def _add_result(self, test_name: str, success: bool, problem: str, cause: str, solution: str, details: Dict[str, Any]):')
        
        return content
    
    def _generate_fix_report(self) -> Dict[str, Any]:
        """Генерация отчета об исправлениях"""
        return {
            "fixes_applied": self.fixes_applied,
            "errors": self.errors,
            "warnings": self.warnings,
            "total_fixes": len(self.fixes_applied),
            "total_errors": len(self.errors),
            "success": len(self.errors) == 0
        }

async def main():
    """Основная функция"""
    logger.info("🚀 Запуск автоматического исправления диагностических тестов...")
    
    fixer = DiagnosticAutoFixer()
    report = await fixer.fix_all_diagnostic_tests()
    
    # Выводим отчет
    print("=" * 60)
    print("📊 ОТЧЕТ ОБ АВТОМАТИЧЕСКИХ ИСПРАВЛЕНИЯХ")
    print("=" * 60)
    
    print(f"\n🔧 ИСПРАВЛЕНИЯ ({report['total_fixes']}):")
    for fix in report['fixes_applied']:
        print(f"   ✅ {fix}")
    
    if report['errors']:
        print(f"\n❌ ОШИБКИ ({report['total_errors']}):")
        for error in report['errors']:
            print(f"   ❌ {error}")
    
    if report['warnings']:
        print(f"\n⚠️ ПРЕДУПРЕЖДЕНИЯ ({len(report['warnings'])}):")
        for warning in report['warnings']:
            print(f"   ⚠️ {warning}")
    
    if report['success']:
        print(f"\n🎉 Все исправления применены успешно!")
        print(f"   Система диагностики готова к работе")
    else:
        print(f"\n❌ Некоторые исправления не удалось применить")
        print(f"   Проверьте ошибки выше")
    
    return 0 if report['success'] else 1

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
