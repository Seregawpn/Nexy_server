"""
MVP-12: Full Integration - Input + Output

Цель: Полная интеграция всех компонентов:
- Input: Push-to-talk, device switching, Google SR (из MVP-11)
- Output: AVAudioEngine playback, device switching (из MVP-6)
- Сценарий: Запись речи → распознавание → воспроизведение ответа

Exit Gate:
- [ ] Push-to-talk активирует микрофон
- [ ] Переключение input устройств работает
- [ ] Распознавание речи работает
- [ ] Output playback воспроизводит аудио
- [ ] Переключение output устройств работает
- [ ] Полный цикл: запись → распознавание → воспроизведение работает

FIX PACK INCLUDED:
- FIX-03: epoch-gating для callback → убираем race stop/close vs callback append
- FIX-04: input_stream_lock для open/stop/close из разных потоков
- FIX-05: defer output switch while playing → не пересоздаём engine в середине playback
- Улучшенные метрики/логи (latency_ms, event_id, epoch, sr)
"""

import sys
import os
import time
import logging
import threading
import queue
import numpy as np
from typing import Optional, Dict, List, Tuple, Any
from dataclasses import dataclass
from pathlib import Path

# -----------------------------------------------------------------------------
# Logging
# -----------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# Optional deps
# -----------------------------------------------------------------------------
try:
    import sounddevice as sd
    SOUNDDEVICE_AVAILABLE = True
except ImportError:
    SOUNDDEVICE_AVAILABLE = False
    logger.error("❌ sounddevice не доступен")
    sd = None  # type: ignore

try:
    from pynput import keyboard
    PYNPUT_AVAILABLE = True
except ImportError:
    PYNPUT_AVAILABLE = False
    logger.warning("⚠️ pynput не доступен, используем симуляцию")

try:
    import speech_recognition as sr
    SR_AVAILABLE = True
except ImportError:
    SR_AVAILABLE = False
    logger.error("❌ speech_recognition не доступен")

try:
    from AVFoundation import (  # type: ignore[reportMissingImports, reportAttributeAccessIssue]
        AVAudioEngine,  # type: ignore[reportAttributeAccessIssue] # noqa: F401
        AVAudioPlayerNode,  # type: ignore[reportAttributeAccessIssue] # noqa: F401
        AVAudioFormat,  # type: ignore[reportAttributeAccessIssue] # noqa: F401
        AVAudioPCMBuffer,  # type: ignore[reportAttributeAccessIssue] # noqa: F401
        AVAudioSession,  # type: ignore[reportAttributeAccessIssue] # noqa: F401
    )
    PYOBJC_AVAILABLE = True
except ImportError:
    PYOBJC_AVAILABLE = False
    logger.error("❌ AVFoundation не доступен")

# -----------------------------------------------------------------------------
# Paths to previous MVP modules
# -----------------------------------------------------------------------------
mvp1_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/mvp1_device_discovery"
mvp2_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/mvp2_device_mapping"
mvp6_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/mvp6_output_playback"
sys.path.insert(0, mvp1_path)
sys.path.insert(0, mvp2_path)
sys.path.insert(0, mvp6_path)

# Imports from previous MVP
from test_device_discovery import DeviceDiscoveryPrototype, DeviceInfo  # type: ignore[reportMissingImports]
from test_device_mapping import DeviceMappingPrototype  # type: ignore[reportMissingImports]
from test_output_playback import OutputPlaybackPrototype  # type: ignore[reportMissingImports]


# -----------------------------------------------------------------------------
# Data models
# -----------------------------------------------------------------------------
@dataclass
class FullCycleEvent:
    """Событие полного цикла: запись → распознавание → воспроизведение"""
    timestamp: float
    input_device: str
    output_device: str
    recognized_text: Optional[str]
    playback_success: bool
    duration_ms: int
    # extra debug fields
    event_id: int = -1
    record_epoch: int = 0
    record_sr: int = 0
    recognize_latency_ms: int = 0
    playback_latency_ms: int = 0


