"""
Основной класс системы обновлений
"""

import json
import tempfile
import os
import subprocess
from typing import Optional, Dict, Any
from packaging import version
from pathlib import Path
from .config import UpdaterConfig
from .net import UpdateHTTPClient
from .verify import sha256_checksum, verify_ed25519_signature, verify_app_signature
from .dmg import mount_dmg, unmount_dmg, find_app_in_dmg
from .pkg import install_pkg, verify_pkg_signature, extract_pkg_contents, find_app_in_pkg, cleanup_pkg_extract
from .replace import atomic_replace_app
from .migrate import get_user_app_path
import logging

logger = logging.getLogger(__name__)

class Updater:
    """Основной класс системы обновлений"""
    
    def __init__(self, config: UpdaterConfig):
        self.config = config
        self.http_client = UpdateHTTPClient(config.timeout, config.retries)
        self.on_download_progress = None
        self.on_install_progress = None
        # Настраиваем файловый логгер для апдейтера
        try:
            log_file = Path(self.config.get_log_path())
            if not any(
                isinstance(handler, logging.FileHandler)
                and Path(getattr(handler, "baseFilename", "")) == log_file
                for handler in logger.handlers
            ):
                log_file.parent.mkdir(parents=True, exist_ok=True)
                file_handler = logging.FileHandler(log_file, encoding="utf-8")
                file_handler.setLevel(logging.INFO)
                formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
                file_handler.setFormatter(formatter)
                logger.addHandler(file_handler)
        except Exception as log_err:
            logger.debug(f"Не удалось настроить файловый логгер обновлений: {log_err}")
    
    def get_current_build(self) -> str:
        """Получение текущего номера сборки (строка из Info.plist)"""
        try:
            import plistlib
            info_plist_path = os.path.join(get_user_app_path(), "Contents", "Info.plist")
            with open(info_plist_path, "rb") as f:
                plist = plistlib.load(f)
            build_value = plist.get("CFBundleVersion", "0")
            return str(build_value)
        except Exception:
            return "0"
    
    def check_for_updates(self) -> Optional[Dict[str, Any]]:
        """Проверка доступности обновлений"""
        try:
            manifest = self.http_client.get_manifest(self.config.manifest_url)
            current_build_str = self.get_current_build()
            latest_build_str = str(manifest.get("build", "0"))

            try:
                current_build = version.parse(current_build_str)
            except Exception:
                logger.warning(f"Не удалось распарсить текущую версию '{current_build_str}', используем 0")
                current_build = version.parse("0")

            try:
                latest_build = version.parse(latest_build_str)
            except Exception:
                logger.error(f"Не удалось распарсить версию манифеста '{latest_build_str}'")
                return None

            if latest_build > current_build:
                return manifest
            return None
        except Exception as e:
            logger.error(f"Ошибка проверки обновлений: {e}")
            return None
    
    def download_and_verify(self, artifact_info: Dict[str, Any]) -> str:
        """Скачивание и проверка артефакта"""
        artifact_type = artifact_info.get("type", "dmg")
        artifact_url = artifact_info["url"]
        expected_size = artifact_info.get("size")
        expected_sha256 = artifact_info.get("sha256")
        expected_signature = artifact_info.get("ed25519")
        
        # Создаем временный файл
        suffix = ".dmg" if artifact_type == "dmg" else ".zip"
        temp_file = tempfile.mktemp(suffix=suffix)
        
        logger.info(f"Скачивание {artifact_type}...")
        self.http_client.download_file(
            artifact_url,
            temp_file,
            expected_size,
            on_progress=self._report_download_progress,
        )
        
        # Проверяем SHA256
        if expected_sha256:
            actual_sha256 = sha256_checksum(temp_file)
            if actual_sha256.lower() != expected_sha256.lower():
                os.unlink(temp_file)
                raise RuntimeError("SHA256 хеш не совпадает")
        
        # Проверяем Ed25519 подпись
        if expected_signature and self.config.public_key:
            if not verify_ed25519_signature(temp_file, expected_signature, self.config.public_key):
                os.unlink(temp_file)
                raise RuntimeError("Ed25519 подпись неверна")
        
        return temp_file
    
    def install_update(self, artifact_path: str, artifact_info: Dict[str, Any]):
        """Установка обновления"""
        artifact_type = artifact_info.get("type", "dmg")
        user_app_path = get_user_app_path()
        
        self._report_install_progress("start", 0)

        if artifact_type == "dmg":
            mount_point = mount_dmg(artifact_path)
            try:
                new_app_path = find_app_in_dmg(mount_point)
                if not new_app_path:
                    raise RuntimeError("Не найден .app файл в DMG")
                
                # Проверяем подпись нового приложения
                if not verify_app_signature(new_app_path):
                    raise RuntimeError("Подпись нового приложения неверна")
                
                # Атомарно заменяем приложение
                self._report_install_progress("copy", 50)
                atomic_replace_app(new_app_path, user_app_path)
                
            finally:
                self._report_install_progress("unmount", 80)
                unmount_dmg(mount_point)
                self._report_install_progress("finish", 100)
                
        elif artifact_type == "pkg":
            # Установка PKG файла
            logger.info("Установка PKG файла...")
            
            # Проверяем подпись PKG
            if not verify_pkg_signature(artifact_path):
                logger.warning("PKG подпись не проверена, продолжаем установку")
            
            # Устанавливаем PKG
            self._report_install_progress("install", 50)
            install_pkg(artifact_path)
            
            # PKG устанавливается в /Applications, поэтому просто перезапускаем
            logger.info("PKG установлен, приложение будет перезапущено")
            self._report_install_progress("finish", 100)
            
        else:
            # ZIP файл - аналогично, но с распаковкой
            raise NotImplementedError(f"Тип файла {artifact_type} пока не поддерживается")
        
        # Удаляем временный файл
        os.unlink(artifact_path)
    
    def relaunch_app(self):
        """Перезапуск приложения"""
        user_app_path = get_user_app_path()
        logger.info("🔁 Updater: relaunching app after update, exiting current process")
        subprocess.Popen(["/usr/bin/open", "-a", user_app_path])
        os._exit(0)
    
    def update(self) -> bool:
        """Полный цикл обновления"""
        try:
            # Проверяем обновления
            manifest = self.check_for_updates()
            if not manifest:
                return False
            
            logger.info(f"Найдено обновление до версии {manifest.get('version')}")
            
            # Скачиваем и проверяем
            artifact_path = self.download_and_verify(manifest["artifact"])
            
            # Устанавливаем
            self.install_update(artifact_path, manifest["artifact"])
            
            # Перезапускаем
            self.relaunch_app()
            
            return True
            
        except Exception as e:
            logger.error(f"Ошибка обновления: {e}")
            return False

    def _report_download_progress(self, downloaded: int, expected_size: Optional[int]) -> None:
        if not callable(self.on_download_progress):
            return
        try:
            self.on_download_progress(downloaded, expected_size)
        except Exception as callback_error:
            logger.debug(f"download progress callback error: {callback_error}")

    def _report_install_progress(self, stage: str, percent: int) -> None:
        if not callable(self.on_install_progress):
            return
        try:
            self.on_install_progress(stage, percent)
        except Exception as callback_error:
            logger.debug(f"install progress callback error: {callback_error}")
