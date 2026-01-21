#!/usr/bin/env python3
"""
Скрипт для быстрого открытия Azure Portal и Azure OpenAI Studio
"""

import sys
import subprocess
import webbrowser
from urllib.parse import quote


def open_azure_portal(resource_name: str, resource_group: str = None):
    """Открывает Azure Portal с нужным ресурсом"""
    if resource_group:
        url = f"https://portal.azure.com/#@/resource/subscriptions/*/resourceGroups/{resource_group}/providers/Microsoft.CognitiveServices/accounts/{resource_name}/overview"
    else:
        # Пробуем найти ресурс через поиск
        url = f"https://portal.azure.com/#view/Microsoft_Azure_ProjectOxford/CognitiveServicesHub/~/search/{quote(resource_name)}"
    
    print(f"🌐 Открываю Azure Portal для ресурса: {resource_name}")
    webbrowser.open(url)


def open_azure_openai_studio(resource_name: str):
    """Открывает Azure OpenAI Studio"""
    url = f"https://oai.azure.com/portal/{resource_name}/deployments"
    print(f"🌐 Открываю Azure OpenAI Studio для ресурса: {resource_name}")
    webbrowser.open(url)


def main():
    """Главная функция"""
    resource_name = "nexy-ai-core-01"
    resource_group = "NetworkWatcherRG"
    
    if len(sys.argv) > 1:
        resource_name = sys.argv[1]
    if len(sys.argv) > 2:
        resource_group = sys.argv[2]
    
    print("=" * 70)
    print("🚀 БЫСТРОЕ ОТКРЫТИЕ AZURE PORTAL")
    print("=" * 70)
    print(f"\n📋 Ресурс: {resource_name}")
    if resource_group:
        print(f"📋 Группа ресурсов: {resource_group}")
    print()
    
    # Открываем оба портала автоматически
    print("🌐 Открываю Azure Portal и Azure OpenAI Studio...")
    print()
    
    open_azure_portal(resource_name, resource_group)
    open_azure_openai_studio(resource_name)
    
    print("\n✅ Готово! Портал должен открыться в браузере.")
    print("\n💡 Следующие шаги:")
    print("   1. В Azure Portal → Model deployments → Create")
    print("   2. Или в Azure OpenAI Studio → Deployments → + Create")
    print("   3. Выберите модель (например, gpt-4o)")
    print("   4. Укажите имя развертывания (например, gpt-4o)")
    print("   5. Дождитесь статуса 'Succeeded'")


if __name__ == "__main__":
    main()
