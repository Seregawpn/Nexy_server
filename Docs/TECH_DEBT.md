# Technical Debt Register

Документ отслеживает технический долг в серверной части Nexy.

---

## TD-001: Workflow Integrations используют прямой доступ к внутренним объектам модулей

**Создан**: 2025-11-05
**Приоритет**: HIGH
**Затронутые файлы**:
- `modules/grpc_service/core/grpc_service_manager.py:189-227`
- `integrations/workflow_integrations/streaming_workflow_integration.py`
- `integrations/workflow_integrations/memory_workflow_integration.py`
- `integrations/workflow_integrations/interrupt_workflow_integration.py`
- Все адаптеры в `modules/*/adapter.py`

**Проблема**:
Workflow интеграции напрямую используют внутренние объекты модулей (text_processor, audio_processor, memory_manager, interrupt_manager) через методы `get_processor()` и `get_manager()`. Это нарушает:
- Инкапсуляцию модулей
- Принцип работы через `UniversalModuleInterface.process()`
- Раздел 4 SERVER_DEVELOPMENT_RULES: "Workflow интеграции должны работать через module.process(), а не напрямую с процессорами"

**Текущее состояние**:
```python
# ПЛОХО (текущее):
text_processor = text_module.get_processor()  # Прямой доступ
result = text_processor.process_text(input)

# ХОРОШО (цель):
result = await text_module.process({'action': 'process_text', 'input': input})
```

**План исправления**:

### Этап 1: Унификация интерфейса `process()`
- [ ] Стандартизировать формат входных данных для `process()` всех модулей
- [ ] Определить общий контракт: `{'action': str, 'params': dict}`
- [ ] Обновить `UniversalModuleInterface` с документацией стандартного контракта

### Этап 2: Рефакторинг Workflow Integrations
- [ ] `StreamingWorkflowIntegration`: заменить `text_processor.process_text()` на `text_module.process()`
- [ ] `StreamingWorkflowIntegration`: заменить `audio_processor.generate_audio()` на `audio_module.process()`
- [ ] `MemoryWorkflowIntegration`: заменить `memory_manager.*` на `memory_module.process()`
- [ ] `InterruptWorkflowIntegration`: заменить `interrupt_manager.*` на `interrupt_module.process()`

### Этап 3: Удаление методов-нарушителей
- [ ] Пометить `get_processor()` и `get_manager()` как @deprecated
- [ ] Добавить warnings при вызове этих методов
- [ ] После рефакторинга workflow - удалить эти методы полностью

### Этап 4: Обновление тестов
- [ ] Обновить модульные тесты для новых workflow
- [ ] Добавить интеграционные тесты для проверки изоляции

**Риски**:
- Большой объем изменений (затрагивает 3 workflow интеграции + 7 адаптеров)
- Возможные регрессии в стриминге аудио
- Требуется тщательное тестирование с реальным клиентом

**Временное решение**:
Методы `get_processor/get_manager` ВРЕМЕННО оставлены с комментарием TODO и warning логами. См. `grpc_service_manager.py:189-223`.

**Owner**: @backend-team
**Tracking Issue**: https://github.com/nexy/server/issues/XXX (создать)

---

## TD-002: Версия сервера хардкодится в main.py

**Создан**: 2025-11-05
**Приоритет**: MEDIUM
**Затронутые файлы**:
- `main.py:34`

**Проблема**:
Версия сервера определяется через `os.getenv("SERVER_VERSION", "3.11.0")`, что требует ручного обновления. Нет интеграции с `UpdateManager` для динамического получения версии из манифестов.

**План исправления**:
- [ ] Создать метод `UpdateManager.get_current_version()` для получения версии из манифестов
- [ ] Интегрировать в `health_handler()` и `status_handler()`
- [ ] Обеспечить fallback на env-переменную при недоступности UpdateManager

**Owner**: @backend-team

---

## TD-003: config.env был в репозитории (RESOLVED)

**Создан**: 2025-11-05
**Решён**: 2025-11-05
**Приоритет**: CRITICAL (был)

**Проблема**:
Файл `config.env` с секретами был отслеживаем git'ом, несмотря на наличие в `.gitignore`.

**Решение**:
- ✅ Удалён из git через `git rm --cached config.env`
- ✅ Создан `config.env.example` как шаблон
- ⚠️ TODO: Ротация всех API-ключей, которые могли попасть в историю git

**Owner**: @devops-team (для ротации ключей)

---

## Процесс управления Tech Debt

1. **Новая запись**: Создать секцию TD-XXX с описанием проблемы
2. **Приоритизация**: Обсудить на еженедельном review
3. **Планирование**: Разбить на этапы, назначить owner
4. **Tracking**: Создать issue в GitHub/Jira с ссылкой на TD-XXX
5. **Закрытие**: Пометить как RESOLVED с датой, обновить статусы

---

**Last Updated**: 2025-11-05
