#!/usr/bin/env python3
"""
Диагностический скрипт для выявления проблем с иконкой меню
"""
import os
import sys
import tempfile
import logging

# Настройка логирования
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def check_environment():
    """Проверить окружение"""
    logger.info("=" * 60)
    logger.info("ПРОВЕРКА ОКРУЖЕНИЯ")
    logger.info("=" * 60)

    # Текущая директория
    logger.info(f"Current working directory: {os.getcwd()}")

    # Путь к исполняемому файлу
    logger.info(f"Executable: {sys.executable}")
    logger.info(f"Script path: {sys.argv[0]}")

    # Переменные окружения
    logger.info(f"TMPDIR: {os.environ.get('TMPDIR', 'NOT SET')}")
    logger.info(f"HOME: {os.environ.get('HOME', 'NOT SET')}")
    logger.info(f"PATH: {os.environ.get('PATH', 'NOT SET')[:100]}...")

    # Проверка прав доступа к temp
    temp_dir = tempfile.gettempdir()
    logger.info(f"Temp directory: {temp_dir}")
    logger.info(f"Temp dir exists: {os.path.exists(temp_dir)}")
    logger.info(f"Temp dir writable: {os.access(temp_dir, os.W_OK)}")

    # Попытка создать временный файл
    try:
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as f:
            temp_path = f.name
            logger.info(f"✅ Успешно создан временный файл: {temp_path}")
            f.write(b"test")

        # Проверка существования
        if os.path.exists(temp_path):
            logger.info(f"✅ Временный файл существует")
            logger.info(f"✅ Размер: {os.path.getsize(temp_path)} bytes")
            os.unlink(temp_path)
            logger.info(f"✅ Временный файл удален")
        else:
            logger.error(f"❌ Временный файл НЕ существует!")

    except Exception as e:
        logger.error(f"❌ Ошибка создания временного файла: {e}", exc_info=True)

def check_pillow():
    """Проверить доступность Pillow"""
    logger.info("=" * 60)
    logger.info("ПРОВЕРКА PIL/PILLOW")
    logger.info("=" * 60)

    try:
        from PIL import Image, ImageDraw
        logger.info("✅ PIL доступен")

        # Попытка создать изображение
        img = Image.new("RGBA", (32, 32), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        draw.ellipse([8, 8, 24, 24], fill="#FF0000")

        # Сохранить в temp
        temp_file = tempfile.NamedTemporaryFile(suffix='.png', delete=False)
        temp_path = temp_file.name
        temp_file.close()

        img.save(temp_path, format="PNG")
        logger.info(f"✅ Успешно создана тестовая иконка: {temp_path}")
        logger.info(f"✅ Размер: {os.path.getsize(temp_path)} bytes")

        os.unlink(temp_path)
        logger.info(f"✅ Тестовая иконка удалена")

    except ImportError as e:
        logger.error(f"❌ PIL НЕ доступен: {e}")
    except Exception as e:
        logger.error(f"❌ Ошибка при работе с PIL: {e}", exc_info=True)

def check_rumps():
    """Проверить доступность rumps"""
    logger.info("=" * 60)
    logger.info("ПРОВЕРКА RUMPS")
    logger.info("=" * 60)

    try:
        import rumps
        logger.info("✅ rumps доступен")
        logger.info(f"✅ rumps version: {rumps.__version__ if hasattr(rumps, '__version__') else 'unknown'}")
    except ImportError as e:
        logger.error(f"❌ rumps НЕ доступен: {e}")
    except Exception as e:
        logger.error(f"❌ Ошибка при импорте rumps: {e}", exc_info=True)

def check_tray_icon_module():
    """Проверить модуль tray_icon"""
    logger.info("=" * 60)
    logger.info("ПРОВЕРКА МОДУЛЯ TRAY_ICON")
    logger.info("=" * 60)

    try:
        # Добавляем путь к модулям
        client_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if client_dir not in sys.path:
            sys.path.insert(0, client_dir)
            logger.info(f"Добавлен путь: {client_dir}")

        from modules.tray_controller.macos.tray_icon import MacOSTrayIcon
        from modules.tray_controller.core.tray_types import TrayStatus

        logger.info("✅ Модуль tray_icon успешно импортирован")

        # Попытка создать иконку
        icon = MacOSTrayIcon()
        icon_path = icon.create_icon_file(TrayStatus.SLEEPING)

        if icon_path:
            logger.info(f"✅ Иконка создана: {icon_path}")
            logger.info(f"✅ Иконка существует: {os.path.exists(icon_path)}")
            if os.path.exists(icon_path):
                logger.info(f"✅ Размер иконки: {os.path.getsize(icon_path)} bytes")
        else:
            logger.error("❌ create_icon_file вернул пустую строку!")

    except ImportError as e:
        logger.error(f"❌ Не удалось импортировать модуль: {e}", exc_info=True)
    except Exception as e:
        logger.error(f"❌ Ошибка при проверке модуля: {e}", exc_info=True)

def main():
    logger.info("🔍 ДИАГНОСТИКА ПРОБЛЕМЫ С ИКОНКОЙ МЕНЮ")
    logger.info("")

    check_environment()
    logger.info("")

    check_pillow()
    logger.info("")

    check_rumps()
    logger.info("")

    check_tray_icon_module()
    logger.info("")

    logger.info("=" * 60)
    logger.info("ДИАГНОСТИКА ЗАВЕРШЕНА")
    logger.info("=" * 60)

if __name__ == "__main__":
    main()
