"""
Простой bridge для захвата скриншотов через системную утилиту screencapture
Использует CoreGraphics API напрямую если доступен, иначе fallback на screencapture CLI
"""

import base64
import io
import logging
from pathlib import Path
import shlex
import subprocess
import tempfile
import time
from typing import Any

from ..core.quality_utils import get_jpeg_quality, get_webp_quality
from ..core.types import ScreenshotConfig, ScreenshotData, ScreenshotFormat, ScreenshotResult

logger = logging.getLogger(__name__)

# Пытаемся импортировать CoreGraphics API
try:
    import AppKit as _AppKit
    import Quartz as _Quartz

    _coregraphics_available = True
except ImportError:
    _AppKit = None
    _Quartz = None
    _coregraphics_available = False

NSBitmapImageRep = getattr(_AppKit, "NSBitmapImageRep", None)
NSBitmapImageFileTypePNG = getattr(_AppKit, "NSBitmapImageFileTypePNG", None)
NSBitmapImageFileTypeJPEG = getattr(_AppKit, "NSBitmapImageFileTypeJPEG", None)
NSImageCompressionFactor = getattr(_AppKit, "NSImageCompressionFactor", None)
CGDisplayCreateImage = getattr(_Quartz, "CGDisplayCreateImage", None)
CGMainDisplayID = getattr(_Quartz, "CGMainDisplayID", None)
CGWindowListCreateImage = getattr(_Quartz, "CGWindowListCreateImage", None)
kCGNullWindowID = getattr(_Quartz, "kCGNullWindowID", 0)
kCGWindowImageDefault = getattr(_Quartz, "kCGWindowImageDefault", 0)
kCGWindowListOptionOnScreenOnly = getattr(_Quartz, "kCGWindowListOptionOnScreenOnly", 0)
CGBitmapContextCreate = getattr(_Quartz, "CGBitmapContextCreate", None)
CGBitmapContextCreateImage = getattr(_Quartz, "CGBitmapContextCreateImage", None)
CGColorSpaceCreateDeviceRGB = getattr(_Quartz, "CGColorSpaceCreateDeviceRGB", None)
CGContextDrawImage = getattr(_Quartz, "CGContextDrawImage", None)
CGImageGetHeight = getattr(_Quartz, "CGImageGetHeight", None)
CGImageGetWidth = getattr(_Quartz, "CGImageGetWidth", None)
kCGImageAlphaPremultipliedLast = getattr(_Quartz, "kCGImageAlphaPremultipliedLast", 0)


