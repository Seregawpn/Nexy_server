"""
Работа с PKG файлами для системы обновлений
Установка PKG пакетов через installer
"""

import logging
import os
import subprocess
from typing import Any

logger = logging.getLogger(__name__)


def install_pkg(pkg_path: str, target: str = "/") -> bool:
    """
    Установка PKG файла через installer

    Args:
        pkg_path: Путь к PKG файлу
        target: Целевая директория (по умолчанию /)

    Returns:
        bool: True если установка успешна

    Raises:
        RuntimeError: Если установка не удалась
    """
    try:
        logger.info(f"Установка PKG: {pkg_path} -> {target}")

        # Проверяем, что файл существует
        if not os.path.exists(pkg_path):
            raise RuntimeError(f"PKG файл не найден: {pkg_path}")

        # Запускаем installer
        result = subprocess.run(
            ["sudo", "installer", "-pkg", pkg_path, "-target", target, "-verbose"],
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:
            raise RuntimeError(f"Ошибка установки PKG: {result.stderr}")

        logger.info("✅ PKG успешно установлен")
        return True

    except Exception as e:
        logger.error(f"❌ Ошибка установки PKG: {e}")
        raise RuntimeError(f"Ошибка установки PKG: {e}")


def verify_pkg_signature(pkg_path: str) -> bool:
    """
    Проверка подписи PKG файла

    Args:
        pkg_path: Путь к PKG файлу

    Returns:
        bool: True если подпись валидна
    """
    try:
        logger.info(f"Проверка подписи PKG: {pkg_path}")

        # Проверяем подпись через pkgutil
        result = subprocess.run(
            ["pkgutil", "--check-signature", pkg_path], capture_output=True, text=True
        )

        if result.returncode != 0:
            logger.warning(f"PKG подпись не проверена: {result.stderr}")
            return False

        logger.info("✅ PKG подпись валидна")
        return True

    except Exception as e:
        logger.error(f"Ошибка проверки подписи PKG: {e}")
        return False


def get_pkg_info(pkg_path: str) -> dict[str, Any]:
    """
    Получение информации о PKG файле

    Args:
        pkg_path: Путь к PKG файлу

    Returns:
        dict: Информация о PKG
    """
    try:
        logger.info(f"Получение информации о PKG: {pkg_path}")

        # Получаем информацию через pkgutil
        result = subprocess.run(
            ["pkgutil", "--payload-files", pkg_path], capture_output=True, text=True
        )

        if result.returncode != 0:
            return {"error": result.stderr}

        # Парсим информацию
        files = result.stdout.strip().split("\n") if result.stdout.strip() else []

        info = {
            "file_size": os.path.getsize(pkg_path),
            "files_count": len(files),
            "files": files[:10] if files else [],  # Первые 10 файлов
        }

        logger.info(f"PKG информация: {info['file_size']} байт, {info['files_count']} файлов")
        return info

    except Exception as e:
        logger.error(f"Ошибка получения информации о PKG: {e}")
        return {"error": str(e)}


def extract_pkg_contents(pkg_path: str, extract_path: str) -> bool:
    """
    Извлечение содержимого PKG файла

    Args:
        pkg_path: Путь к PKG файлу
        extract_path: Путь для извлечения

    Returns:
        bool: True если извлечение успешно
    """
    try:
        logger.info(f"Извлечение PKG: {pkg_path} -> {extract_path}")

        # Создаем директорию для извлечения
        os.makedirs(extract_path, exist_ok=True)

        # Извлекаем через pkgutil
        result = subprocess.run(
            ["pkgutil", "--expand", pkg_path, extract_path], capture_output=True, text=True
        )

        if result.returncode != 0:
            raise RuntimeError(f"Ошибка извлечения PKG: {result.stderr}")

        logger.info("✅ PKG содержимое извлечено")
        return True

    except Exception as e:
        logger.error(f"❌ Ошибка извлечения PKG: {e}")
        raise RuntimeError(f"Ошибка извлечения PKG: {e}")


def find_app_in_pkg(extract_path: str, app_name: str = "Nexy.app") -> str | None:
    """
    Поиск .app файла в извлеченном PKG

    Args:
        extract_path: Путь к извлеченному PKG
        app_name: Имя искомого приложения

    Returns:
        str: Путь к .app файлу или None если не найден
    """
    try:
        logger.info(f"Поиск {app_name} в {extract_path}")

        # Рекурсивный поиск по всей структуре
        for root, dirs, files in os.walk(extract_path):
            for dir_name in dirs:
                if dir_name.endswith(".app"):
                    found_app = os.path.join(root, dir_name)
                    logger.info(f"✅ Найден .app файл: {found_app}")
                    return found_app

        logger.warning(f"❌ {app_name} не найден в PKG")
        return None

    except Exception as e:
        logger.error(f"Ошибка поиска .app файла в PKG: {e}")
        return None


def cleanup_pkg_extract(extract_path: str):
    """
    Очистка извлеченного PKG

    Args:
        extract_path: Путь к извлеченному PKG
    """
    try:
        import shutil

        if os.path.exists(extract_path):
            shutil.rmtree(extract_path)
            logger.info(f"Очищена директория извлечения: {extract_path}")
    except Exception as e:
        logger.error(f"Ошибка очистки извлеченного PKG: {e}")
