# PR #1 (Close_app): Список файлов

## Дата: 2025-01-XX

---

## ✅ Файлы для включения в PR #1

### Серверная часть (6 файлов)

1. **`server/config/unified_config.py`**
   - Добавлен `close_app` в промпт
   - Статус: ✅ Изменен

2. **`server/config/unified_config_example.yaml`**
   - Синхронизирован промпт с `unified_config.py`
   - Статус: ✅ Изменен

3. **`server/config.env.example`**
   - Добавлены фича-флаги для `close_app`
   - Статус: ✅ Изменен (нужно проверить, что изменения только для close_app)

4. **`server/integrations/core/response_models.py`**
   - Добавлен `CloseAppArgs`
   - Валидация `close_app` в `ActionResponse`
   - Статус: ✅ Изменен

5. **`server/integrations/core/assistant_response_parser.py`**
   - Fallback-валидация для `close_app`
   - Статус: ✅ Изменен

6. **`server/scripts/test_mcp_chain.py`**
   - Добавлены тесты для `close_app`
   - Статус: ✅ Изменен

7. **`server/scripts/verify_close_app_production_readiness.py`** (новый файл)
   - Readiness скрипт для сервера
   - Статус: ✅ Новый файл

---

### Клиентская часть (3 файла)

8. **`client/integration/integrations/action_execution_integration.py`**
   - Идемпотентность для `close_app`
   - Нормализация `app_name`
   - Публикация событий для дубликатных сессий
   - Статус: ✅ Изменен

9. **`client/scripts/test_close_app_e2e.py`**
   - E2E тест для `close_app`
   - Статус: ✅ Изменен

10. **`client/scripts/verify_close_app_client_readiness.py`** (новый файл)
    - Readiness скрипт для клиента
    - Статус: ✅ Новый файл

---

### Документация (8 файлов)

11. **`Docs/CLOSE_APP_CHANGES_SUMMARY.md`** (новый)
12. **`Docs/CLOSE_APP_CODE_REVIEW.md`** (новый)
13. **`Docs/CLOSE_APP_FINAL_REVIEW_SUMMARY.md`** (новый)
14. **`Docs/CLOSE_APP_IDEMPOTENCY_FIXES.md`** (новый)
15. **`Docs/CLOSE_APP_PRODUCTION_DEPLOYMENT.md`** (новый)
16. **`Docs/CLOSE_APP_PR_SPLIT_PLAN.md`** (новый)
17. **`Docs/CLOSE_APP_TESTS_RESULTS.md`** (новый)
18. **`Docs/CLOSE_APP_PRODUCTION_CHECKLIST.md`** (новый, если есть)
19. **`Docs/CLOSE_APP_E2E_IMPLEMENTATION_GUIDE.md`** (новый, если есть)

---

### Скрипты (1 файл)

20. **`scripts/cleanup_close_app_artifacts.sh`** (новый)
    - Скрипт очистки артефактов
    - Статус: ✅ Новый файл

---

## ❌ Файлы для исключения из PR #1

### Unrelated изменения (не относятся к close_app)

**Audio/Edge TTS:**
- `server/modules/audio_generation/*` - все изменения
- `server/modules/audio_generation/config.py`
- `server/modules/audio_generation/core/audio_processor.py`
- `server/modules/audio_generation/providers/azure_tts_provider.py`

**Text Processing:**
- `server/modules/text_processing/*` - все изменения
- `server/modules/text_processing/__init__.py`
- `server/modules/text_processing/config.py`
- `server/modules/text_processing/core/text_processor.py`
- `server/modules/text_processing/module.py`
- `server/modules/text_processing/providers/__init__.py`
- `server/modules/text_processing/providers/gemini_live_provider.py` (удален)

**Database:**
- `server/modules/database/*` - все изменения

**GRPC:**
- `server/modules/grpc_service/*` - все изменения

**Update:**
- `server/modules/update/*` - все изменения

**Memory Management:**
- `server/modules/memory_management/*` - все изменения

**Session Management:**
- `server/modules/session_management/*` - все изменения

**Text Filtering:**
- `server/modules/text_filtering/*` - все изменения

**Interrupt Handling:**
- `server/modules/interrupt_handling/*` - все изменения

**Workflow Integrations:**
- `server/integrations/workflow_integrations/*` - все изменения (кроме проверки на close_app)

**Service Integrations:**
- `server/integrations/service_integrations/*` - все изменения

**Core:**
- `server/integrations/core/universal_fallback_manager.py` - проверить, связано ли с close_app

**Main:**
- `server/main.py` - проверить, связано ли с close_app

**Requirements:**
- `server/requirements.txt` - проверить, связано ли с close_app

**Scripts:**
- `server/scripts/test_gemini_api_access.py`
- `server/scripts/test_server_full.py`
- `server/updates/scripts/*`

**Client (unrelated):**
- `client/integration/integrations/grpc_client_integration.py` - проверить
- `client/integration/integrations/input_processing_integration.py` - проверить
- `client/integration/integrations/speech_playback_integration.py` - проверить
- `client/integration/integrations/voice_recognition_integration.py` - проверить
- `client/test_mcp_open_app_integration.py` - новый тест, не относится к close_app
- `client/test_open_close_safari.py` - новый тест, не относится к close_app

---

## 📋 Чек-лист проверки файлов

### Для каждого файла в PR #1:

- [ ] Файл напрямую связан с `close_app` функциональностью
- [ ] Изменения минимальны и изолированы
- [ ] Нет побочных изменений в unrelated модулях
- [ ] Тесты проходят для этого файла

### Для исключенных файлов:

- [ ] Файл не связан с `close_app`
- [ ] Изменения будут в отдельном PR
- [ ] Нет зависимостей от close_app изменений

---

## 🔍 Проверка scope

### Команда для проверки:

```bash
# Проверить, что в PR только close_app файлы
git diff --name-only HEAD | grep -v -E "(close_app|CLOSE_APP)" | grep -E "(server|client)" | head -20
```

### Ожидаемый результат:

Должны быть только файлы, которые:
- Не связаны с `close_app`
- Или являются документацией/скриптами

---

## ✅ Итоговый список для PR #1

**Всего файлов:** ~20 файлов

**Сервер:** 7 файлов
**Клиент:** 3 файла
**Документация:** 8-9 файлов
**Скрипты:** 1-2 файла

**Статус:** ✅ Готово к формированию PR после проверки исключений
