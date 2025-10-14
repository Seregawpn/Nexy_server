"""
Боевой слой автопереключения аудио устройств
Решает проблему флаппинга HFP⇄A2DP для AirPods
"""

import subprocess
import shlex
import time
import threading
import sounddevice as sd
import numpy as np
import re
import logging

logger = logging.getLogger(__name__)

# ---- настройки/паттерны ----
POLL_SEC = 1.0
DEBOUNCE_MS = 1000
HEALTH_SEC = 0.30
RMS_MIN = 1e-3
FAILS_TO_QUARANTINE = 2
QUARANTINE_SEC = 45

AIRPODS_PATTERNS = [re.compile(r"airpods", re.I)]
HEADSET_PATTERNS = [re.compile(r"headset|usb audio|jabra|logitech|bose", re.I)]
BUILTIN_IN_NAMES = [re.compile(r"mac.*microphone|built.*mic", re.I)]
BUILTIN_OUT_NAMES = [re.compile(r"mac.*speaker|built.*output", re.I)]

def _run(cmd: str) -> str:
    """Выполняет команду и возвращает результат"""
    try:
        return subprocess.check_output(shlex.split(cmd), text=True).strip()
    except subprocess.CalledProcessError as e:
        logger.error(f"❌ Команда не выполнена: {cmd} - {e}")
        return ""
    except Exception as e:
        logger.error(f"❌ Ошибка выполнения команды: {e}")
        return ""

def list_inputs():
    """Получает список input устройств"""
    result = _run("SwitchAudioSource -a -t input")
    return [line.strip() for line in result.splitlines() if line.strip()]

def list_outputs():
    """Получает список output устройств"""
    result = _run("SwitchAudioSource -a -t output")
    return [line.strip() for line in result.splitlines() if line.strip()]

def cur_input():
    """Получает текущее input устройство"""
    return _run("SwitchAudioSource -c -t input")

def cur_output():
    """Получает текущее output устройство"""
    return _run("SwitchAudioSource -c -t output")

def set_inout(name: str):
    """Устанавливает input и output на одно устройство (сцепка)"""
    logger.info(f"🔗 Сцепка IN+OUT на: {name}")
    _run(f'SwitchAudioSource -t input  -s "{name}"')
    time.sleep(0.1)  # Небольшая задержка для стабилизации
    _run(f'SwitchAudioSource -t output -s "{name}"')

def set_input(name: str):
    """Устанавливает input устройство"""
    _run(f'SwitchAudioSource -t input  -s "{name}"')

def set_output(name: str):
    """Устанавливает output устройство"""
    _run(f'SwitchAudioSource -t output -s "{name}"')

def find_by_patterns(cands, pats):
    """Находит устройство по паттернам"""
    for s in cands:
        for p in pats:
            if p.search(s):
                return s
    return None

def query_input_idx(name_substr: str):
    """Находит индекс устройства в PortAudio"""
    s = name_substr.lower()
    for i, d in enumerate(sd.query_devices()):
        if d.get("max_input_channels", 0) > 0 and s in d["name"].lower():
            rate = int(d["default_samplerate"] or 16000)
            return i, rate
    return None, None

def health_rms(idx: int, rate: int) -> float:
    """Проверяет здоровье устройства через RMS"""
    try:
        sd.default.device = (idx, None)
        sd.default.channels = 1
        sd.default.dtype = "int16"
        sd.default.samplerate = rate
        frames = int(rate * HEALTH_SEC)
        
        data = sd.rec(frames, samplerate=rate, channels=1, dtype="int16")
        sd.wait()
        
        x = data.astype(np.float32)
        return float(np.sqrt(np.mean(x**2))) if x.size else 0.0
    except Exception as e:
        logger.error(f"❌ Ошибка health check: {e}")
        return 0.0

