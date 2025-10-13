#!/usr/bin/env python3
"""
Исправления проблем с импортами и зависимостями в диагностических тестах
"""

import asyncio
import logging
import sys
import os
from typing import Dict, List, Any, Optional

# Добавляем путь к модулям
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

logger = logging.getLogger(__name__)

class ImportFixer:
    """Класс для исправления проблем с импортами"""
    
    @staticmethod
    def fix_input_processing_imports():
        """Исправление импортов для InputProcessing"""
        try:
            # Проверяем существование файлов
            keyboard_monitor_path = "modules/input_processing/keyboard/keyboard_monitor.py"
            types_path = "modules/input_processing/keyboard/types.py"
            
            if os.path.exists(keyboard_monitor_path):
                from modules.input_processing.keyboard.keyboard_monitor import KeyboardMonitor
                logger.info("✅ KeyboardMonitor импортирован успешно")
                return KeyboardMonitor
            else:
                logger.warning(f"⚠️ Файл {keyboard_monitor_path} не найден")
                return None
                
        except ImportError as e:
            logger.error(f"❌ Ошибка импорта KeyboardMonitor: {e}")
            return None
    
    @staticmethod
    def fix_speech_playback_imports():
        """Исправление импортов для SpeechPlayback"""
        try:
            # Проверяем существование файлов
            player_path = "modules/speech_playback/core/player.py"
            buffer_path = "modules/speech_playback/core/buffer.py"
            
            if os.path.exists(player_path) and os.path.exists(buffer_path):
                from modules.speech_playback.core.player import SequentialSpeechPlayer
                from modules.speech_playback.core.buffer import ChunkBuffer
                logger.info("✅ SpeechPlayback компоненты импортированы успешно")
                return SequentialSpeechPlayer, ChunkBuffer
            else:
                logger.warning(f"⚠️ Файлы SpeechPlayback не найдены")
                return None, None
                
        except ImportError as e:
            logger.error(f"❌ Ошибка импорта SpeechPlayback: {e}")
            return None, None
    
    @staticmethod
    def fix_network_manager_imports():
        """Исправление импортов для NetworkManager"""
        try:
            # Проверяем существование файлов
            network_manager_path = "modules/network_manager/core/network_manager.py"
            
            if os.path.exists(network_manager_path):
                from modules.network_manager.core.network_manager import NetworkManager
                logger.info("✅ NetworkManager импортирован успешно")
                return NetworkManager
            else:
                logger.warning(f"⚠️ Файл {network_manager_path} не найден")
                return None
                
        except ImportError as e:
            logger.error(f"❌ Ошибка импорта NetworkManager: {e}")
            return None
    
    @staticmethod
    def fix_grpc_client_imports():
        """Исправление импортов для GrpcClient"""
        try:
            # Проверяем существование файлов
            grpc_client_path = "modules/grpc_client/core/grpc_client.py"
            connection_manager_path = "modules/grpc_client/core/connection_manager.py"
            health_checker_path = "modules/grpc_client/core/health_checker.py"
            retry_manager_path = "modules/grpc_client/core/retry_manager.py"
            
            if all(os.path.exists(p) for p in [grpc_client_path, connection_manager_path, health_checker_path, retry_manager_path]):
                from modules.grpc_client.core.grpc_client import GrpcClient
                from modules.grpc_client.core.connection_manager import ConnectionManager
                from modules.grpc_client.core.health_checker import HealthChecker
                from modules.grpc_client.core.retry_manager import RetryManager
                logger.info("✅ GrpcClient компоненты импортированы успешно")
                return GrpcClient, ConnectionManager, HealthChecker, RetryManager
            else:
                logger.warning(f"⚠️ Файлы GrpcClient не найдены")
                return None, None, None, None
                
        except ImportError as e:
            logger.error(f"❌ Ошибка импорта GrpcClient: {e}")
            return None, None, None, None
    
    @staticmethod
    def fix_permissions_imports():
        """Исправление импортов для Permissions"""
        try:
            # Проверяем существование файлов
            permissions_manager_path = "modules/permissions/core/permissions_manager.py"
            permission_handler_path = "modules/permissions/macos/permission_handler.py"
            
            if os.path.exists(permissions_manager_path) and os.path.exists(permission_handler_path):
                from modules.permissions.core.permissions_manager import PermissionManager
                from modules.permissions.macos.permission_handler import MacOSPermissionHandler
                logger.info("✅ Permissions компоненты импортированы успешно")
                return PermissionManager, MacOSPermissionHandler
            else:
                logger.warning(f"⚠️ Файлы Permissions не найдены")
                return None, None
                
        except ImportError as e:
            logger.error(f"❌ Ошибка импорта Permissions: {e}")
            return None, None
    
    @staticmethod
    def fix_mode_management_imports():
        """Исправление импортов для ModeManagement"""
        try:
            # Проверяем существование файлов
            mode_controller_path = "modules/mode_management/core/mode_controller.py"
            types_path = "modules/mode_management/core/types.py"
            
            if os.path.exists(mode_controller_path) and os.path.exists(types_path):
                from modules.mode_management.core.mode_controller import ModeController
                from modules.mode_management.core.types import AppMode
                logger.info("✅ ModeManagement компоненты импортированы успешно")
                return ModeController, AppMode
            else:
                logger.warning(f"⚠️ Файлы ModeManagement не найдены")
                return None, None
                
        except ImportError as e:
            logger.error(f"❌ Ошибка импорта ModeManagement: {e}")
            return None, None

