#!/usr/bin/env python3
"""
Тест мониторинга аудио устройств в реальном времени
Тестирует подключение/отключение устройств и корректность определения
"""

import asyncio
import logging
import sys
import time
from pathlib import Path
from datetime import datetime

# Добавляем путь к модулям
sys.path.insert(0, str(Path(__file__).parent))

from modules.audio_device_manager.core.device_manager import AudioDeviceManager
from modules.audio_device_manager.core.types import AudioDeviceManagerConfig
from config.unified_config_loader import UnifiedConfigLoader

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DeviceMonitor:
    """Монитор для отслеживания изменений устройств"""
    
    def __init__(self):
        self.last_devices = {}
        self.device_changes = []
        self.start_time = datetime.now()
    
    def on_device_change(self, devices_dict):
        """Callback для отслеживания изменений устройств"""
        current_time = datetime.now()
        current_devices = {device_id: device.name for device_id, device in devices_dict.items()}
        
        # Определяем изменения
        added_devices = set(current_devices.keys()) - set(self.last_devices.keys())
        removed_devices = set(self.last_devices.keys()) - set(current_devices.keys())
        
        if added_devices or removed_devices:
            change_info = {
                'timestamp': current_time,
                'added': {device_id: current_devices[device_id] for device_id in added_devices},
                'removed': {device_id: self.last_devices[device_id] for device_id in removed_devices}
            }
            self.device_changes.append(change_info)
            
            # Выводим изменения в реальном времени
            print(f"\n🔄 ИЗМЕНЕНИЕ УСТРОЙСТВ [{current_time.strftime('%H:%M:%S')}]")
            if added_devices:
                print("➕ ПОДКЛЮЧЕНЫ:")
                for device_id in added_devices:
                    print(f"   📱 {current_devices[device_id]} (ID: {device_id})")
            
            if removed_devices:
                print("➖ ОТКЛЮЧЕНЫ:")
                for device_id in removed_devices:
                    print(f"   📱 {self.last_devices[device_id]} (ID: {device_id})")
            
            print(f"📊 Всего устройств: {len(current_devices)}")
        
        self.last_devices = current_devices.copy()
    
    def print_summary(self):
        """Выводит сводку изменений"""
        print(f"\n📋 СВОДКА ИЗМЕНЕНИЙ УСТРОЙСТВ")
        print(f"⏱️  Время тестирования: {datetime.now() - self.start_time}")
        print(f"🔄 Всего изменений: {len(self.device_changes)}")
        
        if self.device_changes:
            print(f"\n📝 ДЕТАЛИ ИЗМЕНЕНИЙ:")
            for i, change in enumerate(self.device_changes, 1):
                print(f"\n{i}. {change['timestamp'].strftime('%H:%M:%S')}")
                if change['added']:
                    print("   ➕ Подключены:", ", ".join(change['added'].values()))
                if change['removed']:
                    print("   ➖ Отключены:", ", ".join(change['removed'].values()))

