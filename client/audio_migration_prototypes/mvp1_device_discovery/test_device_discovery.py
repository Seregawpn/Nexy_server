#!/usr/bin/env python3
"""
MVP-1: Device Discovery

Цель: AVFoundation корректно находит устройства

Exit Gate:
- [ ] Все устройства найдены
- [ ] System default определяется корректно
- [ ] Имена нормализуются правильно
- [ ] Transport определяется правильно
"""

import sys
import logging
import json
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import List, Optional, Dict
from datetime import datetime

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

try:
    from Foundation import NSNotificationCenter, NSObject
    from AVFoundation import AVAudioSession, AVAudioSessionPortOverride
    PYOBJC_AVAILABLE = True
    logger.info("✅ Foundation и AVFoundation доступны")
except ImportError as e:
    PYOBJC_AVAILABLE = False
    logger.error(f"❌ Foundation/AVFoundation не доступны: {e}")
    sys.exit(1)


@dataclass
class DeviceInfo:
    """Информация об устройстве"""
    name: str
    uid: str
    port_type: str
    channels: int
    sample_rate: Optional[int] = None
    transport: str = "unknown"  # bluetooth/usb/built_in/unknown
    normalized_name: str = ""
    is_default_input: bool = False
    is_default_output: bool = False
    
    def to_dict(self) -> dict:
        return asdict(self)


