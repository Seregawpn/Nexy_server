"""
Атомарная замена приложений с возможностью отката
"""

import logging
import os
import shutil
import subprocess

logger = logging.getLogger(__name__)


def atomic_replace_app(new_app_path: str, target_app_path: str):
    """
    Атомарная замена приложения с возможностью отката.

    Если target_app_path не существует (первая установка), приложение
    копируется напрямую без создания backup.

    Args:
        new_app_path: Путь к новому приложению
        target_app_path: Путь к целевому приложению
    """
    target_exists = os.path.exists(target_app_path)
    backup_path = target_app_path + ".backup"

    logger.info(f"Атомарная замена: {new_app_path} -> {target_app_path}")

    try:
        # Удаляем старый backup если есть
        if os.path.exists(backup_path):
            shutil.rmtree(backup_path, ignore_errors=True)

        if target_exists:
            # Создаем backup текущего приложения
            os.rename(target_app_path, backup_path)
            logger.info(f"Создан backup: {backup_path}")
        else:
            # Первая установка — убеждаемся, что родительская директория существует
            os.makedirs(os.path.dirname(target_app_path), exist_ok=True)
            logger.info("Target app absent — fresh install (no backup needed)")

        # Копируем новое приложение
        subprocess.check_call(["/usr/bin/ditto", new_app_path, target_app_path])
        logger.info("✅ Приложение успешно обновлено")

        # Удаляем backup при успехе
        if target_exists:
            shutil.rmtree(backup_path, ignore_errors=True)

    except Exception as e:
        logger.error(f"❌ Ошибка обновления: {e}")

        if target_exists:
            # Откатываемся при ошибке — восстанавливаем из backup
            if os.path.exists(target_app_path):
                shutil.rmtree(target_app_path, ignore_errors=True)
            if os.path.exists(backup_path):
                os.rename(backup_path, target_app_path)
                logger.info("Выполнен откат к предыдущей версии")
        else:
            # Первая установка провалилась — убираем частичную копию
            if os.path.exists(target_app_path):
                shutil.rmtree(target_app_path, ignore_errors=True)
                logger.info("Partial install cleaned up")

        raise
