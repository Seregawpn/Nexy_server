# ruff: noqa: I001
"""
Основной класс для управления экземплярами приложения.
"""

import fcntl
import json
import os
from pathlib import Path
import tempfile
import time

import psutil
from typing import Any

from .types import InstanceManagerConfig, InstanceStatus


class InstanceManager:
    """Менеджер экземпляров приложения с защитой от дублирования."""
    
    def __init__(self, config: InstanceManagerConfig):
        self.config = config
        self.lock_file = os.path.expanduser(config.lock_file)
        self.timeout_seconds = config.timeout_seconds
        self.lock_grace_ms = config.lock_grace_ms
        self.pid_check = config.pid_check
        self.lock_fd = None
        
    async def check_single_instance(self, retry_count: int = 0) -> InstanceStatus:
        """Проверка на дублирование экземпляров с усиленной очисткой."""
        MAX_RETRIES = 2  # Максимум 2 попытки для защиты от рекурсии
        
        try:
            # Создаем директорию если не существует
            lock_dir = os.path.dirname(self.lock_file)
            os.makedirs(lock_dir, exist_ok=True)
            
            # Проверяем существующий lock
            if os.path.exists(self.lock_file):
                # УСИЛЕННАЯ ПРОВЕРКА: PID + имя процесса
                if self._is_lock_valid():
                    return InstanceStatus.DUPLICATE
                else:
                    # Lock невалиден - очищаем
                    cleaned = self._cleanup_invalid_lock()
                    if not cleaned:
                        if retry_count < MAX_RETRIES and self._switch_to_fallback_lock():
                            return await self.check_single_instance(retry_count + 1)
                        return InstanceStatus.ERROR
            
            return InstanceStatus.SINGLE
            
        except Exception as e:
            print(f"❌ Ошибка проверки дублирования: {e}")
            return InstanceStatus.ERROR
    
    async def acquire_lock(self, retry_count: int = 0) -> bool:
        """Захват блокировки с TOCTOU защитой."""
        MAX_RETRIES = 2  # Максимум 2 попытки для защиты от рекурсии
        
        try:
            # TOCTOU защита: O_CREAT | O_EXCL
            self.lock_fd = os.open(self.lock_file, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            fcntl.flock(self.lock_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            
            # Записываем информацию о процессе
            lock_info = {
                "pid": os.getpid(),
                "timestamp": time.time(),
                "bundle_id": "com.nexy.assistant",
                "process_name": "Nexy"
            }
            os.write(self.lock_fd, json.dumps(lock_info).encode())
            os.fsync(self.lock_fd)
            
            print("✅ Блокировка захвачена успешно")
            return True
            
        except FileExistsError:
            # Файл уже существует - проверяем валидность
            if self._is_lock_valid():
                return False  # Дублирование обнаружено
            else:
                # Очищаем невалидный lock и пробуем снова
                cleaned = self._cleanup_invalid_lock()
                if cleaned and retry_count < MAX_RETRIES:
                    return await self.acquire_lock(retry_count + 1)
                if retry_count < MAX_RETRIES and self._switch_to_fallback_lock():
                    return await self.acquire_lock(retry_count + 1)
                return False
                
        except (OSError, IOError) as e:
            print(f"❌ Ошибка захвата блокировки: {e}")
            # Разрешаем автоматический переход на fallback при ограничениях доступа
            errno = getattr(e, "errno", None)
            if isinstance(e, PermissionError) or errno in (1, 13, 30):
                if retry_count < MAX_RETRIES and self._switch_to_fallback_lock():
                    return await self.acquire_lock(retry_count + 1)
            return False
    
    async def release_lock(self) -> bool:
        """Освобождение блокировки."""
        try:
            current_pid = os.getpid()
            if self.lock_fd:
                fcntl.flock(self.lock_fd, fcntl.LOCK_UN)
                os.close(self.lock_fd)
                self.lock_fd = None
                if os.path.exists(self.lock_file):
                    os.remove(self.lock_file)
            else:
                # Если блокировка не была захвачена этим процессом, не удаляем чужой lock.
                if os.path.exists(self.lock_file):
                    try:
                        with open(self.lock_file, 'r') as f:
                            lock_info = json.load(f)
                        lock_pid = lock_info.get("pid")
                        if lock_pid == current_pid:
                            os.remove(self.lock_file)
                        else:
                            print(
                                f"⚠️ Lock принадлежит другому процессу (pid={lock_pid}), "
                                "удаление пропущено"
                            )
                    except Exception:
                        # На ошибке чтения не удаляем lock, чтобы не снести чужой.
                        print("⚠️ Не удалось прочитать lock-файл — удаление пропущено")
            
            print("✅ Блокировка освобождена")
            return True
            
        except Exception as e:
            print(f"❌ Ошибка освобождения блокировки: {e}")
            return False
    
    def _is_lock_valid(self) -> bool:
        """УСИЛЕННАЯ проверка валидности блокировки."""
        try:
            if not os.path.exists(self.lock_file):
                return False
                
            # Проверяем содержимое файла
            try:
                with open(self.lock_file, 'r') as f:
                    lock_info = json.load(f)
            except (json.JSONDecodeError, IOError):
                # Возможен race: файл создан, но еще не записан полностью.
                # Если файл очень свежий — считаем lock валидным, чтобы не запускать второй экземпляр.
                try:
                    mod_time = os.path.getmtime(self.lock_file)
                    current_time = time.time()
                    if (current_time - mod_time) <= (self.lock_grace_ms / 1000.0):
                        return True
                except Exception:
                    pass
                return False  # Невалидный JSON после grace-паузы
            
            # Проверяем PID процесса
            if self.pid_check and 'pid' in lock_info:
                pid = lock_info['pid']
                current_pid = os.getpid()
                
                # КРИТИЧНО: Если PID в lock-файле совпадает с текущим PID - это не дублирование
                # Это может произойти при быстром перезапуске или если lock-файл не был очищен
                if pid == current_pid:
                    print(f"⚠️ DEBUG: Lock file PID ({pid}) совпадает с текущим PID ({current_pid}) - это не дублирование")
                    return False  # Не дублирование - это тот же процесс
                
                try:
                    # Проверяем что процесс существует и это наш процесс
                    process = psutil.Process(pid)
                    cmdline = ' '.join(process.cmdline())
                    process_name = process.name()
                    
                    print(f"🔍 DEBUG: Checking lock PID {pid}: name={process_name}, cmdline={cmdline[:100]}")
                    
                    # Проверяем что это наш процесс
                    # Варианты: Nexy.app (prod), python main.py (dev), debug/test scripts
                    exe_path = ""
                    try:
                        exe_path = process.exe()
                    except Exception:
                        exe_path = ""

                    is_nexy_app = (
                        process_name == "Nexy"
                        or "/Applications/Nexy.app/Contents/MacOS/Nexy" in cmdline
                        or exe_path.endswith("/Nexy.app/Contents/MacOS/Nexy")
                    )
                    is_python_main = process_name in ["python3", "Python"] and "main.py" in cmdline
                    is_debug_script = process_name in ["python3", "Python"] and "debug_lock_validation.py" in cmdline
                    is_test_script = process_name in ["python3", "Python"] and "test_duplicate_detection.py" in cmdline
                    
                    print(f"🔍 DEBUG: Process checks: is_nexy_app={is_nexy_app}, is_python_main={is_python_main}")
                    
                    if not (is_nexy_app or is_python_main or is_debug_script or is_test_script):
                        print(f"⚠️ DEBUG: Process {pid} is not Nexy - lock invalid")
                        return False  # Не наш процесс

                    print(f"✅ DEBUG: Lock valid - duplicate instance detected (PID {pid})")
                    return True  # Дублирование обнаружено
                        
                except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
                    print(f"⚠️ DEBUG: Process {pid} not found or access denied: {e}")
                    # Процесс не существует. Оцениваем stale по времени.
                    try:
                        mod_time = os.path.getmtime(self.lock_file)
                        current_time = time.time()
                        if (current_time - mod_time) > self.timeout_seconds:
                            return False  # Устарел по времени
                    except Exception:
                        return False
                    return False
            
            return True
            
        except Exception as e:
            print(f"⚠️ Ошибка проверки валидности lock: {e}")
            return False
    
    def _cleanup_invalid_lock(self) -> bool:
        """Очистка невалидной блокировки."""
        try:
            if os.path.exists(self.lock_file):
                try:
                    os.chmod(self.lock_file, 0o600)
                except Exception:
                    pass
                os.remove(self.lock_file)
            print("🧹 Невалидная блокировка очищена")
            return True
        except PermissionError as e:
            print(f"❌ Ошибка очистки невалидной блокировки (нет доступа): {e}")
            print(f"👉 Удалите файл вручную: {self.lock_file}")
            return False
        except Exception as e:
            print(f"❌ Ошибка очистки невалидной блокировки: {e}")
            return False

    def is_other_instance_running(self) -> bool:
        """Проверка, что активен другой экземпляр (не текущий PID)."""
        try:
            if not os.path.exists(self.lock_file):
                return False
            return self._is_lock_valid()
        except Exception as e:
            print(f"⚠️ Ошибка проверки другого экземпляра: {e}")
            return False

    def _switch_to_fallback_lock(self) -> bool:
        """Переключается на запасной путь lock-файла в каталоге /tmp."""
        try:
            tmp_dir = Path(tempfile.gettempdir()) / "nexy"
            tmp_dir.mkdir(parents=True, exist_ok=True)
            fallback_path = tmp_dir / "nexy.lock"
            if fallback_path.exists():
                try:
                    fallback_path.unlink()
                except Exception:
                    pass
            print(f"⚠️ Переключаем lock-файл на резервный путь: {fallback_path}")
            self.lock_file = str(fallback_path)
            self.lock_fd = None
            return True
        except Exception as e:
            print(f"❌ Не удалось переключить lock-файл на резервный путь: {e}")
            return False
    
    async def get_lock_info(self) -> dict[str, Any] | None:
        """Получение информации о текущей блокировке."""
        try:
            if os.path.exists(self.lock_file):
                with open(self.lock_file, 'r') as f:
                    return json.load(f)
        except Exception as e:
            print(f"❌ Ошибка чтения информации о блокировке: {e}")
        return None
