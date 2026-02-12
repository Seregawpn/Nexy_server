"""
Атомарный файл-флаг для обнаружения перезапуска.

Реализует атомарную запись через временный файл + rename(),
чтение-и-удаление под файловой блокировкой,
проверку времени и PID для игнорирования протухших флагов.
"""

from dataclasses import asdict, dataclass
import fcntl
import json
import logging
import os
from pathlib import Path
import time

logger = logging.getLogger(__name__)


@dataclass
class RestartFlagData:
    """Данные флага перезапуска"""

    timestamp: float  # Unix timestamp создания
    pid: int  # PID процесса, создавшего флаг
    reason: str  # Причина перезапуска
    permissions: list[str]  # Список разрешений, для которых был перезапуск


class AtomicRestartFlag:
    """
    Атомарный файл-флаг для обнаружения перезапуска.

    Использует временный файл + rename() для атомарной записи,
    файловую блокировку для чтения-и-удаления,
    проверку времени и PID для валидации.
    """

    # Максимальный возраст флага (60 секунд)
    MAX_FLAG_AGE_SEC = 60.0

    def __init__(self, flag_path: Path):
        """
        Args:
            flag_path: Путь к файлу флага
        """
        self.flag_path = Path(flag_path)
        self.flag_path.parent.mkdir(parents=True, exist_ok=True)

    def write(self, reason: str, permissions: list[str]) -> bool:
        """
        Атомарно записать флаг перезапуска.

        Args:
            reason: Причина перезапуска
            permissions: Список разрешений, для которых был перезапуск

        Returns:
            True если флаг успешно записан, False в противном случае
        """
        try:
            # Создаем временный файл
            temp_path = self.flag_path.with_suffix(self.flag_path.suffix + ".tmp")

            # Подготавливаем данные
            data = RestartFlagData(
                timestamp=time.time(), pid=os.getpid(), reason=reason, permissions=permissions
            )

            # Записываем во временный файл
            with open(temp_path, "w", encoding="utf-8") as f:
                json.dump(asdict(data), f, indent=2)
                f.flush()
                os.fsync(f.fileno())  # Принудительная синхронизация

            # Атомарно переименовываем
            temp_path.rename(self.flag_path)

            # КРИТИЧНО: Логируем атомарную запись для приёмки
            logger.info(
                f"✅ [ATOMIC_FLAG] Restart flag written (atomic write -> rename): {self.flag_path} "
                f"(pid={data.pid}, reason={reason}, timestamp={data.timestamp:.2f})"
            )
            return True

        except Exception as exc:
            logger.error(f"❌ [ATOMIC_FLAG] Failed to write restart flag: {exc}", exc_info=True)
            # Очищаем временный файл при ошибке
            try:
                temp_path.unlink(missing_ok=True)
            except Exception:
                pass
            return False

    def read_and_remove(self) -> RestartFlagData | None:
        """
        Прочитать флаг и удалить его атомарно под файловой блокировкой.

        Returns:
            RestartFlagData если флаг существует и валиден, None в противном случае
        """
        if not self.flag_path.exists():
            return None

        try:
            # Открываем файл с блокировкой
            with open(self.flag_path, "r+", encoding="utf-8") as f:
                # Блокируем файл для чтения
                fcntl.flock(f.fileno(), fcntl.LOCK_EX)

                try:
                    # Читаем данные
                    content = f.read()
                    if not content:
                        logger.debug(f"[ATOMIC_FLAG] Flag file is empty: {self.flag_path}")
                        return None

                    data_dict = json.loads(content)
                    data = RestartFlagData(**data_dict)

                    # Проверяем валидность флага
                    if not self._is_valid(data):
                        logger.warning(
                            f"⚠️ [ATOMIC_FLAG] Flag is invalid or expired: "
                            f"age={time.time() - data.timestamp:.2f}s, "
                            f"pid={data.pid}"
                        )
                        # Удаляем невалидный флаг
                        f.seek(0)
                        f.truncate()
                        return None

                    # Удаляем флаг (очищаем файл)
                    f.seek(0)
                    f.truncate()
                    os.fsync(f.fileno())

                    # Удаляем файл после разблокировки
                    flag_path = self.flag_path
                    fcntl.flock(f.fileno(), fcntl.LOCK_UN)
                    flag_path.unlink(missing_ok=True)

                    age_sec = time.time() - data.timestamp
                    age_ms = max(0, int(age_sec * 1000))
                    # КРИТИЧНО: Логируем чтение-и-удаление для приёмки
                    logger.info(
                        f"✅ [ATOMIC_FLAG] Restart flag read and removed (atomic read-and-remove): "
                        f"{self.flag_path} (pid={data.pid}, reason={data.reason}, "
                        f"age_ms={age_ms}, seen_ts={data.timestamp:.2f})"
                    )
                    return data

                except json.JSONDecodeError as exc:
                    logger.error(
                        f"❌ [ATOMIC_FLAG] Invalid JSON in flag file: {exc}", exc_info=True
                    )
                    # Удаляем поврежденный флаг
                    f.seek(0)
                    f.truncate()
                    return None

        except FileNotFoundError:
            # Файл был удален между проверкой и открытием
            return None
        except Exception as exc:
            logger.error(f"❌ [ATOMIC_FLAG] Failed to read restart flag: {exc}", exc_info=True)
            return None

    def peek(self) -> RestartFlagData | None:
        """
        Прочитать флаг без удаления (для idempotency-guard).

        Returns:
            RestartFlagData если флаг существует и валиден, None в противном случае
        """
        if not self.flag_path.exists():
            return None

        try:
            with open(self.flag_path, "r", encoding="utf-8") as f:
                fcntl.flock(f.fileno(), fcntl.LOCK_SH)
                content = f.read()
                fcntl.flock(f.fileno(), fcntl.LOCK_UN)

            if not content:
                logger.debug(f"[ATOMIC_FLAG] Flag file is empty: {self.flag_path}")
                return None

            data_dict = json.loads(content)
            data = RestartFlagData(**data_dict)

            if not self._is_valid(data):
                logger.warning(
                    f"⚠️ [ATOMIC_FLAG] Flag is invalid or expired (peek): "
                    f"age={time.time() - data.timestamp:.2f}s, pid={data.pid}"
                )
                # Удаляем невалидный флаг
                self.remove()
                return None

            return data

        except json.JSONDecodeError as exc:
            logger.error(f"❌ [ATOMIC_FLAG] Invalid JSON in flag file (peek): {exc}", exc_info=True)
            self.remove()
            return None
        except FileNotFoundError:
            return None
        except Exception as exc:
            logger.error(f"❌ [ATOMIC_FLAG] Failed to peek restart flag: {exc}", exc_info=True)
            return None

    def _is_valid(self, data: RestartFlagData) -> bool:
        """
        Проверяет валидность флага.

        Args:
            data: Данные флага

        Returns:
            True если флаг валиден, False в противном случае
        """
        # Проверяем возраст флага (TTL = 10 минут по умолчанию)
        age_sec = time.time() - data.timestamp
        age_ms = max(0, int(age_sec * 1000))
        if age_sec > self.MAX_FLAG_AGE_SEC:
            logger.warning(
                f"⚠️ [ATOMIC_FLAG] Flag is too old (TTL expired): "
                f"age_ms={age_ms} > {int(self.MAX_FLAG_AGE_SEC * 1000)}ms, "
                f"ignoring and removing"
            )
            return False

        # Проверяем, что процесс еще существует (опционально)
        # Не проверяем строго, так как процесс мог завершиться после создания флага
        try:
            os.kill(data.pid, 0)  # Проверка существования процесса
        except ProcessLookupError:
            # Процесс не существует - это нормально для флага перезапуска
            pass
        except OSError:
            # Другие ошибки - игнорируем
            pass

        return True

    def exists(self) -> bool:
        """Проверяет существование флага"""
        return self.flag_path.exists()

    def remove(self) -> bool:
        """Удаляет флаг без чтения"""
        try:
            if self.flag_path.exists():
                self.flag_path.unlink()
                logger.info(f"✅ [ATOMIC_FLAG] Restart flag removed: {self.flag_path}")
                return True
            return False
        except Exception as exc:
            logger.error(f"❌ [ATOMIC_FLAG] Failed to remove restart flag: {exc}", exc_info=True)
            return False
