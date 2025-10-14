# default_audio_runner.py
import time
import queue
import numpy as np
import sounddevice as sd

# --- параметры ---
IN_SR = 16000         # удобно для ASR и HFP; можно 24000/48000 для встроенного
OUT_SR = 48000
RMS_WINDOW_SEC = 0.3  # окно оценки громкости
RMS_MIN = 1e-4        # минимальный RMS, ниже считаем «тишиной»
CHECK_EVERY_SEC = 1.0 # период проверки

# --- буферы и коллбеки ---
_in_q = queue.Queue(maxsize=8)

def _in_cb(indata, frames, time_info, status):
    if status: print("[input] status:", status)
    try:
        _in_q.put_nowait(indata.copy())
    except queue.Full:
        pass

def _out_cb(outdata, frames, time_info, status):
    if status: print("[output] status:", status)
    # простая заглушка тишиной — ваш TTS/плеер подставит сюда свой буфер
    outdata.fill(0)

# --- утилиты ---
def rms_of(buf: np.ndarray) -> float:
    if buf.size == 0: return 0.0
    x = buf.astype(np.float32)
    return float(np.sqrt(np.mean(x**2)))

def collect_rms(window_sec=RMS_WINDOW_SEC, sr=IN_SR) -> float:
    need = int(window_sec * sr)
    acc = []
    got = 0
    deadline = time.time() + window_sec + 1.0
    while got < need and time.time() < deadline:
        try:
            chunk = _in_q.get(timeout=0.2)
            acc.append(chunk)
            got += len(chunk)
        except queue.Empty:
            pass
    if not acc: return 0.0
    data = np.concatenate(acc, axis=0)
    # mono, int16 по умолчанию — конвертируем безопасно
    if data.ndim == 2 and data.shape[1] > 1:
        data = data.mean(axis=1, dtype=np.float32)  # усредним каналы
    return rms_of(data)

# --- основной цикл ---
def run_default_io():
    print("→ Открываем DEF input/output (device=None)")
    in_stream = sd.InputStream(
        device=None,            # Default Input
        channels=1,             # mono
        samplerate=IN_SR,
        dtype="int16",
        callback=_in_cb,
    )
    out_stream = sd.OutputStream(
        device=None,            # Default Output
        channels=1,
        samplerate=OUT_SR,
        dtype="int16",
        callback=_out_cb,
    )

    def _open():
        in_stream.start()
        out_stream.start()
        print("✅ Потоки запущены на системных дефолтах")

    def _close():
        try: in_stream.stop()
        except: pass
        try: out_stream.stop()
        except: pass

    _open()

    try:
        while True:
            time.sleep(CHECK_EVERY_SEC)
            # проверяем «жив ли» микрофон
            r = collect_rms()
            print(f"[health] RMS={r:.6f}")
            # если явная тишина несколько раз подряд — переоткроем (без смены устройств)
            if r < RMS_MIN:
                print("⚠️  Тишина/сбой? Переоткрываем дефолтные потоки…")
                _close()
                time.sleep(0.2)
                _open()
    except KeyboardInterrupt:
        pass
    finally:
        _close()
        print("⏹ Остановлено.")

if __name__ == "__main__":
    run_default_io()