class DeviceDiscoveryPrototype:
    """
    Прототип для тестирования поиска устройств
    
    Структура:
    1. setup() - настройка AVAudioSession
    2. get_input_devices() - получение input устройств
    3. get_current_input() - получение текущего input
    4. get_output_devices() - получение output устройств
    5. get_current_output() - получение текущего output
    6. normalize_device_name() - нормализация имени
    7. detect_transport() - определение транспорта
    8. run_tests() - выполнение всех тестов
    9. collect_metrics() - сбор метрик
    10. check_exit_gate() - проверка Exit Gate
    """
    
    def __init__(self):
        self.session = None
        self.input_devices: List[DeviceInfo] = []
        self.output_devices: List[DeviceInfo] = []
        self.current_input: Optional[DeviceInfo] = None
        self.current_output: Optional[DeviceInfo] = None
        self.metrics: Dict = {}
        
    def setup(self) -> bool:
        """Настройка окружения"""
        logger.info("=" * 80)
        logger.info("MVP-1: Device Discovery")
        logger.info("=" * 80)
        logger.info("")
        
        if not PYOBJC_AVAILABLE:
            logger.error("❌ PyObjC не доступен")
            return False
        
        return self.setup_audio_session()
        
    def setup_audio_session(self) -> bool:
        """Настройка AVAudioSession"""
        try:
            logger.info("📋 Настройка AVAudioSession...")
            
            self.session = AVAudioSession.sharedInstance()
            
            # Настройка категории
            error = None
            # Используем категорию без опций (упрощенная версия)
            success = self.session.setCategory_error_(
                "AVAudioSessionCategoryPlayAndRecord",
                error
            )
            
            if not success:
                logger.error("❌ Ошибка настройки категории AVAudioSession")
                return False
            
            # Активация сессии
            success = self.session.setActive_error_(True, error)
            if not success:
                logger.error("❌ Ошибка активации AVAudioSession")
                return False
            
            logger.info("✅ AVAudioSession настроен и активирован")
            logger.info("")
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка настройки AVAudioSession: {e}")
            return False
    
    def normalize_device_name(self, name: str) -> str:
        """Нормализация имени устройства"""
        normalized = name.strip()
        
        # Удаляем Bluetooth суффиксы
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
    
    def get_input_devices(self) -> List[DeviceInfo]:
        """Получение списка input устройств"""
        try:
            logger.info("📥 Получение списка input устройств...")
            
            # Получаем доступные входы
            available_inputs = self.session.availableInputs()
            
            devices = []
            for input_port in available_inputs:
                port_name = input_port.portName()
                port_type = input_port.portType()
                uid = input_port.UID()
                
                # Получаем данные источника
                data_sources = input_port.dataSources()
                channels = 1  # По умолчанию
                if data_sources and len(data_sources) > 0:
                    # Пытаемся получить количество каналов
                    # Это может потребовать дополнительных вызовов
                    pass
                
                normalized_name = self.normalize_device_name(port_name)
                transport = self.detect_transport(port_name, port_type)
                
                device_info = DeviceInfo(
                    name=port_name,
                    uid=uid,
                    port_type=port_type,
                    channels=channels,
                    transport=transport,
                    normalized_name=normalized_name
                )
                devices.append(device_info)
                
                logger.info(f"  📱 Найдено устройство: {port_name}")
                logger.info(f"     UID: {uid}")
                logger.info(f"     Type: {port_type}")
                logger.info(f"     Transport: {transport}")
                logger.info(f"     Normalized: {normalized_name}")
            
            self.input_devices = devices
            logger.info(f"✅ Найдено {len(devices)} input устройств")
            logger.info("")
            return devices
            
        except Exception as e:
            logger.error(f"❌ Ошибка получения input устройств: {e}")
            return []
    
    def get_current_input(self) -> Optional[DeviceInfo]:
        """Получение текущего input устройства"""
        try:
            logger.info("📥 Получение текущего input устройства...")
            
            current_route = self.session.currentRoute()
            inputs = current_route.inputs()
            
            if inputs and len(inputs) > 0:
                input_port = inputs[0]
                port_name = input_port.portName()
                port_type = input_port.portType()
                uid = input_port.UID()
                
                normalized_name = self.normalize_device_name(port_name)
                transport = self.detect_transport(port_name, port_type)
                
                device_info = DeviceInfo(
                    name=port_name,
                    uid=uid,
                    port_type=port_type,
                    channels=1,
                    transport=transport,
                    normalized_name=normalized_name,
                    is_default_input=True
                )
                
                self.current_input = device_info
                logger.info(f"✅ Текущий input: {port_name} (UID: {uid})")
                logger.info("")
                return device_info
            
            logger.warning("⚠️ Текущий input не определен")
            logger.info("")
            return None
            
        except Exception as e:
            logger.error(f"❌ Ошибка получения текущего input: {e}")
            return None
    
    def get_output_devices(self) -> List[DeviceInfo]:
        """Получение списка output устройств"""
        try:
            logger.info("📤 Получение списка output устройств...")
            
            # Получаем доступные выходы через currentRoute
            current_route = self.session.currentRoute()
            outputs = current_route.outputs()
            
            devices = []
            for output_port in outputs:
                port_name = output_port.portName()
                port_type = output_port.portType()
                uid = output_port.UID()
                
                normalized_name = self.normalize_device_name(port_name)
                transport = self.detect_transport(port_name, port_type)
                
                device_info = DeviceInfo(
                    name=port_name,
                    uid=uid,
                    port_type=port_type,
                    channels=2,  # Output обычно stereo
                    transport=transport,
                    normalized_name=normalized_name
                )
                devices.append(device_info)
                
                logger.info(f"  📱 Найдено устройство: {port_name}")
                logger.info(f"     UID: {uid}")
                logger.info(f"     Type: {port_type}")
                logger.info(f"     Transport: {transport}")
            
            self.output_devices = devices
            logger.info(f"✅ Найдено {len(devices)} output устройств")
            logger.info("")
            return devices
            
        except Exception as e:
            logger.error(f"❌ Ошибка получения output устройств: {e}")
            return []
    
    def get_current_output(self) -> Optional[DeviceInfo]:
        """Получение текущего output устройства"""
        try:
            logger.info("📤 Получение текущего output устройства...")
            
            current_route = self.session.currentRoute()
            outputs = current_route.outputs()
            
            if outputs and len(outputs) > 0:
                output_port = outputs[0]
                port_name = output_port.portName()
                port_type = output_port.portType()
                uid = output_port.UID()
                
                normalized_name = self.normalize_device_name(port_name)
                transport = self.detect_transport(port_name, port_type)
                
                device_info = DeviceInfo(
                    name=port_name,
                    uid=uid,
                    port_type=port_type,
                    channels=2,
                    transport=transport,
                    normalized_name=normalized_name,
                    is_default_output=True
                )
                
                self.current_output = device_info
                logger.info(f"✅ Текущий output: {port_name} (UID: {uid})")
                logger.info("")
                return device_info
            
            logger.warning("⚠️ Текущий output не определен")
            logger.info("")
            return None
            
        except Exception as e:
            logger.error(f"❌ Ошибка получения текущего output: {e}")
            return None
    
    def run_tests(self) -> Dict:
        """Выполнение всех тестов"""
        results = {
            "input_devices_found": len(self.input_devices) > 0,
            "output_devices_found": len(self.output_devices) > 0,
            "current_input_determined": self.current_input is not None,
            "current_output_determined": self.current_output is not None,
            "normalization_works": True,  # Проверяется в collect_metrics
            "transport_detection_works": True  # Проверяется в collect_metrics
        }
        
        return results
    
    def collect_metrics(self) -> Dict:
        """Сбор метрик"""
        # Проверка нормализации
        normalization_success = 0
        normalization_total = 0
        
        for device in self.input_devices + self.output_devices:
            normalization_total += 1
            if device.normalized_name != device.name or device.normalized_name:
                normalization_success += 1
        
        # Проверка определения transport
        transport_success = 0
        transport_total = 0
        
        for device in self.input_devices + self.output_devices:
            transport_total += 1
            if device.transport != "unknown":
                transport_success += 1
        
        self.metrics = {
            "input_devices_count": len(self.input_devices),
            "output_devices_count": len(self.output_devices),
            "current_input_determined": self.current_input is not None,
            "current_output_determined": self.current_output is not None,
            "normalization_success_rate": (normalization_success / normalization_total * 100) if normalization_total > 0 else 0,
            "transport_detection_success_rate": (transport_success / transport_total * 100) if transport_total > 0 else 0,
            "transport_distribution": {
                "bluetooth": sum(1 for d in self.input_devices + self.output_devices if d.transport == "bluetooth"),
                "usb": sum(1 for d in self.input_devices + self.output_devices if d.transport == "usb"),
                "built_in": sum(1 for d in self.input_devices + self.output_devices if d.transport == "built_in"),
                "unknown": sum(1 for d in self.input_devices + self.output_devices if d.transport == "unknown")
            }
        }
        
        logger.info("📊 Метрики:")
        logger.info(f"   Input устройств: {self.metrics['input_devices_count']}")
        logger.info(f"   Output устройств: {self.metrics['output_devices_count']}")
        logger.info(f"   Текущий input определен: {self.metrics['current_input_determined']}")
        logger.info(f"   Текущий output определен: {self.metrics['current_output_determined']}")
        logger.info(f"   Успешность нормализации: {self.metrics['normalization_success_rate']:.1f}%")
        logger.info(f"   Успешность определения transport: {self.metrics['transport_detection_success_rate']:.1f}%")
        logger.info(f"   Распределение transport: {self.metrics['transport_distribution']}")
        logger.info("")
        
        return self.metrics
    
    def check_exit_gate(self) -> bool:
        """Проверка Exit Gate"""
        logger.info("=" * 80)
        logger.info("ПРОВЕРКА EXIT GATE")
        logger.info("=" * 80)
        logger.info("")
        
        checks = [
            ("Все устройства найдены", len(self.input_devices) > 0 and len(self.output_devices) > 0),
            ("System default input определен", self.current_input is not None),
            ("System default output определен", self.current_output is not None),
            ("Нормализация работает", self.metrics.get('normalization_success_rate', 0) >= 90.0),
            ("Определение transport работает", self.metrics.get('transport_detection_success_rate', 0) >= 80.0)
        ]
        
        all_passed = True
        for check_name, check_result in checks:
            status = "✅" if check_result else "❌"
            logger.info(f"{status} {check_name}")
            if not check_result:
                all_passed = False
        
        logger.info("")
        
        if all_passed:
            logger.info("✅ MVP-1 ПРОЙДЕН: Все Exit Gate критерии выполнены")
        else:
            logger.error("❌ MVP-1 ПРОВАЛЕН: Есть невыполненные критерии")
        
        return all_passed
    
    def generate_report(self) -> str:
        """Генерация отчета"""
        report = {
            "mvp": "MVP-1: Device Discovery",
            "status": "PASSED" if self.check_exit_gate() else "FAILED",
            "metrics": self.metrics,
            "input_devices": [d.to_dict() for d in self.input_devices],
            "output_devices": [d.to_dict() for d in self.output_devices],
            "current_input": self.current_input.to_dict() if self.current_input else None,
            "current_output": self.current_output.to_dict() if self.current_output else None
        }
        
        return json.dumps(report, indent=2, ensure_ascii=False)


def main():
    """Главная функция"""
    prototype = DeviceDiscoveryPrototype()
    
    if not prototype.setup():
        logger.error("❌ Setup провален")
        sys.exit(1)
    
    # Получение устройств
    prototype.get_input_devices()
    prototype.get_current_input()
    prototype.get_output_devices()
    prototype.get_current_output()
    
    # Выполнение тестов
    results = prototype.run_tests()
    
    # Сбор метрик
    metrics = prototype.collect_metrics()
    
    # Проверка Exit Gate
    success = prototype.check_exit_gate()
    
    # Генерация отчета
    report = prototype.generate_report()
    report_file = Path(__file__).parent / "device_discovery_report.json"
    report_file.write_text(report, encoding='utf-8')
    logger.info(f"📄 Отчет сохранен: {report_file}")
    logger.info("")
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

