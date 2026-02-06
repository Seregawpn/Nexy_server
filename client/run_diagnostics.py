#!/usr/bin/env python3
"""
Главный диагностический скрипт
Запускает все диагностические тесты и выводит сводный отчет
"""

import asyncio
import importlib
import logging
import os
import sys
from typing import Any

# Добавляем путь к модулям
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '.'))

# Импортируем диагностические модули
# DiagnosticSuite теперь встроен в этот файл

# Добавляем путь к тестам
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'tests/modules'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'tests/integrations'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'tests/config'))

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def _load_diagnostic_class(module_name: str, class_name: str) -> type:
    """Динамически загружает диагностический класс с fallback-реализацией."""
    try:
        module = importlib.import_module(module_name)
        loaded_class = getattr(module, class_name)
        if isinstance(loaded_class, type):
            return loaded_class
        raise TypeError(f"{class_name} is not a class")
    except Exception as exc:
        logger.warning(f"⚠️ Diagnostic import skipped: {module_name}.{class_name} ({exc})")

        class _MissingDiagnostic:
            async def run_diagnostic(self) -> dict[str, Any]:
                return {
                    "success": False,
                    "skipped": True,
                    "error": f"Diagnostic module unavailable: {module_name}.{class_name}",
                    "total_tests": 0,
                    "successful_tests": 0,
                    "results": [],
                }

        return _MissingDiagnostic


AudioDeviceIntegrationDiagnostic = _load_diagnostic_class("diagnostic_audio_device_integration", "AudioDeviceIntegrationDiagnostic")
AudioDeviceManagerDiagnostic = _load_diagnostic_class("diagnostic_audio_device_manager", "AudioDeviceManagerDiagnostic")
AutostartManagerIntegrationDiagnostic = _load_diagnostic_class("diagnostic_autostart_manager_integration", "AutostartManagerIntegrationDiagnostic")
GrpcClientDiagnostic = _load_diagnostic_class("diagnostic_grpc_client", "GrpcClientDiagnostic")
GrpcClientIntegrationDiagnostic = _load_diagnostic_class("diagnostic_grpc_client_integration", "GrpcClientIntegrationDiagnostic")
HardwareIdIntegrationDiagnostic = _load_diagnostic_class("diagnostic_hardware_id_integration", "HardwareIdIntegrationDiagnostic")
InputProcessingDiagnostic = _load_diagnostic_class("diagnostic_input_processing", "InputProcessingDiagnostic")
InputProcessingIntegrationDiagnostic = _load_diagnostic_class("diagnostic_input_processing_integration", "InputProcessingIntegrationDiagnostic")
InstanceManagerIntegrationDiagnostic = _load_diagnostic_class("diagnostic_instance_manager_integration", "InstanceManagerIntegrationDiagnostic")
InterruptManagementIntegrationDiagnostic = _load_diagnostic_class("diagnostic_interrupt_management_integration", "InterruptManagementIntegrationDiagnostic")
ModeManagementDiagnostic = _load_diagnostic_class("diagnostic_mode_management", "ModeManagementDiagnostic")
ModeManagementIntegrationDiagnostic = _load_diagnostic_class("diagnostic_mode_management_integration", "ModeManagementIntegrationDiagnostic")
NetworkManagerDiagnostic = _load_diagnostic_class("diagnostic_network_manager", "NetworkManagerDiagnostic")
NetworkManagerIntegrationDiagnostic = _load_diagnostic_class("diagnostic_network_manager_integration", "NetworkManagerIntegrationDiagnostic")
PermissionsDiagnostic = _load_diagnostic_class("diagnostic_permissions", "PermissionsDiagnostic")
ScreenshotCaptureIntegrationDiagnostic = _load_diagnostic_class("diagnostic_screenshot_capture_integration", "ScreenshotCaptureIntegrationDiagnostic")
SignalIntegrationDiagnostic = _load_diagnostic_class("diagnostic_signal_integration", "SignalIntegrationDiagnostic")
SpeechPlaybackDiagnostic = _load_diagnostic_class("diagnostic_speech_playback", "SpeechPlaybackDiagnostic")
SpeechPlaybackIntegrationDiagnostic = _load_diagnostic_class("diagnostic_speech_playback_integration", "SpeechPlaybackIntegrationDiagnostic")
TrayControllerIntegrationDiagnostic = _load_diagnostic_class("diagnostic_tray_controller_integration", "TrayControllerIntegrationDiagnostic")
UnifiedConfigDiagnostic = _load_diagnostic_class("diagnostic_unified_config", "UnifiedConfigDiagnostic")
UpdaterIntegrationDiagnostic = _load_diagnostic_class("diagnostic_updater_integration", "UpdaterIntegrationDiagnostic")
VoiceRecognitionDiagnostic = _load_diagnostic_class("diagnostic_voice_recognition", "VoiceRecognitionDiagnostic")
VoiceRecognitionIntegrationDiagnostic = _load_diagnostic_class("diagnostic_voice_recognition_integration", "VoiceRecognitionIntegrationDiagnostic")
VoiceOverDuckingIntegrationDiagnostic = _load_diagnostic_class("diagnostic_voiceover_ducking_integration", "VoiceOverDuckingIntegrationDiagnostic")
WelcomeMessageIntegrationDiagnostic = _load_diagnostic_class("diagnostic_welcome_message_integration", "WelcomeMessageIntegrationDiagnostic")

