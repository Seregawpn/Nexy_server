"""
CoreGraphics-based bridge for high-performance screen capture on macOS.
Encodes screenshots directly in JPEG or WebP format with configurable quality and optional resizing.

Requirements (ensure in requirements.txt and PyInstaller hiddenimports):
- pyobjc-core
- pyobjc-framework-Quartz
- pyobjc-framework-Cocoa
- Pillow (for WebP support)
"""

import base64
import io
import logging
import time
from typing import Any, Dict, Tuple

from AppKit import NSBitmapImageRep, NSImageCompressionFactor, NSBitmapImageFileTypeJPEG
from Quartz import (
    CGMainDisplayID,
    CGDisplayCreateImage,
    CGWindowListCreateImage,
    kCGWindowListOptionOnScreenOnly,
    kCGNullWindowID,
    kCGWindowImageDefault,
    CGBitmapContextCreate,
    CGBitmapContextCreateImage,
    CGColorSpaceCreateDeviceRGB,
    CGContextDrawImage,
    kCGImageAlphaPremultipliedLast,
    CGImageGetWidth,
    CGImageGetHeight,
)

logger = logging.getLogger(__name__)

from ..core.types import (
    ScreenshotResult,
    ScreenshotConfig,
    ScreenshotData,
    ScreenshotFormat,
)
from ..core.quality_utils import get_webp_quality, get_jpeg_quality


