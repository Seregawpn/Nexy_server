"""
AudioRecoveryManager - автоматическое восстановление аудио потока при "тишине" CoreAudio.

Решает классическую проблему macOS: CoreAudio отдает нули для конкретного input-устройства,
при этом пайплайн Nexy исправен. Автоматически восстанавливает работу без вмешательства пользователя.
"""

import asyncio
from dataclasses import dataclass
from enum import Enum
import logging
import time
from typing import Any

import numpy as np

logger = logging.getLogger(__name__)

# Lazy sounddevice import to prevent TCC trigger on module load
_sd_module = None


def _get_sd():
    """Lazy import sounddevice only when first needed."""
    global _sd_module
    if _sd_module is None:
        import sounddevice as sd

        _sd_module = sd
        logger.debug("🔧 sounddevice imported lazily in AudioRecoveryManager")
    return _sd_module


class RecoveryStep(Enum):
    """Шаги восстановления аудио."""

    REPRIME = "reprime"  # Мягкий перезапуск потока
    RECREATE_44K1 = "recreate_44k1"  # Пересоздание с 44.1kHz
    TOGGLE_DEVICE = "toggle_device"  # Переключение устройства
    FFMPEG_PROBE = "ffmpeg_probe"  # Проверка через ffmpeg
    SYSTEM_FIX = "system_fix"  # Требуется системное исправление


@dataclass
class AudioConfig:
    """Конфигурация аудио потока."""

    samplerate: int
    blocksize: int
    dtype: str
    channels: int = 1

    def __str__(self) -> str:
        return f"{self.samplerate}Hz/{self.blocksize}/{self.dtype}"


@dataclass
class RecoveryStats:
    """Статистика восстановления."""

    silent_chunks: int = 0
    recovery_steps_taken: list[RecoveryStep] | None = None
    first_peak_ts: float | None = None
    max_peak: float = 0.0
    rms_avg: float = 0.0
    config_used: AudioConfig | None = None
    ffmpeg_probe_result: bool | None = None

    def __post_init__(self):
        if self.recovery_steps_taken is None:
            self.recovery_steps_taken = []


