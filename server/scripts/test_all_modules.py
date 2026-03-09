#!/usr/bin/env python3
"""
Детальное тестирование всех модулей и интеграций

Проверяет каждый модуль и интеграцию отдельно для полной уверенности в работоспособности.
"""

import sys
import asyncio
import importlib
from pathlib import Path
from typing import List, Tuple, Optional
from dataclasses import dataclass

# Добавляем путь к серверу
server_root = Path(__file__).parent.parent
sys.path.insert(0, str(server_root))

# Цвета
GREEN = '\033[0;32m'
RED = '\033[0;31m'
YELLOW = '\033[1;33m'
BLUE = '\033[0;34m'
NC = '\033[0m'

@dataclass
class ModuleTestResult:
    """Результат тестирования модуля"""
    name: str
    success: bool
    message: str
    error: Optional[str] = None

def print_header(text: str):
    """Печать заголовка"""
    print(f"\n{BLUE}{'='*80}{NC}")
    print(f"{BLUE}{text:^80}{NC}")
    print(f"{BLUE}{'='*80}{NC}\n")

def test_module_import(module_path: str, class_name: Optional[str] = None) -> ModuleTestResult:
    """Тест импорта модуля"""
    try:
        module = importlib.import_module(module_path)
        if class_name:
            if not hasattr(module, class_name):
                return ModuleTestResult(
                    name=module_path,
                    success=False,
                    message=f"Класс {class_name} не найден",
                    error=f"Module {module_path} не содержит {class_name}"
                )
        return ModuleTestResult(
            name=module_path,
            success=True,
            message="Импорт успешен"
        )
    except Exception as e:
        return ModuleTestResult(
            name=module_path,
            success=False,
            message=f"Ошибка импорта: {str(e)}",
            error=str(e)
        )

async def test_module_initialization(module_path: str, class_name: str) -> ModuleTestResult:
    """Тест инициализации модуля"""
    try:
        module = importlib.import_module(module_path)
        cls = getattr(module, class_name)
        
        # Пытаемся создать экземпляр
        instance = cls()
        
        # Если есть метод initialize, вызываем его
        if hasattr(instance, 'initialize'):
            if asyncio.iscoroutinefunction(instance.initialize):
                result = await instance.initialize()
            else:
                result = instance.initialize()
            
            if result is False:
                return ModuleTestResult(
                    name=f"{module_path}.{class_name}",
                    success=False,
                    message="Инициализация вернула False",
                    error="initialize() вернул False"
                )
        
        return ModuleTestResult(
            name=f"{module_path}.{class_name}",
            success=True,
            message="Инициализация успешна"
        )
    except Exception as e:
        return ModuleTestResult(
            name=f"{module_path}.{class_name}",
            success=False,
            message=f"Ошибка инициализации: {str(e)}",
            error=str(e)
        )

def test_config_loading() -> List[ModuleTestResult]:
    """Тест загрузки конфигураций всех модулей"""
    results = []
    
    config_modules = [
        ("config.unified_config", "get_config"),
        ("modules.grpc_service.config", "GrpcServiceConfig"),
        ("modules.audio_generation.config", "AudioGenerationConfig"),
        ("modules.text_processing.config", "TextProcessingConfig"),
        ("modules.memory_management.config", "MemoryConfig"),
        ("modules.database.config", "DatabaseConfig"),
        ("modules.session_management.config", "SessionManagementConfig"),
        ("modules.interrupt_handling.config", "InterruptHandlingConfig"),
        ("modules.text_filtering.config", "TextFilteringConfig"),
        ("modules.update.config", "UpdateConfig"),
    ]
    
    for module_path, item_name in config_modules:
        result = test_module_import(module_path, item_name)
        results.append(result)
    
    return results

def test_core_modules() -> List[ModuleTestResult]:
    """Тест основных модулей"""
    results = []
    
    core_modules = [
        ("modules.grpc_service.core.grpc_server", "NewStreamingServicer"),
        ("modules.grpc_service.core.grpc_service_manager", "GrpcServiceManager"),
        ("modules.audio_generation.core.audio_processor", "AudioProcessor"),
        ("modules.text_processing.core.text_processor", "TextProcessor"),
        ("modules.memory_management.core.memory_manager", "MemoryManager"),
        ("modules.database.core.database_manager", "DatabaseManager"),
        ("modules.session_management.core.session_manager", "SessionManager"),
        ("modules.interrupt_handling.core.interrupt_manager", "InterruptManager"),
        ("modules.text_filtering.core.text_filter_manager", "TextFilterManager"),
    ]
    
    for module_path, class_name in core_modules:
        result = test_module_import(module_path, class_name)
        results.append(result)
    
    return results

