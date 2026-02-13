#!/usr/bin/env python3
"""
Генерация манифеста обновлений
"""

import argparse
import os
import json
import hashlib
import sys
import re
from typing import Optional
from datetime import datetime
from sign_file import sign_file

VERSION_PATTERN = re.compile(r"^\d+\.\d+\.\d+$")

def calculate_sha256(file_path: str) -> str:
    """Вычисление SHA256 хеша файла"""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()

def generate_manifest(artifact_path: str, version: str, build: str,
                     artifact_type: str = "dmg", private_key_path: Optional[str] = None,
                     notes_url: Optional[str] = None, critical: bool = False) -> dict:
    """
    Генерация манифеста обновлений
    
    Args:
        artifact_path: Путь к артефакту (DMG/ZIP)
        version: Версия приложения (например, "2.6.0")
        build: Номер сборки (по умолчанию равен версии)
        artifact_type: Тип артефакта ("dmg" или "zip")
        private_key_path: Путь к приватному ключу для подписи
        notes_url: URL с заметками о версии
        critical: Критическое ли обновление
        
    Returns:
        dict: Манифест обновлений
    """
    
    if not os.path.exists(artifact_path):
        raise FileNotFoundError(f"Артефакт не найден: {artifact_path}")
    
    # Получаем информацию о файле
    file_size = os.path.getsize(artifact_path)
    sha256_hash = calculate_sha256(artifact_path)
    
    # Генерируем URL (в реальном проекте будет из конфигурации)
    filename = os.path.basename(artifact_path)
    artifact_url = f"https://updates.nexy.ai/artifacts/{filename}"
    
    # Создаем базовый манифест
    manifest = {
        "version": version,
        "build": build,
        "release_date": datetime.utcnow().isoformat() + "Z",
        "artifact": {
            "type": artifact_type,
            "url": artifact_url,
            "size": file_size,
            "sha256": sha256_hash,
            "arch": "arm64",
            "min_os": "11.0"
        },
        "critical": critical,
        "auto_install": not critical  # Критические обновления требуют подтверждения
    }
    
    # Добавляем Ed25519 подпись если есть ключ
    if private_key_path and os.path.exists(private_key_path):
        try:
            ed25519_signature = sign_file(artifact_path, private_key_path)
            manifest["artifact"]["ed25519"] = ed25519_signature
            print(f"✅ Артефакт подписан Ed25519")
        except Exception as e:
            print(f"⚠️ Не удалось подписать артефакт: {e}")
    
    # Добавляем URL заметок если указан
    if notes_url:
        manifest["notes_url"] = notes_url
    
    return manifest

def save_manifest(manifest: dict, output_path: str):
    """Сохранение манифеста в файл"""
    
    # Создаем директорию если нужно
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Сохраняем с красивым форматированием
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Манифест сохранен: {output_path}")

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Генерация update-манифеста (size/sha256 вычисляются автоматически)"
    )
    parser.add_argument("artifact_path", help="Путь к артефакту (DMG/ZIP)")
    parser.add_argument("version", help="Версия приложения в формате X.Y.Z")
    parser.add_argument(
        "--build",
        help="Номер сборки. Если не указан, используется значение version.",
    )
    parser.add_argument(
        "--type",
        dest="artifact_type",
        default="dmg",
        help="Тип артефакта (по умолчанию: dmg)",
    )
    parser.add_argument(
        "--private-key",
        dest="private_key_path",
        help="Путь к приватному ключу для Ed25519 подписи",
    )
    parser.add_argument(
        "--notes-url",
        dest="notes_url",
        help="URL заметок к релизу",
    )
    parser.add_argument(
        "--critical",
        action="store_true",
        help="Пометить обновление как критическое",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    artifact_path = args.artifact_path
    version = args.version
    build = args.build or version
    artifact_type = args.artifact_type
    private_key_path = args.private_key_path
    notes_url = args.notes_url
    critical = args.critical

    if not VERSION_PATTERN.match(version):
        print(f"❌ Неверный формат версии: {version}. Ожидается X.Y.Z")
        sys.exit(1)
    
    try:
        # Генерируем манифест
        manifest = generate_manifest(
            artifact_path=artifact_path,
            version=version,
            build=build,
            artifact_type=artifact_type,
            private_key_path=private_key_path,
            notes_url=notes_url,
            critical=critical,
        )
        
        # Сохраняем манифест
        manifests_dir = os.path.join(os.path.dirname(__file__), "..", "manifests")
        output_path = os.path.join(manifests_dir, "manifest.json")
        save_manifest(manifest, output_path)
        
        print(f"📋 Манифест для версии {version} (сборка {build}) создан")
        print("ℹ️ Поля artifact.size и artifact.sha256 рассчитаны автоматически")
        
    except Exception as e:
        print(f"❌ Ошибка генерации манифеста: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
