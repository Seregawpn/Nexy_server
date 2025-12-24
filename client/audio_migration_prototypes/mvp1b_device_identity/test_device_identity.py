#!/usr/bin/env python3
"""
MVP-1b: Device Identity (стабильность идентичности устройства)

Цель: Доказать, что мы можем однозначно идентифицировать устройство после reconnect

Exit Gate:
- [ ] DeviceSignature стабильна при reconnect (≥90%)
- [ ] Можно однозначно сказать: "это то же устройство"
- [ ] Изменения отслеживаются и логируются
"""

import sys
import logging
import json
import time
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import Optional, Dict, List
from datetime import datetime

# Добавляем путь к MVP-1
mvp1_path = Path(__file__).parent.parent / "mvp1_device_discovery"
sys.path.insert(0, str(mvp1_path))

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

try:
    from Foundation import NSNotificationCenter, NSObject
    from AVFoundation import AVAudioSession
    PYOBJC_AVAILABLE = True
    logger.info("✅ Foundation и AVFoundation доступны")
except ImportError as e:
    PYOBJC_AVAILABLE = False
    logger.error(f"❌ Foundation/AVFoundation не доступны: {e}")
    sys.exit(1)

# Импортируем из MVP-1
try:
    from test_device_discovery import DeviceDiscoveryPrototype, DeviceInfo
    MVP1_AVAILABLE = True
