#!/usr/bin/env python3
"""
Тест аудио записи для диагностики
"""

import sounddevice as sd
import numpy as np
import logging
import time
from typing import Optional

# Настройка логирования
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class AudioRecordingTest:
    """Тест аудио записи"""
    
    def __init__(self, sample_rate: int = 16000, channels: int = 1):
        self.sample_rate = sample_rate
        self.channels = channels
        self.audio_data = []
        self.is_recording = False
        
    def test_microphone_access(self) -> bool:
        """Тестирует доступ к микрофону"""
        try:
            logger.info("🎤 Тестируем доступ к микрофону...")
            
            # Проверяем доступные устройства
            devices = sd.query_devices()
            logger.info(f"📱 Доступные аудио устройства: {len(devices)}")
            
            # Ищем устройство ввода по умолчанию
            default_input = sd.default.device[0]
            logger.info(f"🎯 Устройство ввода по умолчанию: {default_input}")
            
            if default_input is None:
                logger.error("❌ Нет устройства ввода по умолчанию")
                return False
                
            # Проверяем информацию об устройстве
            device_info = sd.query_devices(default_input)
            logger.info(f"📊 Информация об устройстве: {device_info}")
            
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка доступа к микрофону: {e}")
            return False
            
    def test_audio_recording(self, duration: float = 3.0) -> bool:
        """Тестирует запись аудио"""
        try:
            logger.info(f"🔴 Тестируем запись аудио ({duration} сек)...")
            
            # Записываем аудио
            audio_data = sd.rec(
                int(duration * self.sample_rate),
                samplerate=self.sample_rate,
                channels=self.channels,
                dtype='int16'
            )
            
            logger.info("⏳ Записываем...")
            sd.wait()  # Ждем завершения записи
            
            # Анализируем записанные данные
            if len(audio_data) > 0:
                # Вычисляем статистику
                peak = np.max(np.abs(audio_data))
                rms = np.sqrt(np.mean(audio_data.astype(np.float32) ** 2))
                rms_db = 20 * np.log10(rms + 1e-10)
                
                logger.info(f"📈 Статистика аудио:")
                logger.info(f"   - Длительность: {len(audio_data) / self.sample_rate:.2f} сек")
                logger.info(f"   - Пик: {peak}")
                logger.info(f"   - RMS: {rms:.6f}")
                logger.info(f"   - RMS (dB): {rms_db:.1f}")
                
                # Проверяем, есть ли звук
                if peak > 100:  # Пороговое значение
                    logger.info("✅ Аудио записано успешно, есть звук")
                    return True
                else:
                    logger.warning("⚠️ Аудио записано, но звук очень тихий")
                    return False
            else:
                logger.error("❌ Аудио данные не записаны")
                return False
                
        except Exception as e:
            logger.error(f"❌ Ошибка записи аудио: {e}")
            return False
            
    def test_audio_stream(self, duration: float = 2.0) -> bool:
        """Тестирует потоковую запись аудио"""
        try:
            logger.info(f"🌊 Тестируем потоковую запись аудио ({duration} сек)...")
            
            self.audio_data = []
            self.is_recording = True
            
            def audio_callback(indata, frames, time, status):
                if status:
                    logger.warning(f"⚠️ Статус аудио: {status}")
                
                if self.is_recording:
                    self.audio_data.append(indata.copy())
            
            # Запускаем потоковую запись
            with sd.InputStream(
                callback=audio_callback,
                channels=self.channels,
                samplerate=self.sample_rate,
                dtype='int16',
                blocksize=1024
            ):
                logger.info("⏳ Потоковая запись запущена...")
                time.sleep(duration)
                self.is_recording = False
            
            # Анализируем данные
            if self.audio_data:
                # Объединяем все чанки
                full_audio = np.concatenate(self.audio_data, axis=0)
                
                # Вычисляем статистику
                peak = np.max(np.abs(full_audio))
                rms = np.sqrt(np.mean(full_audio.astype(np.float32) ** 2))
                rms_db = 20 * np.log10(rms + 1e-10)
                
                logger.info(f"📈 Статистика потокового аудио:")
                logger.info(f"   - Чанков: {len(self.audio_data)}")
                logger.info(f"   - Длительность: {len(full_audio) / self.sample_rate:.2f} сек")
                logger.info(f"   - Пик: {peak}")
                logger.info(f"   - RMS: {rms:.6f}")
                logger.info(f"   - RMS (dB): {rms_db:.1f}")
                
                if peak > 100:
                    logger.info("✅ Потоковая запись работает, есть звук")
                    return True
                else:
                    logger.warning("⚠️ Потоковая запись работает, но звук тихий")
                    return False
            else:
                logger.error("❌ Потоковые аудио данные не получены")
                return False
                
        except Exception as e:
            logger.error(f"❌ Ошибка потоковой записи: {e}")
            return False

def main():
    """Основная функция теста"""
    logger.info("🚀 Запуск теста аудио записи")
    
    test = AudioRecordingTest()
    
    try:
        # Тест доступа к микрофону
        mic_ok = test.test_microphone_access()
        
        if mic_ok:
            # Тест записи аудио
            recording_ok = test.test_audio_recording()
            
            # Тест потоковой записи
            stream_ok = test.test_audio_stream()
            
            if recording_ok and stream_ok:
                logger.info("🎉 Все аудио тесты пройдены успешно!")
            else:
                logger.warning("⚠️ Некоторые аудио тесты не прошли")
        else:
            logger.error("💥 Тест доступа к микрофону не прошел")
            
    except Exception as e:
        logger.error(f"💥 Критическая ошибка: {e}")

if __name__ == "__main__":
    main()