class BattleReadyAutoSwitch:
    """Боевой класс автопереключения аудио устройств"""
    
    def __init__(self, logger_func=None):
        self.log = logger_func or logger.info
        self._stop = threading.Event()
        self._snap = ([], [], "", "")
        self._last_ms = 0
        self._fails = 0
        self._quarantine_until = 0
        self._running = False
        self._thread = None
        
        self.log("🚀 BattleReadyAutoSwitch инициализирован")

    def start(self):
        """Запускает фоновый поток"""
        if self._running:
            self.log("⚠️  AutoSwitch уже запущен")
            return
        
        self._running = True
        self._thread = threading.Thread(target=self._loop, daemon=True)
        self._thread.start()
        self.log("✅ BattleReadyAutoSwitch запущен")

    def stop(self):
        """Останавливает фоновый поток"""
        if not self._running:
            self.log("⚠️  AutoSwitch уже остановлен")
            return
        
        self._running = False
        self._stop.set()
        if self._thread:
            self._thread.join(timeout=2)
        self.log("🛑 BattleReadyAutoSwitch остановлен")

    def _snapshot(self):
        """Получает снимок текущего состояния"""
        try:
            return (list_inputs(), list_outputs(), cur_input(), cur_output())
        except Exception as e:
            self.log(f"❌ Ошибка снимка: {e}")
            return ([], [], "", "")

    def _changed(self, a, b):
        """Проверяет, изменилось ли состояние"""
        return a[0] != b[0] or a[1] != b[1] or a[2] != b[2] or a[3] != b[3]

    def _choose_builtin(self):
        """Выбирает встроенные устройства"""
        ins, outs, *_ = self._snapshot()
        bi = find_by_patterns(ins, BUILTIN_IN_NAMES) or (ins[0] if ins else None)
        bo = find_by_patterns(outs, BUILTIN_OUT_NAMES) or (outs[0] if outs else None)
        return bi, bo

    def _choose_headset(self):
        """Выбирает гарнитуру по приоритету"""
        ins, outs, *_ = self._snapshot()
        
        # Ищем AirPods
        ap_in = find_by_patterns(ins, AIRPODS_PATTERNS)
        ap_out = find_by_patterns(outs, AIRPODS_PATTERNS)
        if ap_in and ap_out:
            return ap_in
        
        # Ищем другие гарнитуры
        hs_in = find_by_patterns(ins, HEADSET_PATTERNS)
        hs_out = find_by_patterns(outs, HEADSET_PATTERNS)
        if hs_in and hs_out:
            return hs_in
        
        return None

    def _activate_coupled(self, name: str) -> bool:
        """Активирует устройство сцепкой с проверкой здоровья"""
        for delay in (0.0, 0.3, 0.8):
            time.sleep(delay)
            try:
                set_inout(name)
            except Exception as e:
                self.log(f"❌ set_inout failed: {e}")
                continue
            
            idx, rate = query_input_idx(name)
            if idx is None:
                continue
            
            rms = health_rms(idx, rate)
            self.log(f"🔍 {name} health rms={rms:.6f} rate={rate}")
            
            if rms >= RMS_MIN:
                self._fails = 0
                self.log(f"✅ {name} активирован успешно")
                return True
        
        self._fails += 1
        self.log(f"❌ {name} не активирован, счетчик провалов: {self._fails}")
        return False

    def _fallback_builtin(self):
        """Переключается на встроенные устройства"""
        bi, bo = self._choose_builtin()
        if bi:
            try:
                set_input(bi)
            except:
                pass
        if bo:
            try:
                set_output(bo)
            except:
                pass
        self.log(f"🔄 Fallback builtin: in={bi} out={bo}")

    def _apply_policy(self):
        """Применяет политику автопереключения"""
        now = time.time()
        if now < self._quarantine_until:
            remaining = int(self._quarantine_until - now)
            self.log(f"🚫 В карантине, осталось {remaining}s")
            self._fallback_builtin()
            return

        target = self._choose_headset()
        if target and self._activate_coupled(target):
            self.log(f"✅ Активна гарнитура: {target}")
            return

        if self._fails >= FAILS_TO_QUARANTINE:
            self._quarantine_until = now + QUARANTINE_SEC
            self.log(f"🚫 Карантин {QUARANTINE_SEC}s после {self._fails} провалов")

        self._fallback_builtin()

    def _loop(self):
        """Основной цикл автопереключения"""
        self.log("🔄 Запуск основного цикла")
        self._snap = self._snapshot()
        
        while not self._stop.is_set():
            time.sleep(POLL_SEC)
            snap = self._snapshot()
            
            if self._changed(snap, self._snap):
                ms = time.time() * 1000
                if ms - self._last_ms < DEBOUNCE_MS:
                    self._snap = snap
                    continue
                
                self._last_ms = ms
                self.log("🔄 Обнаружены изменения в устройствах")
                self._apply_policy()
                self._snap = self._snapshot()

    def get_status(self):
        """Получает текущий статус"""
        return {
            'running': self._running,
            'fail_count': self._fails,
            'quarantine_until': self._quarantine_until,
            'in_quarantine': time.time() < self._quarantine_until,
            'current_snapshot': self._snap
        }

    def force_switch(self, device_name: str) -> bool:
        """Принудительно переключает на устройство"""
        self.log(f"🔄 Принудительное переключение на: {device_name}")
        return self._activate_coupled(device_name)

    def reset_quarantine(self):
        """Сбрасывает карантин"""
        self._quarantine_until = 0
        self._fails = 0
        self.log("🔄 Карантин сброшен")

