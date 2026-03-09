"""
Manifest Provider - управление манифестами версий
"""

import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any, Optional, List

logger = logging.getLogger(__name__)


class ManifestProvider:
    """Провайдер для управления манифестами версий"""

    PRIMARY_MANIFEST_NAME = "manifest.json"
    CHANNEL_MANIFESTS = {
        "stable": "manifest.json",
        "beta": "manifest_beta.json",
    }
    
    def __init__(self, config):
        self.config = config
        self.manifests_dir = Path(config.manifests_dir)
    
    async def initialize(self) -> bool:
        """Инициализация провайдера"""
        try:
            logger.info("🔧 Инициализация ManifestProvider...")
            
            # Создаем директорию манифестов если не существует
            self.manifests_dir.mkdir(parents=True, exist_ok=True)
            
            return True
        except Exception as e:
            logger.error(f"❌ Ошибка инициализации ManifestProvider: {e}")
            return False
    
    def create_manifest(self, version: str, build: str, artifact_info: Dict[str, Any]) -> Dict[str, Any]:
        """
        Создание манифеста для версии
        
        Args:
            version: Версия приложения
            build: Номер сборки
            artifact_info: Информация об артефакте
            
        Returns:
            Dict[str, Any]: Созданный манифест
        """
        manifest = {
            "version": version,
            "build": build,
            "release_date": datetime.now(timezone.utc).isoformat(),
            "artifact": {
                "type": artifact_info.get("type", "dmg"),
                "url": artifact_info.get("url", ""),
                "size": artifact_info.get("size", 0),
                "sha256": artifact_info.get("sha256", ""),
                "arch": artifact_info.get("arch", self.config.default_arch),
                "min_os": artifact_info.get("min_os", self.config.default_min_os),
                "ed25519": artifact_info.get("ed25519", "")
            },
            "critical": artifact_info.get("critical", False),
            "auto_install": artifact_info.get("auto_install", True),
            "notes_url": artifact_info.get("notes_url", "")
        }
        
        return manifest
    
    def save_manifest(self, manifest: Dict[str, Any], filename: Optional[str] = None) -> str:
        """
        Сохранение манифеста в файл
        
        Args:
            manifest: Манифест для сохранения
            filename: Имя файла (если не указано, генерируется автоматически)
            
        Returns:
            str: Путь к сохраненному файлу
        """
        if filename is None:
            filename = self.PRIMARY_MANIFEST_NAME
        
        file_path = self.manifests_dir / filename
        
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(manifest, f, indent=2, ensure_ascii=False)
            
            logger.info(f"✅ Манифест сохранен: {file_path}")
            return str(file_path)
            
        except Exception as e:
            logger.error(f"❌ Ошибка сохранения манифеста: {e}")
            raise
    
    def load_manifest(self, filename: str) -> Optional[Dict[str, Any]]:
        """
        Загрузка манифеста из файла
        
        Args:
            filename: Имя файла манифеста
            
        Returns:
            Optional[Dict[str, Any]]: Загруженный манифест или None
        """
        file_path = self.manifests_dir / filename
        
        if not file_path.exists():
            logger.warning(f"⚠️ Манифест не найден: {file_path}")
            return None
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                manifest = json.load(f)
            
            logger.info(f"✅ Манифест загружен: {file_path}")
            return manifest
            
        except Exception as e:
            logger.error(f"❌ Ошибка загрузки манифеста {file_path}: {e}")
            return None
    
    def get_latest_manifest(self) -> Optional[Dict[str, Any]]:
        """
        Получение последнего манифеста
        
        Returns:
            Optional[Dict[str, Any]]: Последний манифест или None
        """
        try:
            primary_manifest = self.load_manifest(self.PRIMARY_MANIFEST_NAME)
            if primary_manifest:
                return primary_manifest

            # Legacy fallback: versioned manifests are no longer primary owner.
            manifest_files = list(self.manifests_dir.glob("manifest_*.json"))
            if not manifest_files:
                logger.info("📄 Манифесты не найдены")
                return None

            manifest_files.sort(key=lambda x: x.stat().st_mtime, reverse=True)
            latest_file = manifest_files[0]
            logger.warning(
                "⚠️ Используется legacy manifest owner path: %s. "
                "Рекомендуется использовать только manifest.json",
                latest_file.name,
            )
            return self.load_manifest(latest_file.name)
            
        except Exception as e:
            logger.error(f"❌ Ошибка получения последнего манифеста: {e}")
            return None

    def get_manifest_for_channel(self, channel: str) -> Optional[Dict[str, Any]]:
        """
        Получение манифеста с учетом канала обновлений.

        stable -> manifest.json
        beta -> manifest_beta.json
        """
        try:
            normalized = (channel or "stable").strip().lower()
            filename = self.CHANNEL_MANIFESTS.get(normalized)
            if filename is None:
                logger.warning("⚠️ Неизвестный канал '%s', fallback на stable", channel)
                filename = self.PRIMARY_MANIFEST_NAME

            manifest = self.load_manifest(filename)
            if manifest:
                return manifest

            if filename != self.PRIMARY_MANIFEST_NAME:
                logger.warning(
                    "⚠️ Манифест канала %s (%s) не найден, fallback на stable",
                    normalized,
                    filename,
                )
                return self.load_manifest(self.PRIMARY_MANIFEST_NAME)

            return self.get_latest_manifest()
        except Exception as e:
            logger.error(f"❌ Ошибка получения манифеста канала {channel}: {e}")
            return None
    
    def get_all_manifests(self) -> List[Dict[str, Any]]:
        """
        Получение всех манифестов
        
        Returns:
            List[Dict[str, Any]]: Список всех манифестов
        """
        manifests = []
        
        try:
            primary = self.load_manifest(self.PRIMARY_MANIFEST_NAME)
            if primary:
                manifests.append(primary)

            manifest_files = list(self.manifests_dir.glob("manifest_*.json"))
            
            for manifest_file in manifest_files:
                manifest = self.load_manifest(manifest_file.name)
                if manifest:
                    manifests.append(manifest)
            
            # Сортируем по версии (новые сначала)
            def version_key(data: Dict[str, Any]) -> tuple:
                version_str = str(data.get("version", "0.0.0"))
                try:
                    major, minor, patch = [int(part) for part in version_str.split('.')]
                    return major, minor, patch
                except ValueError:
                    return 0, 0, 0

            manifests.sort(key=version_key, reverse=True)
            
            return manifests
            
        except Exception as e:
            logger.error(f"❌ Ошибка получения всех манифестов: {e}")
            return []
    
    def validate_manifest(self, manifest: Dict[str, Any]) -> bool:
        """
        Валидация манифеста
        
        Args:
            manifest: Манифест для валидации
            
        Returns:
            bool: True если манифест валиден
        """
        required_fields = ["version", "build", "artifact"]
        
        # Проверяем обязательные поля
        for field in required_fields:
            if field not in manifest:
                logger.error(f"❌ Отсутствует обязательное поле: {field}")
                return False
        
        # Проверяем artifact
        artifact = manifest.get("artifact", {})
        artifact_required = ["type", "url", "size", "sha256"]
        
        for field in artifact_required:
            if field not in artifact:
                logger.error(f"❌ Отсутствует обязательное поле artifact: {field}")
                return False
        
        # Проверяем версию
        version = manifest.get("version", "")
        if not version or not isinstance(version, str):
            logger.error("❌ Неверная версия")
            return False
        
        # Проверяем номер сборки
        build = manifest.get("build", 0)
        # Build в проекте хранится как строка версии (например, "1.6.1.35"),
        # но поддерживаем и int для обратной совместимости.
        if isinstance(build, int):
            if build <= 0:
                logger.error("❌ Неверный номер сборки")
                return False
        elif isinstance(build, str):
            if not build.strip():
                logger.error("❌ Неверный номер сборки")
                return False
        else:
            logger.error("❌ Неверный номер сборки")
            return False

        artifact_url = str(artifact.get("url", "")).strip()
        if not artifact_url.startswith("https://"):
            logger.error("❌ Artifact URL должен использовать HTTPS")
            return False
        if artifact_url.endswith("/appcast.xml") or artifact_url.endswith("/appcast-beta.xml"):
            logger.error("❌ Artifact URL не должен указывать на appcast feed")
            return False
        
        logger.info(f"✅ Манифест валиден: {version} (build {build})")
        return True
    
    def update_manifest(self, filename: str, updates: Dict[str, Any]) -> bool:
        """
        Обновление манифеста
        
        Args:
            filename: Имя файла манифеста
            updates: Обновления для применения
            
        Returns:
            bool: True если обновление прошло успешно
        """
        try:
            manifest = self.load_manifest(filename)
            if not manifest:
                return False
            
            # Применяем обновления
            for key, value in updates.items():
                if key == "artifact" and isinstance(value, dict):
                    # Обновляем artifact рекурсивно
                    artifact = manifest.get("artifact", {})
                    artifact.update(value)
                    manifest["artifact"] = artifact
                else:
                    manifest[key] = value
            
            # Обновляем дату релиза
            manifest["release_date"] = datetime.now(timezone.utc).isoformat()
            
            # Сохраняем обновленный манифест
            self.save_manifest(manifest, filename)
            
            logger.info(f"✅ Манифест обновлен: {filename}")
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка обновления манифеста {filename}: {e}")
            return False
    
    def delete_manifest(self, filename: str) -> bool:
        """
        Удаление манифеста
        
        Args:
            filename: Имя файла манифеста
            
        Returns:
            bool: True если удаление прошло успешно
        """
        try:
            file_path = self.manifests_dir / filename
            
            if not file_path.exists():
                logger.warning(f"⚠️ Манифест не найден для удаления: {file_path}")
                return False
            
            file_path.unlink()
            logger.info(f"✅ Манифест удален: {file_path}")
            return True
            
        except Exception as e:
            logger.error(f"❌ Ошибка удаления манифеста {filename}: {e}")
            return False
    
    async def stop(self) -> bool:
        """Остановка провайдера"""
        try:
            logger.info("🛑 Остановка ManifestProvider...")
            return True
        except Exception as e:
            logger.error(f"❌ Ошибка остановки ManifestProvider: {e}")
            return False
    
    def get_status(self) -> Dict[str, Any]:
        """Получение статуса провайдера"""
        try:
            manifests_count = len(list(self.manifests_dir.glob("manifest_*.json")))
            if (self.manifests_dir / self.PRIMARY_MANIFEST_NAME).exists():
                manifests_count += 1
            latest_manifest = self.get_latest_manifest()
            
            return {
                "status": "running",
                "provider": "manifest",
                "manifests_dir": str(self.manifests_dir),
                "manifests_count": manifests_count,
                "latest_version": latest_manifest.get("version") if latest_manifest else None,
                "latest_build": latest_manifest.get("build") if latest_manifest else None
            }
        except Exception as e:
            logger.error(f"❌ Ошибка получения статуса ManifestProvider: {e}")
            return {
                "status": "error",
                "provider": "manifest",
                "error": str(e)
            }
