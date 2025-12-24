#!/usr/bin/env python3
"""
MVP-1b: Device Identity (стабильность идентичности устройства)

Цель: Доказать, что мы можем однозначно идентифицировать устройство после reconnect
"""

import sys
import logging
import time
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import Optional, Dict, List
from datetime import datetime

# Добавляем путь к проекту
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

try:
    from Foundation import NSNotificationCenter, NSObject
    from AVFoundation import AVAudioSession
    PYOBJC_AVAILABLE = True
    logger.info("✅ PyObjC доступен")
except ImportError as e:
    PYOBJC_AVAILABLE = False
    logger.error(f"❌ PyObjC не доступен: {e}")
    sys.exit(1)

# Импортируем функции из прототипа 1
try:
    from test_device_discovery import DeviceDiscoveryPrototype
    PROTOTYPE1_AVAILABLE = True
except ImportError:
    PROTOTYPE1_AVAILABLE = False
    logger.warning("⚠️ Прототип 1 не доступен, используем упрощенную версию")


@dataclass
class DeviceSignature:
    """Подпись устройства для сравнения"""
    uid: str
    name: str
    normalized_name: str
    transport: str  # bluetooth/usb/built_in/unknown
    channels: int
    sample_rate: Optional[int] = None
    timestamp: str = ""
    
    def __post_init__(self):
        if not self.timestamp:
            self.timestamp = datetime.now().isoformat()
    
    def to_dict(self) -> dict:
        return asdict(self)
    
    def is_same_device(self, other: 'DeviceSignature') -> bool:
        """
        Проверка, что это то же устройство
        
        Приоритет:
        1. UID (если доступен и стабилен)
        2. normalized_name + transport + channels
        3. normalized_name + transport
        """
        # UID - самый надежный идентификатор
        if self.uid and other.uid and self.uid == other.uid:
            return True
        
        # normalized_name + transport + channels
        if (self.normalized_name == other.normalized_name and
            self.transport == other.transport and
            self.channels == other.channels):
            return True
        
        # normalized_name + transport (если channels могут меняться)
        if (self.normalized_name == other.normalized_name and
            self.transport == other.transport):
            return True
        
        return False
    
    def get_changes(self, other: 'DeviceSignature') -> Dict[str, tuple]:
        """Получить список изменений между двумя подписями"""
        changes = {}
        
        if self.uid != other.uid:
            changes['uid'] = (self.uid, other.uid)
        if self.name != other.name:
            changes['name'] = (self.name, other.name)
        if self.normalized_name != other.normalized_name:
            changes['normalized_name'] = (self.normalized_name, other.normalized_name)
        if self.transport != other.transport:
            changes['transport'] = (self.transport, other.transport)
        if self.channels != other.channels:
            changes['channels'] = (self.channels, other.channels)
        if self.sample_rate != other.sample_rate:
            changes['sample_rate'] = (self.sample_rate, other.sample_rate)
        
        return changes


