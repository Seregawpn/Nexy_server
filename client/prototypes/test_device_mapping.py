#!/usr/bin/env python3
"""
Прототип 2: Маппинг AVFoundation → PortAudio

Цель: Проверить, что мы можем найти PortAudio device_index для AVFoundation устройства
"""

import sys
import logging
from pathlib import Path

# Добавляем путь к проекту
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

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

# Импортируем функции из прототипа 1
try:
    from test_device_discovery import DeviceDiscoveryPrototype
    PROTOTYPE1_AVAILABLE = True
except ImportError:
    PROTOTYPE1_AVAILABLE = False
    logger.warning("⚠️ Прототип 1 не доступен, используем упрощенную версию")


class DeviceMappingPrototype:
    """Прототип для тестирования маппинга устройств"""
    
    def __init__(self):
        self.device_discovery = DeviceDiscoveryPrototype() if PROTOTYPE1_AVAILABLE else None
    
    def normalize_device_name(self, name: str) -> str:
        """Нормализация имени устройства"""
        normalized = name.strip()
        
        suffixes = [" (Hands-Free)", " HFP", " Hands-Free", " Bluetooth"]
        for suffix in suffixes:
            if normalized.endswith(suffix):
                normalized = normalized[:-len(suffix)]
                break
        
        return normalized
    
    def find_portaudio_match(self, avf_name: str, avf_channels: int = 1) -> dict:
        """
        Поиск совпадения в PortAudio
        
        Returns:
            {
                "device_index": int or None,
                "confidence": "HIGH" | "MEDIUM" | "LOW" | "NONE",
                "reason": str,
                "score": float
            }
        """
        try:
            all_devices = sd.query_devices()
            normalized_avf = self.normalize_device_name(avf_name)
            
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
                
                # Channels match
                if device_channels == avf_channels:
                    score += 5.0
                elif abs(device_channels - avf_channels) <= 1:
                    score += 2.0
                
                if score > 0:
                    candidates.append({
                        "index": idx,
                        "name": device_name,
                        "channels": device_channels,
                        "score": score
                    })
            
            if not candidates:
                return {
                    "device_index": None,
                    "confidence": "NONE",
                    "reason": "No matching devices found",
                    "score": 0.0
                }
            
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
            
            return {
                "device_index": best['index'],
                "confidence": confidence,
                "reason": f"Matched '{best['name']}' with score {best['score']:.1f}",
                "score": best['score']
            }
            
        except Exception as e:
            logger.error(f"❌ Ошибка поиска в PortAudio: {e}")
            return {
                "device_index": None,
                "confidence": "NONE",
                "reason": f"Error: {e}",
                "score": 0.0
            }
    
    def test_mapping_for_all_devices(self):
        """Тестирование маппинга для всех найденных устройств"""
        logger.info("=" * 80)
        logger.info("ПРОТОТИП 2: Маппинг AVFoundation → PortAudio")
        logger.info("=" * 80)
        
        # Получаем устройства от AVFoundation
        if self.device_discovery:
            if not self.device_discovery.setup_audio_session():
                logger.error("❌ Не удалось настроить AVAudioSession")
                return False
            
            avf_devices = self.device_discovery.get_input_devices()
        else:
            # Упрощенная версия - используем системное устройство
            logger.warning("⚠️ Используем упрощенную версию (без AVFoundation)")
            avf_devices = [{"name": "Built-in Microphone", "channels": 1}]
        
        if not avf_devices:
            logger.error("❌ Нет устройств для тестирования")
            return False
        
        logger.info(f"\n🔍 Тестирование маппинга для {len(avf_devices)} устройств...\n")
        
        results = []
        success_count = 0
        
        for device in avf_devices:
            name = device['name']
            channels = device.get('channels', 1)
            
            logger.info(f"📱 Устройство: {name} ({channels} channels)")
            
            result = self.find_portaudio_match(name, channels)
            results.append({
                "avf_name": name,
                "mapping": result
            })
            
            if result['confidence'] in ("HIGH", "MEDIUM"):
                success_count += 1
                logger.info(f"  ✅ Маппинг успешен: index={result['device_index']}, confidence={result['confidence']}")
                logger.info(f"     Причина: {result['reason']}")
            elif result['confidence'] == "LOW":
                logger.warning(f"  ⚠️ Маппинг с низкой уверенностью: index={result['device_index']}, confidence={result['confidence']}")
                logger.warning(f"     Причина: {result['reason']}")
            else:
                logger.error(f"  ❌ Маппинг не найден: {result['reason']}")
            
            logger.info("")
        
        # Итоги
        logger.info("=" * 80)
        logger.info("ИТОГИ ТЕСТИРОВАНИЯ:")
        logger.info("=" * 80)
        logger.info(f"Всего устройств: {len(avf_devices)}")
        logger.info(f"Успешных маппингов (HIGH/MEDIUM): {success_count}")
        logger.info(f"Низкая уверенность (LOW): {sum(1 for r in results if r['mapping']['confidence'] == 'LOW')}")
        logger.info(f"Не найдено (NONE): {sum(1 for r in results if r['mapping']['confidence'] == 'NONE')}")
        
        success_rate = (success_count / len(avf_devices)) * 100
        logger.info(f"\n📊 Успешность маппинга: {success_rate:.1f}%")
        
        # Критерий успеха: ≥80% успешных маппингов
        success = success_rate >= 80.0
        
        if success:
            logger.info("\n✅ ПРОТОТИП 2 ПРОЙДЕН: Маппинг работает корректно")
        else:
            logger.error("\n❌ ПРОТОТИП 2 ПРОВАЛЕН: Маппинг работает некорректно")
            logger.error(f"   Требуется ≥80%, получено {success_rate:.1f}%")
        
        return success


def main():
    """Главная функция"""
    prototype = DeviceMappingPrototype()
    success = prototype.test_mapping_for_all_devices()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