async def test_device_monitoring():
    """Тест мониторинга устройств в реальном времени"""
    print("🎧 ТЕСТ МОНИТОРИНГА АУДИО УСТРОЙСТВ В РЕАЛЬНОМ ВРЕМЕНИ")
    print("=" * 70)
    print("💡 ИНСТРУКЦИИ:")
    print("   1. Подключайте/отключайте наушники, AirPods, USB микрофоны")
    print("   2. Следите за сообщениями об изменениях устройств")
    print("   3. Нажмите Ctrl+C для завершения теста")
    print("=" * 70)
    
    try:
        # 1. Загружаем конфигурацию
        print("\n📋 ЭТАП 1: Загрузка конфигурации")
        config_loader = UnifiedConfigLoader()
        audio_config = config_loader.get_audio_config()
        print(f"✅ Конфигурация загружена")
        
        # 2. Создаем AudioDeviceManager
        print("\n📋 ЭТАП 2: Создание AudioDeviceManager")
        config = AudioDeviceManagerConfig(
            input_device_priorities=audio_config.get('input_device_priorities', {}),
            output_device_priorities=audio_config.get('output_device_priorities', {}),
            monitoring_interval=audio_config.get('monitoring_interval', 1.0),
            auto_switch_enabled=audio_config.get('auto_switch_enabled', True)
        )
        
        manager = AudioDeviceManager(config)
        print(f"✅ AudioDeviceManager создан")
        
        # 3. Создаем монитор устройств
        print("\n📋 ЭТАП 3: Создание монитора устройств")
        monitor = DeviceMonitor()
        
        # 4. Регистрируем callback для мониторинга
        print("\n📋 ЭТАП 4: Регистрация callback мониторинга")
        manager.device_monitor.register_callback("test_monitor", monitor.on_device_change)
        print(f"✅ Callback зарегистрирован")
        
        # 5. Запускаем AudioDeviceManager
        print("\n📋 ЭТАП 5: Запуск AudioDeviceManager")
        await manager.start()
        print(f"✅ AudioDeviceManager запущен")
        
        # 6. Показываем начальное состояние
        print("\n📋 ЭТАП 6: Начальное состояние устройств")
        print(f"📊 INPUT устройств: {len(manager.input_devices)}")
        for device_id, device in manager.input_devices.items():
            print(f"   🎤 {device.name} (ID: {device_id}, portaudio_index: {device.portaudio_index})")
        
        print(f"📊 OUTPUT устройств: {len(manager.output_devices)}")
        for device_id, device in manager.output_devices.items():
            print(f"   🔊 {device.name} (ID: {device_id}, portaudio_index: {device.portaudio_index})")
        
        # 7. Запускаем мониторинг в реальном времени
        print(f"\n🎧 МОНИТОРИНГ ЗАПУЩЕН!")
        print(f"⏱️  Интервал проверки: {config.monitoring_interval} сек")
        print(f"🔄 Подключайте/отключайте устройства для тестирования...")
        print(f"⏹️  Нажмите Ctrl+C для завершения")
        
        # Мониторинг в бесконечном цикле
        try:
            while True:
                await asyncio.sleep(1)
                
                # Показываем статистику каждые 10 секунд
                if int(time.time()) % 10 == 0:
                    current_time = datetime.now()
                    elapsed = current_time - monitor.start_time
                    print(f"\n⏱️  [{current_time.strftime('%H:%M:%S')}] Мониторинг активен ({elapsed.total_seconds():.0f}с)")
                    print(f"📊 Устройств: INPUT={len(manager.input_devices)}, OUTPUT={len(manager.output_devices)}")
                    print(f"🔄 Изменений: {len(monitor.device_changes)}")
                
        except KeyboardInterrupt:
            print(f"\n⏹️  Мониторинг остановлен пользователем")
        
        # 8. Показываем финальное состояние
        print(f"\n📋 ЭТАП 8: Финальное состояние устройств")
        print(f"📊 INPUT устройств: {len(manager.input_devices)}")
        for device_id, device in manager.input_devices.items():
            print(f"   🎤 {device.name} (ID: {device_id}, portaudio_index: {device.portaudio_index})")
        
        print(f"📊 OUTPUT устройств: {len(manager.output_devices)}")
        for device_id, device in manager.output_devices.items():
            print(f"   🔊 {device.name} (ID: {device_id}, portaudio_index: {device.portaudio_index})")
        
        # 9. Выводим сводку изменений
        monitor.print_summary()
        
        # 10. Останавливаем AudioDeviceManager
        print(f"\n📋 ЭТАП 10: Остановка AudioDeviceManager")
        await manager.stop()
        print(f"✅ AudioDeviceManager остановлен")
        
        # 11. Итоговый результат
        print(f"\n📋 ЭТАП 11: ИТОГОВЫЙ РЕЗУЛЬТАТ")
        if monitor.device_changes:
            print(f"✅ МОНИТОРИНГ РАБОТАЕТ! Обнаружено {len(monitor.device_changes)} изменений устройств")
            print(f"🎉 Приложение корректно определяет подключение/отключение устройств")
        else:
            print(f"⚠️  Изменений не обнаружено - попробуйте подключить/отключить устройства")
            print(f"💡 Убедитесь, что устройства действительно подключаются/отключаются")
        
    except Exception as e:
        logger.error(f"❌ Ошибка теста: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    try:
        asyncio.run(test_device_monitoring())
    except KeyboardInterrupt:
        print(f"\n⏹️  Тест прерван пользователем")
    except Exception as e:
        print(f"\n❌ Критическая ошибка: {e}")