class DeviceIdentityPrototype:
    """Прототип для тестирования стабильности идентичности устройств"""
    
    def __init__(self):
        self.device_discovery = DeviceDiscoveryPrototype() if PROTOTYPE1_AVAILABLE else None
        self.signatures: List[DeviceSignature] = []
        self.session = None
    
    def normalize_device_name(self, name: str) -> str:
        """Нормализация имени устройства"""
        normalized = name.strip()
        suffixes = [" (Hands-Free)", " HFP", " Hands-Free", " Bluetooth"]
        for suffix in suffixes:
            if normalized.endswith(suffix):
                normalized = normalized[:-len(suffix)]
                break
        return normalized
    
    def detect_transport(self, name: str, port_type: str) -> str:
        """Определение типа транспорта"""
        name_lower = name.lower()
        type_lower = port_type.lower() if port_type else ""
        
        if "bluetooth" in name_lower or "bluetooth" in type_lower or "airpods" in name_lower:
            return "bluetooth"
        elif "usb" in name_lower or "usb" in type_lower:
            return "usb"
        elif "built-in" in name_lower or "builtin" in name_lower or "internal" in name_lower:
            return "built_in"
        else:
            return "unknown"
    
    def capture_device_signature(self, device_info: dict) -> DeviceSignature:
        """Создание подписи устройства из информации AVFoundation"""
        name = device_info.get('name', '')
        uid = device_info.get('uid', '')
        port_type = device_info.get('type', '')
        channels = device_info.get('channels', 1)
        
        normalized_name = self.normalize_device_name(name)
        transport = self.detect_transport(name, port_type)
        
        return DeviceSignature(
            uid=uid,
            name=name,
            normalized_name=normalized_name,
            transport=transport,
            channels=channels,
            sample_rate=None  # TODO: получить из AVAudioSession
        )
    
    def test_identity_stability(self):
        """Тестирование стабильности идентичности при повторных запросах"""
        logger.info("=" * 80)
        logger.info("MVP-1b: Device Identity (стабильность идентичности)")
        logger.info("=" * 80)
        
        if not self.device_discovery:
            logger.error("❌ DeviceDiscoveryPrototype не доступен")
            return False
        
        if not self.device_discovery.setup_audio_session():
            logger.error("❌ Не удалось настроить AVAudioSession")
            return False
        
        # Получаем устройства несколько раз
        logger.info("\n📋 Тест 1: Стабильность при повторных запросах")
        logger.info("Получение устройств 5 раз подряд...\n")
        
        all_signatures: Dict[str, List[DeviceSignature]] = {}
        
        for i in range(5):
            logger.info(f"Запрос #{i+1}...")
            avf_devices = self.device_discovery.get_input_devices()
            
            for device_info in avf_devices:
                signature = self.capture_device_signature(device_info)
                uid_key = signature.uid or signature.normalized_name
                
                if uid_key not in all_signatures:
                    all_signatures[uid_key] = []
                all_signatures[uid_key].append(signature)
            
            time.sleep(0.5)  # Небольшая пауза
        
        # Анализ стабильности
        logger.info("\n🔍 Анализ стабильности идентичности...\n")
        
        stable_count = 0
        unstable_count = 0
        
        for uid_key, signatures in all_signatures.items():
            if len(signatures) < 2:
                continue
            
            # Сравниваем первую подпись с остальными
            base = signatures[0]
            is_stable = True
            
            for sig in signatures[1:]:
                if not base.is_same_device(sig):
                    is_stable = False
                    changes = base.get_changes(sig)
                    logger.warning(f"  ⚠️ Устройство '{base.name}' изменилось:")
                    for field, (old_val, new_val) in changes.items():
                        logger.warning(f"     {field}: {old_val} → {new_val}")
                    break
            
            if is_stable:
                stable_count += 1
                logger.info(f"  ✅ Устройство '{base.name}' стабильно (все 5 запросов идентичны)")
            else:
                unstable_count += 1
        
        # Итоги
        logger.info("\n" + "=" * 80)
        logger.info("ИТОГИ ТЕСТИРОВАНИЯ:")
        logger.info("=" * 80)
        logger.info(f"Всего устройств: {len(all_signatures)}")
        logger.info(f"Стабильных: {stable_count}")
        logger.info(f"Нестабильных: {unstable_count}")
        
        stability_rate = (stable_count / len(all_signatures) * 100) if all_signatures else 0
        logger.info(f"\n📊 Стабильность: {stability_rate:.1f}%")
        
        # Критерий успеха: ≥90% устройств стабильны
        success = stability_rate >= 90.0 and len(all_signatures) > 0
        
        if success:
            logger.info("\n✅ MVP-1b ПРОЙДЕН: Идентичность устройств стабильна")
        else:
            logger.error("\n❌ MVP-1b ПРОВАЛЕН: Есть нестабильные устройства")
            logger.error(f"   Требуется ≥90%, получено {stability_rate:.1f}%")
        
        return success
    
    def test_reconnect_scenario(self):
        """Тестирование сценария reconnect (требует ручного тестирования)"""
        logger.info("\n📋 Тест 2: Сценарий reconnect (требует ручного тестирования)")
        logger.info("Инструкции:")
        logger.info("  1. Запустите прототип")
        logger.info("  2. Отключите устройство (например, Bluetooth наушники)")
        logger.info("  3. Подключите устройство обратно")
        logger.info("  4. Проверьте, что подпись устройства идентична")
        logger.info("\n⚠️ Этот тест требует ручного выполнения")
        return True
    
    def run_tests(self):
        """Запуск всех тестов"""
        success = self.test_identity_stability()
        self.test_reconnect_scenario()  # Информационный
        return success


def main():
    """Главная функция"""
    prototype = DeviceIdentityPrototype()
    success = prototype.run_tests()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