class AudioRecoveryManager:
    """
    Менеджер автоматического восстановления аудио потока.

    Пороги восстановления:
    - A: 10 пустых → мягкий reprime
    - B: 50 пустых → пересоздание с 44.1kHz
    - C: 100 пустых → переключение устройства
    - D: 150+ пустых → ffmpeg-probe + системное исправление
    """

    # Пороги восстановления
    THRESHOLD_A = 10  # reprime
    THRESHOLD_B = 50  # recreate 44.1kHz
    THRESHOLD_C = 100  # toggle device
    THRESHOLD_D = 150  # ffmpeg probe + system fix

    # Конфигурации для перебора
    AUDIO_CONFIGS = [
        AudioConfig(48000, 1024, "float32"),
        AudioConfig(44100, 1024, "float32"),
        AudioConfig(44100, 512, "int16"),
        AudioConfig(48000, 512, "float32"),
        AudioConfig(44100, 1024, "int16"),
    ]

    def __init__(self, device_id: int, device_name: str):
        self.device_id = device_id
        self.device_name = device_name
        self.stats = RecoveryStats()
        self.tried_steps: dict[RecoveryStep, bool] = {step: False for step in RecoveryStep}
        self.current_config_index = 0
        self.fallback_devices: list[int] = []
        self._setup_fallback_devices()

    def _setup_fallback_devices(self):
        """Настройка резервных устройств."""
        try:
            devices = _get_sd().query_devices()
            for i, device in enumerate(devices):
                if device["max_input_channels"] > 0 and i != self.device_id:  # type: ignore[reportArgumentType]
                    self.fallback_devices.append(i)
            logger.debug(f"🔧 Fallback devices: {self.fallback_devices}")
        except Exception as e:
            logger.warning(f"⚠️ Не удалось получить список устройств: {e}")
            self.fallback_devices = []

    def on_chunk_received(self, chunk: np.ndarray, peak: float, rms: float) -> RecoveryStep | None:
        """
        Обработка полученного чанка аудио.

        Returns:
            RecoveryStep если нужно выполнить восстановление, иначе None
        """
        # Обновляем статистику
        if peak > 0 and self.stats.first_peak_ts is None:
            self.stats.first_peak_ts = time.time()

        self.stats.max_peak = max(self.stats.max_peak, peak)
        self.stats.rms_avg = (self.stats.rms_avg * self.stats.silent_chunks + rms) / (
            self.stats.silent_chunks + 1
        )

        # Проверяем на тишину
        if peak < 0.001:  # Практически тишина
            self.stats.silent_chunks += 1
            return self._check_recovery_thresholds()
        else:
            # Сигнал есть - сбрасываем счетчик
            if self.stats.silent_chunks > 0:
                logger.info(
                    f"🎉 Аудио восстановлено! Silent chunks: {self.stats.silent_chunks} → 0"
                )
            self.stats.silent_chunks = 0
            return None

    def _check_recovery_thresholds(self) -> RecoveryStep | None:
        """Проверка порогов восстановления."""
        silent_count = self.stats.silent_chunks

        # Порог A: Мягкий reprime
        if silent_count >= self.THRESHOLD_A and not self.tried_steps[RecoveryStep.REPRIME]:
            logger.warning(f"🔧 Порог A: {silent_count} пустых чанков → reprime")
            return RecoveryStep.REPRIME

        # Порог B: Пересоздание с 44.1kHz
        elif silent_count >= self.THRESHOLD_B and not self.tried_steps[RecoveryStep.RECREATE_44K1]:
            logger.warning(f"🔧 Порог B: {silent_count} пустых чанков → recreate 44.1kHz")
            return RecoveryStep.RECREATE_44K1

        # Порог C: Переключение устройства
        elif silent_count >= self.THRESHOLD_C and not self.tried_steps[RecoveryStep.TOGGLE_DEVICE]:
            logger.warning(f"🔧 Порог C: {silent_count} пустых чанков → toggle device")
            return RecoveryStep.TOGGLE_DEVICE

        # Порог D: ffmpeg probe + системное исправление
        elif silent_count >= self.THRESHOLD_D and not self.tried_steps[RecoveryStep.FFMPEG_PROBE]:
            logger.warning(f"🔧 Порог D: {silent_count} пустых чанков → ffmpeg probe")
            return RecoveryStep.FFMPEG_PROBE

        return None

    async def execute_recovery(self, step: RecoveryStep, stream_callback) -> bool:
        """
        Выполнение шага восстановления.

        Args:
            step: Шаг восстановления
            stream_callback: Функция для пересоздания потока

        Returns:
            True если восстановление выполнено успешно
        """
        self.tried_steps[step] = True
        assert self.stats.recovery_steps_taken is not None
        self.stats.recovery_steps_taken.append(step)

        try:
            if step == RecoveryStep.REPRIME:
                return await self._reprime_stream(stream_callback)
            elif step == RecoveryStep.RECREATE_44K1:
                return await self._recreate_stream_44k1(stream_callback)
            elif step == RecoveryStep.TOGGLE_DEVICE:
                return await self._toggle_device_cycle(stream_callback)
            elif step == RecoveryStep.FFMPEG_PROBE:
                return await self._ffmpeg_probe_and_fix(stream_callback)
            else:
                logger.error(f"❌ Неизвестный шаг восстановления: {step}")
                return False

        except Exception as e:
            logger.error(f"❌ Ошибка при выполнении {step}: {e}")
            return False

    async def _reprime_stream(self, stream_callback) -> bool:
        """Мягкий перезапуск потока."""
        logger.info("🔄 Выполняем reprime: остановка → пауза → запуск")

        # Останавливаем поток
        await stream_callback(stop=True)
        await asyncio.sleep(0.1)  # 100ms пауза

        # Запускаем заново
        await stream_callback(start=True)
        return True

    async def _recreate_stream_44k1(self, stream_callback) -> bool:
        """Пересоздание потока с 44.1kHz."""
        logger.info("🔄 Пересоздаем поток с 44.1kHz")

        # Переходим к следующей конфигурации
        self.current_config_index = min(1, len(self.AUDIO_CONFIGS) - 1)  # 44.1kHz
        config = self.AUDIO_CONFIGS[self.current_config_index]
        self.stats.config_used = config

        await stream_callback(recreate=True, config=config)
        return True

    async def _toggle_device_cycle(self, stream_callback) -> bool:
        """Цикл переключения устройства."""
        if not self.fallback_devices:
            logger.warning("⚠️ Нет резервных устройств для переключения")
            return False

        logger.info("🔄 Переключаем устройство для 'пинка' CoreAudio")

        # Переключаемся на резервное устройство
        fallback_device = self.fallback_devices[0]
        await stream_callback(device_id=fallback_device)
        await asyncio.sleep(0.2)

        # Возвращаемся к основному
        await stream_callback(device_id=self.device_id)
        return True

    async def _ffmpeg_probe_and_fix(self, stream_callback) -> bool:
        """Проверка через ffmpeg и системное исправление."""
        logger.info("🔍 Выполняем ffmpeg probe")

        # Проверяем через ffmpeg
        ffmpeg_ok = await self._ffmpeg_probe_device()
        self.stats.ffmpeg_probe_result = ffmpeg_ok

        if ffmpeg_ok:
            logger.info("✅ ffmpeg слышит устройство - проблема в Python/CoreAudio")
            # Пробуем пересоздать с другой конфигурацией
            self.current_config_index = (self.current_config_index + 1) % len(self.AUDIO_CONFIGS)
            config = self.AUDIO_CONFIGS[self.current_config_index]
            self.stats.config_used = config
            await stream_callback(recreate=True, config=config)
            return True
        else:
            logger.warning("❌ ffmpeg тоже не слышит - требуется системное исправление")
            # Требуется системное исправление
            await self._show_system_fix_dialog()
            return False

    async def _ffmpeg_probe_device(self) -> bool:
        """Проверка устройства через ffmpeg."""
        try:
            # Команда ffmpeg для записи 1 секунды с устройства
            cmd = [
                "ffmpeg",
                "-f",
                "avfoundation",
                "-i",
                f":{self.device_id}",  # :device_id для macOS
                "-t",
                "1",  # 1 секунда
                "-ar",
                "44100",
                "-ac",
                "1",
                "-f",
                "wav",
                "-",  # stdout
            ]

            logger.debug(f"🔍 Запускаем ffmpeg probe: {' '.join(cmd)}")

            # Запускаем ffmpeg
            process = await asyncio.create_subprocess_exec(
                *cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
            )

            stdout, stderr = await asyncio.wait_for(process.communicate(), timeout=5.0)

            if process.returncode == 0:
                # Проверяем размер вывода (пустой файл = тишина)
                audio_size = len(stdout)
                logger.debug(f"🔍 ffmpeg probe: размер аудио = {audio_size} байт")
                return audio_size > 1000  # Минимальный размер для непустого аудио
            else:
                logger.warning(f"⚠️ ffmpeg probe failed: {stderr.decode()}")
                return False

        except asyncio.TimeoutError:
            logger.warning("⚠️ ffmpeg probe timeout")
            return False
        except Exception as e:
            logger.warning(f"⚠️ ffmpeg probe error: {e}")
            return False

    async def _show_system_fix_dialog(self):
        """Показ диалога системного исправления."""
        logger.warning("🚨 Требуется системное исправление микрофона")
        # TODO: Реализовать UI диалог с кнопками:
        # - "Перезапустить CoreAudio"
        # - "Открыть Sound/Input"
        # - "Открыть Privacy/Microphone"
        # - "Показать чек-лист"

    def get_current_config(self) -> AudioConfig:
        """Получение текущей конфигурации."""
        return self.AUDIO_CONFIGS[self.current_config_index]

    def get_recovery_status(self) -> dict[str, Any]:
        """Получение статуса восстановления для логирования."""
        assert self.stats.recovery_steps_taken is not None
        return {
            "silent_chunks": self.stats.silent_chunks,
            "recovery_steps": [step.value for step in self.stats.recovery_steps_taken],
            "config_used": str(self.stats.config_used) if self.stats.config_used else None,
            "max_peak": self.stats.max_peak,
            "rms_avg": self.stats.rms_avg,
            "ffmpeg_probe": self.stats.ffmpeg_probe_result,
            "tried_steps": {step.value: tried for step, tried in self.tried_steps.items()},
        }

    def reset(self):
        """Сброс состояния восстановления."""
        self.stats = RecoveryStats()
        self.tried_steps = {step: False for step in RecoveryStep}
        self.current_config_index = 0
        logger.debug("🔄 AudioRecoveryManager сброшен")


async def preflight_check(
    device_id: int, device_name: str, duration_ms: int = 100
) -> tuple[bool, float]:
    """
    Preflight проверка устройства перед началом записи.

    Args:
        device_id: ID устройства
        device_name: Имя устройства
        duration_ms: Длительность проверки в миллисекундах

    Returns:
        Tuple[успех, peak_значение]
    """
    logger.info(f"🔍 Preflight check: {device_name} ({device_id}) на {duration_ms}ms")

    try:
        # Записываем короткий буфер
        frames = int(48000 * duration_ms / 1000)  # Примерно duration_ms
        audio_data = _get_sd().rec(
            frames, device=device_id, samplerate=48000, channels=1, dtype="float32"
        )
        _get_sd().wait()  # Ждем завершения

        # Анализируем результат
        peak = float(np.abs(audio_data).max())
        success = peak > 0.001

        logger.info(f"🔍 Preflight result: peak={peak:.6f}, success={success}")
        return success, peak

    except Exception as e:
        logger.warning(f"⚠️ Preflight check failed: {e}")
        return False, 0.0