class SimpleCoreGraphicsBridge:
    """Bridge использующий CoreGraphics API напрямую (без PNG промежуточного формата) или screencapture CLI как fallback"""

    def __init__(self):
        """Инициализация bridge"""
        self.initialized = True
        self._use_coregraphics = _coregraphics_available

        if self._use_coregraphics:
            logger.info("✅ SimpleCoreGraphicsBridge инициализирован (CoreGraphics API)")
        else:
            logger.info("✅ SimpleCoreGraphicsBridge инициализирован (screencapture CLI fallback)")

    def capture_full_screen(self, config: ScreenshotConfig) -> ScreenshotResult:
        """
        Захват полного экрана через CoreGraphics API (без PNG) или screencapture CLI

        Args:
            config: Конфигурация захвата

        Returns:
            ScreenshotResult: Результат захвата
        """
        # Используем CoreGraphics API напрямую если доступен (без PNG!)
        if self._use_coregraphics:
            return self._capture_via_coregraphics(config, None)
        else:
            # Fallback на screencapture CLI (использует PNG как промежуточный формат)
            return self._capture_via_screencapture(config, None)

    def _capture_via_coregraphics(
        self, config: ScreenshotConfig, region: tuple[int, int, int, int] | None
    ) -> ScreenshotResult:
        """Захват через CoreGraphics API напрямую в WebP (без PNG промежуточного формата)"""
        try:
            start_time = time.time()
            if not (
                CGDisplayCreateImage
                and CGMainDisplayID
                and CGWindowListCreateImage
                and NSBitmapImageRep
            ):
                return self._capture_via_screencapture(config, region)

            # Захватываем CGImage
            if region:
                x, y, w, h = region
                rect = ((x, y), (w, h))
                cg_image = CGWindowListCreateImage(
                    rect,
                    kCGWindowListOptionOnScreenOnly,
                    kCGNullWindowID,
                    kCGWindowImageDefault,
                )
            else:
                cg_image = CGDisplayCreateImage(CGMainDisplayID())

            if not cg_image:
                return ScreenshotResult(
                    success=False,
                    error="CGDisplayCreateImage/CGWindowListCreateImage failed",
                    capture_time=time.time() - start_time,
                )

            # Применяем resize если нужно
            cg_image = self._resize_cgimage_if_needed(cg_image, config)

            # Кодируем напрямую в нужный формат
            if config.format == ScreenshotFormat.WEBP:
                return self._encode_cgimage_to_webp(
                    cg_image,
                    config,
                    start_time,
                    {"bridge_type": "simple_coregraphics", "capture_method": "coregraphics_direct"},
                )
            else:
                return self._encode_cgimage_to_jpeg(
                    cg_image,
                    config,
                    start_time,
                    {"bridge_type": "simple_coregraphics", "capture_method": "coregraphics_direct"},
                )

        except Exception as e:
            logger.error(f"❌ CoreGraphics capture error: {e}")
            return ScreenshotResult(
                success=False,
                error=f"CoreGraphics capture error: {e}",
                capture_time=time.time() - start_time if "start_time" in locals() else 0.0,
            )

    def _capture_via_screencapture(
        self, config: ScreenshotConfig, region: tuple[int, int, int, int] | None
    ) -> ScreenshotResult:
        """Fallback захват через screencapture CLI (использует PNG как промежуточный формат)"""
        try:
            start_time = time.time()

            # Создаем временный файл
            temp_dir = Path(tempfile.gettempdir()) / "nexy_screenshots"
            temp_dir.mkdir(parents=True, exist_ok=True)
            timestamp = int(time.time() * 1000)

            # Определяем формат захвата: для WebP используем PNG (screencapture не поддерживает WebP напрямую)
            if config.format == ScreenshotFormat.WEBP:
                temp_file = temp_dir / f"screenshot_{timestamp}.png"
                format_flag = "png"
            else:
                temp_file = temp_dir / f"screenshot_{timestamp}.jpg"
                format_flag = "jpg"

            # Команда захвата экрана
            if region:
                x, y, w, h = region
                cmd = f"screencapture -x -t {format_flag} -R {x},{y},{w},{h} {shlex.quote(str(temp_file))}"
            else:
                cmd = f"screencapture -x -t {format_flag} {shlex.quote(str(temp_file))}"

            # Выполняем команду
            result = subprocess.run(
                cmd, shell=True, capture_output=True, text=True, timeout=config.timeout
            )

            if result.returncode != 0:
                error_msg = f"screencapture failed: {result.stderr.strip()}"
                logger.error(f"❌ {error_msg}")
                return ScreenshotResult(
                    success=False, error=error_msg, capture_time=time.time() - start_time
                )

            if not temp_file.exists():
                error_msg = "Screenshot file was not created"
                logger.error(f"❌ {error_msg}")
                return ScreenshotResult(
                    success=False, error=error_msg, capture_time=time.time() - start_time
                )

            # Применяем ограничения размера если нужно
            self._resize_if_needed(temp_file, config)

            # Получаем размеры изображения ДО обработки (файл еще существует)
            width, height = self._get_image_dimensions(temp_file)

            # Обрабатываем в зависимости от формата
            if config.format == ScreenshotFormat.WEBP:
                # Конвертируем PNG в WebP напрямую в память (без промежуточного файла)
                try:
                    webp_bytes = self._convert_to_webp_bytes(temp_file, config)
                    temp_file.unlink()  # Удаляем промежуточный PNG
                    image_data = webp_bytes
                    format_type = ScreenshotFormat.WEBP
                    mime_type = "image/webp"
                    file_size = len(webp_bytes)
                    # Проверяем размеры WebP (могут отличаться от PNG)
                    try:
                        from PIL import Image

                        img = Image.open(io.BytesIO(image_data))
                        width, height = img.size
                    except Exception:
                        pass  # Используем размеры из исходного файла
                except Exception as e:
                    logger.warning(f"⚠️ WebP конвертация не удалась: {e}, используем PNG")
                    # Fallback на PNG
                    with open(temp_file, "rb") as f:
                        image_data = f.read()
                    format_type = ScreenshotFormat.PNG
                    mime_type = "image/png"
                    file_size = len(image_data)
                    temp_file.unlink()
            else:
                # Оптимизируем качество JPEG для уменьшения размера файла
                self._optimize_jpeg_quality(temp_file, config)
                format_type = ScreenshotFormat.JPEG
                mime_type = "image/jpeg"
                # Читаем файл
                with open(temp_file, "rb") as f:
                    image_data = f.read()
                file_size = len(image_data)
                temp_file.unlink()

            # Кодируем в base64 напрямую из памяти
            base64_data = base64.b64encode(image_data).decode("utf-8")

            # Создаем результат
            screenshot_data = ScreenshotData(
                base64_data=base64_data,
                width=width,
                height=height,
                format=format_type,
                size_bytes=file_size,
                mime_type=mime_type,
                metadata={
                    "bridge_type": "simple_cli",
                    "capture_method": "screencapture",
                    "timestamp": time.time(),
                },
            )

            capture_time = time.time() - start_time
            logger.info(
                f"✅ Скриншот захвачен: {width}x{height}, {file_size} bytes, {capture_time:.3f}s"
            )

            return ScreenshotResult(success=True, data=screenshot_data, capture_time=capture_time)

        except subprocess.TimeoutExpired:
            error_msg = f"Screenshot capture timeout ({config.timeout}s)"
            logger.error(f"❌ {error_msg}")
            return ScreenshotResult(success=False, error=error_msg, capture_time=config.timeout)
        except Exception as e:
            error_msg = f"Screenshot capture error: {e}"
            logger.error(f"❌ {error_msg}")
            return ScreenshotResult(
                success=False,
                error=error_msg,
                capture_time=time.time() - start_time if "start_time" in locals() else 0.0,
            )

    def _resize_cgimage_if_needed(self, cg_image, config: ScreenshotConfig):
        """Изменяет размер CGImage если нужно"""
        if not self._use_coregraphics:
            return cg_image

        try:
            max_w = config.max_width or 0
            max_h = config.max_height or 0
            if not (
                CGBitmapContextCreate
                and CGBitmapContextCreateImage
                and CGColorSpaceCreateDeviceRGB
                and CGContextDrawImage
                and CGImageGetHeight
                and CGImageGetWidth
            ):
                return cg_image

            if max_w <= 0 and max_h <= 0:
                return cg_image

            src_w = int(CGImageGetWidth(cg_image))
            src_h = int(CGImageGetHeight(cg_image))

            if (max_w <= 0 or src_w <= max_w) and (max_h <= 0 or src_h <= max_h):
                return cg_image

            scale_w = max_w / src_w if max_w > 0 else 1.0
            scale_h = max_h / src_h if max_h > 0 else 1.0
            scale = min(scale_w, scale_h, 1.0)

            new_w = int(src_w * scale)
            new_h = int(src_h * scale)
            if new_w <= 0 or new_h <= 0:
                return cg_image

            cs = CGColorSpaceCreateDeviceRGB()
            ctx = CGBitmapContextCreate(
                None,
                new_w,
                new_h,
                8,
                new_w * 4,
                cs,
                kCGImageAlphaPremultipliedLast,
            )
            CGContextDrawImage(ctx, ((0, 0), (new_w, new_h)), cg_image)
            return CGBitmapContextCreateImage(ctx)
        except Exception as e:
            logger.debug(f"Failed to resize CGImage: {e}")
            return cg_image

    def _encode_cgimage_to_webp(
        self, cg_image, config: ScreenshotConfig, start_ts: float, meta: dict[str, Any]
    ) -> ScreenshotResult:
        """Кодирует CGImage напрямую в WebP через Pillow БЕЗ промежуточного PNG"""
        try:
            from PIL import Image

            bitmap_rep_cls = self._require_nsbitmap_rep()
            rep = bitmap_rep_cls.alloc().initWithCGImage_(cg_image)
            width = rep.pixelsWide()
            height = rep.pixelsHigh()

            # Получаем raw pixel data напрямую (без промежуточного PNG!)
            bitmap_data = rep.bitmapData()
            bytes_per_row = rep.bytesPerRow()
            bits_per_pixel = rep.bitsPerPixel()
            samples_per_pixel = rep.samplesPerPixel()

            # Определяем формат пикселей
            if bits_per_pixel == 32 and samples_per_pixel == 4:
                mode = "RGBA"
                img = Image.frombuffer(
                    mode, (width, height), bitmap_data, "raw", mode, bytes_per_row, 1
                )
            elif bits_per_pixel == 24 and samples_per_pixel == 3:
                mode = "RGB"
                img = Image.frombuffer(
                    mode, (width, height), bitmap_data, "raw", mode, bytes_per_row, 1
                )
            else:
                # Fallback на PNG только для нестандартных форматов
                logger.debug(
                    f"Нестандартный формат пикселей ({bits_per_pixel}bpp, {samples_per_pixel}spp), используем PNG fallback"
                )
                if NSBitmapImageFileTypePNG is None:
                    raise RuntimeError("NSBitmapImageFileTypePNG unavailable")
                nsdata = rep.representationUsingType_properties_(NSBitmapImageFileTypePNG, {})
                img = Image.open(io.BytesIO(bytes(nsdata)))

            # Получаем качество WebP из общей утилиты
            webp_quality = get_webp_quality(config.quality, default=80)

            # Кодируем в WebP напрямую в память и сразу в Base64 (без промежуточных переменных)
            output = io.BytesIO()
            img.save(output, "WEBP", quality=webp_quality, method=6)
            webp_bytes = output.getvalue()
            # Генерируем Base64 сразу из WebP bytes
            base64_data = base64.b64encode(webp_bytes).decode("utf-8")

            metadata = {
                **meta,
                "timestamp": time.time(),
                "quality": webp_quality,
                "encoding": "pillow_webp_direct_base64",
            }

            logger.debug(
                f"✅ WebP → Base64 напрямую: {width}x{height}, {len(webp_bytes)} bytes, quality={webp_quality}"
            )

            return ScreenshotResult(
                success=True,
                data=ScreenshotData(
                    base64_data=base64_data,
                    width=width,
                    height=height,
                    format=ScreenshotFormat.WEBP,
                    size_bytes=len(webp_bytes),
                    mime_type="image/webp",
                    metadata=metadata,
                ),
                capture_time=time.time() - start_ts,
            )
        except Exception as e:
            logger.warning(f"⚠️ WebP кодирование не удалось: {e}, fallback на JPEG")
            return self._encode_cgimage_to_jpeg(cg_image, config, start_ts, meta)

    def _encode_cgimage_to_jpeg(
        self, cg_image, config: ScreenshotConfig, start_ts: float, meta: dict[str, Any]
    ) -> ScreenshotResult:
        """Кодирует CGImage в JPEG через нативный NSBitmapImageRep"""
        try:
            if NSBitmapImageFileTypeJPEG is None or NSImageCompressionFactor is None:
                raise RuntimeError("Native JPEG symbols unavailable")

            bitmap_rep_cls = self._require_nsbitmap_rep()
            rep = bitmap_rep_cls.alloc().initWithCGImage_(cg_image)
            width = rep.pixelsWide()
            height = rep.pixelsHigh()

            # Получаем качество JPEG из общей утилиты
            compression = get_jpeg_quality(config.quality, default=0.75)

            nsdata = rep.representationUsingType_properties_(
                NSBitmapImageFileTypeJPEG, {NSImageCompressionFactor: compression}
            )
            jpeg_bytes = bytes(nsdata)
            # Генерируем Base64 сразу из JPEG bytes
            base64_data = base64.b64encode(jpeg_bytes).decode("utf-8")

            metadata = {
                **meta,
                "timestamp": time.time(),
                "quality": compression,
                "encoding": "native_jpeg_base64",
            }

            return ScreenshotResult(
                success=True,
                data=ScreenshotData(
                    base64_data=base64_data,
                    width=width,
                    height=height,
                    format=ScreenshotFormat.JPEG,
                    size_bytes=len(jpeg_bytes),
                    mime_type="image/jpeg",
                    metadata=metadata,
                ),
                capture_time=time.time() - start_ts,
            )
        except Exception as e:
            logger.error(f"❌ JPEG кодирование не удалось: {e}")
            return ScreenshotResult(
                success=False,
                error=f"JPEG encoding failed: {e}",
                capture_time=time.time() - start_ts,
            )

    def capture_region(
        self, region: tuple[int, int, int, int], config: ScreenshotConfig
    ) -> ScreenshotResult:
        """
        Захват области экрана через CoreGraphics API (без PNG) или screencapture CLI

        Args:
            region: Область (x, y, width, height)
            config: Конфигурация захвата

        Returns:
            ScreenshotResult: Результат захвата
        """
        # Используем CoreGraphics API напрямую если доступен (без PNG!)
        if self._use_coregraphics:
            return self._capture_via_coregraphics(config, region)
        else:
            # Fallback на screencapture CLI (использует PNG как промежуточный формат)
            return self._capture_via_screencapture(config, region)

    def test_capture(self) -> bool:
        """
        Тестирует возможность захвата скриншота

        Returns:
            bool: True если захват возможен
        """
        try:
            # Проверяем доступность команды screencapture
            result = subprocess.run(
                ["which", "screencapture"], capture_output=True, text=True, timeout=5.0
            )

            if result.returncode != 0:
                logger.warning("⚠️ screencapture command not found")
                return False

            # Пробуем сделать тестовый снимок
            temp_dir = Path(tempfile.gettempdir()) / "nexy_screenshots"
            temp_dir.mkdir(parents=True, exist_ok=True)
            test_file = temp_dir / "test_screenshot.jpg"

            cmd = f"screencapture -x -t jpg {shlex.quote(str(test_file))}"
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=10.0)

            success = result.returncode == 0 and test_file.exists()

            # Удаляем тестовый файл
            if test_file.exists():
                test_file.unlink()

            if success:
                logger.info("✅ Screenshot capture test passed")
            else:
                logger.warning(f"⚠️ Screenshot capture test failed: {result.stderr.strip()}")

            return success

        except Exception as e:
            logger.error(f"❌ Screenshot test error: {e}")
            return False

    def get_screen_info(self) -> dict[str, Any]:
        """
        Получает информацию об экране

        Returns:
            dict: Информация об экране
        """
        try:
            # Используем system_profiler для получения информации о дисплее
            result = subprocess.run(
                ["system_profiler", "SPDisplaysDataType", "-json"],
                capture_output=True,
                text=True,
                timeout=10.0,
            )

            if result.returncode == 0:
                import json

                data = json.loads(result.stdout)

                # Извлекаем информацию о первом дисплее
                displays = data.get("SPDisplaysDataType", [])
                if displays and len(displays) > 0:
                    display = displays[0]
                    return {
                        "displays": displays,
                        "primary_display": display,
                        "resolution": display.get("_spdisplays_resolution", "Unknown"),
                        "pixel_depth": display.get("_spdisplays_pixeldepth", "Unknown"),
                        "main_display": display.get("_spdisplays_main", "Unknown"),
                    }

            # Fallback - простая информация
            return {
                "displays": [],
                "primary_display": None,
                "resolution": "Unknown",
                "pixel_depth": "Unknown",
                "main_display": "Unknown",
                "bridge_type": "simple_cli",
            }

        except Exception as e:
            logger.debug(f"Failed to get screen info: {e}")
            return {"displays": [], "error": str(e), "bridge_type": "simple_cli"}

    def _resize_if_needed(self, image_path: Path, config: ScreenshotConfig):
        """Изменяет размер изображения если нужно с пропорциональным масштабированием"""
        try:
            max_width = int(config.max_width or 0)
            max_height = int(config.max_height or 0)
            if max_width <= 0 and max_height <= 0:
                return

            # Получаем текущие размеры изображения
            current_width, current_height = self._get_image_dimensions(image_path)
            if current_width <= 0 or current_height <= 0:
                return

            # Вычисляем коэффициент масштабирования для пропорционального изменения
            scale_width = max_width / current_width if max_width > 0 else 1.0
            scale_height = max_height / current_height if max_height > 0 else 1.0
            scale_factor = min(scale_width, scale_height, 1.0)  # Не увеличиваем, только уменьшаем

            if scale_factor >= 1.0:
                logger.debug(
                    f"Resize not needed: current={current_width}x{current_height}, scale={scale_factor:.2f}"
                )
                return

            # Вычисляем новые размеры
            new_width = int(current_width * scale_factor)
            new_height = int(current_height * scale_factor)

            logger.info(
                f"📐 Изменяем размер: {current_width}x{current_height} → {new_width}x{new_height} (scale={scale_factor:.2f})"
            )

            # Используем sips для пропорционального изменения размера
            cmd = f"sips -z {new_height} {new_width} {shlex.quote(str(image_path))}"
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=10.0)

            if result.returncode == 0:
                logger.info(f"✅ Размер изменен успешно: {new_width}x{new_height}")
            else:
                logger.warning(f"⚠️ Ошибка изменения размера: {result.stderr.strip()}")

        except Exception as e:
            logger.debug(f"Failed to resize image: {e}")

    def _convert_to_webp_bytes(self, image_path: Path, config: ScreenshotConfig) -> bytes:
        """Конвертирует изображение (PNG/JPEG) в WebP через Pillow и возвращает bytes напрямую"""
        try:
            import io

            from PIL import Image

            # Получаем качество WebP из общей утилиты
            webp_quality = get_webp_quality(config.quality, default=80)

            # Конвертация напрямую в память
            img = Image.open(image_path)
            output = io.BytesIO()
            img.save(
                output, "WEBP", quality=webp_quality, method=6
            )  # method=6 - максимальное сжатие
            webp_bytes = output.getvalue()

            logger.debug(
                f"✅ Конвертировано в WebP: {image_path.name}, {len(webp_bytes)} bytes, quality={webp_quality}"
            )
            return webp_bytes

        except Exception as e:
            logger.warning(f"⚠️ WebP конвертация не удалась: {e}")
            raise

    def _optimize_jpeg_quality(self, image_path: Path, config: ScreenshotConfig):
        """Оптимизирует качество JPEG для уменьшения размера файла"""
        try:
            # Получаем качество JPEG для sips (проценты 0-100)
            # Конвертируем из float (0.0-1.0) в проценты
            jpeg_compression = get_jpeg_quality(config.quality, default=0.75)
            jpeg_quality = int(jpeg_compression * 100)  # 0.75 → 75

            logger.debug(f"Оптимизируем JPEG качество: {jpeg_compression:.2f} → {jpeg_quality}%")

            # Используем sips для сжатия JPEG
            cmd = f"sips -s formatOptions {jpeg_quality} {shlex.quote(str(image_path))}"
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=10.0)

            if result.returncode == 0:
                logger.debug(f"✅ JPEG оптимизирован с качеством {jpeg_quality}%")
            else:
                logger.debug(f"⚠️ Не удалось оптимизировать JPEG: {result.stderr.strip()}")

        except Exception as e:
            logger.debug(f"Failed to optimize JPEG quality: {e}")

    def _get_image_dimensions(self, image_path: Path) -> tuple[int, int]:
        """Получает размеры изображения"""
        try:
            # Используем sips для получения размеров
            cmd = f"sips -g pixelWidth -g pixelHeight {shlex.quote(str(image_path))}"
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=5.0)

            if result.returncode == 0:
                width = height = None
                for line in result.stdout.splitlines():
                    if "pixelWidth:" in line:
                        try:
                            width = int(line.split(":")[-1].strip())
                        except ValueError:
                            pass
                    elif "pixelHeight:" in line:
                        try:
                            height = int(line.split(":")[-1].strip())
                        except ValueError:
                            pass

                if width and height:
                    return width, height

            # Fallback - возвращаем размеры по умолчанию
            return 1920, 1080

        except Exception as e:
            logger.debug(f"Failed to get image dimensions: {e}")
            return 1920, 1080

    def _require_nsbitmap_rep(self) -> Any:
        """Возвращает NSBitmapImageRep класс или поднимает исключение."""
        if NSBitmapImageRep is None:
            raise RuntimeError("NSBitmapImageRep unavailable")
        return NSBitmapImageRep