# -----------------------------------------------------------------------------
# Main Prototype
# -----------------------------------------------------------------------------
class FullInputOutputPrototype:
    """
    Полная интеграция Input + Output

    Потоки:
      - keyboard listener thread → _start_recording / _stop_recording
      - device monitor thread → switch input/output
      - worker thread → SR + playback (heavy ops)
    """

    def __init__(self):
        # Input
        self.device_discovery = DeviceDiscoveryPrototype()
        self.device_mapping = DeviceMappingPrototype()

        # Output
        self.output_playback = OutputPlaybackPrototype()

        # Device state
        self.current_input_device_data: Optional[Dict[str, Any]] = None
        self.current_output_device_data: Optional[Dict[str, Any]] = None
        self.last_input_device_uid: Optional[str] = None
        self.last_output_device_uid: Optional[str] = None

        # Debounce (BT flapping)
        self.pending_input_uid: Optional[str] = None
        self.pending_input_count: int = 0
        self.pending_output_uid: Optional[str] = None
        self.pending_output_count: int = 0
        self.DEBOUNCE_TICKS = 2

        # Input stream owner
        if not SOUNDDEVICE_AVAILABLE or sd is None:
            raise RuntimeError("sounddevice не доступен")
        self.input_stream: Optional[Any] = None
        self.audio_buffer: List[np.ndarray] = []
        self.audio_lock = threading.Lock()

        # FIX-04: global lock for input stream open/stop/close across threads
        self.input_stream_lock = threading.Lock()

        # FIX-03: epoch gating for callback
        self._stream_epoch = 0

        self.current_sample_rate = 44100

        # SR recognizer (does not own microphone)
        if not SR_AVAILABLE:
            raise RuntimeError("speech_recognition не доступен")
        self.current_recognizer: Optional["sr.Recognizer"] = None  # type: ignore

        # Recording state
        self.is_recording = False
        self.recording_started_at: Optional[float] = None
        self.key_pressed = False
        self._pressed_keys = set()

        # Worker thread for heavy ops
        self.work_queue: "queue.Queue[Tuple[str, Any]]" = queue.Queue()
        self.worker_thread: Optional[threading.Thread] = None
        self.stop_worker = threading.Event()

        # Output engine lock (re-entrant)
        self.engine_lock = threading.RLock()

        # Playback state
        self.is_playing = False
        self.output_key_pressed = False

        # FIX-05: defer output switch while playing
        self.pending_output_switch: Optional[Dict[str, Any]] = None

        # Monitoring threads
        self.stop_device_monitoring = threading.Event()
        self.device_monitor_thread: Optional[threading.Thread] = None
        self.key_listener: Optional["keyboard.Listener"] = None if PYNPUT_AVAILABLE else None  # type: ignore

        # Events storage
        self.event_counter = 0
        self.full_cycle_events: List[FullCycleEvent] = []
        self.events_by_id: Dict[int, FullCycleEvent] = {}

    # -------------------------------------------------------------------------
    # Setup
    # -------------------------------------------------------------------------
    def setup(self) -> bool:
        logger.info("=" * 80)
        logger.info("MVP-12: Full Integration - Input + Output")
        logger.info("=" * 80)
        logger.info("")

        logger.info("📋 Инициализация компонентов...")

        if not self.device_discovery.setup():
            logger.error("❌ Ошибка инициализации DeviceDiscovery")
            return False

        if not self.device_mapping.setup():
            logger.error("❌ Ошибка инициализации DeviceMapping")
            return False

        if not self.output_playback.setup():
            logger.error("❌ Ошибка инициализации OutputPlayback")
            return False

        if not self.output_playback.setup_audio_session():
            logger.error("❌ Ошибка настройки AVAudioSession для Output")
            return False

        if not self.output_playback.initialize_engine():
            logger.error("❌ Ошибка инициализации AVAudioEngine")
            return False

        # Start engine
        try:
            error = None
            if not self.output_playback.engine.startAndReturnError_(error):
                logger.error("❌ Не удалось запустить AVAudioEngine")
                return False
            logger.info("✅ AVAudioEngine запущен")
        except Exception as e:
            logger.error(f"❌ Ошибка запуска AVAudioEngine: {e}")
            return False

        # Worker thread
        self.worker_thread = threading.Thread(target=self._worker_loop, daemon=True)
        self.worker_thread.start()
        logger.info("✅ Worker thread запущен")

        # Initial devices
        if not self._get_initial_devices():
            logger.error("❌ Не удалось получить начальные устройства")
            return False

        logger.info("✅ Инициализация завершена")
        logger.info(f"   Input устройство: {self.current_input_device_data['name'] if self.current_input_device_data else 'Unknown'}")
        logger.info(f"   Output устройство: {self.current_output_device_data['name'] if self.current_output_device_data else 'Unknown'}")
        logger.info("")
        return True

    def _get_initial_devices(self) -> bool:
        try:
            self.current_input_device_data = self._get_current_input_device_data()
            if not self.current_input_device_data:
                logger.error("❌ Не удалось получить начальное input устройство")
                return False

            self.current_output_device_data = self._get_current_output_device_data()
            if not self.current_output_device_data:
                logger.error("❌ Не удалось получить начальное output устройство")
                return False

            self.current_recognizer = sr.Recognizer()  # type: ignore

            self.last_input_device_uid = self.current_input_device_data["uid"]
            self.last_output_device_uid = self.current_output_device_data["uid"]

            logger.info("✅ Начальные устройства получены")
            return True
        except Exception as e:
            logger.error(f"❌ Ошибка получения устройств: {e}")
            import traceback
            logger.error(traceback.format_exc())
            return False

    # -------------------------------------------------------------------------
    # Device reading (Source of Truth: AVFoundation default)
    # -------------------------------------------------------------------------
    def _get_current_input_device_data(self) -> Optional[Dict[str, Any]]:
        """
        Returns dict with:
          uid (canonical AVFoundation UID), name, device_index (PortAudio),
          sample_rate, max_input_channels
        """
        try:
            import sounddevice as sd  # type: ignore

            current_avf_device = self.device_discovery.get_current_input()
            if not current_avf_device:
                logger.warning("⚠️ AVFoundation не определил current input device, fallback на PortAudio default")
                try:
                    default_input = sd.default.device[0]
                    if default_input is None or default_input < 0:
                        return None
                    info = sd.query_devices(default_input)
                    name = info.get("name", "Unknown") if isinstance(info, dict) else "Unknown"
                    return {
                        "uid": f"portaudio_{default_input}",
                        "name": name,
                        "device_index": default_input,
                        "sample_rate": int(info.get("default_samplerate", 44100)) if isinstance(info, dict) else 44100,
                        "max_input_channels": int(info.get("max_input_channels", 1)) if isinstance(info, dict) else 1,
                    }
                except Exception as e:
                    logger.warning(f"⚠️ Ошибка получения PortAudio default input: {e}")
                    return None

            mapping_result = self.device_mapping.find_portaudio_match(
                current_avf_device.name, current_avf_device.channels, current_avf_device.transport
            )

            if not mapping_result.is_usable():
                logger.warning(f"⚠️ Не найден PortAudio match для {current_avf_device.name} (UID: {current_avf_device.uid}), fallback на PortAudio default")
                try:
                    default_input = sd.default.device[0]
                    if default_input is None or default_input < 0:
                        return None
                    info = sd.query_devices(default_input)
                    return {
                        "uid": current_avf_device.uid,  # keep canonical UID
                        "name": current_avf_device.name,
                        "device_index": default_input,
                        "sample_rate": int(info.get("default_samplerate", 44100)) if isinstance(info, dict) else 44100,
                        "max_input_channels": int(info.get("max_input_channels", 1)) if isinstance(info, dict) else 1,
                    }
                except Exception as e:
                    logger.warning(f"⚠️ Ошибка fallback на PortAudio default: {e}")
                    return None

            device_index = mapping_result.device_index
            try:
                pa_info = sd.query_devices(device_index)
                sample_rate = int(pa_info.get("default_samplerate", 44100)) if isinstance(pa_info, dict) else 44100
                max_ch = int(pa_info.get("max_input_channels", 1)) if isinstance(pa_info, dict) else 1
            except Exception:
                sample_rate = 44100
                max_ch = 1

            return {
                "uid": current_avf_device.uid,
                "name": current_avf_device.name,
                "device_index": device_index,
                "sample_rate": sample_rate,
                "max_input_channels": max_ch,
            }

        except Exception as e:
            logger.error(f"❌ Ошибка получения input устройства: {e}")
            import traceback
            logger.error(traceback.format_exc())
            return None

    def _get_current_output_device_data(self) -> Optional[Dict[str, Any]]:
        """
        Returns dict with:
          uid (canonical AVFoundation UID), name, device_index (optional),
          sample_rate, max_output_channels
        """
        try:
            import sounddevice as sd  # type: ignore

            current_avf_device = self.device_discovery.get_current_output()
            if not current_avf_device:
                logger.warning("⚠️ AVFoundation не определил current output device, fallback на PortAudio default")
                try:
                    default_output = sd.default.device[1]
                    if default_output is None or default_output < 0:
                        return None
                    info = sd.query_devices(default_output)
                    name = info.get("name", "Unknown") if isinstance(info, dict) else "Unknown"
                    return {
                        "uid": f"portaudio_{default_output}",
                        "name": name,
                        "device_index": default_output,
                        "sample_rate": int(info.get("default_samplerate", 44100)) if isinstance(info, dict) else 44100,
                        "max_output_channels": int(info.get("max_output_channels", 2)) if isinstance(info, dict) else 2,
                    }
                except Exception as e:
                    logger.warning(f"⚠️ Ошибка получения PortAudio default output: {e}")
                    return None

            mapping_result = self.device_mapping.find_portaudio_match(
                current_avf_device.name, current_avf_device.channels, current_avf_device.transport
            )

            device_index = None
            if mapping_result.is_usable():
                device_index = mapping_result.device_index
                try:
                    pa_info = sd.query_devices(device_index)
                    sample_rate = int(pa_info.get("default_samplerate", 44100)) if isinstance(pa_info, dict) else 44100
                    max_ch = int(pa_info.get("max_output_channels", 2)) if isinstance(pa_info, dict) else 2
                except Exception:
                    sample_rate = 44100
                    max_ch = 2
            else:
                try:
                    default_output = sd.default.device[1]
                    if default_output is not None and default_output >= 0:
                        info = sd.query_devices(default_output)
                        sample_rate = int(info.get("default_samplerate", 44100)) if isinstance(info, dict) else 44100
                        max_ch = int(info.get("max_output_channels", 2)) if isinstance(info, dict) else 2
                        device_index = default_output
                    else:
                        sample_rate = 44100
                        max_ch = 2
                except Exception:
                    sample_rate = 44100
                    max_ch = 2

            return {
                "uid": current_avf_device.uid,
                "name": current_avf_device.name,
                "device_index": device_index,
                "sample_rate": sample_rate,
                "max_output_channels": max_ch,
            }

        except Exception as e:
            logger.error(f"❌ Ошибка получения output устройства: {e}")
            import traceback
            logger.error(traceback.format_exc())
            return None

    # -------------------------------------------------------------------------
    # Input stream open/close (FIX-03 + FIX-04)
    # -------------------------------------------------------------------------
    def _open_input_stream_with_fallback(self, device_index: int, log_prefix: str = "") -> bool:
        """
        Open InputStream with fallback samplerates.
        FIX-03: epoch gating callback.
        NOTE: Caller should hold self.input_stream_lock for multi-thread safety.
        """
        if not SOUNDDEVICE_AVAILABLE or sd is None:
            if log_prefix:
                logger.error(f"{log_prefix}❌ sounddevice не доступен")
            return False

        candidate_srs = [int(self.current_sample_rate), 48000, 44100, 16000]
        candidate_srs = [sr_ for sr_ in candidate_srs if sr_ > 0]
        seen = set()
        candidate_srs = [sr_ for sr_ in candidate_srs if not (sr_ in seen or seen.add(sr_))]

        last_err = None
        for sr_try in candidate_srs:
            try:
                # FIX-03: new epoch for this stream
                self._stream_epoch += 1
                epoch = self._stream_epoch

                def cb(indata, frames, time_info, status, _epoch=epoch):
                    self._audio_callback(indata, frames, time_info, status, _epoch)

                st = sd.InputStream(  # type: ignore
                    device=device_index,
                    channels=1,
                    samplerate=sr_try,
                    blocksize=1024,
                    callback=cb,
                    dtype=np.float32,
                )
                st.start()  # type: ignore
                self.input_stream = st
                self.current_sample_rate = sr_try

                try:
                    is_active = st.active  # type: ignore
                    if not is_active:
                        if log_prefix:
                            logger.warning(f"{log_prefix}⚠️ InputStream открыт, но не активен, пробуем следующий samplerate")
                        try:
                            st.close()  # type: ignore
                        except Exception:
                            pass
                        self.input_stream = None
                        continue

                    if log_prefix:
                        logger.info(f"{log_prefix}✅ InputStream открыт и активен (epoch={epoch}, sample_rate={self.current_sample_rate}Hz)")
                    return True
                except Exception as active_check_e:
                    if log_prefix:
                        logger.warning(f"{log_prefix}⚠️ active status check failed: {active_check_e} (epoch={epoch}) → считаем успешным")
                    if log_prefix:
                        logger.info(f"{log_prefix}✅ InputStream открыт (epoch={epoch}, sample_rate={self.current_sample_rate}Hz)")
                    return True

            except Exception as e:
                last_err = e
                try:
                    if self.input_stream is not None:
                        self.input_stream.close()  # type: ignore
                except Exception:
                    pass
                self.input_stream = None

        if log_prefix:
            logger.error(f"{log_prefix}❌ Не удалось открыть InputStream ни на одном samplerate. Последняя ошибка: {last_err}")
        return False

    def _audio_callback(self, indata, frames, time_info, status, epoch: int):
        """Callback for InputStream. FIX-03: epoch gating."""
        if status:
            logger.warning(f"⚠️ Audio stream status: {status}")

        # epoch gate: ignore callbacks from older stream instances
        if (not self.is_recording) or (epoch != self._stream_epoch):
            return

        with self.audio_lock:
            self.audio_buffer.append(indata.copy())

    # -------------------------------------------------------------------------
    # Switch input/output
    # -------------------------------------------------------------------------
    def _switch_input_device(self, device_data: Dict[str, Any]) -> bool:
        """
        Switch input device: stop/close existing stream only (do not start new).
        NOTE: caller should handle re-open if recording.
        """
        try:
            logger.info(f"      🔄 Переключение input на: {device_data['name']}")

            with self.input_stream_lock:
                if self.input_stream is not None:
                    try:
                        if getattr(self.input_stream, "active", False):  # type: ignore
                            self.input_stream.stop()  # type: ignore
                        self.input_stream.close()  # type: ignore
                    except Exception:
                        pass
                    self.input_stream = None

                device_index = device_data.get("device_index")
                if device_index is None:
                    logger.error(f"      ❌ Нет device_index для устройства {device_data['name']}")
                    return False

                self.current_sample_rate = device_data.get("sample_rate", 44100)

            logger.info(f"      ✅ Input готов: {device_data['name']} (index={device_index}, sample_rate={self.current_sample_rate})")
            return True

        except Exception as e:
            logger.error(f"      ❌ Ошибка переключения input: {e}")
            import traceback
            logger.error(traceback.format_exc())
            return False

    def _switch_output_device(self, device_data: Dict[str, Any]) -> bool:
        """Switch output: stop engine, reinit, start. Protected by engine_lock."""
        try:
            logger.info(f"      🔄 Переключение output на: {device_data['name']}")

            with self.engine_lock:
                try:
                    if self.output_playback.engine and self.output_playback.engine.isRunning():
                        self.output_playback.engine.stop()
                        logger.info("      ⏸️ AVAudioEngine остановлен")

                    if not self.output_playback.initialize_engine():
                        logger.error("      ❌ Не удалось переинициализировать AVAudioEngine")
                        return False

                    error = None
                    if not self.output_playback.engine.startAndReturnError_(error):
                        logger.error("      ❌ Не удалось запустить AVAudioEngine после переключения")
                        return False

                    logger.info(f"      ✅ Output переключен: {device_data['name']} (index={device_data.get('device_index')})")
                    logger.info("      ✅ AVAudioEngine пересоздан и запущен")
                    return True

                except Exception as engine_e:
                    logger.error(f"      ❌ Ошибка пересоздания AVAudioEngine: {engine_e}")
                    import traceback
                    logger.error(traceback.format_exc())
                    return False

        except Exception as e:
            logger.error(f"      ❌ Ошибка переключения output: {e}")
            import traceback
            logger.error(traceback.format_exc())
            return False

    # -------------------------------------------------------------------------
    # Refresh helpers (source of truth: AVFoundation)
    # -------------------------------------------------------------------------
    def _refresh_input_before_recording(self) -> Dict[str, Any]:
        import sounddevice as sd  # type: ignore

        fresh = self._get_current_input_device_data()
        if not fresh:
            raise RuntimeError("Cannot read current input device (system default)")

        self.current_input_device_data = fresh
        self.last_input_device_uid = fresh["uid"]

        device_index = fresh.get("device_index")
        if device_index is None:
            raise RuntimeError("No PortAudio device_index for current input")

        # validate PortAudio index name vs AVF name
        try:
            info = sd.query_devices(device_index)
            pa_name = info.get("name", "") if isinstance(info, dict) else ""
            if pa_name and (fresh["name"].lower() not in pa_name.lower()) and (pa_name.lower() not in fresh["name"].lower()):
                logger.warning(f"      ⚠️ PortAudio device name mismatch, re-reading: '{pa_name}' vs '{fresh['name']}'")
                fresh2 = self._get_current_input_device_data()
                if fresh2 and fresh2.get("device_index") is not None:
                    self.current_input_device_data = fresh2
                    self.last_input_device_uid = fresh2["uid"]
                    return fresh2
        except Exception as e:
            logger.debug(f"      ⚠️ PortAudio validation skipped: {e}")

        return fresh

    def _refresh_output_before_playback(self) -> Dict[str, Any]:
        fresh = self._get_current_output_device_data()
        if not fresh:
            raise RuntimeError("Cannot read current output device (system default)")

        if self.last_output_device_uid != fresh["uid"]:
            logger.info(f"      🔄 Output device changed: {self.last_output_device_uid} → {fresh['uid']} (reinit engine)")
            ok = self._switch_output_device(fresh)
            if not ok:
                raise RuntimeError(f"Failed to switch output device / reinit engine: {fresh['name']}")

        self.current_output_device_data = fresh
        self.last_output_device_uid = fresh["uid"]
        return fresh

    # -------------------------------------------------------------------------
    # Resampling
    # -------------------------------------------------------------------------
    def _resample_linear(self, x: np.ndarray, src_sr: int, dst_sr: int) -> np.ndarray:
        if src_sr == dst_sr:
            return x.astype(np.float32, copy=False)

        x = x.astype(np.float32, copy=False)
        n_src = int(len(x))
        if n_src <= 0:
            return np.zeros((0,), dtype=np.float32)
        if n_src == 1:
            ratio = dst_sr / src_sr
            n_dst = max(1, int(round(n_src * ratio)))
            return np.full((n_dst,), float(x[0]), dtype=np.float32)

        ratio = dst_sr / src_sr
        n_dst = max(1, int(round(n_src * ratio)))

        xp = np.linspace(0.0, 1.0, num=n_src, endpoint=False)
        x_dst = np.interp(np.linspace(0.0, 1.0, num=n_dst, endpoint=False), xp, x).astype(np.float32)
        return x_dst

    # -------------------------------------------------------------------------
    # Recording
    # -------------------------------------------------------------------------
    def _start_recording(self) -> bool:
        try:
            device_name = self.current_input_device_data["name"] if self.current_input_device_data else "Unknown"
            logger.info("=" * 80)
            logger.info("🎙️ НАЧАЛО ЗАПИСИ (Push-to-talk)")
            logger.info(f"   📱 Input: {device_name}")
            logger.info(f"   📱 Output: {self.current_output_device_data['name'] if self.current_output_device_data else 'Unknown'}")
            logger.info("")

            with self.audio_lock:
                self.audio_buffer.clear()

            # refresh input
            try:
                fresh_input = self._refresh_input_before_recording()
                device_index = fresh_input["device_index"]
                self.current_sample_rate = fresh_input.get("sample_rate", 44100)
                device_name = fresh_input["name"]
            except RuntimeError as e:
                logger.error(f"   ❌ Ошибка refresh input device: {e}")
                return False

            # set flags BEFORE open
            self.is_recording = True
            self.recording_started_at = time.time()

            # open stream (FIX-04: lock)
            with self.input_stream_lock:
                ok = self._open_input_stream_with_fallback(device_index, log_prefix="   ")
            if not ok:
                self.is_recording = False
                self.recording_started_at = None
                return False

            # sanity active
            if self.input_stream is not None:
                try:
                    if not self.input_stream.active:  # type: ignore
                        logger.warning("   ⚠️ InputStream открыт, но не активен")
                        self.is_recording = False
                        self.recording_started_at = None
                        return False
                except Exception as e:
                    logger.warning(f"   ⚠️ Не удалось проверить active status: {e}")

            logger.info(f"   ✅ ЗАПИСЬ АКТИВНА - ГОВОРИТЕ (epoch={self._stream_epoch}, sample_rate={self.current_sample_rate}Hz)")
            logger.info("=" * 80)
            logger.info("")
            return True

        except Exception as e:
            logger.error(f"❌ Ошибка начала записи: {e}")
            import traceback
            logger.error(traceback.format_exc())
            self.is_recording = False
            self.recording_started_at = None
            return False

    def _stop_recording(self) -> Optional[str]:
        """Stop recording: close stream, build AudioData, enqueue SR+play."""
        try:
            device_name = self.current_input_device_data["name"] if self.current_input_device_data else "Unknown"
            logger.info("=" * 80)
            logger.info("🛑 ОСТАНОВКА ЗАПИСИ")
            logger.info(f"   📱 Input: {device_name}")
            logger.info("")

            if not self.is_recording:
                logger.debug("   ℹ️ Запись уже остановлена, пропуск")
                return None

            # stop gating first
            self.is_recording = False

            if self.recording_started_at is not None:
                rec_dur_ms = int((time.time() - self.recording_started_at) * 1000)
            else:
                logger.warning("   ⚠️ recording_started_at не установлен, длительность = 0ms")
                rec_dur_ms = 0
            self.recording_started_at = None

            # close stream (FIX-04: lock)
            with self.input_stream_lock:
                if self.input_stream is not None:
                    stream_to_close = self.input_stream
                    self.input_stream = None
                    try:
                        try:
                            if hasattr(stream_to_close, "active") and stream_to_close.active:  # type: ignore
                                stream_to_close.stop()  # type: ignore
                                logger.debug("   ✅ Stream остановлен (stop)")
                        except Exception as e1:
                            logger.debug(f"   ⚠️ Ошибка stop: {e1}")

                        time.sleep(0.05)

                        try:
                            stream_to_close.close()  # type: ignore
                            logger.debug("   ✅ Stream закрыт (close)")
                        except Exception as e2:
                            logger.warning(f"   ⚠️ Ошибка close: {e2}")

                    except Exception as stream_e:
                        logger.warning(f"   ⚠️ Критическая ошибка остановки stream: {stream_e}")

            # pull buffer
            with self.audio_lock:
                if not self.audio_buffer:
                    logger.warning("   ⚠️ Буфер пуст, запись не была начата/успела")
                    return None
                try:
                    audio_data = np.concatenate(self.audio_buffer, axis=0)
                    if audio_data.ndim > 1 and audio_data.shape[1] > 1:
                        audio_data = audio_data[:, 0]
                    audio_data = audio_data.flatten()
                except Exception as concat_e:
                    logger.error(f"   ❌ Ошибка объединения буфера: {concat_e}")
                    return None

            logger.info(f"   ✅ Аудио записано: {len(audio_data)} samples, {rec_dur_ms}ms")

            audio_float = np.clip(audio_data, -1.0, 1.0).astype(np.float32, copy=False)
            audio_16k = self._resample_linear(audio_float, self.current_sample_rate, 16000)
            logger.info(f"   🔄 Ресемплинг: {self.current_sample_rate}Hz → 16000Hz ({len(audio_16k)} samples)")
            audio_bytes = (audio_16k * 32767.0).astype(np.int16).tobytes()

            # refresh device names for event
            fresh_in = self._get_current_input_device_data()
            fresh_out = self._get_current_output_device_data()
            input_name = fresh_in["name"] if fresh_in else device_name
            output_name = fresh_out["name"] if fresh_out else (self.current_output_device_data["name"] if self.current_output_device_data else "Unknown")

            event_id = self.event_counter
            self.event_counter += 1

            event = FullCycleEvent(
                timestamp=time.time(),
                input_device=input_name,
                output_device=output_name,
                recognized_text=None,
                playback_success=False,
                duration_ms=rec_dur_ms,
                event_id=event_id,
                record_epoch=self._stream_epoch,
                record_sr=self.current_sample_rate,
            )
            self.full_cycle_events.append(event)
            self.events_by_id[event_id] = event

            logger.info(f"   🔍 Queue SR+PLAY (event_id={event_id}, epoch={event.record_epoch}, sr={event.record_sr})")
            self.work_queue.put(("RECOGNIZE_AND_PLAY", (event_id, audio_bytes, 16000)))

            logger.info(f"   ✅ Задача поставлена в очередь (event_id={event_id})")
            logger.info("=" * 80)
            logger.info("")
            return None

        except Exception as e:
            logger.error(f"❌ Ошибка остановки записи: {e}")
            import traceback
            logger.error(traceback.format_exc())
            self.is_recording = False
            self.recording_started_at = None
            return None

    # -------------------------------------------------------------------------
    # Worker loop
    # -------------------------------------------------------------------------
    def _worker_loop(self):
        logger.info("🔧 Worker thread запущен")
        while not self.stop_worker.is_set():
            try:
                try:
                    task_type, data = self.work_queue.get(timeout=0.1)
                except queue.Empty:
                    continue

                if task_type == "RECOGNIZE_AND_PLAY":
                    event_id, audio_bytes, sample_rate = data
                    self._recognize_and_play_worker(event_id, audio_bytes, sample_rate)
                elif task_type == "PLAY_RESPONSE":
                    text = data
                    self._play_response_worker(text)
                elif task_type == "PLAY_TEST_SOUND":
                    self._play_test_sound_worker()

                self.work_queue.task_done()

            except Exception as e:
                logger.error(f"❌ Ошибка в worker thread: {e}")
                import traceback
                logger.error(traceback.format_exc())

        logger.info("🔧 Worker thread остановлен")

    def _recognize_and_play_worker(self, event_id: int, audio_bytes: bytes, sample_rate: int) -> bool:
        try:
            ev = self.events_by_id.get(event_id)

            if not SR_AVAILABLE or self.current_recognizer is None:
                logger.error("   ❌ SR не доступен или Recognizer не инициализирован")
                if ev:
                    ev.recognized_text = None
                    ev.playback_success = False
                return False

            audio_obj = sr.AudioData(audio_bytes, sample_rate, 2)  # type: ignore

            # recognize latency
            t0 = time.time()
            recognized_text = None
            logger.info(f"   🔍 Google SR... (event_id={event_id})")
            try:
                recognized_text = self.current_recognizer.recognize_google(audio_obj, language="ru-RU")  # type: ignore
                logger.info(f"   ✅ RASPOZNANO (event_id={event_id}): {recognized_text}")
            except sr.UnknownValueError:  # type: ignore
                logger.warning(f"   ⚠️ Google SR не смог распознать речь (event_id={event_id})")
            except sr.RequestError as e:  # type: ignore
                logger.error(f"   ❌ Ошибка Google SR (event_id={event_id}): {e}")
            t1 = time.time()

            if ev:
                ev.recognized_text = recognized_text
                ev.recognize_latency_ms = int((t1 - t0) * 1000)

            # playback
            playback_t0 = time.time()
            ok = self._play_response_worker(recognized_text)
            playback_t1 = time.time()

            if ev:
                ev.playback_success = ok
                ev.playback_latency_ms = int((playback_t1 - playback_t0) * 1000)

            return ok

        except Exception as e:
            logger.error(f"   ❌ Ошибка recognize+play (event_id={event_id}): {e}")
            import traceback
            logger.error(traceback.format_exc())
            ev = self.events_by_id.get(event_id)
            if ev:
                ev.playback_success = False
            return False

    # -------------------------------------------------------------------------
    # Playback (FIX-05: defer output switch while playing)
    # -------------------------------------------------------------------------
    def _apply_deferred_output_switch_if_any(self):
        if self.pending_output_switch is None:
            return
        sw = self.pending_output_switch
        self.pending_output_switch = None
        logger.info("   🔄 Applying deferred output switch after playback...")
        try:
            self._switch_output_device(sw)
        except Exception as e:
            logger.error(f"   ❌ Deferred output switch failed: {e}")

    def _play_response_worker(self, text: Optional[str]) -> bool:
        try:
            if not text:
                logger.info("   🔊 Пропуск воспроизведения (нет текста)")
                return False

            logger.info(f"   🔊 Воспроизведение ответа: '{text}'")

            sample_rate = 44100
            duration_sec = 1.0
            frequency = 440.0

            t = np.linspace(0, duration_sec, int(sample_rate * duration_sec), False)
            audio_data = np.sin(2 * np.pi * frequency * t).astype(np.float32)

            self.is_playing = True
            try:
                with self.engine_lock:
                    # refresh output (may reinit engine)
                    try:
                        self._refresh_output_before_playback()
                    except RuntimeError as e:
                        logger.error(f"   ❌ refresh output device error: {e}")
                        return False

                    if not self.output_playback.engine.isRunning():
                        logger.warning("   ⚠️ AVAudioEngine не запущен, запускаем...")
                        error = None
                        if not self.output_playback.engine.startAndReturnError_(error):
                            logger.error("   ❌ Не удалось запустить AVAudioEngine")
                            return False
                        logger.info("   ✅ AVAudioEngine запущен")

                    logger.info("   🎵 AVAudioEngine play_audio_chunk() ...")
                    success = self.output_playback.play_audio_chunk(audio_data, sample_rate)
            finally:
                # keep is_playing true until after sleep (sound finishes)
                pass

            if success:
                time.sleep(duration_sec + 0.2)
                logger.info("   ✅ Playback завершено")
            else:
                logger.error("   ❌ Playback error via AVAudioEngine (fallback disabled)")

            self.is_playing = False
            self._apply_deferred_output_switch_if_any()
            return success

        except Exception as e:
            logger.error(f"   ❌ Ошибка воспроизведения: {e}")
            import traceback
            logger.error(traceback.format_exc())
            self.is_playing = False
            self._apply_deferred_output_switch_if_any()
            return False

    def _play_test_sound_worker(self) -> bool:
        try:
            device_name = self.current_output_device_data["name"] if self.current_output_device_data else "Unknown"
            logger.info("=" * 80)
            logger.info("🔊 ВОСПРОИЗВЕДЕНИЕ ТЕСТОВОГО ЗВУКА")
            logger.info(f"   📱 Output: {device_name}")
            logger.info("")

            sample_rate = 44100
            duration_sec = 1.0
            frequency = 440.0

            t = np.linspace(0, duration_sec, int(sample_rate * duration_sec), False)
            audio_data = np.sin(2 * np.pi * frequency * t).astype(np.float32)

            self.is_playing = True
            try:
                with self.engine_lock:
                    try:
                        self._refresh_output_before_playback()
                    except RuntimeError as e:
                        logger.error(f"   ❌ refresh output device error: {e}")
                        self.is_playing = False
                        return False

                    if not self.output_playback.engine.isRunning():
                        logger.warning("   ⚠️ AVAudioEngine не запущен, запускаем...")
                        error = None
                        if not self.output_playback.engine.startAndReturnError_(error):
                            logger.error("   ❌ Не удалось запустить AVAudioEngine")
                            self.is_playing = False
                            return False
                        logger.info("   ✅ AVAudioEngine запущен")

                    success = self.output_playback.play_audio_chunk(audio_data, sample_rate)
            finally:
                pass

            if success:
                time.sleep(duration_sec + 0.2)
                logger.info("   ✅ Тестовый звук завершён")
            else:
                logger.error("   ❌ Ошибка воспроизведения тестового звука (fallback disabled)")

            self.is_playing = False
            self._apply_deferred_output_switch_if_any()

            logger.info("=" * 80)
            logger.info("")
            return success

        except Exception as e:
            logger.error(f"❌ Ошибка воспроизведения тестового звука: {e}")
            import traceback
            logger.error(traceback.format_exc())
            self.is_playing = False
            self._apply_deferred_output_switch_if_any()
            return False

    def _play_response(self, text: Optional[str]) -> bool:
        self.work_queue.put(("PLAY_RESPONSE", text))
        return True

    def _play_test_sound(self) -> bool:
        self.work_queue.put(("PLAY_TEST_SOUND", None))
        return True

    # -------------------------------------------------------------------------
    # Keyboard monitoring
    # -------------------------------------------------------------------------
    def start_keyboard_monitoring(self):
        if not PYNPUT_AVAILABLE:
            logger.warning("⚠️ pynput не доступен, используем симуляцию")
            return

        try:
            self._pressed_keys = set()

            def key_token(k):
                try:
                    if k == keyboard.Key.ctrl_l:  # type: ignore
                        return "ctrl_l"
                    if k == keyboard.Key.ctrl_r:  # type: ignore
                        return "ctrl_r"
                except Exception:
                    pass
                if hasattr(k, "char") and k.char:  # type: ignore
                    return str(k.char).lower()  # type: ignore
                return None

            def is_ctrl_down():
                return ("ctrl_l" in self._pressed_keys) or ("ctrl_r" in self._pressed_keys)

            def is_char_down(ch: str):
                return ch.lower() in self._pressed_keys

            def on_press(key):
                try:
                    tok = key_token(key)
                    if tok:
                        self._pressed_keys.add(tok)

                    # INPUT: Ctrl+N
                    if is_ctrl_down() and is_char_down("n"):
                        if not self.key_pressed:
                            self.key_pressed = True
                            logger.info("⌨️ Control+N нажата - начало записи")
                            self._start_recording()

                    # OUTPUT: Ctrl+M
                    if is_ctrl_down() and is_char_down("m"):
                        if not self.output_key_pressed:
                            self.output_key_pressed = True
                            logger.info("⌨️ Control+M нажата - воспроизведение тестового звука")
                            self._play_test_sound()
                            self.output_key_pressed = False

                except Exception as e:
                    logger.error(f"❌ Ошибка on_press: {e}")

            def on_release(key):
                try:
                    tok = key_token(key)
                    if tok and tok in self._pressed_keys:
                        self._pressed_keys.remove(tok)

                    if self.key_pressed:
                        released_ctrl = tok in ("ctrl_l", "ctrl_r")
                        released_n = tok == "n"
                        if released_ctrl or released_n:
                            self.key_pressed = False
                            logger.info("⌨️ Control+N отпущена - остановка записи")
                            self._stop_recording()

                except Exception as e:
                    logger.error(f"❌ Ошибка on_release: {e}")

            self.key_listener = keyboard.Listener(on_press=on_press, on_release=on_release)  # type: ignore
            self.key_listener.start()
            logger.info("✅ Мониторинг клавиатуры запущен (Control+N / Control+M)")

        except Exception as e:
            logger.error(f"❌ Ошибка запуска мониторинга клавиатуры: {e}")

    def stop_keyboard_monitoring(self):
        if self.key_listener:
            self.key_listener.stop()
            logger.info("🛑 Мониторинг клавиатуры остановлен")

    # -------------------------------------------------------------------------
    # Device monitoring (FIX-05 included)
    # -------------------------------------------------------------------------
    def _monitor_devices(self):
        logger.info("🔄 Мониторинг устройств запущен")
        logger.info("")

        while not self.stop_device_monitoring.is_set():
            try:
                # INPUT
                current_input = self._get_current_input_device_data()
                if current_input:
                    detected_uid = current_input["uid"]
                    detected_name = current_input["name"]

                    if detected_uid != self.last_input_device_uid:
                        if detected_uid == self.pending_input_uid:
                            self.pending_input_count += 1
                        else:
                            self.pending_input_uid = detected_uid
                            self.pending_input_count = 1

                        if self.pending_input_count >= self.DEBOUNCE_TICKS:
                            logger.info("=" * 80)
                            logger.info("🔄 ОБНАРУЖЕНО ПЕРЕКЛЮЧЕНИЕ INPUT УСТРОЙСТВА!")
                            logger.info(f"   📱 Старое: {self.last_input_device_uid}")
                            logger.info(f"   📱 Новое:  {detected_uid} ({detected_name})")

                            if self.is_recording:
                                logger.warning("   ⚠️ Переключение во время записи: будет restart")

                            was_recording = self.is_recording and (self.input_stream is not None)

                            if self._switch_input_device(current_input):
                                self.current_input_device_data = current_input
                                self.last_input_device_uid = detected_uid

                                logger.info(f"decision=start ctx={{input_device={detected_name},input_uid={detected_uid}}} source=audio_route_manager duration_ms=0")

                                if was_recording:
                                    logger.info("   🔄 Restart записи на новом input...")

                                    with self.audio_lock:
                                        self.audio_buffer.clear()
                                    logger.info("   🧹 Буфер очищен из-за смены input во время записи")

                                    self.current_sample_rate = current_input.get("sample_rate", 44100)
                                    device_index = current_input.get("device_index")

                                    if device_index is not None:
                                        # flags BEFORE open
                                        self.is_recording = True
                                        self.recording_started_at = time.time()

                                        with self.input_stream_lock:
                                            ok = self._open_input_stream_with_fallback(device_index, log_prefix="   ")
                                        if ok:
                                            logger.info(f"   ✅ Запись перезапущена (epoch={self._stream_epoch}, sr={self.current_sample_rate})")
                                        else:
                                            logger.error("   ❌ Не удалось перезапустить запись")
                                            self.is_recording = False
                                            self.recording_started_at = None
                                    else:
                                        logger.warning("   ⚠️ Нет device_index для restart записи")
                                        self.is_recording = False
                                        self.recording_started_at = None

                                self.pending_input_uid = None
                                self.pending_input_count = 0
                                logger.info("=" * 80)
                                logger.info("")
                            else:
                                self.pending_input_uid = None
                                self.pending_input_count = 0
                                logger.info("=" * 80)
                                logger.info("")
                    else:
                        self.pending_input_uid = None
                        self.pending_input_count = 0

                # OUTPUT
                current_output = self._get_current_output_device_data()
                if current_output:
                    detected_uid = current_output["uid"]
                    detected_name = current_output["name"]

                    if detected_uid != self.last_output_device_uid:
                        if detected_uid == self.pending_output_uid:
                            self.pending_output_count += 1
                        else:
                            self.pending_output_uid = detected_uid
                            self.pending_output_count = 1

                        if self.pending_output_count >= self.DEBOUNCE_TICKS:
                            logger.info("=" * 80)
                            logger.info("🔄 ОБНАРУЖЕНО ПЕРЕКЛЮЧЕНИЕ OUTPUT УСТРОЙСТВА!")
                            logger.info(f"   📱 Старое: {self.last_output_device_uid}")
                            logger.info(f"   📱 Новое:  {detected_uid} ({detected_name})")

                            # FIX-05: defer while playing
                            if self.is_playing:
                                logger.warning("   ⚠️ Output switch deferred (is_playing=True)")
                                self.pending_output_switch = current_output
                                # update uid to avoid repeated logs/flapping
                                self.last_output_device_uid = detected_uid
                                self.current_output_device_data = current_output
                                self.pending_output_uid = None
                                self.pending_output_count = 0
                                logger.info("=" * 80)
                                logger.info("")
                                time.sleep(1.0)
                                continue

                            if self._switch_output_device(current_output):
                                self.current_output_device_data = current_output
                                self.last_output_device_uid = detected_uid
                                logger.info(f"decision=start ctx={{output_device={detected_name},output_uid={detected_uid}}} source=audio_route_manager duration_ms=0")

                                self.pending_output_uid = None
                                self.pending_output_count = 0
                                logger.info("=" * 80)
                                logger.info("")
                            else:
                                self.pending_output_uid = None
                                self.pending_output_count = 0
                                logger.info("=" * 80)
                                logger.info("")
                    else:
                        self.pending_output_uid = None
                        self.pending_output_count = 0

                time.sleep(1.0)

            except Exception as e:
                logger.error(f"❌ Ошибка мониторинга устройств: {e}")
                import traceback
                logger.error(traceback.format_exc())
                time.sleep(1.0)

    # -------------------------------------------------------------------------
    # Test runner
    # -------------------------------------------------------------------------
    def test_full_integration(self):
        logger.info("=" * 80)
        logger.info("MVP-12: Full Integration - Input + Output")
        logger.info("=" * 80)
        logger.info("")
        logger.info("📋 Инструкция:")
        logger.info("   INPUT (запись):")
        logger.info("   1. Нажмите и удерживайте Control+N для начала записи")
        logger.info("   2. Говорите в микрофон")
        logger.info("   3. Отпустите Control+N для остановки записи и воспроизведения ответа")
        logger.info("")
        logger.info("   OUTPUT (воспроизведение):")
        logger.info("   4. Нажмите Control+M для воспроизведения тестового звука")
        logger.info("   5. Переключайте input/output устройства (отключите/подключите наушники)")
        logger.info("   6. Повторите несколько раз")
        logger.info("")

        self.start_keyboard_monitoring()

        self.device_monitor_thread = threading.Thread(target=self._monitor_devices, daemon=True)
        self.device_monitor_thread.start()
        logger.info("🔄 Мониторинг устройств запущен")
        logger.info("⏳ Ожидание действий пользователя (Ctrl+C для остановки)...")
        logger.info("")

        try:
            while True:
                time.sleep(1.0)
        except KeyboardInterrupt:
            logger.info("")
            logger.info("🛑 Получен сигнал остановки (Ctrl+C)")
            logger.info("")

        # stop monitoring
        self.stop_device_monitoring.set()
        self.stop_keyboard_monitoring()

        # wait for queued tasks
        try:
            self.work_queue.join()
        except Exception:
            pass

        # stop worker
        self.stop_worker.set()
        if self.worker_thread and self.worker_thread.is_alive():
            self.worker_thread.join(timeout=2.0)
            logger.info("✅ Worker thread остановлен")

        # stop input stream
        with self.input_stream_lock:
            if self.input_stream is not None:
                try:
                    if getattr(self.input_stream, "active", False):  # type: ignore
                        self.input_stream.stop()  # type: ignore
                    self.input_stream.close()  # type: ignore
                    logger.info("✅ Input stream остановлен")
                except Exception:
                    pass
                self.input_stream = None

        # stop engine
        try:
            self.output_playback.engine.stop()
            logger.info("✅ AVAudioEngine остановлен")
        except Exception:
            pass

        # results
        logger.info("")
        logger.info("=" * 80)
        logger.info("РЕЗУЛЬТАТЫ")
        logger.info("=" * 80)
        logger.info("")
        logger.info(f"📊 Всего циклов: {len(self.full_cycle_events)}")
        successful_playback = sum(1 for e in self.full_cycle_events if e.playback_success)
        successful_sr = sum(1 for e in self.full_cycle_events if e.recognized_text)
        logger.info(f"✅ Playback OK: {successful_playback}")
        logger.info(f"✅ SR OK: {successful_sr}")
        logger.info(f"❌ Playback FAIL: {len(self.full_cycle_events) - successful_playback}")
        logger.info("")

        for i, event in enumerate(self.full_cycle_events, 1):
            logger.info(f"📝 Цикл #{i} (event_id={event.event_id}):")
            logger.info(f"   Input: {event.input_device}")
            logger.info(f"   Output: {event.output_device}")
            logger.info(f"   SR: {event.recognized_text or 'Нет'} (latency_ms={event.recognize_latency_ms})")
            logger.info(f"   Playback: {'✅' if event.playback_success else '❌'} (latency_ms={event.playback_latency_ms})")
            logger.info(f"   Record: dur_ms={event.duration_ms}, epoch={event.record_epoch}, sr={event.record_sr}")
            logger.info("")

        logger.info("✅ MVP-12: Full Integration - завершено")
        logger.info("")


# -----------------------------------------------------------------------------
# Entrypoint
# -----------------------------------------------------------------------------
def main():
    prototype = FullInputOutputPrototype()

    if not prototype.setup():
        logger.error("❌ Setup провален")
        sys.exit(1)

    try:
        prototype.test_full_integration()
    except KeyboardInterrupt:
        logger.info("")
        logger.info("🛑 Прервано пользователем")
    except Exception as e:
        logger.error(f"❌ Ошибка: {e}")
        import traceback
        logger.error(traceback.format_exc())
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