Боевой слой автопереключения аудио устройств
Решает проблему флаппинга HFP⇄A2DP для AirPods
"""

import subprocess
import shlex
import time
import threading
import sounddevice as sd
import numpy as np
import re
import logging

logger = logging.getLogger(__name__)

# ---- настройки/паттерны ----
POLL_SEC = 1.0
DEBOUNCE_MS = 1000
HEALTH_SEC = 0.30
RMS_MIN = 1e-3
FAILS_TO_QUARANTINE = 2
QUARANTINE_SEC = 45

AIRPODS_PATTERNS = [re.compile(r"airpods", re.I)]
HEADSET_PATTERNS = [re.compile(r"headset|usb audio|jabra|logitech|bose", re.I)]
BUILTIN_IN_NAMES = [re.compile(r"mac.*microphone|built.*mic", re.I)]
BUILTIN_OUT_NAMES = [re.compile(r"mac.*speaker|built.*output", re.I)]

def _run(cmd: str) -> str:
    """Выполняет команду и возвращает результат"""
    try:
        return subprocess.check_output(shlex.split(cmd), text=True).strip()
    except subprocess.CalledProcessError as e:
        logger.error(f"❌ Команда не выполнена: {cmd} - {e}")
        return ""
    except Exception as e:
        logger.error(f"❌ Ошибка выполнения команды: {e}")
        return ""

def list_inputs():
    """Получает список input устройств"""
    result = _run("SwitchAudioSource -a -t input")
    return [line.strip() for line in result.splitlines() if line.strip()]

def list_outputs():
    """Получает список output устройств"""
    result = _run("SwitchAudioSource -a -t output")
    return [line.strip() for line in result.splitlines() if line.strip()]

def cur_input():
    """Получает текущее input устройство"""
    return _run("SwitchAudioSource -c -t input")

def cur_output():
    """Получает текущее output устройство"""
    return _run("SwitchAudioSource -c -t output")

def set_inout(name: str):
    """Устанавливает input и output на одно устройство (сцепка)"""
    logger.info(f"🔗 Сцепка IN+OUT на: {name}")
    _run(f'SwitchAudioSource -t input  -s "{name}"')
    time.sleep(0.1)  # Небольшая задержка для стабилизации
    _run(f'SwitchAudioSource -t output -s "{name}"')

def set_input(name: str):
    """Устанавливает input устройство"""
    _run(f'SwitchAudioSource -t input  -s "{name}"')

def set_output(name: str):
    """Устанавливает output устройство"""
    _run(f'SwitchAudioSource -t output -s "{name}"')

def find_by_patterns(cands, pats):
    """Находит устройство по паттернам"""
    for s in cands:
        for p in pats:
            if p.search(s):
                return s
    return None

def query_input_idx(name_substr: str):
    """Находит индекс устройства в PortAudio"""
    s = name_substr.lower()
    for i, d in enumerate(sd.query_devices()):
        if d.get("max_input_channels", 0) > 0 and s in d["name"].lower():
            rate = int(d["default_samplerate"] or 16000)
            return i, rate
    return None, None

def health_rms(idx: int, rate: int) -> float:
    """Проверяет здоровье устройства через RMS"""
    try:
        sd.default.device = (idx, None)
        sd.default.channels = 1
        sd.default.dtype = "int16"
        sd.default.samplerate = rate
        frames = int(rate * HEALTH_SEC)
        
        data = sd.rec(frames, samplerate=rate, channels=1, dtype="int16")
        sd.wait()
        
        x = data.astype(np.float32)
        return float(np.sqrt(np.mean(x**2))) if x.size else 0.0
    except Exception as e:
        logger.error(f"❌ Ошибка health check: {e}")
        return 0.0

class BattleReadyAutoSwitch:
    """Боевой класс автопереключения аудио устройств"""
    
    def __init__(self, logger_func=None):
        self.log = logger_func or logger.info
        self._stop = threading.Event()
        self._snap = ([], [], "", "")
        self._last_ms = 0
        self._fails = 0
        self._quarantine_until = 0
        self._running = False
        self._thread = None
        
        self.log("🚀 BattleReadyAutoSwitch инициализирован")

    def start(self):
        """Запускает фоновый поток"""
        if self._running:
            self.log("⚠️  AutoSwitch уже запущен")
            return
        
        self._running = True
        self._thread = threading.Thread(target=self._loop, daemon=True)
        self._thread.start()
        self.log("✅ BattleReadyAutoSwitch запущен")

    def stop(self):
        """Останавливает фоновый поток"""
        if not self._running:
            self.log("⚠️  AutoSwitch уже остановлен")
            return
        
        self._running = False
        self._stop.set()
        if self._thread:
            self._thread.join(timeout=2)
        self.log("🛑 BattleReadyAutoSwitch остановлен")

    def _snapshot(self):
        """Получает снимок текущего состояния"""
        try:
            return (list_inputs(), list_outputs(), cur_input(), cur_output())
        except Exception as e:
            self.log(f"❌ Ошибка снимка: {e}")
            return ([], [], "", "")

    def _changed(self, a, b):
        """Проверяет, изменилось ли состояние"""
        return a[0] != b[0] or a[1] != b[1] or a[2] != b[2] or a[3] != b[3]

    def _choose_builtin(self):
        """Выбирает встроенные устройства"""
        ins, outs, *_ = self._snapshot()
        bi = find_by_patterns(ins, BUILTIN_IN_NAMES) or (ins[0] if ins else None)
        bo = find_by_patterns(outs, BUILTIN_OUT_NAMES) or (outs[0] if outs else None)
        return bi, bo

    def _choose_headset(self):
        """Выбирает гарнитуру по приоритету"""
        ins, outs, *_ = self._snapshot()
        
        # Ищем AirPods
        ap_in = find_by_patterns(ins, AIRPODS_PATTERNS)
        ap_out = find_by_patterns(outs, AIRPODS_PATTERNS)
        if ap_in and ap_out:
            return ap_in
        
        # Ищем другие гарнитуры
        hs_in = find_by_patterns(ins, HEADSET_PATTERNS)
        hs_out = find_by_patterns(outs, HEADSET_PATTERNS)
        if hs_in and hs_out:
            return hs_in
        
        return None

    def _activate_coupled(self, name: str) -> bool:
        """Активирует устройство сцепкой с проверкой здоровья"""
        for delay in (0.0, 0.3, 0.8):
            time.sleep(delay)
            try:
                set_inout(name)
            except Exception as e:
                self.log(f"❌ set_inout failed: {e}")
                continue
            
            idx, rate = query_input_idx(name)
            if idx is None:
                continue
            
            rms = health_rms(idx, rate)
            self.log(f"🔍 {name} health rms={rms:.6f} rate={rate}")
            
            if rms >= RMS_MIN:
                self._fails = 0
                self.log(f"✅ {name} активирован успешно")
                return True
        
        self._fails += 1
        self.log(f"❌ {name} не активирован, счетчик провалов: {self._fails}")
        return False

    def _fallback_builtin(self):
        """Переключается на встроенные устройства"""
        bi, bo = self._choose_builtin()
        if bi:
            try:
                set_input(bi)
            except:
                pass
        if bo:
            try:
                set_output(bo)
            except:
                pass
        self.log(f"🔄 Fallback builtin: in={bi} out={bo}")

    def _apply_policy(self):
        """Применяет политику автопереключения"""
        now = time.time()
        if now < self._quarantine_until:
            remaining = int(self._quarantine_until - now)
            self.log(f"🚫 В карантине, осталось {remaining}s")
            self._fallback_builtin()
            return

        target = self._choose_headset()
        if target and self._activate_coupled(target):
            self.log(f"✅ Активна гарнитура: {target}")
            return

        if self._fails >= FAILS_TO_QUARANTINE:
            self._quarantine_until = now + QUARANTINE_SEC
            self.log(f"🚫 Карантин {QUARANTINE_SEC}s после {self._fails} провалов")

        self._fallback_builtin()

    def _loop(self):
        """Основной цикл автопереключения"""
        self.log("🔄 Запуск основного цикла")
        self._snap = self._snapshot()
        
        while not self._stop.is_set():
            time.sleep(POLL_SEC)
            snap = self._snapshot()
            
            if self._changed(snap, self._snap):
                ms = time.time() * 1000
                if ms - self._last_ms < DEBOUNCE_MS:
                    self._snap = snap
                    continue
                
                self._last_ms = ms
                self.log("🔄 Обнаружены изменения в устройствах")
                self._apply_policy()
                self._snap = self._snapshot()

    def get_status(self):
        """Получает текущий статус"""
        return {
            'running': self._running,
            'fail_count': self._fails,
            'quarantine_until': self._quarantine_until,
            'in_quarantine': time.time() < self._quarantine_until,
            'current_snapshot': self._snap
        }

    def force_switch(self, device_name: str) -> bool:
        """Принудительно переключает на устройство"""
        self.log(f"🔄 Принудительное переключение на: {device_name}")
        return self._activate_coupled(device_name)

    def reset_quarantine(self):
        """Сбрасывает карантин"""
        self._quarantine_until = 0
        self._fails = 0
        self.log("🔄 Карантин сброшен")
