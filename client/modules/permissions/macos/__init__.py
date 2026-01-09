"""
macOS специфичные компоненты для permissions

Сохраненные модули:
- screen_capture_permission.py: Обработчик разрешений Screen Capture (использует CGPreflightScreenCaptureAccess)

Удаленные модули (2026-01-08):
- permission_handler.py: содержал устаревший tccutil check
- accessibility_handler.py: содержал устаревший tccutil check
- permission_queue_old.py: устаревший файл
- notifications_handler.py: не использовался
"""

from .screen_capture_permission import ScreenCapturePermissionManager

__all__ = ['ScreenCapturePermissionManager']
