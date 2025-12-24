#!/usr/bin/env python3
"""
MVP-2: Device Mapping

Цель: Маппинг AVFoundation → PortAudio с ≥80% success, FP ≈ 0

Exit Gate:
- [ ] ≥80% success rate
- [ ] FP ≈ 0
- [ ] Fallback работает
"""

import sys
import logging
import json
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import Optional, Dict, List
from datetime import datetime

# Добавляем пути к предыдущим MVP
mvp1_path = Path(__file__).parent.parent / "mvp1_device_discovery"
mvp1b_path = Path(__file__).parent.parent / "mvp1b_device_identity"
sys.path.insert(0, str(mvp1_path))
sys.path.insert(0, str(mvp1b_path))

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

try:
    import sounddevice as sd
    SOUNDDEVICE_AVAILABLE = True
    logger.info("✅ sounddevice доступен")
except ImportError:
    SOUNDDEVICE_AVAILABLE = False
    logger.error("❌ sounddevice не доступен")
    sys.exit(1)

# Импортируем из предыдущих MVP
try:
    from test_device_discovery import DeviceDiscoveryPrototype, DeviceInfo
    from test_device_identity import DeviceSignature
    MVP1_AVAILABLE = True
    MVP1B_AVAILABLE = True
except ImportError as e:
    MVP1_AVAILABLE = False
    MVP1B_AVAILABLE = False
    logger.warning(f"⚠️ Предыдущие MVP не доступны: {e}")


@dataclass
class MappingResult:
    """Результат маппинга устройства"""
    device_index: Optional[int]
    confidence: str  # HIGH/MEDIUM/LOW/NONE
    reason: str
    score: float
    avf_device_name: str
    portaudio_device_name: Optional[str] = None
    
    def to_dict(self) -> dict:
        return asdict(self)
    
    def is_usable(self) -> bool:
        """Проверка, можно ли использовать маппинг"""
        return self.confidence in ("HIGH", "MEDIUM") and self.device_index is not None


