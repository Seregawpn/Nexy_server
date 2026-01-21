"""
Основной класс для управления экземплярами приложения.
"""

import os
import fcntl
import time
import json
import psutil
import tempfile
from typing import Optional
from pathlib import Path

from .types import InstanceStatus, LockInfo, InstanceManagerConfig

class InstanceManager:
    """Менеджер экземпляров приложения с защитой от дублирования."""
    
    def __init__(self, config: InstanceManagerConfig):
        self.config = config
        self.lock_file = os.path.expanduser(config.lock_file)
        self.timeout_seconds = config.timeout_seconds
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
                if await self._is_lock_valid():
                    return InstanceStatus.DUPLICATE
                else:
                    # Lock невалиден - очищаем
                    cleaned = await self._cleanup_invalid_lock()
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
            if await self._is_lock_valid():
                return False  # Дублирование обнаружено
            else:
                # Очищаем невалидный lock и пробуем снова
                cleaned = await self._cleanup_invalid_lock()
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
            if self.lock_fd:
                fcntl.flock(self.lock_fd, fcntl.LOCK_UN)
                os.close(self.lock_fd)
                self.lock_fd = None
            
            if os.path.exists(self.lock_file):
                os.remove(self.lock_file)
            
            print("✅ Блокировка освобождена")
            return True
            
        except Exception as e:
            print(f"❌ Ошибка освобождения блокировки: {e}")
            return False
    
    async def _is_lock_valid(self) -> bool:
        """УСИЛЕННАЯ проверка валидности блокировки."""
        try:
            if not os.path.exists(self.lock_file):
                return False
                
            # Проверяем время модификации файла
            mod_time = os.path.getmtime(self.lock_file)
            current_time = time.time()
            
            if (current_time - mod_time) > self.timeout_seconds:
                return False  # Устарел по времени
            
            # Проверяем содержимое файла
            try:
                with open(self.lock_file, 'r') as f:
                    lock_info = json.load(f)
            except (json.JSONDecodeError, IOError):
                return False  # Невалидный JSON
            
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
                    # Варианты: Nexy.app, python3 main.py, Python debug_script.py, Python test_script.py
                    is_nexy_app = process_name == "Nexy"
                    is_python_main = process_name in ["python3", "Python"] and "main.py" in cmdline
                    is_debug_script = process_name in ["python3", "Python"] and "debug_lock_validation.py" in cmdline
                    is_test_script = process_name in ["python3", "Python"] and "test_duplicate_detection.py" in cmdline
                    
                    print(f"🔍 DEBUG: Process checks: is_nexy_app={is_nexy_app}, is_python_main={is_python_main}")
                    
                    if not (is_nexy_app or is_python_main or is_debug_script or is_test_script):
                        print(f"⚠️ DEBUG: Process {pid} is not Nexy - lock invalid")
                        return False  # Не наш процесс
                        
                    # Дополнительная проверка через bundle_id или скрипты
                    cmdline_check = ('com.nexy.assistant' in cmdline or 'main.py' in cmdline or 
                                   'debug_lock_validation.py' in cmdline or 'test_duplicate_detection.py' in cmdline)
                    
                    print(f"🔍 DEBUG: cmdline_check={cmdline_check}")
                    
                    if not cmdline_check:
                        print(f"⚠️ DEBUG: cmdline_check failed - lock invalid")
                        return False  # Не наш процесс
                    
                    print(f"✅ DEBUG: Lock valid - duplicate instance detected (PID {pid})")
                    return True  # Дублирование обнаружено
                        
                except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
                    print(f"⚠️ DEBUG: Process {pid} not found or access denied: {e}")
                    return False  # Процесс не существует
            
            return True
            
        except Exception as e:
            print(f"⚠️ Ошибка проверки валидности lock: {e}")
            return False
    
    async def _cleanup_invalid_lock(self) -> bool:
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
    
    async def get_lock_info(self) -> Optional[dict]:
        """Получение информации о текущей блокировке."""
        try:
            if os.path.exists(self.lock_file):
                with open(self.lock_file, 'r') as f:
                    return json.load(f)
        except Exception as e:
            print(f"❌ Ошибка чтения информации о блокировке: {e}")
        return None
