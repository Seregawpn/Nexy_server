#!/usr/bin/env python3
"""
Скрипт для централизованного обновления IP адреса сервера
Использование: python scripts/update_server_ip.py <новый_ip>
"""

import sys
import re
from pathlib import Path

def update_server_ip(new_ip: str):
    """Обновляет IP адрес сервера во всех местах конфигурации"""
    config_path = Path(__file__).parent.parent / "config" / "unified_config.yaml"
    
    if not config_path.exists():
        print(f"❌ Файл конфигурации не найден: {config_path}")
        return False
    
    # Читаем файл
    with open(config_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Валидация IP
    ip_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if not re.match(ip_pattern, new_ip):
        print(f"❌ Неверный формат IP адреса: {new_ip}")
        return False
    
    original_content = content
    updated_count = 0
    
    # Обновляем IP в grpc.servers.production.host
    pattern1 = r'(grpc:\s+servers:\s+production:\s+host:\s+)(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    if re.search(pattern1, content, re.MULTILINE):
        content = re.sub(pattern1, rf'\g<1>{new_ip}', content, flags=re.MULTILINE)
        updated_count += 1
        print(f"✅ Обновлен grpc.servers.production.host")
    
    # Обновляем IP в updater.default.appcast_url
    pattern2 = r'(appcast_url:\s+https://)(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(/updates/appcast\.xml)'
    if re.search(pattern2, content):
        content = re.sub(pattern2, rf'\g<1>{new_ip}\g<3>', content)
        updated_count += 1
        print(f"✅ Обновлен updater.default.appcast_url")
    
    # Обновляем IP в updater.default.manifest_url
    pattern3 = r'(manifest_url:\s+https://)(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(/updates/appcast\.xml)'
    if re.search(pattern3, content):
        content = re.sub(pattern3, rf'\g<1>{new_ip}\g<3>', content)
        updated_count += 1
        print(f"✅ Обновлен updater.default.manifest_url")
    
    # Обновляем IP в updater.default.channels.*.url
    pattern4 = r'(url:\s+https://)(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(/updates/appcast[^.]*\.xml)'
    matches = re.findall(pattern4, content)
    if matches:
        content = re.sub(pattern4, rf'\g<1>{new_ip}\g<3>', content)
        updated_count += len(matches)
        print(f"✅ Обновлено {len(matches)} каналов обновлений")
    
    # Обновляем IP в комментариях (если есть)
    pattern5 = r'(#.*?)(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(.*?)'
    # Более аккуратная замена в комментариях - только если это явно IP сервера
    comment_pattern = r'(#.*подключение к удаленному серверу\s+)(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(:443)'
    if re.search(comment_pattern, content):
        content = re.sub(comment_pattern, rf'\g<1>{new_ip}\g<3>', content)
        updated_count += 1
        print(f"✅ Обновлены комментарии")
    
    # Обновляем централизованную секцию server (если есть) - ПЕРВЫМ, чтобы anchor обновился
    pattern6 = r'(production_host:\s+&server_production_host\s+)(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    if re.search(pattern6, content):
        content = re.sub(pattern6, rf'\g<1>{new_ip}', content)
        updated_count += 1
        print(f"✅ Обновлен server.production_host (централизованное значение)")
    
    if content == original_content:
        print("⚠️  IP адрес не найден в конфигурации или уже установлен")
        if updated_count > 0:
            # Если были обновления, но контент не изменился - значит IP уже правильный
            print(f"✅ IP адрес уже установлен: {new_ip}")
            return True
        return False
    
    # Сохраняем файл
    with open(config_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n✅ Обновлено {updated_count} мест(а) в конфигурации")
    print(f"✅ Новый IP адрес: {new_ip}")
    return True

def main():
    if len(sys.argv) != 2:
        print("Использование: python scripts/update_server_ip.py <новый_ip>")
        print("Пример: python scripts/update_server_ip.py 20.63.24.187")
        sys.exit(1)
    
    new_ip = sys.argv[1]
    
    print("=" * 70)
    print("🔧 ОБНОВЛЕНИЕ IP АДРЕСА СЕРВЕРА")
    print("=" * 70)
    print(f"\n📋 Новый IP: {new_ip}\n")
    
    if update_server_ip(new_ip):
        print("\n" + "=" * 70)
        print("✅ ОБНОВЛЕНИЕ ЗАВЕРШЕНО")
        print("=" * 70)
        sys.exit(0)
    else:
        print("\n" + "=" * 70)
        print("❌ ОБНОВЛЕНИЕ НЕ ВЫПОЛНЕНО")
        print("=" * 70)
        sys.exit(1)

if __name__ == "__main__":
    main()