class DependencyChecker:
    """Класс для проверки зависимостей"""
    
    @staticmethod
    def check_python_packages():
        """Проверка Python пакетов"""
        required_packages = [
            'asyncio',
            'logging',
            'typing',
            'dataclasses',
            'numpy',
            'sounddevice',
            'grpcio',
            'grpcio-tools'
        ]
        
        missing_packages = []
        
        for package in required_packages:
            try:
                __import__(package.replace('-', '_'))
                logger.info(f"✅ Пакет {package} доступен")
            except ImportError:
                missing_packages.append(package)
                logger.warning(f"⚠️ Пакет {package} не найден")
        
        if missing_packages:
            logger.error(f"❌ Отсутствующие пакеты: {missing_packages}")
            return False
        else:
            logger.info("✅ Все необходимые пакеты доступны")
            return True
    
    @staticmethod
    def check_system_dependencies():
        """Проверка системных зависимостей"""
        system_deps = [
            'switchaudio',
            'ffmpeg'
        ]
        
        missing_deps = []
        
        for dep in system_deps:
            try:
                result = os.system(f"which {dep} > /dev/null 2>&1")
                if result == 0:
                    logger.info(f"✅ Системная зависимость {dep} доступна")
                else:
                    missing_deps.append(dep)
                    logger.warning(f"⚠️ Системная зависимость {dep} не найдена")
            except Exception as e:
                missing_deps.append(dep)
                logger.error(f"❌ Ошибка проверки {dep}: {e}")
        
        if missing_deps:
            logger.error(f"❌ Отсутствующие системные зависимости: {missing_deps}")
            return False
        else:
            logger.info("✅ Все необходимые системные зависимости доступны")
            return True

async def main():
    """Демонстрация исправлений импортов"""
    logger.info("🔧 Демонстрация исправлений проблем с импортами...")
    
    # Проверяем зависимости
    logger.info("\n📦 Проверка зависимостей...")
    dep_checker = DependencyChecker()
    
    python_ok = dep_checker.check_python_packages()
    system_ok = dep_checker.check_system_dependencies()
    
    if not python_ok or not system_ok:
        logger.error("❌ Не все зависимости доступны")
        return 1
    
    # Исправляем импорты
    logger.info("\n🔧 Исправление импортов...")
    import_fixer = ImportFixer()
    
    # Тестируем импорты для каждого модуля
    modules = [
        ('InputProcessing', import_fixer.fix_input_processing_imports),
        ('SpeechPlayback', import_fixer.fix_speech_playback_imports),
        ('NetworkManager', import_fixer.fix_network_manager_imports),
        ('GrpcClient', import_fixer.fix_grpc_client_imports),
        ('Permissions', import_fixer.fix_permissions_imports),
        ('ModeManagement', import_fixer.fix_mode_management_imports)
    ]
    
    success_count = 0
    
    for module_name, fix_func in modules:
        try:
            logger.info(f"\n📱 Тестирование импортов {module_name}...")
            result = fix_func()
            
            if result is not None:
                logger.info(f"✅ {module_name} импорты исправлены")
                success_count += 1
            else:
                logger.error(f"❌ {module_name} импорты не исправлены")
                
        except Exception as e:
            logger.error(f"❌ Ошибка при исправлении импортов {module_name}: {e}")
    
    logger.info(f"\n🎯 Результат: {success_count}/{len(modules)} модулей успешно импортированы")
    
    if success_count == len(modules):
        logger.info("🎉 Все импорты исправлены успешно!")
        return 0
    else:
        logger.error("❌ Некоторые импорты не удалось исправить")
        return 1

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