class CoreGraphicsBridge:
    """Bridge that uses CoreGraphics to capture screen and encodes directly in JPEG or WebP."""

    def __init__(self) -> None:
        # Preflight could be added here if needed
        pass

    def capture_full_screen(self, config: ScreenshotConfig) -> ScreenshotResult:
        start_ts = time.time()
        cg_image = CGDisplayCreateImage(CGMainDisplayID())
        if not cg_image:
            return ScreenshotResult(success=False, error="CGDisplayCreateImage failed")
        return self._encode_result(
            cg_image,
            config,
            start_ts,
            meta={"bridge_type": "core_graphics"},
        )

    def capture_region(
        self, region: Tuple[int, int, int, int], config: ScreenshotConfig
    ) -> ScreenshotResult:
        start_ts = time.time()
        x, y, w, h = region
        # Use PyObjC CGRect tuple representation instead of CGRectMake to avoid dlsym/macros issues
        rect = ((x, y), (w, h))
        cg_image = CGWindowListCreateImage(
            rect,
            kCGWindowListOptionOnScreenOnly,
            kCGNullWindowID,
            kCGWindowImageDefault,
        )
        if not cg_image:
            return ScreenshotResult(success=False, error="CGWindowListCreateImage failed")
        return self._encode_result(
            cg_image,
            config,
            start_ts,
            meta={"bridge_type": "core_graphics_region", "region": region},
        )

    def test_capture(self) -> bool:
        return CGDisplayCreateImage(CGMainDisplayID()) is not None

    def get_screen_info(self) -> Dict[str, Any]:
        return {"bridge_type": "core_graphics"}

    def _encode_result(
        self, cg_image, config: ScreenshotConfig, start_ts: float, meta: Dict[str, Any]
    ) -> ScreenshotResult:
        """Кодирует CGImage напрямую в нужный формат (JPEG или WebP) без промежуточных форматов."""
        target_cg_image = self._resize_if_needed(cg_image, config)
        
        # Определяем формат из конфигурации
        target_format = config.format
        
        # Для WebP используем Pillow для прямого кодирования из CGImage
        if target_format == ScreenshotFormat.WEBP:
            return self._encode_as_webp_result(target_cg_image, config, start_ts, meta)
        else:
            # Для JPEG используем нативный NSBitmapImageRep (быстрее)
            return self._encode_as_jpeg_result(target_cg_image, config, start_ts, meta)
    
    def _encode_as_webp_result(
        self, cg_image, config: ScreenshotConfig, start_ts: float, meta: Dict[str, Any]
    ) -> ScreenshotResult:
        """Кодирует CGImage напрямую в WebP через Pillow БЕЗ промежуточных форматов."""
        try:
            from PIL import Image
        except ImportError:
            logger.warning("⚠️ Pillow недоступен, fallback на JPEG")
            return self._encode_as_jpeg_result(cg_image, config, start_ts, meta)
        
        try:
            # Конвертируем CGImage в PIL Image напрямую из raw pixel data
            rep = NSBitmapImageRep.alloc().initWithCGImage_(cg_image)
            width = rep.pixelsWide()
            height = rep.pixelsHigh()
            
            # Получаем raw pixel data напрямую (без промежуточного PNG!)
            bitmap_data = rep.bitmapData()
            bytes_per_row = rep.bytesPerRow()
            bits_per_pixel = rep.bitsPerPixel()
            samples_per_pixel = rep.samplesPerPixel()
            
            # Определяем формат пикселей
            if bits_per_pixel == 32 and samples_per_pixel == 4:
                # RGBA формат (8 бит на канал)
                mode = 'RGBA'
                # Создаем PIL Image напрямую из raw данных
                img = Image.frombuffer(
                    mode,
                    (width, height),
                    bitmap_data,
                    'raw',
                    mode,
                    bytes_per_row,
                    1
                )
            elif bits_per_pixel == 24 and samples_per_pixel == 3:
                # RGB формат
                mode = 'RGB'
                img = Image.frombuffer(
                    mode,
                    (width, height),
                    bitmap_data,
                    'raw',
                    mode,
                    bytes_per_row,
                    1
                )
            else:
                # Fallback: используем PNG как промежуточный формат (только если не удалось получить raw data)
                logger.debug(f"Нестандартный формат пикселей ({bits_per_pixel}bpp, {samples_per_pixel}spp), используем PNG fallback")
                from AppKit import NSBitmapImageFileTypePNG
                nsdata = rep.representationUsingType_properties_(
                    NSBitmapImageFileTypePNG, {}
                )
                img = Image.open(io.BytesIO(bytes(nsdata)))
            
            # Получаем качество WebP из общей утилиты
            webp_quality = get_webp_quality(config.quality, default=80)
            
            # Кодируем в WebP напрямую в память и сразу в Base64 (без промежуточных переменных)
            output = io.BytesIO()
            img.save(output, 'WEBP', quality=webp_quality, method=6)  # method=6 - максимальное сжатие
            webp_bytes = output.getvalue()
            # Генерируем Base64 сразу из WebP bytes
            base64_data = base64.b64encode(webp_bytes).decode("utf-8")
            
            metadata = {
                **meta,
                "timestamp": time.time(),
                "quality": webp_quality,
                "encoding": "pillow_webp_direct_base64"  # Прямое кодирование WebP → Base64 без PNG
            }
            
            logger.debug(f"✅ WebP → Base64 напрямую: {width}x{height}, {len(webp_bytes)} bytes, quality={webp_quality}")
            
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
            import traceback
            logger.debug(traceback.format_exc())
            return self._encode_as_jpeg_result(cg_image, config, start_ts, meta)
    
    def _encode_as_jpeg_result(
        self, cg_image, config: ScreenshotConfig, start_ts: float, meta: Dict[str, Any]
    ) -> ScreenshotResult:
        """Кодирует CGImage в JPEG через нативный NSBitmapImageRep (быстрее чем через Pillow)."""
        rep = NSBitmapImageRep.alloc().initWithCGImage_(cg_image)

        # Получаем качество JPEG из общей утилиты
        compression = get_jpeg_quality(config.quality, default=0.75)

        nsdata = rep.representationUsingType_properties_(
            NSBitmapImageFileTypeJPEG, {NSImageCompressionFactor: compression}
        )
        jpeg_bytes = bytes(nsdata)
        # Генерируем Base64 сразу из JPEG bytes
        base64_data = base64.b64encode(jpeg_bytes).decode("utf-8")
        width, height = rep.pixelsWide(), rep.pixelsHigh()

        metadata = {
            **meta,
            "timestamp": time.time(),
            "quality": compression,
            "encoding": "native_jpeg_base64"
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

    def _resize_if_needed(self, cg_image, config: ScreenshotConfig):
        max_w = getattr(config, "max_width", 0) or 0
        max_h = getattr(config, "max_height", 0) or 0

        # Obtain source dimensions
        src_w = int(CGImageGetWidth(cg_image))
        src_h = int(CGImageGetHeight(cg_image))

        if (max_w <= 0 and max_h <= 0) or (
            (max_w <= 0 or src_w <= max_w) and (max_h <= 0 or src_h <= max_h)
        ):
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
        # Use CGRect tuple representation instead of CGRectMake
        CGContextDrawImage(ctx, ((0, 0), (new_w, new_h)), cg_image)
        return CGBitmapContextCreateImage(ctx)


