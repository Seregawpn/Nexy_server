# Архитектурные проблемы (отдельно от флагов)

**Generated**: 2025-12-29T13:00:34

## Статус

- ✅ **Feature Flags**: PASSED (client + server)
- ❌ **Architecture Issues**: 2 FAIL (требуют отдельного плана)

## Проблема 1: Client Architecture Verification

**Status**: ❌ FAIL  
**Script**: `verify_architecture.py`  
**Exit code**: 1

### Детали

- **18 Errors**: Direct State Access violations
  - `input_processing_integration.py`: 9 violations (ptt_pressed state)
  - `voice_recognition_integration.py`: 5 violations (ptt_pressed, first_run_in_progress)
  
- **118 Warnings**: Logger Instantiation
  - Использование `logging.getLogger(__name__)` вместо `integration.utils.get_logger`
  - Затронуты файлы: `main.py`, `run_diagnostics.py`, модули, интеграции, тесты

### План исправления

1. **Direct State Access**:
   - Заменить `state_manager.get_state_data("ptt_pressed")` на использование selectors/gateways
   - Файлы: `input_processing_integration.py`, `voice_recognition_integration.py`
   
2. **Logger Instantiation**:
   - Массовая замена `logging.getLogger(__name__)` на `get_logger(__name__)`
   - Или добавить исключения в `verify_architecture.py` для допустимых случаев

### Приоритет

- **Direct State Access**: Высокий (нарушает архитектурные принципы)
- **Logger Instantiation**: Средний (предупреждения, не блокируют работу)

---

## Проблема 2: Server Architecture Docs

**Status**: ❌ FAIL  
**Check**: `check_server_architecture_docs()`  
**Issue**: Extra modules: `update`

### Детали

- **Actual module**: `server/server/modules/update/` существует
- **Documented**: Модуль `update` отсутствует в `ARCHITECTURE_OVERVIEW.md`

### План исправления

**Вариант 1**: Добавить модуль в документацию
- Обновить `server/server/Docs/ARCHITECTURE_OVERVIEW.md`
- Добавить `update` в список модулей

**Вариант 2**: Удалить модуль (если не используется)
- Проверить использование модуля `update`
- Если не используется → удалить
- Если используется → добавить в документацию

### Приоритет

- **Средний**: Не критично для работы, но нарушает синхронизацию документации и кода

---

## Следующие шаги

1. ✅ Флаговая часть завершена и подтверждена
2. ⏭️ Архитектурные проблемы требуют отдельного плана исправлений
3. ⏭️ После исправлений → повторный запуск `verify_implementation.py`
