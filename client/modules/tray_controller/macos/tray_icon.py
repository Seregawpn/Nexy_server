"""
macOS реализация иконки трея
"""

import base64
import logging
import os
import tempfile

from ..core.tray_types import TrayIconGenerator, TrayStatus

logger = logging.getLogger(__name__)

try:
    from PIL import Image, ImageDraw  # type: ignore

    _PIL_AVAILABLE = True
except Exception:
    _PIL_AVAILABLE = False  # type: ignore[reportConstantRedefinition]


class MacOSTrayIcon:
    """macOS реализация иконки трея"""

    # Минимальный набор fallback-иконок (32x32, прозрачный фон) для случаев,
    # когда Pillow недоступен в окружении (например, в упакованном .app).
    _FALLBACK_ICON_DATA = {
        TrayStatus.SLEEPING: (
            "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAmElEQVR4nO2XSwrAIAxEkzl5bt7SRaGUaP3kI9RZqpk3RkQk+rt4pEhEjspclydbQGfCwAveWsce4IIXd3VADOE1P0TAa76gZCFq9yV/RMI1DihZWCaABLX/zQMlCzsA7QALXUOOBN88ULKwVAAJOoYnB7VJb7gaIFrQBr26oPmiZ7E1/FITZOap/toILExm6njQ2OxvmK4T1nZENmSmUOcAAAAASUVORK5CYII="
        ),
        TrayStatus.LISTENING: (
            "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAmklEQVR4nO2XQQ7AIAgEYZ/tA/y2TZMemgatKIJJu0eVnRUPKtHXxUNVqZTqXGaVJ5tAJ8JgGbyzjpeAFd2AC7zhBxd4wxcULLjtvuIPV7jAAQUL+wRITu1/8EDBwh+A/gDbBMi6l8y0Lh4oWNgrQHY6hhsHrcnVcDmAsyCOruqC4AvNYmv4qT7IzFX9shFYmMzU8ZCx4d8wXAcsOTM22pQ3vQAAAABJRU5ErkJggg=="
        ),
        TrayStatus.PROCESSING: (
            "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAm0lEQVR4nO2XUQrAIAxD21x359l5HQwGY1RnbW2FLZ9q82L9UIm+Lh4pKjuVquGm82QPqCUMZsF763gGWNMNRMBbfoiAt3xByULU7mv+iIRLHFCysEyAEtT+Jw+ULPwB6A+wSgBWvmSsunigZGGpABx0DHcOWpOz4WKAaEEanNUFyReaxd7wc7yn2HJVv20EHiaWOh4x9vwbpusACbIzNnxlb+0AAAAASUVORK5CYII="
        ),
    }

    def __init__(self, status: TrayStatus = TrayStatus.SLEEPING, size: int = 16):
        self.status = status
        self.size = size
        self.icon_generator = TrayIconGenerator()
        self._temp_files = []
        self._current_icon_path: str | None = None

    def create_icon_file(self, status: TrayStatus) -> str:
        """Создать файл иконки для macOS (PNG)."""
        try:
            # Создаём временный PNG-файл
            temp_file = tempfile.NamedTemporaryFile(
                suffix=".png", delete=False, dir=tempfile.gettempdir()
            )
            temp_path = temp_file.name
            temp_file.close()

            # Вычисляем параметры рисунка (retina-friendly: рендерим в 2x размера)
            scale = 2
            w = h = max(16, self.size) * scale
            radius = int(min(w, h) * 0.45)
            cx = cy = int(min(w, h) / 2)

            # Цвет для статуса
            icon = self.icon_generator.create_circle_icon(status, self.size)
            color = icon.color or "#808080"

            # 🎯 TRAY DEBUG: Логируем создание иконки
            logger.debug(f"🎯 TRAY DEBUG: create_icon_file вызван для status={status}")
            logger.debug(f"🎯 TRAY DEBUG: generated color={color}, PIL_available={_PIL_AVAILABLE}")

            rendered = False

            if _PIL_AVAILABLE:
                try:
                    # Рисуем круг в прозрачном PNG
                    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
                    draw = ImageDraw.Draw(img)
                    bbox = [cx - radius, cy - radius, cx + radius, cy + radius]
                    draw.ellipse(bbox, fill=color)
                    # Сохраняем PNG (умеренная компрессия)
                    img.save(temp_path, format="PNG", optimize=True)
                    rendered = True
                except Exception as pil_error:
                    logger.warning(f"⚠️ Ошибка создания иконки через Pillow: {pil_error}")

            if not rendered:
                # Fallback: используем заранее подготовленные PNG в base64
                if not self._write_fallback_icon(status, temp_path):
                    # Если иконку не удалось записать, возвращаем пустую строку
                    return ""

            self._temp_files.append(temp_path)
            self._current_icon_path = temp_path
            return temp_path

        except Exception as e:
            logger.error(
                f"❌ Критическая ошибка создания иконки для status={status}: {e}", exc_info=True
            )
            return ""

    def update_status(self, status: TrayStatus) -> bool:
        """Обновить статус иконки"""
        try:
            self.status = status
            new_icon_path = self.create_icon_file(status)

            if new_icon_path and new_icon_path != self._current_icon_path:
                # Удаляем старую иконку
                if self._current_icon_path and os.path.exists(self._current_icon_path):
                    try:
                        os.unlink(self._current_icon_path)
                    except Exception:
                        pass

                self._current_icon_path = new_icon_path
                return True

            return False

        except Exception as e:
            logger.error(f"❌ Ошибка обновления статуса иконки: {e}", exc_info=True)
            return False

    def get_icon_path(self) -> str | None:
        """Получить путь к текущей иконке"""
        return self._current_icon_path

    def cleanup(self):
        """Очистить временные файлы"""
        for temp_file in self._temp_files:
            try:
                if os.path.exists(temp_file):
                    os.unlink(temp_file)
            except Exception:
                pass
        self._temp_files.clear()

    def __del__(self):
        """Деструктор для очистки"""
        self.cleanup()

    def _write_fallback_icon(self, status: TrayStatus, temp_path: str) -> bool:
        """Записать fallback-иконку в PNG формате, если Pillow недоступен."""
        data = self._FALLBACK_ICON_DATA.get(status)
        if not data:
            return False
        try:
            with open(temp_path, "wb") as f:
                f.write(base64.b64decode(data))
            return True
        except Exception as e:
            logger.error(f"❌ Ошибка записи fallback иконки: {e}", exc_info=True)
            return False