class DeviceMappingPrototype:
    """
    Прототип для тестирования маппинга устройств
    
    Структура:
    1. setup() - настройка
    2. normalize_device_name() - нормализация имени
    3. find_portaudio_match() - поиск совпадения
    4. test_mapping_for_all_devices() - тест для всех устройств
    5. collect_metrics() - сбор метрик
    6. check_exit_gate() - проверка Exit Gate
    """
    
    def __init__(self):
        self.device_discovery = None
        self.mapping_results: List[MappingResult] = []
        self.metrics: Dict = {}
        self.cache: Dict[str, MappingResult] = {}
        
    def setup(self) -> bool:
        """Настройка окружения"""
        logger.info("=" * 80)
        logger.info("MVP-2: Device Mapping")
        logger.info("=" * 80)
        logger.info("")
        
        if not SOUNDDEVICE_AVAILABLE:
            logger.error("❌ sounddevice не доступен")
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
    
    def normalize_device_name(self, name: str) -> str:
        """Нормализация имени устройства"""
        normalized = name.strip()
        
        suffixes = [" (Hands-Free)", " HFP", " Hands-Free", " Bluetooth"]
        for suffix in suffixes:
            if normalized.endswith(suffix):
                normalized = normalized[:-len(suffix)]
                break
        
        return normalized
    
    def find_portaudio_match(self, avf_name: str, avf_channels: int = 1, avf_transport: str = "unknown") -> MappingResult:
        """
        Поиск совпадения в PortAudio
        
        Returns:
            MappingResult с device_index, confidence, reason, score
        """
        try:
            all_devices = sd.query_devices()
            normalized_avf = self.normalize_device_name(avf_name)
            
            # Проверяем кэш
            cache_key = f"{normalized_avf}_{avf_channels}_{avf_transport}"
            if cache_key in self.cache:
                cached_result = self.cache[cache_key]
                logger.info(f"  💾 Использован кэш для '{avf_name}'")
                return cached_result
            
            candidates = []
            
            for idx, device in enumerate(all_devices):
                if device.get('max_input_channels', 0) == 0:
                    continue
                
                device_name = device.get('name', '')
                device_channels = device.get('max_input_channels', 0)
                
                score = 0.0
                
                # Exact name match
                if device_name == normalized_avf:
                    score += 10.0
                elif normalized_avf.lower() in device_name.lower():
                    score += 5.0
                elif device_name.lower() in normalized_avf.lower():
                    score += 3.0
                
                # Channels match
                if device_channels == avf_channels:
                    score += 5.0
                elif abs(device_channels - avf_channels) <= 1:
                    score += 2.0
                
                # Transport hints (если доступны)
                device_name_lower = device_name.lower()
                if avf_transport == "bluetooth" and ("bluetooth" in device_name_lower or "airpods" in device_name_lower):
                    score += 2.0
                elif avf_transport == "usb" and "usb" in device_name_lower:
                    score += 2.0
                elif avf_transport == "built_in" and ("built-in" in device_name_lower or "builtin" in device_name_lower or "internal" in device_name_lower):
                    score += 2.0
                
                if score > 0:
                    candidates.append({
                        "index": idx,
                        "name": device_name,
                        "channels": device_channels,
                        "score": score
                    })
            
            if not candidates:
                result = MappingResult(
                    device_index=None,
                    confidence="NONE",
                    reason="No matching devices found",
                    score=0.0,
                    avf_device_name=avf_name
                )
                self.cache[cache_key] = result
                return result
            
            # Сортируем по score
            candidates.sort(key=lambda x: x['score'], reverse=True)
            best = candidates[0]
            
            # Определяем confidence
            if best['score'] >= 15.0 and len(candidates) == 1:
                confidence = "HIGH"
            elif best['score'] >= 10.0:
                confidence = "MEDIUM"
            elif best['score'] >= 5.0:
                confidence = "LOW"
            else:
                confidence = "NONE"
            
            # Если есть несколько кандидатов с близким score - снижаем confidence
            if len(candidates) > 1 and candidates[1]['score'] >= best['score'] * 0.8:
                if confidence == "HIGH":
                    confidence = "MEDIUM"
                elif confidence == "MEDIUM":
                    confidence = "LOW"
            
            result = MappingResult(
                device_index=best['index'],
                confidence=confidence,
                reason=f"Matched '{best['name']}' with score {best['score']:.1f}",
                score=best['score'],
                avf_device_name=avf_name,
                portaudio_device_name=best['name']
            )
            
            # Кэшируем только успешные маппинги (HIGH/MEDIUM)
            if confidence in ("HIGH", "MEDIUM"):
                self.cache[cache_key] = result
            
            return result
            
        except Exception as e:
            logger.error(f"❌ Ошибка поиска в PortAudio: {e}")
            return MappingResult(
                device_index=None,
                confidence="NONE",
                reason=f"Error: {e}",
                score=0.0,
                avf_device_name=avf_name
            )
    
    def test_mapping_for_all_devices(self) -> bool:
        """Тестирование маппинга для всех найденных устройств"""
        logger.info("📋 Тестирование маппинга для всех устройств...")
        logger.info("")
        
        # Получаем устройства от AVFoundation
        avf_devices = self.device_discovery.get_input_devices()
        
        if not avf_devices:
            logger.error("❌ Нет устройств для тестирования")
            return False
        
        logger.info(f"🔍 Тестирование маппинга для {len(avf_devices)} устройств...\n")
        
        results = []
        success_count = 0
        false_positive_count = 0
        
        for device in avf_devices:
            name = device.name
            channels = device.channels
            transport = device.transport
            
            logger.info(f"📱 Устройство: {name} ({channels} channels, {transport})")
            
            result = self.find_portaudio_match(name, channels, transport)
            results.append(result)
            self.mapping_results.append(result)
            
            if result.confidence in ("HIGH", "MEDIUM"):
                success_count += 1
                logger.info(f"  ✅ Маппинг успешен: index={result.device_index}, confidence={result.confidence}")
                logger.info(f"     PortAudio: {result.portaudio_device_name}")
                logger.info(f"     Причина: {result.reason}")
                
                # Проверка на false positive (упрощенная)
                # В реальности нужна более сложная проверка
                if result.portaudio_device_name and result.portaudio_device_name.lower() != self.normalize_device_name(name).lower():
                    if not (self.normalize_device_name(name).lower() in result.portaudio_device_name.lower() or 
                            result.portaudio_device_name.lower() in self.normalize_device_name(name).lower()):
                        false_positive_count += 1
                        logger.warning(f"  ⚠️ Возможный false positive: имена не совпадают")
            elif result.confidence == "LOW":
                logger.warning(f"  ⚠️ Маппинг с низкой уверенностью: index={result.device_index}, confidence={result.confidence}")
                logger.warning(f"     Причина: {result.reason}")
            else:
                logger.error(f"  ❌ Маппинг не найден: {result.reason}")
            
            logger.info("")
        
        # Итоги
        logger.info("=" * 80)
        logger.info("ИТОГИ ТЕСТИРОВАНИЯ:")
        logger.info("=" * 80)
        logger.info(f"Всего устройств: {len(avf_devices)}")
        logger.info(f"Успешных маппингов (HIGH/MEDIUM): {success_count}")
        logger.info(f"Низкая уверенность (LOW): {sum(1 for r in results if r.confidence == 'LOW')}")
        logger.info(f"Не найдено (NONE): {sum(1 for r in results if r.confidence == 'NONE')}")
        logger.info(f"Возможные false positives: {false_positive_count}")
        logger.info("")
        
        success_rate = (success_count / len(avf_devices)) * 100
        fp_rate = (false_positive_count / success_count * 100) if success_count > 0 else 0
        
        logger.info(f"📊 Успешность маппинга: {success_rate:.1f}%")
        logger.info(f"📊 False positive rate: {fp_rate:.1f}%")
        logger.info("")
        
        # Критерий успеха: ≥80% success, FP ≈ 0
        success = success_rate >= 80.0 and fp_rate < 5.0
        
        if success:
            logger.info("✅ Тест маппинга пройден")
        else:
            logger.error("❌ Тест маппинга провален")
            if success_rate < 80.0:
                logger.error(f"   Требуется ≥80% success, получено {success_rate:.1f}%")
            if fp_rate >= 5.0:
                logger.error(f"   Требуется FP < 5%, получено {fp_rate:.1f}%")
        
        return success
    
    def test_fallback(self) -> bool:
        """Тестирование fallback на system default"""
        logger.info("📋 Тест fallback на system default...")
        logger.info("")
        
        # Находим устройство с LOW/NONE confidence
        low_confidence_results = [r for r in self.mapping_results if r.confidence in ("LOW", "NONE")]
        
        if not low_confidence_results:
            logger.info("  ℹ️ Нет устройств с LOW/NONE confidence для тестирования fallback")
            return True
        
        logger.info(f"  Найдено {len(low_confidence_results)} устройств с LOW/NONE confidence")
        
        # Проверяем, что fallback работает (device_index = None означает system default)
        fallback_works = all(r.device_index is None for r in low_confidence_results)
        
        if fallback_works:
            logger.info("  ✅ Fallback работает: device_index = None для LOW/NONE confidence")
        else:
            logger.error("  ❌ Fallback не работает: есть device_index для LOW/NONE confidence")
        
        logger.info("")
        return fallback_works
    
    def collect_metrics(self) -> Dict:
        """Сбор метрик"""
        total = len(self.mapping_results)
        high_confidence = sum(1 for r in self.mapping_results if r.confidence == "HIGH")
        medium_confidence = sum(1 for r in self.mapping_results if r.confidence == "MEDIUM")
        low_confidence = sum(1 for r in self.mapping_results if r.confidence == "LOW")
        none_confidence = sum(1 for r in self.mapping_results if r.confidence == "NONE")
        
        success_count = high_confidence + medium_confidence
        success_rate = (success_count / total * 100) if total > 0 else 0
        
        self.metrics = {
            "total_devices": total,
            "high_confidence": high_confidence,
            "medium_confidence": medium_confidence,
            "low_confidence": low_confidence,
            "none_confidence": none_confidence,
            "success_count": success_count,
            "success_rate": success_rate,
            "cache_size": len(self.cache)
        }
        
        logger.info("📊 Метрики:")
        logger.info(f"   Всего устройств: {self.metrics['total_devices']}")
        logger.info(f"   HIGH confidence: {self.metrics['high_confidence']}")
        logger.info(f"   MEDIUM confidence: {self.metrics['medium_confidence']}")
        logger.info(f"   LOW confidence: {self.metrics['low_confidence']}")
        logger.info(f"   NONE confidence: {self.metrics['none_confidence']}")
        logger.info(f"   Success rate: {self.metrics['success_rate']:.1f}%")
        logger.info(f"   Cache size: {self.metrics['cache_size']}")
        logger.info("")
        
        return self.metrics
    
    def check_exit_gate(self) -> bool:
        """Проверка Exit Gate"""
        logger.info("=" * 80)
        logger.info("ПРОВЕРКА EXIT GATE")
        logger.info("=" * 80)
        logger.info("")
        
        success_rate = self.metrics.get('success_rate', 0)
        total = self.metrics.get('total_devices', 0)
        
        checks = [
            ("≥80% success rate", success_rate >= 80.0),
            ("FP ≈ 0", True),  # Проверяется в тестах
            ("Fallback работает", self.test_fallback())
        ]
        
        all_passed = True
        for check_name, check_result in checks:
            status = "✅" if check_result else "❌"
            logger.info(f"{status} {check_name}")
            if not check_result:
                all_passed = False
        
        logger.info("")
        
        if all_passed:
            logger.info("✅ MVP-2 ПРОЙДЕН: Все Exit Gate критерии выполнены")
        else:
            logger.error("❌ MVP-2 ПРОВАЛЕН: Есть невыполненные критерии")
        
        return all_passed
    
    def generate_report(self) -> str:
        """Генерация отчета"""
        report = {
            "mvp": "MVP-2: Device Mapping",
            "status": "PASSED" if self.check_exit_gate() else "FAILED",
            "metrics": self.metrics,
            "mapping_results": [r.to_dict() for r in self.mapping_results]
        }
        
        return json.dumps(report, indent=2, ensure_ascii=False)


def main():
    """Главная функция"""
    prototype = DeviceMappingPrototype()
    
    if not prototype.setup():
        logger.error("❌ Setup провален")
        sys.exit(1)
    
    # Тест маппинга
    if not prototype.test_mapping_for_all_devices():
        logger.error("❌ Тест маппинга провален")
        sys.exit(1)
    
    # Сбор метрик
    metrics = prototype.collect_metrics()
    
    # Проверка Exit Gate
    success = prototype.check_exit_gate()
    
    # Генерация отчета
    report = prototype.generate_report()
    report_file = Path(__file__).parent / "device_mapping_report.json"
    report_file.write_text(report, encoding='utf-8')
    logger.info(f"📄 Отчет сохранен: {report_file}")
    logger.info("")
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

