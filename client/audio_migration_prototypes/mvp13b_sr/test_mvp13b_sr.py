#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Nexy MVP13b-SR — AVFoundation raw float ring + worker conversion + SpeechRecognition (PTT)

Goal:
- Stable mic capture on macOS (incl. AirPods/Bluetooth) using AVAudioEngine (AVFoundation)
- Avoid PyAudio/PortAudio (so no AUHAL -10851 / PaError -9986 class of issues)
- Use `SpeechRecognition` ONLY after PTT_END by passing finalized PCM16 to `sr.AudioData`

Flow:
Mic (AVFoundation) -> tap (RT thread: memcpy float32 mono records) -> record ring (SPSC)
Worker: reads records -> converts float32@in_sr -> PCM16@16k -> accumulates while PTT held
On PTT_END: drain tail -> create sr.AudioData -> recognize -> speak via AVSpeechSynthesizer

Privacy:
- AVAudioEngine starts ONLY on PTT_BEGIN and stops after recognition completes.

Install:
  pip install pyobjc pynput SpeechRecognition

STT modes:
  - recognize_google (default): no creds, may be rate limited
  - recognize_google_cloud: needs Google creds json (optional)

Run:
  python test_mvp13b_sr.py
Hold Control+N to talk. Release to recognize and speak.
"""

from __future__ import annotations

import ctypes
import os
import threading
import time
import logging
from dataclasses import dataclass
from typing import Optional, Callable, Tuple

import objc  # noqa: F401
from Foundation import NSNotificationCenter  # type: ignore[reportMissingImports, reportAttributeAccessIssue] # noqa: F401
from AVFoundation import (  # type: ignore[reportMissingImports, reportAttributeAccessIssue]
    AVAudioEngine,  # type: ignore[reportAttributeAccessIssue] # noqa: F401
    AVAudioFormat,  # type: ignore[reportAttributeAccessIssue] # noqa: F401
    AVAudioPCMBuffer,  # type: ignore[reportAttributeAccessIssue] # noqa: F401
    AVAudioConverter,  # type: ignore[reportAttributeAccessIssue] # noqa: F401
    AVAudioEngineConfigurationChangeNotification,  # type: ignore[reportAttributeAccessIssue] # noqa: F401
    AVSpeechSynthesizer,  # type: ignore[reportAttributeAccessIssue] # noqa: F401
    AVSpeechUtterance,  # type: ignore[reportAttributeAccessIssue] # noqa: F401
    AVCaptureDevice,  # type: ignore[reportAttributeAccessIssue] # noqa: F401
    AVMediaTypeAudio,  # type: ignore[reportAttributeAccessIssue] # noqa: F401
)

from pynput import keyboard
import speech_recognition as sr


# -----------------------------
# Logging
# -----------------------------
import sys

LOG = logging.getLogger("nexy.mic_sr_mvp13b")
LOG.setLevel(logging.INFO)

LOG.handlers.clear()
_handler = logging.StreamHandler(sys.stdout)
_handler.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))
_handler.setLevel(logging.INFO)
LOG.addHandler(_handler)

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(line_buffering=True)  # type: ignore[attr-defined]
    except Exception:
        pass


# -----------------------------
# Permissions
# -----------------------------
def ensure_microphone_permission(timeout_s: float = 10.0) -> bool:
    """
    Requests Microphone permission if not determined.
    Returns True when authorized.
    """
    status = AVCaptureDevice.authorizationStatusForMediaType_(AVMediaTypeAudio)
    # macOS: 3=authorized, 2=denied, 1=restricted, 0=notDetermined
    if int(status) == 3:
        return True
    if int(status) in (1, 2):
        LOG.error("❌ Microphone permission denied/restricted. System Settings → Privacy & Security → Microphone.")
        return False

    done = threading.Event()
    ok_box = {"ok": False}

    def _cb(granted: bool):
        ok_box["ok"] = bool(granted)
        done.set()

    AVCaptureDevice.requestAccessForMediaType_completionHandler_(AVMediaTypeAudio, _cb)
    done.wait(timeout=timeout_s)

    if not ok_box["ok"]:
        LOG.error("❌ Microphone permission not granted.")
    return bool(ok_box["ok"])


# -----------------------------
# Record-based SPSC Ring Buffer
# -----------------------------
class RecordSPSCRing:
    """
    Single-producer / single-consumer preallocated ring buffer.

    Record format: [u32_le length][payload bytes...]
    Writer never blocks. On overflow -> returns False (drop record).
    """

    def __init__(self, capacity_bytes: int):
        if capacity_bytes < 4096:
            raise ValueError("capacity_bytes too small")
        self._buf = bytearray(int(capacity_bytes))
        self._cap = int(capacity_bytes)
        self._w = 0
        self._r = 0

    def reset(self) -> None:
        self._w = 0
        self._r = 0

    def _used(self) -> int:
        w, r, cap = self._w, self._r, self._cap
        return w - r if w >= r else cap - (r - w)

    def _free(self) -> int:
        # keep one byte free to disambiguate full/empty
        return self._cap - self._used() - 1

    def _write_u32_le(self, value: int) -> None:
        cap = self._cap
        w = self._w
        self._buf[w] = value & 0xFF
        self._buf[(w + 1) % cap] = (value >> 8) & 0xFF
        self._buf[(w + 2) % cap] = (value >> 16) & 0xFF
        self._buf[(w + 3) % cap] = (value >> 24) & 0xFF
        self._w = (w + 4) % cap

    def _write_bytes_from_ptr(self, src_ptr: int, nbytes: int) -> None:
        cap = self._cap
        w = self._w
        first = min(nbytes, cap - w)
        ctypes.memmove((ctypes.c_ubyte * first).from_buffer(self._buf, w), src_ptr, first)
        if nbytes > first:
            rest = nbytes - first
            ctypes.memmove((ctypes.c_ubyte * rest).from_buffer(self._buf, 0), src_ptr + first, rest)
        self._w = (w + nbytes) % cap

    def write_record_from_ptr(self, src_ptr: int, nbytes: int) -> bool:
        if nbytes <= 0:
            return True
        total = 4 + nbytes
        free = self._free()
        if total > free:
            # Диагностика: логируем первую неудачную запись
            if not hasattr(self, '_first_fail_logged'):
                self._first_fail_logged = True
                used = self._used()
                LOG.warning("⚠️ write_record_from_ptr FAILED: nbytes=%s, total=%s, free=%s, used=%s/%s, w=%s, r=%s", 
                           nbytes, total, free, used, self._cap, self._w, self._r)
            return False
        self._write_u32_le(nbytes)
        self._write_bytes_from_ptr(src_ptr, nbytes)
        return True

    def _peek_u32_le(self) -> Optional[int]:
        if self._used() < 4:
            return None
        cap = self._cap
        r = self._r
        b0 = self._buf[r]
        b1 = self._buf[(r + 1) % cap]
        b2 = self._buf[(r + 2) % cap]
        b3 = self._buf[(r + 3) % cap]
        return int(b0 | (b1 << 8) | (b2 << 16) | (b3 << 24))

    def _skip(self, nbytes: int) -> None:
        self._r = (self._r + nbytes) % self._cap

    def _read_into(self, dst: bytearray, nbytes: int) -> None:
        cap = self._cap
        r = self._r
        first = min(nbytes, cap - r)
        dst[0:first] = self._buf[r:r + first]
        if nbytes > first:
            dst[first:nbytes] = self._buf[0:nbytes - first]
        self._r = (r + nbytes) % cap

    def read_record(self, max_payload_bytes: int) -> bytes:
        used = self._used()
        if used < 4:
            return b""
        
        ln = self._peek_u32_le()
        if ln is None:
            return b""
        if ln <= 0:
            self._skip(4)
            return b""
        if used < 4 + ln:
            # Недостаточно данных для полной записи - ждем
            return b""

        self._skip(4)
        n = min(int(ln), int(max_payload_bytes))
        out = bytearray(n)
        self._read_into(out, n)
        if ln > n:
            self._skip(int(ln - n))
        return bytes(out)

    def get_stats(self) -> dict:
        return {
            "used": self._used(),
            "free": self._free(),
            "capacity": self._cap,
            "w": self._w,
            "r": self._r,
        }


# -----------------------------
# Audio input snapshot
# -----------------------------
@dataclass(frozen=True)
class InputSnapshot:
    sample_rate: float
    channels: int
    common_format: int
    interleaved: bool

    @staticmethod
    def from_format(fmt: AVAudioFormat) -> "InputSnapshot":
        return InputSnapshot(
            sample_rate=float(fmt.sampleRate()),
            channels=int(fmt.channelCount()),
            common_format=int(fmt.commonFormat()),
            interleaved=bool(fmt.isInterleaved()),
        )


# -----------------------------
# AVAudioEngine tap -> ring (raw mono float32)
# -----------------------------
class AVFRawFloatStreamer:
    def __init__(self, ring: RecordSPSCRing, max_frames_per_record: int = 2048):
        self._ring = ring
        self._max_frames = int(max_frames_per_record)

        self._engine: Optional[AVAudioEngine] = None
        self._snapshot: Optional[InputSnapshot] = None
        self._obs_token = None

        self._running = False
        self._gen = 0

        self._lock = threading.Lock()
        self._current_gen = 0
        self._current_sr = 48000.0

        self.drop_records = 0
        self.drop_bytes = 0
        self.write_success = 0  # Счетчик успешных записей

    def get_state(self) -> Tuple[int, float]:
        with self._lock:
            return int(self._current_gen), float(self._current_sr)
    
    def reset_ring(self) -> None:
        """Сброс ring buffer (публичный метод для сброса на PTT_BEGIN)"""
        self._ring.reset()

    def start(self) -> None:
        if self._running:
            return
        self._running = True
        self._rebuild("start")

        nc = NSNotificationCenter.defaultCenter()
        self._obs_token = nc.addObserverForName_object_queue_usingBlock_(
            AVAudioEngineConfigurationChangeNotification,
            self._engine,
            None,
            self._on_engine_config_change,
        )
        gen, sr_ = self.get_state()
        LOG.info("✅ Input streamer started (gen=%s sr=%.1f)", gen, sr_)

    def stop(self) -> None:
        if not self._running and self._engine is None:
            return
        self._running = False
        try:
            if self._engine is not None:
                inp = self._engine.inputNode()
                inp.removeTapOnBus_(0)
                self._engine.stop()
        except Exception:
            pass

        try:
            if self._obs_token is not None:
                NSNotificationCenter.defaultCenter().removeObserver_(self._obs_token)
        except Exception:
            pass

        self._obs_token = None
        self._engine = None
        self._snapshot = None
        LOG.info("🛑 Input streamer stopped")

    def _on_engine_config_change(self, _notification) -> None:
        if not self._running:
            return
        self._rebuild("engine_config_change")

    def _rebuild(self, reason: str) -> None:
        self._gen += 1
        gen_now = self._gen
        self._ring.reset()

        try:
            if self._engine is not None:
                inp = self._engine.inputNode()
                inp.removeTapOnBus_(0)
                self._engine.stop()
        except Exception:
            pass

        self._engine = AVAudioEngine.alloc().init()
        inp = self._engine.inputNode()  # type: ignore[union-attr]
        in_fmt = inp.inputFormatForBus_(0)
        snap = InputSnapshot.from_format(in_fmt)
        self._snapshot = snap

        with self._lock:
            self._current_gen = gen_now
            self._current_sr = snap.sample_rate

        bufsize = 1024
        inp.installTapOnBus_bufferSize_format_block_(0, bufsize, in_fmt, self._make_tap(gen_now))

        ok = True
        try:
            ok = bool(self._engine.startAndReturnError_(None))  # type: ignore[union-attr]
        except Exception:
            ok = False

        if not ok:
            LOG.error("❌ AVAudioEngine start failed (reason=%s gen=%s)", reason, gen_now)
        else:
            LOG.info(
                "🔄 Rebuilt input: reason=%s gen=%s sr=%.1f ch=%s fmt=%s interleaved=%s",
                reason, gen_now, snap.sample_rate, snap.channels, snap.common_format, snap.interleaved
            )

    def _make_tap(self, gen_at_install: int):
        tap_call_count = [0]  # Используем список для мутабельного счетчика в closure
        
        def tap_block(in_buf, _when):
            tap_call_count[0] += 1
            
            # Диагностика: логируем первый вызов tap_block
            if tap_call_count[0] == 1:
                LOG.info("🔵 tap_block called for first time: running=%s, gen_at_install=%s, current_gen=%s", 
                        self._running, gen_at_install, self._gen)
            
            if not self._running or gen_at_install != self._gen:
                if tap_call_count[0] <= 3:  # Логируем первые 3 пропуска
                    LOG.warning("⚠️ tap_block skipped: running=%s, gen_match=%s (install=%s, current=%s)", 
                               self._running, gen_at_install == self._gen, gen_at_install, self._gen)
                return

            # drift check (best-effort)
            try:
                if self._engine is not None:
                    cur_fmt = self._engine.inputNode().inputFormatForBus_(0)
                    cur_snap = InputSnapshot.from_format(cur_fmt)
                    if self._snapshot is not None and cur_snap != self._snapshot:
                        self._rebuild("input_format_drift")
                        return
            except Exception:
                pass

            try:
                frames = int(in_buf.frameLength())
                if frames <= 0:
                    if tap_call_count[0] <= 3:
                        LOG.warning("⚠️ tap_block: frames=%s (skipping)", frames)
                    return
                frames = min(frames, self._max_frames)

                fch = in_buf.floatChannelData()
                if fch is None:
                    self.drop_records += 1
                    if tap_call_count[0] <= 3:
                        LOG.warning("⚠️ tap_block: floatChannelData() is None")
                    return

                src_ptr = int(fch[0])   # mono float32
                nbytes = frames * 4     # float32 bytes

                # Диагностика: логируем первую попытку записи
                if tap_call_count[0] == 1:
                    stats = self._ring.get_stats()
                    LOG.info("🔵 First write attempt: nbytes=%s, ring_free=%s, ring_used=%s/%s, w=%s, r=%s", 
                            nbytes, stats['free'], stats['used'], stats['capacity'], stats['w'], stats['r'])

                if self._ring.write_record_from_ptr(src_ptr, nbytes):
                    self.write_success += 1
                    if self.write_success == 1:
                        LOG.info("✅ First successful write: nbytes=%s", nbytes)
                else:
                    self.drop_records += 1
                    self.drop_bytes += nbytes
                    # Диагностика: логируем первую неудачную запись и периодически
                    stats = self._ring.get_stats()
                    if self.drop_records == 1 or self.drop_records % 50 == 0:
                        LOG.warning("⚠️ Ring buffer write failed: drops=%s, writes=%s, nbytes=%s, used=%s/%s (%.1f%%), free=%s, w=%s, r=%s", 
                                   self.drop_records, self.write_success, nbytes, stats['used'], stats['capacity'], 
                                   100.0 * stats['used'] / stats['capacity'] if stats['capacity'] > 0 else 0.0, 
                                   stats['free'], stats['w'], stats['r'])
            except Exception as e:
                self.drop_records += 1
                if tap_call_count[0] <= 3:
                    LOG.error("❌ tap_block exception: %s", e, exc_info=True)

        return tap_block


# -----------------------------
# Worker converter: float32 mono @in_sr -> PCM16 mono @16k
# -----------------------------
class FloatToPCM16Converter:
    def __init__(self, target_sr: int = 16000):
        self._target_sr = int(target_sr)
        self._in_sr: Optional[float] = None
        self._conv: Optional[AVAudioConverter] = None
        self._in_fmt: Optional[AVAudioFormat] = None
        self._out_fmt: Optional[AVAudioFormat] = None
        self._out_buf: Optional[AVAudioPCMBuffer] = None

    def ensure(self, in_sr: float) -> None:
        if self._conv is None or self._in_sr is None or abs(float(in_sr) - float(self._in_sr)) > 1e-3:
            self._build(float(in_sr))

    def _build(self, in_sr: float) -> None:
        in_settings = {
            "AVFormatIDKey": 1819304813,  # kAudioFormatLinearPCM
            "AVSampleRateKey": float(in_sr),
            "AVNumberOfChannelsKey": 1,
            "AVLinearPCMBitDepthKey": 32,
            "AVLinearPCMIsFloatKey": True,
            "AVLinearPCMIsBigEndianKey": False,
            "AVLinearPCMIsNonInterleaved": False,
        }
        self._in_fmt = AVAudioFormat.alloc().initWithSettings_(in_settings)

        out_settings = {
            "AVFormatIDKey": 1819304813,  # kAudioFormatLinearPCM
            "AVSampleRateKey": float(self._target_sr),
            "AVNumberOfChannelsKey": 1,
            "AVLinearPCMBitDepthKey": 16,
            "AVLinearPCMIsFloatKey": False,
            "AVLinearPCMIsBigEndianKey": False,
            "AVLinearPCMIsNonInterleaved": False,
        }
        self._out_fmt = AVAudioFormat.alloc().initWithSettings_(out_settings)

        self._conv = AVAudioConverter.alloc().initFromFormat_toFormat_(self._in_fmt, self._out_fmt)
        self._out_buf = AVAudioPCMBuffer.alloc().initWithPCMFormat_frameCapacity_(self._out_fmt, 4096)
        self._in_sr = float(in_sr)

        LOG.info("🔧 Worker converter rebuilt: in_sr=%.1f -> out_sr=%s", self._in_sr, self._target_sr)

    def convert_float_bytes(self, float_bytes: bytes) -> bytes:
        if not float_bytes or self._conv is None or self._in_fmt is None or self._out_buf is None:
            return b""

        frames = len(float_bytes) // 4
        if frames <= 0:
            return b""

        in_buf = AVAudioPCMBuffer.alloc().initWithPCMFormat_frameCapacity_(self._in_fmt, frames)
        in_buf.setFrameLength_(frames)

        fch = in_buf.floatChannelData()
        if fch is None:
            return b""

        dst_ptr = int(fch[0])
        src = (ctypes.c_char * (frames * 4)).from_buffer_copy(float_bytes)
        ctypes.memmove(dst_ptr, ctypes.addressof(src), frames * 4)

        out_buf = self._out_buf
        out_buf.setFrameLength_(0)

        provided = {"done": False}

        def input_block(_in_packets, out_status_ptr):
            if provided["done"]:
                out_status_ptr[0] = 1  # NoDataNow
                return None
            provided["done"] = True
            out_status_ptr[0] = 0  # HaveData
            return in_buf

        ok = self._conv.convertToBuffer_error_withInputFromBlock_(out_buf, None, input_block)
        if not ok:
            return b""

        out_frames = int(out_buf.frameLength())
        if out_frames <= 0:
            return b""

        ich = out_buf.int16ChannelData()
        if ich is None:
            return b""

        pcm_ptr = int(ich[0])
        nbytes = out_frames * 2
        return ctypes.string_at(pcm_ptr, nbytes)


# -----------------------------
# Playback (reliable routing)
# -----------------------------
class TextPlayback:
    def __init__(self, enabled: bool = True):
        self.enabled = bool(enabled)
        self._synth = AVSpeechSynthesizer.alloc().init()

    def speak(self, text: str) -> None:
        if not self.enabled:
            return
        try:
            utt = AVSpeechUtterance.speechUtteranceWithString_(text)
            self._synth.speakUtterance_(utt)
        except Exception:
            pass


# -----------------------------
# PTT Gate
# -----------------------------
class PTTGate:
    def __init__(self):
        self._lock = threading.Lock()
        self._open = False
        self._epoch = 0
        self._end_requested = False

    def begin(self) -> int:
        with self._lock:
            self._epoch += 1
            self._open = True
            self._end_requested = False
            return self._epoch

    def request_end(self) -> int:
        with self._lock:
            self._end_requested = True
            return self._epoch

    def close(self) -> None:
        with self._lock:
            self._open = False
            self._end_requested = False

    def snapshot(self) -> Tuple[bool, int, bool]:
        with self._lock:
            return bool(self._open), int(self._epoch), bool(self._end_requested)


# -----------------------------
# SpeechRecognition Controller (utterance recognition)
# -----------------------------
class SpeechRecognitionController:
    """
    Uses SpeechRecognition on finalized PCM audio (AudioData).

    stt_mode:
      - "google" -> recognize_google
      - "google_cloud" -> recognize_google_cloud (requires creds json)
    """

    def __init__(
        self,
        read_float_record: Callable[[int], bytes],
        get_input_state: Callable[[], Tuple[int, float]],
        ptt_gate: PTTGate,
        playback: TextPlayback,
        language_code: str = "ru-RU",
        target_sr: int = 16000,
        chunk_ms: int = 100,
        drain_ms: int = 250,
        max_utterance_s: float = 12.0,
        stt_mode: str = "google",
        credentials_json_path: Optional[str] = None,
        input_streamer: Optional[AVFRawFloatStreamer] = None,
    ):
        self._read_rec = read_float_record
        self._get_state = get_input_state
        self._gate = ptt_gate
        self._playback = playback
        self._input_streamer = input_streamer

        self._lang = str(language_code)
        self._target_sr = int(target_sr)
        self._chunk_ms = int(chunk_ms)
        self._drain_ms = int(drain_ms)
        self._max_utt_s = float(max_utterance_s)

        self._mode = str(stt_mode)
        self._credentials_json_path = credentials_json_path

        self._stop = threading.Event()
        self._thread: Optional[threading.Thread] = None

        self._converter = FloatToPCM16Converter(target_sr=self._target_sr)
        self._recognizer = sr.Recognizer()

        # metrics
        self.utterances = 0
        self.convert_fail = 0
        self.total_pcm_bytes = 0
        self.last_text: str = ""

    def start(self) -> None:
        if self._thread and self._thread.is_alive():
            return
        self._stop.clear()
        self._thread = threading.Thread(target=self._main_loop, name="sr_controller", daemon=True)
        self._thread.start()
        LOG.info("✅ SpeechRecognitionController started (mode=%s)", self._mode)

    def stop(self) -> None:
        self._stop.set()
        if self._thread:
            self._thread.join(timeout=2.0)
        LOG.info("🛑 SpeechRecognitionController stopped")

    def _main_loop(self) -> None:
        while not self._stop.is_set():
            gate_open, epoch, _end_req = self._gate.snapshot()
            if not gate_open:
                time.sleep(0.01)
                continue

            self.utterances += 1
            utt_id = self.utterances
            LOG.info("🎙️ PTT_BEGIN (utt=%s epoch=%s)", utt_id, epoch)

            # ПРАВКА №3: Ждем, пока данные начнут писаться в ring buffer
            # Проверяем write_success (успешные записи), а не drop_records (переполнение)
            wait_start = time.time()
            max_wait = 0.5  # Максимум 500ms ожидания
            data_started = False
            while time.time() - wait_start < max_wait:
                if self._input_streamer is not None and self._input_streamer.write_success > 0:
                    data_started = True
                    break
                time.sleep(0.01)
            
            elapsed_wait = time.time() - wait_start
            if elapsed_wait > 0.01:
                if data_started:
                    LOG.info("⏳ Waited %.2fs for mic data to start writing (writes=%s)", 
                            elapsed_wait, self._input_streamer.write_success if self._input_streamer else 0)
                else:
                    LOG.warning("⚠️ No mic data detected after %.2fs wait (writes=0)", elapsed_wait)

            text = self._capture_and_recognize_one_utterance(ptt_epoch=epoch)
            self.last_text = text or ""

            if text:
                LOG.info("✅ STT: %s", text)
                self._playback.speak(text)
            else:
                LOG.warning("⚠️ STT: empty / failed")

            self._gate.close()
            LOG.info("🛑 PTT_END (utt=%s epoch=%s)", utt_id, epoch)

            # Stop mic AFTER recognition finishes (privacy + avoid always-on)
            if self._input_streamer is not None:
                self._input_streamer.stop()
                LOG.info("🎤 Microphone deactivated")

    def _capture_and_recognize_one_utterance(self, ptt_epoch: int) -> str:
        max_float_payload = 16384  # read bigger bursts, then pacing is controlled by PTT

        pcm_accum = bytearray()
        last_gen = None

        drain_deadline = None
        start_ts = time.time()

        while not self._stop.is_set():
            gate_open, cur_epoch, end_req = self._gate.snapshot()
            if not gate_open or cur_epoch != ptt_epoch:
                break

            if time.time() - start_ts > self._max_utt_s:
                LOG.warning("⏱️ Max utterance exceeded (%.1fs). Forcing end.", self._max_utt_s)
                break

            gen, in_sr = self._get_state()
            if last_gen is None:
                last_gen = gen
            elif gen != last_gen:
                pcm_accum.clear()
                last_gen = gen
                LOG.info("🔄 Input gen changed -> flush pcm_accum (gen=%s)", gen)

            self._converter.ensure(in_sr)

            # ПРАВКА №1: Пакетное чтение (batch drain) для предотвращения переполнения ring buffer
            # Читаем много records за один тик, чтобы consumer не отставал от producer
            raw_batch = bytearray()
            batch_limit = 256 * 1024  # 256KB raw float32 за тик
            records_read = 0
            
            while len(raw_batch) < batch_limit:
                one = self._read_rec(max_float_payload)
                if not one:
                    break
                raw_batch.extend(one)
                records_read += 1
            
            raw = bytes(raw_batch)
            
            # Диагностика: логируем статистику ring buffer при отсутствии данных
            if not raw and len(pcm_accum) == 0:
                elapsed = time.time() - start_ts
                if elapsed > 0.5 and int(elapsed * 2) % 1 == 0:  # Раз в 0.5 секунды
                    if self._input_streamer is not None:
                        drops = self._input_streamer.drop_records
                        writes = self._input_streamer.write_success
                        if drops > 0 or writes > 0:
                            LOG.warning("⚠️ No data read: drops=%s, writes=%s (elapsed=%.2fs) - ring buffer may be full or read_record failing", 
                                       drops, writes, elapsed)
                        elif elapsed > 1.0:
                            LOG.warning("⚠️ No mic data after %.2fs (drops=0, writes=0, mic may not be writing)", elapsed)
            
            if raw:
                # Логируем первое чтение
                if len(pcm_accum) == 0:
                    LOG.info("📥 First batch read: %d bytes (%d records) from ring", len(raw), records_read)
                pcm = self._converter.convert_float_bytes(raw)
                if pcm:
                    pcm_accum.extend(pcm)
                    # Логируем прогресс каждые ~0.5 секунды
                    current_sec = len(pcm_accum) / (self._target_sr * 2)
                    prev_sec = (len(pcm_accum) - len(pcm)) / (self._target_sr * 2)
                    if int(current_sec * 2) != int(prev_sec * 2):
                        LOG.info("📈 Accumulating: %d bytes (%.2fs)", len(pcm_accum), current_sec)
                else:
                    self.convert_fail += 1
                    LOG.warning("⚠️ Conversion failed for %d bytes", len(raw))
            else:
                # Логируем отсутствие данных только в начале
                if len(pcm_accum) == 0:
                    elapsed = time.time() - start_ts
                    if 0.2 < elapsed < 1.0:  # После небольшой задержки, но не слишком часто
                        LOG.info("📭 No data from ring (elapsed=%.2fs, waiting for mic data...)", elapsed)
                time.sleep(0.001)

            if end_req and drain_deadline is None:
                drain_deadline = time.time() + (self._drain_ms / 1000.0)
                LOG.info("⏳ PTT_END requested -> draining for %sms (accumulated: %d bytes, %.2fs)", 
                        self._drain_ms, len(pcm_accum), len(pcm_accum) / (self._target_sr * 2))

            # Keep memory bounded: if huge, keep last ~8s
            max_keep = int(self._target_sr * 2 * 8)
            if len(pcm_accum) > max_keep:
                pcm_accum = pcm_accum[-max_keep:]

            if drain_deadline is not None and time.time() >= drain_deadline:
                break

        self.total_pcm_bytes += len(pcm_accum)

        # Minimum 0.5s audio for STT
        min_bytes = int(0.5 * self._target_sr) * 2
        accumulated_sec = len(pcm_accum) / (self._target_sr * 2)
        LOG.info("📊 Final audio: %d bytes (%.2fs, min=%.2fs)", len(pcm_accum), accumulated_sec, 0.5)
        
        if len(pcm_accum) < min_bytes:
            LOG.warning("⚠️ Insufficient audio: %d bytes (min=%d, %.2fs)", len(pcm_accum), min_bytes, accumulated_sec)
            return ""

        audio = sr.AudioData(bytes(pcm_accum), self._target_sr, 2)

        try:
            if self._mode == "google_cloud":
                creds_json = None
                path = self._credentials_json_path or os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
                if path and os.path.exists(path):
                    with open(path, "r", encoding="utf-8") as f:
                        creds_json = f.read()

                return self._recognizer.recognize_google_cloud(  # type: ignore[attr-defined]
                    audio_data=audio,
                    language=self._lang,
                    credentials_json=creds_json,
                ).strip()

            return self._recognizer.recognize_google(audio, language=self._lang).strip()  # type: ignore[attr-defined]

        except sr.UnknownValueError:
            return ""
        except sr.RequestError as e:
            LOG.error("❌ SpeechRecognition request error: %s", e)
            return ""
        except TypeError as e:
            LOG.error("❌ SpeechRecognition API mismatch: %s", e)
            return ""
        except Exception as e:
            LOG.error("❌ STT unexpected error: %s", e)
            return ""


# -----------------------------
# Keyboard PTT: Control+N
# -----------------------------
class ControlNPTT:
    def __init__(self, gate: PTTGate, input_streamer: Optional[AVFRawFloatStreamer] = None):
        self._gate = gate
        self._input_streamer = input_streamer
        self._ctrl_down = False
        self._n_down = False
        self._ptt_active = False
        self._listener: Optional[keyboard.Listener] = None

    def start(self) -> None:
        self._listener = keyboard.Listener(on_press=self._on_press, on_release=self._on_release)
        self._listener.start()
        LOG.info("⌨️ PTT listener started (Control+N)")

    def stop(self) -> None:
        try:
            if self._listener:
                self._listener.stop()
        except Exception:
            pass
        LOG.info("⌨️ PTT listener stopped")

    def _on_press(self, key):
        if key in (keyboard.Key.ctrl, keyboard.Key.ctrl_l, keyboard.Key.ctrl_r):
            self._ctrl_down = True
        if key == keyboard.KeyCode.from_char("n") or key == keyboard.KeyCode.from_char("N"):
            self._n_down = True

        if self._ctrl_down and self._n_down and not self._ptt_active:
            self._ptt_active = True
            # Start mic only on PTT_BEGIN
            if self._input_streamer is not None:
                # ПРАВКА №2: Сбрасываем ring buffer ДО start() (чтобы избежать race condition)
                try:
                    self._input_streamer.reset_ring()
                except Exception:
                    pass
                self._input_streamer.start()
                LOG.info("🎤 Microphone activated")
            epoch = self._gate.begin()
            LOG.info("⌨️ Control+N pressed -> PTT_BEGIN (epoch=%s)", epoch)

    def _on_release(self, key):
        if key in (keyboard.Key.ctrl, keyboard.Key.ctrl_l, keyboard.Key.ctrl_r):
            self._ctrl_down = False
        if key == keyboard.KeyCode.from_char("n") or key == keyboard.KeyCode.from_char("N"):
            self._n_down = False

        if self._ptt_active and (not self._ctrl_down or not self._n_down):
            self._ptt_active = False
            epoch = self._gate.request_end()
            LOG.info("⌨️ Control+N released -> PTT_END requested (epoch=%s)", epoch)
            # mic stops after recognition completes


# -----------------------------
# App wrapper
# -----------------------------
class NexyMVP13bSR:
    def __init__(
        self,
        language_code: str = "ru-RU",
        playback_enabled: bool = True,
        stt_mode: str = "google",
        credentials_json_path: Optional[str] = None,
    ):
        self.ring = RecordSPSCRing(capacity_bytes=4 * 1024 * 1024)  # 4MB
        self.input_streamer = AVFRawFloatStreamer(ring=self.ring, max_frames_per_record=2048)

        self.playback = TextPlayback(enabled=playback_enabled)
        self.gate = PTTGate()

        self.stt_ctl = SpeechRecognitionController(
            read_float_record=lambda maxb: self.ring.read_record(maxb),
            get_input_state=lambda: self.input_streamer.get_state(),
            ptt_gate=self.gate,
            playback=self.playback,
            language_code=language_code,
            target_sr=16000,
            chunk_ms=100,
            drain_ms=250,
            max_utterance_s=12.0,
            stt_mode=stt_mode,
            credentials_json_path=credentials_json_path,
            input_streamer=self.input_streamer,
        )

        self.ptt = ControlNPTT(self.gate, input_streamer=self.input_streamer)

        self._metrics_stop = threading.Event()
        self._metrics_thread: Optional[threading.Thread] = None

    def start(self) -> None:
        if not ensure_microphone_permission():
            return

        # Do NOT start mic here. Only on PTT.
        self.stt_ctl.start()
        self.ptt.start()

        self._metrics_stop.clear()
        self._metrics_thread = threading.Thread(target=self._metrics_loop, daemon=True)
        self._metrics_thread.start()

        LOG.info("✅ Nexy MVP13b-SR started. Hold Control+N to talk.")
        print("\n" + "=" * 60)
        print("🎤 MVP13b-SR ready")
        print("📌 Hold Control+N to record")
        print("📌 Release Control+N to recognize")
        print("📌 Press Enter to stop")
        print("=" * 60 + "\n")

    def stop(self) -> None:
        self.ptt.stop()
        self.stt_ctl.stop()
        self.input_streamer.stop()
        self._metrics_stop.set()
        LOG.info("🛑 Nexy MVP13b-SR stopped")

    def _metrics_loop(self) -> None:
        while not self._metrics_stop.is_set():
            time.sleep(5.0)
            gen, sr_ = self.input_streamer.get_state()
            gate_open, epoch, end_req = self.gate.snapshot()
            last_text_preview = (self.stt_ctl.last_text[:40] + "…") if len(self.stt_ctl.last_text) > 40 else self.stt_ctl.last_text
            # ПРАВКА №4: Добавляем writes и статистику ring buffer
            stats = self.ring.get_stats()
            ring_used_pct = 100.0 * stats["used"] / stats["capacity"] if stats["capacity"] > 0 else 0.0
            LOG.info(
                "📊 metrics gen=%s in_sr=%.1f gate=%s epoch=%s end_req=%s "
                "writes=%s drops=%s drop_kb=%.1f ring_used=%s/%s (%.1f%%) "
                "utt=%s conv_fail=%s last_text=%s",
                gen, sr_, gate_open, epoch, end_req,
                self.input_streamer.write_success,
                self.input_streamer.drop_records,
                self.input_streamer.drop_bytes / 1024.0,
                stats["used"], stats["capacity"], ring_used_pct,
                self.stt_ctl.utterances,
                self.stt_ctl.convert_fail,
                last_text_preview,
            )


def main():
    LOG.info("=== Nexy MVP13b-SR (SpeechRecognition + AVFoundation + PTT Control+N) ===")

    app = NexyMVP13bSR(
        language_code="ru-RU",
        playback_enabled=True,
        stt_mode="google",  # change to "google_cloud" if you have creds
        credentials_json_path=None,
    )

    app.start()
    LOG.info("Press Enter to stop...")
    try:
        input()
    except KeyboardInterrupt:
        pass
    app.stop()
    LOG.info("=== stopped ===")


if __name__ == "__main__":
    main()