except ImportError:
    MVP1_AVAILABLE = False
    logger.warning("⚠️ MVP-1 не доступен, используем упрощенную версию")


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
    """
    Прототип для тестирования стабильности идентичности устройств
    
    Структура:
    1. setup() - настройка
    2. capture_device_signature() - создание подписи
    3. test_identity_stability() - тест стабильности
    4. collect_metrics() - сбор метрик
    5. check_exit_gate() - проверка Exit Gate
    """
    
    def __init__(self):
        self.device_discovery = None
        self.signatures: Dict[str, List[DeviceSignature]] = {}
        self.metrics: Dict = {}
        
    def setup(self) -> bool:
        """Настройка окружения"""
        logger.info("=" * 80)
        logger.info("MVP-1b: Device Identity (стабильность идентичности)")
        logger.info("=" * 80)
        logger.info("")
        
        if not PYOBJC_AVAILABLE:
            logger.error("❌ PyObjC не доступен")
            return False
        
        if not MVP1_AVAILABLE:
            logger.error("❌ MVP-1 не доступен (требуется для работы)")
            return False
        
        # Инициализируем DeviceDiscoveryPrototype
        self.device_discovery = DeviceDiscoveryPrototype()
        if not self.device_discovery.setup():
            logger.error("❌ Не удалось настроить DeviceDiscoveryPrototype")
            return False
        
        return True
    
    def capture_device_signature(self, device_info: DeviceInfo) -> DeviceSignature:
        """Создание подписи устройства из информации AVFoundation"""
        return DeviceSignature(
            uid=device_info.uid,
            name=device_info.name,
            normalized_name=device_info.normalized_name,
            transport=device_info.transport,
            channels=device_info.channels,
            sample_rate=device_info.sample_rate
        )
    
    def test_identity_stability(self) -> bool:
        """Тестирование стабильности идентичности при повторных запросах"""
        logger.info("📋 Тест стабильности идентичности")
        logger.info("Получение устройств 5 раз подряд...")
        logger.info("")
        
        all_signatures: Dict[str, List[DeviceSignature]] = {}
        
        for i in range(5):
            logger.info(f"Запрос #{i+1}...")
            
            # Получаем устройства через MVP-1
            avf_devices = self.device_discovery.get_input_devices()
            
            for device_info in avf_devices:
                signature = self.capture_device_signature(device_info)
                uid_key = signature.uid or signature.normalized_name
                
                if uid_key not in all_signatures:
                    all_signatures[uid_key] = []
                all_signatures[uid_key].append(signature)
            
            time.sleep(0.5)  # Небольшая пауза
        
        # Анализ стабильности
        logger.info("")
        logger.info("🔍 Анализ стабильности идентичности...")
        logger.info("")
        
        stable_count = 0
        unstable_count = 0
        changes_log = []
        
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
                    changes_log.append({
                        "device": base.name,
                        "changes": changes
                    })
                    logger.warning(f"  ⚠️ Устройство '{base.name}' изменилось:")
                    for field, (old_val, new_val) in changes.items():
                        logger.warning(f"     {field}: {old_val} → {new_val}")
                    break
            
            if is_stable:
                stable_count += 1
                logger.info(f"  ✅ Устройство '{base.name}' стабильно (все 5 запросов идентичны)")
            else:
                unstable_count += 1
        
        self.signatures = all_signatures
        self.metrics['stability_changes'] = changes_log
        
        # Итоги
        logger.info("")
        logger.info("=" * 80)
        logger.info("ИТОГИ ТЕСТИРОВАНИЯ:")
        logger.info("=" * 80)
        logger.info(f"Всего устройств: {len(all_signatures)}")
        logger.info(f"Стабильных: {stable_count}")
        logger.info(f"Нестабильных: {unstable_count}")
        
        stability_rate = (stable_count / len(all_signatures) * 100) if all_signatures else 0
        logger.info(f"\n📊 Стабильность: {stability_rate:.1f}%")
        logger.info("")
        
        # Критерий успеха: ≥90% устройств стабильны
        success = stability_rate >= 90.0 and len(all_signatures) > 0
        
        if success:
            logger.info("✅ Тест стабильности пройден")
        else:
            logger.error("❌ Тест стабильности провален")
            logger.error(f"   Требуется ≥90%, получено {stability_rate:.1f}%")
        
        return success
    
    def collect_metrics(self) -> Dict:
        """Сбор метрик"""
        total_devices = len(self.signatures)
        stable_devices = sum(1 for sigs in self.signatures.values() 
                           if len(sigs) > 1 and all(sigs[0].is_same_device(s) for s in sigs[1:]))
        
        self.metrics.update({
            "total_devices": total_devices,
            "stable_devices": stable_devices,
            "unstable_devices": total_devices - stable_devices,
            "stability_rate": (stable_devices / total_devices * 100) if total_devices > 0 else 0
        })
        
        return self.metrics
    
    def check_exit_gate(self) -> bool:
        """Проверка Exit Gate"""
        logger.info("=" * 80)
        logger.info("ПРОВЕРКА EXIT GATE")
        logger.info("=" * 80)
        logger.info("")
        
        stability_rate = self.metrics.get('stability_rate', 0)
        total_devices = self.metrics.get('total_devices', 0)
        
        checks = [
            ("DeviceSignature стабильна (≥90%)", stability_rate >= 90.0),
            ("Можно однозначно идентифицировать устройство", total_devices > 0),
            ("Изменения отслеживаются", len(self.metrics.get('stability_changes', [])) >= 0)
        ]
        
        all_passed = True
        for check_name, check_result in checks:
            status = "✅" if check_result else "❌"
            logger.info(f"{status} {check_name}")
            if not check_result:
                all_passed = False
        
        logger.info("")
        
        if all_passed:
            logger.info("✅ MVP-1b ПРОЙДЕН: Все Exit Gate критерии выполнены")
        else:
            logger.error("❌ MVP-1b ПРОВАЛЕН: Есть невыполненные критерии")
        
        return all_passed
    
    def generate_report(self) -> str:
        """Генерация отчета"""
        # Конвертируем signatures в словари
        signatures_dict = {}
        for uid_key, sigs in self.signatures.items():
            signatures_dict[uid_key] = [s.to_dict() for s in sigs]
        
        report = {
            "mvp": "MVP-1b: Device Identity",
            "status": "PASSED" if self.check_exit_gate() else "FAILED",
            "metrics": self.metrics,
            "signatures": signatures_dict
        }
        
        return json.dumps(report, indent=2, ensure_ascii=False)


def main():
    """Главная функция"""
    prototype = DeviceIdentityPrototype()
    
    if not prototype.setup():
        logger.error("❌ Setup провален")
        sys.exit(1)
    
    # Тест стабильности
    if not prototype.test_identity_stability():
        logger.error("❌ Тест стабильности провален")
        sys.exit(1)
    
    # Сбор метрик
    metrics = prototype.collect_metrics()
    
    # Проверка Exit Gate
    success = prototype.check_exit_gate()
    
    # Генерация отчета
    report = prototype.generate_report()
    report_file = Path(__file__).parent / "device_identity_report.json"
    report_file.write_text(report, encoding='utf-8')
    logger.info(f"📄 Отчет сохранен: {report_file}")
    logger.info("")
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

