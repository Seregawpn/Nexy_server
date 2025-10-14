#!/usr/bin/env python3
"""
Быстрая диагностика без зависающих тестов
"""

import asyncio
import logging
import sys
import os

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Добавляем пути
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '.'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'tests/modules'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'tests/integrations'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'tests/config'))

async def run_quick_diagnostics():
    """Быстрая диагностика без зависающих тестов"""
    logger.info("🚀 Запуск быстрой диагностики...")
    
    results = {}
    total_tests = 0
    successful_tests = 0
    
    # Тестируем только быстрые модули
    quick_modules = [
        'diagnostic_audio_device_manager',
        'diagnostic_grpc_client', 
        'diagnostic_input_processing',
        'diagnostic_speech_playback',
        'diagnostic_permissions',
        'diagnostic_mode_management',
        'diagnostic_audio_device_integration',
        'diagnostic_unified_config'
    ]
    
    for module_name in quick_modules:
        try:
            logger.info(f"🔍 Тестирование {module_name}...")
            
            if module_name.startswith('diagnostic_'):
                # Импортируем модуль
                module = __import__(module_name)
                
                # Находим класс диагностики
                class_name = None
                for attr_name in dir(module):
                    attr = getattr(module, attr_name)
                    if (isinstance(attr, type) and 
                        hasattr(attr, 'run_diagnostic') and 
                        attr_name.endswith('Diagnostic')):
                        class_name = attr_name
                        break
                
                if class_name:
                    diagnostic_class = getattr(module, class_name)
                    diagnostic = diagnostic_class()
                    
                    # Запускаем диагностику
                    if asyncio.iscoroutinefunction(diagnostic.run_diagnostic):
                        result = await diagnostic.run_diagnostic()
                    else:
                        result = diagnostic.run_diagnostic()
                    
                    if isinstance(result, dict):
                        total = result.get('total_tests', 0)
                        successful = result.get('successful_tests', 0)
                        success_rate = result.get('success_rate', 0)
                        
                        total_tests += total
                        successful_tests += successful
                        
                        results[module_name] = {
                            'total': total,
                            'successful': successful,
                            'success_rate': success_rate,
                            'status': '✅' if success_rate == 100 else '⚠️'
                        }
                        
                        logger.info(f"   {results[module_name]['status']} {module_name}: {successful}/{total} ({success_rate:.1f}%)")
                    else:
                        logger.warning(f"   ⚠️ {module_name}: неожиданный формат результата")
                        results[module_name] = {'status': '❌', 'error': 'Неожиданный формат'}
                else:
                    logger.warning(f"   ❌ {module_name}: класс диагностики не найден")
                    results[module_name] = {'status': '❌', 'error': 'Класс не найден'}
            else:
                logger.warning(f"   ⚠️ {module_name}: пропущен (не диагностический модуль)")
                
        except Exception as e:
            logger.error(f"   ❌ {module_name}: ошибка - {e}")
            results[module_name] = {'status': '❌', 'error': str(e)}
    
    # Выводим итоговую статистику
    overall_success_rate = (successful_tests / total_tests * 100) if total_tests > 0 else 0
    
    print(f"\n{'='*60}")
    print(f"📊 БЫСТРАЯ ДИАГНОСТИКА ЗАВЕРШЕНА")
    print(f"{'='*60}")
    print(f"Всего тестов: {total_tests}")
    print(f"✅ Успешных: {successful_tests}")
    print(f"❌ Неудачных: {total_tests - successful_tests}")
    print(f"📈 Успешность: {overall_success_rate:.1f}%")
    
    print(f"\n📋 РЕЗУЛЬТАТЫ ПО МОДУЛЯМ:")
    for module_name, result in results.items():
        if 'error' in result:
            print(f"   {result['status']} {module_name}: {result['error']}")
        else:
            print(f"   {result['status']} {module_name}: {result['successful']}/{result['total']} ({result['success_rate']:.1f}%)")
    
    return overall_success_rate == 100.0

if __name__ == "__main__":
    success = asyncio.run(run_quick_diagnostics())
    sys.exit(0 if success else 1)