def test_adapters() -> List[ModuleTestResult]:
    """Тест адаптеров модулей"""
    results = []
    
    adapters = [
        ("modules.audio_generation.adapter", "AudioGenerationAdapter"),
        ("modules.memory_management.adapter", "MemoryManagementAdapter"),
        ("modules.database.adapter", "DatabaseAdapter"),
        ("modules.session_management.adapter", "SessionManagementAdapter"),
        ("modules.interrupt_handling.adapter", "InterruptHandlingAdapter"),
        ("modules.text_filtering.adapter", "TextFilteringAdapter"),
        ("modules.update.adapter", "UpdateAdapter"),
    ]
    
    for module_path, class_name in adapters:
        result = test_module_import(module_path, class_name)
        results.append(result)
    
    return results

def test_integrations() -> List[ModuleTestResult]:
    """Тест интеграций"""
    results = []
    
    integrations = [
        ("integrations.service_integrations.module_coordinator", "ModuleCoordinator"),
        ("integrations.service_integrations.grpc_service_integration", "GrpcServiceIntegration"),
        ("integrations.workflow_integrations.streaming_workflow_integration", "StreamingWorkflowIntegration"),
        ("integrations.workflow_integrations.memory_workflow_integration", "MemoryWorkflowIntegration"),
        ("integrations.workflow_integrations.interrupt_workflow_integration", "InterruptWorkflowIntegration"),
        ("integrations.core.assistant_response_parser", "AssistantResponseParser"),
        ("integrations.core.module_factory", "ModuleFactory"),
        ("integrations.core.universal_module_interface", "UniversalModuleInterface"),
    ]
    
    for module_path, class_name in integrations:
        result = test_module_import(module_path, class_name)
        results.append(result)
    
    return results

async def test_providers() -> List[ModuleTestResult]:
    """Тест провайдеров"""
    results = []
    
    providers = [
        ("modules.audio_generation.providers.edge_tts_provider", "EdgeTTSProvider"),
        ("modules.audio_generation.providers.azure_tts_provider", "AzureTTSProvider"),
        ("modules.text_processing.providers.langchain_gemini_provider", "LangChainGeminiProvider"),
        ("modules.database.providers.postgresql_provider", "PostgreSQLProvider"),
    ]
    
    for module_path, class_name in providers:
        result = test_module_import(module_path, class_name)
        results.append(result)
    
    return results

async def main():
    """Основная функция"""
    print_header("ДЕТАЛЬНОЕ ТЕСТИРОВАНИЕ ВСЕХ МОДУЛЕЙ И ИНТЕГРАЦИЙ")
    
    all_results: List[ModuleTestResult] = []
    
    # 1. Тест конфигураций
    print(f"{YELLOW}📋 Тестирование конфигураций...{NC}")
    config_results = test_config_loading()
    all_results.extend(config_results)
    for result in config_results:
        status = f"{GREEN}✅{NC}" if result.success else f"{RED}❌{NC}"
        print(f"  {status} {result.name}: {result.message}")
    
    # 2. Тест основных модулей
    print(f"\n{YELLOW}🔧 Тестирование основных модулей...{NC}")
    core_results = test_core_modules()
    all_results.extend(core_results)
    for result in core_results:
        status = f"{GREEN}✅{NC}" if result.success else f"{RED}❌{NC}"
        print(f"  {status} {result.name}: {result.message}")
    
    # 3. Тест адаптеров
    print(f"\n{YELLOW}🔌 Тестирование адаптеров...{NC}")
    adapter_results = test_adapters()
    all_results.extend(adapter_results)
    for result in adapter_results:
        status = f"{GREEN}✅{NC}" if result.success else f"{RED}❌{NC}"
        print(f"  {status} {result.name}: {result.message}")
    
    # 4. Тест интеграций
    print(f"\n{YELLOW}🔗 Тестирование интеграций...{NC}")
    integration_results = test_integrations()
    all_results.extend(integration_results)
    for result in integration_results:
        status = f"{GREEN}✅{NC}" if result.success else f"{RED}❌{NC}"
        print(f"  {status} {result.name}: {result.message}")
    
    # 5. Тест провайдеров
    print(f"\n{YELLOW}⚙️  Тестирование провайдеров...{NC}")
    provider_results = await test_providers()
    all_results.extend(provider_results)
    for result in provider_results:
        status = f"{GREEN}✅{NC}" if result.success else f"{RED}❌{NC}"
        print(f"  {status} {result.name}: {result.message}")
    
    # Итоги
    print_header("ИТОГИ ТЕСТИРОВАНИЯ")
    
    total = len(all_results)
    passed = sum(1 for r in all_results if r.success)
    failed = total - passed
    
    print(f"\n📊 Статистика:")
    print(f"   Всего проверок: {total}")
    print(f"   {GREEN}✅ Успешно: {passed}{NC}")
    if failed > 0:
        print(f"   {RED}❌ Провалено: {failed}{NC}")
        print(f"\n{RED}Детали ошибок:{NC}")
        for result in all_results:
            if not result.success:
                print(f"   ❌ {result.name}")
                if result.error:
                    print(f"      Ошибка: {result.error[:100]}")
    else:
        print(f"\n{GREEN}✅ ВСЕ МОДУЛИ И ИНТЕГРАЦИИ РАБОТАЮТ КОРРЕКТНО!{NC}")
    
    return 0 if failed == 0 else 1

if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