class MasterDiagnostic:
    """Главный диагностический класс"""
    
    def __init__(self):
        self.results = {}
        self.all_results = {}
        
    async def run_all_diagnostics(self) -> dict[str, Any]:
        """Запуск всех диагностических тестов"""
        logger.info("🚀 Запуск полного диагностического пакета...")
        
        # 1. Общий диагностический пакет
        logger.info("\n" + "="*60)
        logger.info("1️⃣ ОБЩИЙ ДИАГНОСТИЧЕСКИЙ ПАКЕТ")
        logger.info("="*60)
        self.results['general'] = {
            "total_tests": 0,
            "successful_tests": 0,
            "results": [],
            "skipped": True,
            "reason": "legacy_general_suite_removed",
        }
        
        # 2. Тесты модулей
        logger.info("\n" + "="*60)
        logger.info("2️⃣ ТЕСТЫ МОДУЛЕЙ")
        logger.info("="*60)
        
        # AudioDeviceManager
        logger.info("\n📱 Тестирование AudioDeviceManager...")
        try:
            audio_manager_diagnostic = AudioDeviceManagerDiagnostic()
            audio_manager_results = await audio_manager_diagnostic.run_diagnostic()
            self.results['audio_device_manager'] = audio_manager_results
            
        except Exception as e:
            logger.error(f"❌ Ошибка тестирования AudioDeviceManager: {e}")
            self.results['audio_device_manager'] = {"error": str(e), "success": False}
        
        # SpeechRecognizer
        logger.info("\n🎤 Тестирование SpeechRecognizer...")
        try:
            speech_recognizer_diagnostic = VoiceRecognitionDiagnostic()
            speech_recognizer_results = await speech_recognizer_diagnostic.run_diagnostic()
            self.results['speech_recognizer'] = speech_recognizer_results
            
        except Exception as e:
            logger.error(f"❌ Ошибка тестирования SpeechRecognizer: {e}")
            self.results['speech_recognizer'] = {"error": str(e), "success": False}
        
        # GrpcClient
        logger.info("\n🌐 Тестирование GrpcClient...")
        try:
            grpc_client_diagnostic = GrpcClientDiagnostic()
            grpc_client_results = await grpc_client_diagnostic.run_diagnostic()
            self.results['grpc_client'] = grpc_client_results
            
        except Exception as e:
            logger.error(f"❌ Ошибка тестирования GrpcClient: {e}")
            self.results['grpc_client'] = {"error": str(e), "success": False}
        
        # InputProcessing
        logger.info("\n⌨️ Тестирование InputProcessing...")
        try:
            input_processing_diagnostic = InputProcessingDiagnostic()
            input_processing_results = await input_processing_diagnostic.run_diagnostic()
            self.results['input_processing'] = input_processing_results
            
        except Exception as e:
            logger.error(f"❌ Ошибка тестирования InputProcessing: {e}")
            self.results['input_processing'] = {"error": str(e), "success": False}
        
        # SpeechPlayback
        logger.info("\n🔊 Тестирование SpeechPlayback...")
        try:
            speech_playback_diagnostic = SpeechPlaybackDiagnostic()
            speech_playback_results = await speech_playback_diagnostic.run_diagnostic()
            self.results['speech_playback'] = speech_playback_results
            
        except Exception as e:
            logger.error(f"❌ Ошибка тестирования SpeechPlayback: {e}")
            self.results['speech_playback'] = {"error": str(e), "success": False}
        
        # Permissions
        logger.info("\n🔐 Тестирование Permissions...")
        try:
            permissions_diagnostic = PermissionsDiagnostic()
            permissions_results = await permissions_diagnostic.run_diagnostic()
            self.results['permissions'] = permissions_results
            
        except Exception as e:
            logger.error(f"❌ Ошибка тестирования Permissions: {e}")
            self.results['permissions'] = {"error": str(e), "success": False}
        
        # NetworkManager
        logger.info("\n🌐 Тестирование NetworkManager...")
        try:
            network_manager_diagnostic = NetworkManagerDiagnostic()
            network_manager_results = await network_manager_diagnostic.run_diagnostic()
            self.results['network_manager'] = network_manager_results
            
        except Exception as e:
            logger.error(f"❌ Ошибка тестирования NetworkManager: {e}")
            self.results['network_manager'] = {"error": str(e), "success": False}
        
        # ModeManagement
        logger.info("\n🔄 Тестирование ModeManagement...")
        try:
            mode_management_diagnostic = ModeManagementDiagnostic()
            mode_management_results = await mode_management_diagnostic.run_diagnostic()
            self.results['mode_management'] = mode_management_results
            
        except Exception as e:
            logger.error(f"❌ Ошибка тестирования ModeManagement: {e}")
            self.results['mode_management'] = {"error": str(e), "success": False}
        
        # 3. Тесты интеграций
        logger.info("\n" + "="*60)
        logger.info("3️⃣ ТЕСТЫ ИНТЕГРАЦИЙ")
        logger.info("="*60)
        
        # AudioDeviceIntegration
        logger.info("\n🔗 Тестирование AudioDeviceIntegration...")
        try:
            audio_integration_diagnostic = AudioDeviceIntegrationDiagnostic()
            self.results['audio_device_integration'] = await audio_integration_diagnostic.run_diagnostic()
        except Exception as e:
            logger.error(f"❌ Ошибка тестирования AudioDeviceIntegration: {e}")
            self.results['audio_device_integration'] = {"error": str(e), "success": False}
        
        # GrpcClientIntegration
        logger.info("\n🌐 Тестирование GrpcClientIntegration...")
        try:
            grpc_integration_diagnostic = GrpcClientIntegrationDiagnostic()
            self.results['grpc_client_integration'] = await grpc_integration_diagnostic.run_diagnostic()
        except Exception as e:
            logger.error(f"❌ Ошибка тестирования GrpcClientIntegration: {e}")
            self.results['grpc_client_integration'] = {"error": str(e), "success": False}
        
        # ModeManagementIntegration
        logger.info("\n🔄 Тестирование ModeManagementIntegration...")
        try:
            mode_integration_diagnostic = ModeManagementIntegrationDiagnostic()
            self.results['mode_management_integration'] = await mode_integration_diagnostic.run_diagnostic()
        except Exception as e:
            logger.error(f"❌ Ошибка тестирования ModeManagementIntegration: {e}")
            self.results['mode_management_integration'] = {"error": str(e), "success": False}
        
        # InputProcessingIntegration
        logger.info("\n⌨️ Тестирование InputProcessingIntegration...")
        try:
            input_integration_diagnostic = InputProcessingIntegrationDiagnostic()
            self.results['input_processing_integration'] = await input_integration_diagnostic.run_diagnostic()
        except Exception as e:
            logger.error(f"❌ Ошибка тестирования InputProcessingIntegration: {e}")
            self.results['input_processing_integration'] = {"error": str(e), "success": False}
        
        # AutostartManagerIntegration
        logger.info("\n🚀 Тестирование AutostartManagerIntegration...")
        try:
            autostart_integration_diagnostic = AutostartManagerIntegrationDiagnostic()
            self.results['autostart_manager_integration'] = await autostart_integration_diagnostic.run_diagnostic()
        except Exception as e:
            logger.error(f"❌ Ошибка тестирования AutostartManagerIntegration: {e}")
            self.results['autostart_manager_integration'] = {"error": str(e), "success": False}
        
        # HardwareIdIntegration
        logger.info("\n🆔 Тестирование HardwareIdIntegration...")
        try:
            hardware_integration_diagnostic = HardwareIdIntegrationDiagnostic()
            self.results['hardware_id_integration'] = await hardware_integration_diagnostic.run_diagnostic()
        except Exception as e:
            logger.error(f"❌ Ошибка тестирования HardwareIdIntegration: {e}")
            self.results['hardware_id_integration'] = {"error": str(e), "success": False}
        
        # InstanceManagerIntegration
        logger.info("\n📦 Тестирование InstanceManagerIntegration...")
        try:
            instance_integration_diagnostic = InstanceManagerIntegrationDiagnostic()
            self.results['instance_manager_integration'] = await instance_integration_diagnostic.run_diagnostic()
        except Exception as e:
            logger.error(f"❌ Ошибка тестирования InstanceManagerIntegration: {e}")
            self.results['instance_manager_integration'] = {"error": str(e), "success": False}
        
        # SpeechPlaybackIntegration
        logger.info("\n🔊 Тестирование SpeechPlaybackIntegration...")
        try:
            speech_integration_diagnostic = SpeechPlaybackIntegrationDiagnostic()
            self.results['speech_playback_integration'] = await speech_integration_diagnostic.run_diagnostic()
        except Exception as e:
            logger.error(f"❌ Ошибка тестирования SpeechPlaybackIntegration: {e}")
            self.results['speech_playback_integration'] = {"error": str(e), "success": False}
        
        # VoiceRecognitionIntegration
        logger.info("\n🎤 Тестирование VoiceRecognitionIntegration...")
        try:
            voice_integration_diagnostic = VoiceRecognitionIntegrationDiagnostic()
            self.results['voice_recognition_integration'] = await voice_integration_diagnostic.run_diagnostic()
        except Exception as e:
            logger.error(f"❌ Ошибка тестирования VoiceRecognitionIntegration: {e}")
            self.results['voice_recognition_integration'] = {"error": str(e), "success": False}
        
        # TrayControllerIntegration
        logger.info("\n📋 Тестирование TrayControllerIntegration...")
        try:
            tray_integration_diagnostic = TrayControllerIntegrationDiagnostic()
            self.results['tray_controller_integration'] = await tray_integration_diagnostic.run_diagnostic()
        except Exception as e:
            logger.error(f"❌ Ошибка тестирования TrayControllerIntegration: {e}")
            self.results['tray_controller_integration'] = {"error": str(e), "success": False}
        
        # InterruptManagementIntegration
        logger.info("\n⚠️ Тестирование InterruptManagementIntegration...")
        try:
            interrupt_integration_diagnostic = InterruptManagementIntegrationDiagnostic()
            self.results['interrupt_management_integration'] = await interrupt_integration_diagnostic.run_diagnostic()
        except Exception as e:
            logger.error(f"❌ Ошибка тестирования InterruptManagementIntegration: {e}")
            self.results['interrupt_management_integration'] = {"error": str(e), "success": False}
        
        # NetworkManagerIntegration
        logger.info("\n🌐 Тестирование NetworkManagerIntegration...")
        try:
            network_integration_diagnostic = NetworkManagerIntegrationDiagnostic()
            self.results['network_manager_integration'] = await network_integration_diagnostic.run_diagnostic()
        except Exception as e:
            logger.error(f"❌ Ошибка тестирования NetworkManagerIntegration: {e}")
            self.results['network_manager_integration'] = {"error": str(e), "success": False}
        
        # ScreenshotCaptureIntegration
        logger.info("\n📸 Тестирование ScreenshotCaptureIntegration...")
        try:
            screenshot_integration_diagnostic = ScreenshotCaptureIntegrationDiagnostic()
            self.results['screenshot_capture_integration'] = await screenshot_integration_diagnostic.run_diagnostic()
        except Exception as e:
            logger.error(f"❌ Ошибка тестирования ScreenshotCaptureIntegration: {e}")
            self.results['screenshot_capture_integration'] = {"error": str(e), "success": False}
        
        # SignalIntegration
        logger.info("\n📡 Тестирование SignalIntegration...")
        try:
            signal_integration_diagnostic = SignalIntegrationDiagnostic()
            self.results['signal_integration'] = await signal_integration_diagnostic.run_diagnostic()
        except Exception as e:
            logger.error(f"❌ Ошибка тестирования SignalIntegration: {e}")
            self.results['signal_integration'] = {"error": str(e), "success": False}
        
        # UpdaterIntegration
        logger.info("\n🔄 Тестирование UpdaterIntegration...")
        try:
            updater_integration_diagnostic = UpdaterIntegrationDiagnostic()
            self.results['updater_integration'] = await updater_integration_diagnostic.run_diagnostic()
        except Exception as e:
            logger.error(f"❌ Ошибка тестирования UpdaterIntegration: {e}")
            self.results['updater_integration'] = {"error": str(e), "success": False}
        
        # VoiceoverDuckingIntegration
        logger.info("\n🔊 Тестирование VoiceoverDuckingIntegration...")
        try:
            voiceover_integration_diagnostic = VoiceOverDuckingIntegrationDiagnostic()
            self.results['voiceover_ducking_integration'] = await voiceover_integration_diagnostic.run_diagnostic()
        except Exception as e:
            logger.error(f"❌ Ошибка тестирования VoiceoverDuckingIntegration: {e}")
            self.results['voiceover_ducking_integration'] = {"error": str(e), "success": False}
        
        # WelcomeMessageIntegration
        logger.info("\n👋 Тестирование WelcomeMessageIntegration...")
        try:
            welcome_integration_diagnostic = WelcomeMessageIntegrationDiagnostic()
            self.results['welcome_message_integration'] = await welcome_integration_diagnostic.run_diagnostic()
        except Exception as e:
            logger.error(f"❌ Ошибка тестирования WelcomeMessageIntegration: {e}")
            self.results['welcome_message_integration'] = {"error": str(e), "success": False}
        
        # 4. Тесты конфигурации
        logger.info("\n" + "="*60)
        logger.info("4️⃣ ТЕСТЫ КОНФИГУРАЦИИ")
        logger.info("="*60)
        
        # UnifiedConfig
        logger.info("\n⚙️ Тестирование unified_config.yaml...")
        try:
            config_diagnostic = UnifiedConfigDiagnostic()
            config_results = config_diagnostic.run_diagnostic()
            self.results['unified_config'] = config_results
        except Exception as e:
            logger.error(f"❌ Ошибка тестирования unified_config.yaml: {e}")
            self.results['unified_config'] = {"error": str(e), "success": False}
        
        # Копируем все результаты для детального анализа
        self.all_results = self.results.copy()
        
        return self._generate_summary()
    
    def _generate_summary(self) -> dict[str, Any]:
        """Генерация сводного отчета"""
        logger.info("\n" + "="*60)
        logger.info("📊 СВОДНЫЙ ОТЧЕТ")
        logger.info("="*60)
        
        total_tests = 0
        total_successful = 0
        total_failed = 0
        
        print(f"\n📋 РЕЗУЛЬТАТЫ ПО КАТЕГОРИЯМ:")
        
        for category, results in self.results.items():
            if isinstance(results, dict) and 'total_tests' in results:
                category_tests = results['total_tests']
                category_successful = results.get('successful_tests', 0)
                category_failed = category_tests - category_successful
                
                total_tests += category_tests
                total_successful += category_successful
                total_failed += category_failed
                
                success_rate = (category_successful / category_tests * 100) if category_tests > 0 else 0
                status = "✅" if category_failed == 0 else "❌"
                
                print(f"   {status} {category.upper()}: {category_successful}/{category_tests} ({success_rate:.1f}%)")
            elif isinstance(results, dict) and 'error' in results:
                print(f"   ❌ {category.upper()}: ОШИБКА - {results['error']}")
                total_failed += 1
            else:
                print(f"   ⚠️ {category.upper()}: НЕИЗВЕСТНЫЙ РЕЗУЛЬТАТ")
        
        overall_success_rate = (total_successful / total_tests * 100) if total_tests > 0 else 0
        
        print(f"\n{'='*80}")
        print(f"🎯 ФИНАЛЬНЫЙ ОТЧЕТ СИСТЕМЫ")
        print(f"{'='*80}")
        print(f"📊 ОБЩАЯ СТАТИСТИКА:")
        print(f"   Всего тестов: {total_tests}")
        print(f"   ✅ Успешных: {total_successful}")
        print(f"   ❌ Неудачных: {total_failed}")
        print(f"   📈 Успешность: {overall_success_rate:.1f}%")
        
        # Детальный анализ по категориям
        print(f"\n🔍 ДЕТАЛЬНЫЙ АНАЛИЗ ПО КАТЕГОРИЯМ:")
        print(f"{'-'*80}")
        
        for category, results in self.all_results.items():
            if isinstance(results, dict) and 'total_tests' in results:
                category_tests = results['total_tests']
                category_successful = results.get('successful_tests', 0)
                category_failed = category_tests - category_successful
                success_rate = (category_successful / category_tests * 100) if category_tests > 0 else 0
                
                status = "🟢" if category_failed == 0 else "🔴"
                print(f"   {status} {category.upper()}: {category_successful}/{category_tests} ({success_rate:.1f}%)")
                
                # Показываем ключевые результаты для каждой категории
                if 'results' in results and isinstance(results['results'], list) and results['results']:
                    key_results = []
                    for result in list(results['results'])[:3]:  # Показываем первые 3 результата
                        if result.get('success') and result.get('details'):
                            details = result['details']
                            if 'count' in details:
                                key_results.append(f"{details['count']} элементов")
                            elif 'device' in details:
                                key_results.append(f"устройство: {details['device']}")
                            elif 'value' in details:
                                key_results.append(f"значение: {details['value']}")
                    
                    if key_results:
                        print(f"      📋 Ключевые результаты: {', '.join(key_results)}")
        
        # Финальные рекомендации
        print(f"\n💡 ФИНАЛЬНЫЕ РЕКОМЕНДАЦИИ:")
        print(f"{'-'*80}")
        
        if total_failed == 0:
            print("   🎉 ВСЕ ТЕСТЫ ПРОШЛИ УСПЕШНО!")
            print("   🚀 Система полностью готова к работе.")
            print("   ✅ Все модули инициализированы корректно.")
            print("   ✅ Все интеграции функционируют правильно.")
            print("   ✅ Конфигурация загружена без ошибок.")
            print("   🎯 Nexy Client готов к использованию!")
        else:
            print(f"   ⚠️ ОБНАРУЖЕНЫ ПРОБЛЕМЫ:")
            print(f"   🔴 Требуется исправление {total_failed} проблем.")
            print(f"   🔧 Проверьте детальные отчеты выше.")
            print(f"   📋 Рекомендуется исправить проблемы перед использованием.")
            
            # Показываем наиболее проблемные категории
            problem_categories = []
            for category, results in self.all_results.items():
                if isinstance(results, dict) and 'total_tests' in results:
                    category_tests = results['total_tests']
                    category_successful = results.get('successful_tests', 0)
                    category_failed = category_tests - category_successful
                    if category_failed > 0:
                        problem_categories.append(f"{category} ({category_failed} проблем)")
            
            if problem_categories:
                print(f"   🎯 Наиболее проблемные области: {', '.join(problem_categories)}")
        
        print(f"\n{'='*80}")
        
        return {
            "total_tests": total_tests,
            "total_successful": total_successful,
            "total_failed": total_failed,
            "overall_success_rate": overall_success_rate,
            "categories": self.results
        }

async def main():
    """Основная функция"""
    diagnostic = MasterDiagnostic()
    results = await diagnostic.run_all_diagnostics()
    
    # Возвращаем код выхода
    return 1 if results["total_failed"] > 0 else 0

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
