#!/usr/bin/env python3
"""
Тестовый скрипт для проверки конфигурации Azure OpenAI
Проверяет различные форматы запросов и помогает диагностировать ошибки
"""

import json
import os
import sys
import requests
from typing import Dict, Optional, Tuple


class AzureOpenAITester:
    """Класс для тестирования Azure OpenAI конфигурации"""
    
    def __init__(self, base_url: str, deployment_name: str, api_key: str):
        self.base_url = base_url.rstrip('/')
        self.deployment_name = deployment_name
        self.api_key = api_key
        self.api_version = "2024-02-15-preview"
        
    def test_format_1_url_only(self) -> Tuple[bool, Dict]:
        """
        Формат 1: Deployment name только в URL (стандартный Azure OpenAI формат)
        """
        url = f"{self.base_url}/openai/deployments/{self.deployment_name}/chat/completions?api-version={self.api_version}"
        
        payload = {
            "messages": [
                {"role": "user", "content": "Hello, test message"}
            ],
            "max_tokens": 10
        }
        
        return self._make_request(url, payload, "URL-only format")
    
    def test_format_2_with_model_in_body(self) -> Tuple[bool, Dict]:
        """
        Формат 2: Deployment name в URL + model в body (для некоторых клиентов)
        """
        url = f"{self.base_url}/openai/deployments/{self.deployment_name}/chat/completions?api-version={self.api_version}"
        
        payload = {
            "model": self.deployment_name,  # Добавляем model в body
            "messages": [
                {"role": "user", "content": "Hello, test message"}
            ],
            "max_tokens": 10
        }
        
        return self._make_request(url, payload, "URL + model in body format")
    
    def test_format_3_openai_compatible(self) -> Tuple[bool, Dict]:
        """
        Формат 3: OpenAI-совместимый формат (model только в body)
        """
        url = f"{self.base_url}/openai/chat/completions?api-version={self.api_version}"
        
        payload = {
            "model": self.deployment_name,  # Model в body
            "messages": [
                {"role": "user", "content": "Hello, test message"}
            ],
            "max_tokens": 10
        }
        
        return self._make_request(url, payload, "OpenAI-compatible format")
    
    def _make_request(self, url: str, payload: Dict, format_name: str) -> Tuple[bool, Dict]:
        """Выполняет HTTP запрос и возвращает результат"""
        headers = {
            "Content-Type": "application/json",
            "api-key": self.api_key
        }
        
        try:
            print(f"\n🧪 Тестирую формат: {format_name}")
            print(f"   URL: {url}")
            print(f"   Payload: {json.dumps(payload, indent=2, ensure_ascii=False)}")
            
            response = requests.post(url, json=payload, headers=headers, timeout=10)
            
            result = {
                "success": response.status_code == 200,
                "status_code": response.status_code,
                "format": format_name,
                "url": url,
                "payload": payload
            }
            
            try:
                result["response"] = response.json()
            except:
                result["response"] = response.text
            
            if result["success"]:
                print(f"   ✅ УСПЕХ! HTTP {response.status_code}")
            else:
                print(f"   ❌ ОШИБКА! HTTP {response.status_code}")
                if isinstance(result["response"], dict):
                    error_info = result["response"].get("error", {})
                    print(f"   Тип ошибки: {error_info.get('type', 'unknown')}")
                    print(f"   Причина: {error_info.get('reason', 'unknown')}")
                    print(f"   Сообщение: {error_info.get('message', 'unknown')}")
            
            return result["success"], result
            
        except requests.exceptions.RequestException as e:
            print(f"   ❌ ОШИБКА СЕТИ: {e}")
            return False, {
                "success": False,
                "error": str(e),
                "format": format_name,
                "url": url
            }
    
    def test_all_formats(self) -> Dict:
        """Тестирует все форматы и возвращает результаты"""
        print("=" * 70)
        print("🔍 ТЕСТИРОВАНИЕ КОНФИГУРАЦИИ AZURE OPENAI")
        print("=" * 70)
        print(f"\n📋 Конфигурация:")
        print(f"   Base URL: {self.base_url}")
        print(f"   Deployment Name: {self.deployment_name}")
        print(f"   API Key: {self.api_key[:10]}...{self.api_key[-4:]}")
        print(f"   API Version: {self.api_version}")
        
        results = {}
        
        # Тест 1: Стандартный формат Azure OpenAI
        success, result = self.test_format_1_url_only()
        results["format_1_url_only"] = result
        
        # Тест 2: С model в body
        success, result = self.test_format_2_with_model_in_body()
        results["format_2_with_model"] = result
        
        # Тест 3: OpenAI-совместимый формат
        success, result = self.test_format_3_openai_compatible()
        results["format_3_openai_compatible"] = result
        
        return results
    
    def print_summary(self, results: Dict):
        """Выводит итоговую сводку"""
        print("\n" + "=" * 70)
        print("📊 ИТОГОВАЯ СВОДКА")
        print("=" * 70)
        
        working_formats = []
        failed_formats = []
        
        for format_name, result in results.items():
            if result.get("success"):
                working_formats.append((format_name, result))
            else:
                failed_formats.append((format_name, result))
        
        if working_formats:
            print("\n✅ РАБОТАЮЩИЕ ФОРМАТЫ:")
            for format_name, result in working_formats:
                print(f"   • {result.get('format', format_name)}")
                print(f"     HTTP {result.get('status_code')}")
        
        if failed_formats:
            print("\n❌ НЕРАБОТАЮЩИЕ ФОРМАТЫ:")
            for format_name, result in failed_formats:
                print(f"   • {result.get('format', format_name)}")
                print(f"     HTTP {result.get('status_code')}")
                if isinstance(result.get("response"), dict):
                    error = result["response"].get("error", {})
                    print(f"     Ошибка: {error.get('message', 'unknown')}")
        
        print("\n" + "=" * 70)
        
        if working_formats:
            print("✅ РЕКОМЕНДАЦИЯ: Используйте один из работающих форматов выше")
            print("   Для Cursor: проверьте настройки Base URL и Deployment Name")
        else:
            print("❌ ПРОБЛЕМА: Ни один формат не работает")
            print("\n🔧 ЧТО ПРОВЕРИТЬ:")
            print("   1. Правильность API ключа в Azure Portal")
            print("   2. Правильность Deployment Name (регистр важен!)")
            print("   3. Правильность Base URL")
            print("   4. Доступность Azure OpenAI сервиса")
            print("   5. Наличие развертывания в Azure Portal")


def main():
    """Главная функция"""
    # Сначала проверяем аргументы командной строки
    if len(sys.argv) > 1:
        base_url = sys.argv[1]
    else:
        base_url = os.getenv("AZURE_OPENAI_BASE_URL", "https://nexy-ai-core.openai.azure.com")
    
    if len(sys.argv) > 2:
        deployment_name = sys.argv[2]
    else:
        deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "OpenAICreate-2026011")
    
    if len(sys.argv) > 3:
        api_key = sys.argv[3]
    else:
        api_key = os.getenv("AZURE_OPENAI_API_KEY", "")
    
    # Если ключ не передан через env или аргументы, запрашиваем его (только в интерактивном режиме)
    if not api_key:
        if sys.stdin.isatty():  # Проверяем, что это интерактивный терминал
            print("⚠️  API ключ не найден в переменной окружения AZURE_OPENAI_API_KEY")
            api_key = input("📝 Введите ваш API ключ: ").strip()
        else:
            print("❌ API ключ не указан. Используйте переменную окружения или аргументы командной строки.")
            sys.exit(1)
    
    if not api_key:
        print("❌ API ключ не указан. Выход.")
        sys.exit(1)
    
    # Создаем тестер и запускаем тесты
    tester = AzureOpenAITester(base_url, deployment_name, api_key)
    results = tester.test_all_formats()
    tester.print_summary(results)
    
    # Возвращаем код выхода
    has_success = any(r.get("success") for r in results.values())
    sys.exit(0 if has_success else 1)


if __name__ == "__main__":
    main()
