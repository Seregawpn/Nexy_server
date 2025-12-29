# План разделения PR и очистки артефактов

## Проблема

В текущем бранче смешаны изменения:
- ✅ **Close_app ядро** (9 файлов) - готово к merge
- ❌ **Unrelated изменения** (десятки файлов) - audio/edge_tts, text_processing, grpc, update
- ❌ **Артефакты и тестовые файлы** - нельзя тащить в production

---

## 📋 Список файлов по категориям

### ✅ Close_app ядро (готово к merge)

**Серверная часть:**
1. `server/server/config/unified_config.py` - промпт с `close_app`
2. `server/server/config/unified_config_example.yaml` - синхронизация промпта
3. `server/server/integrations/core/response_models.py` - `CloseAppArgs` и валидация
4. `server/server/integrations/core/assistant_response_parser.py` - fallback-валидация
5. `server/server/scripts/verify_close_app_production_readiness.py` - readiness скрипт
6. `server/server/scripts/test_mcp_chain.py` - тесты с `close_app`

**Клиентская часть:**
7. `client/integration/integrations/action_execution_integration.py` - идемпотентность
8. `client/scripts/verify_close_app_client_readiness.py` - readiness скрипт
9. `client/scripts/test_close_app_e2e.py` - E2E тест

**Документация:**
- `Docs/CLOSE_APP_CHANGES_SUMMARY.md`
- `Docs/CLOSE_APP_CODE_REVIEW.md`
- `Docs/CLOSE_APP_IDEMPOTENCY_FIXES.md`
- `Docs/CLOSE_APP_PRODUCTION_DEPLOYMENT.md`
- `Docs/CLOSE_APP_TESTS_RESULTS.md`
- `Docs/CLOSE_APP_PRODUCTION_CHECKLIST.md`
- `Docs/CLOSE_APP_E2E_IMPLEMENTATION_GUIDE.md`

---

### ❌ Артефакты и тестовые файлы (удалить)

**Edge TTS артефакты:**
```
server/server/scripts/edge_tts_output/          # Вся директория
  - test_1_en_US_AriaNeural.mp3
  - test_1_en_US_GuyNeural.mp3
  - test_1_en_US_JennyNeural.mp3
  - test_2_en_US_AriaNeural.mp3
  - test_2_en_US_GuyNeural.mp3
  - test_2_en_US_JennyNeural.mp3
  - test_3_en_US_AriaNeural.mp3
  - test_3_en_US_GuyNeural.mp3
  - test_3_en_US_JennyNeural.mp3
  - simple_test.mp3

server/server/scripts/test_edge_tts_streaming.mp3
server/server/scripts/test_edge_tts_output.mp3
server/server/scripts/edge_tts_check_report.json
server/server/scripts/edge_tts_test_report.md
```

**Статус:** ❌ **УДАЛИТЬ** - это тестовые артефакты, не должны быть в production

---

### ⚠️ Unrelated изменения (отдельный PR)

**Audio/Edge TTS:**
- `server/server/modules/audio_generation/*` - изменения в audio generation
- `server/server/modules/audio_generation/EDGE_TTS_*.md` - документация edge_tts
- `server/server/scripts/test_edge_tts_*.py` - тесты edge_tts
- `server/server/scripts/generate_and_play_edge_tts.py`

**Text Processing:**
- `server/server/modules/text_processing/*` - изменения в text processing
- Удаление `gemini_live_provider.py` (если есть)

**GRPC/Update:**
- `server/server/modules/grpc_service/*` - изменения в grpc
- `server/server/modules/update/*` - изменения в update

**Requirements:**
- `server/requirements.txt` - изменения зависимостей

**Статус:** ⚠️ **ОТДЕЛЬНЫЙ PR** - не относится к `close_app`

---

## 🎯 План действий

### Шаг 1: Очистка артефактов

**Команды для удаления:**

```bash
# Удалить edge_tts_output директорию
rm -rf server/server/scripts/edge_tts_output/

# Удалить тестовые mp3 файлы
rm server/server/scripts/test_edge_tts_streaming.mp3
rm server/server/scripts/test_edge_tts_output.mp3

# Удалить JSON отчеты
rm server/server/scripts/edge_tts_check_report.json

# Удалить MD отчеты (если не нужны для документации)
# rm server/server/scripts/edge_tts_test_report.md
```

**Проверка:**
```bash
# Убедиться, что артефакты удалены
find server/server/scripts -name "*.mp3" -o -name "*edge_tts*.json" | grep -v ".git"
```

---

### Шаг 2: Разделение PR

#### PR #1: Close_app (только ядро)

**Включить:**
- ✅ Все 9 файлов close_app ядра (см. список выше)
- ✅ Вся документация close_app (7 документов)

**Исключить:**
- ❌ Все изменения в audio/text_processing/grpc/update
- ❌ Все артефакты и тестовые файлы
- ❌ Изменения в `requirements.txt` (если не связаны с close_app)

**Проверка перед merge:**
- [ ] `test_mcp_chain.py` проходит
- [ ] `test_close_app_e2e.py` проходит
- [ ] Нет артефактов в PR
- [ ] Нет unrelated изменений

---

#### PR #2: Audio/Edge TTS (отдельный PR)

**Включить:**
- Изменения в `server/server/modules/audio_generation/*`
- Тесты edge_tts (если нужны для production)
- Документация edge_tts (если нужна)

**Исключить:**
- ❌ Артефакты (mp3, json отчеты)
- ❌ Close_app изменения

**Проверка:**
- [ ] Тесты audio generation проходят
- [ ] Нет артефактов
- [ ] Документация актуальна

---

#### PR #3: Text Processing (отдельный PR)

**Включить:**
- Изменения в `server/server/modules/text_processing/*`
- Удаление `gemini_live_provider.py` (если есть)
- Обновления в `requirements.txt` (если связаны)

**Проверка:**
- [ ] Нет импортов удаленного `gemini_live_provider.py`
- [ ] Тесты text_processing проходят
- [ ] Зависимости обновлены корректно

---

### Шаг 3: Проверка удаленного gemini_live_provider.py

**Статус:** ✅ **Проверено** - нет импортов `gemini_live_provider` в коде

**Результат grep:**
```
No matches found
```

**Вывод:** Удаление `gemini_live_provider.py` безопасно, импортов нет.

---

## 📝 Чек-лист перед merge PR #1 (close_app)

### Очистка
- [ ] Удалены все артефакты edge_tts (mp3, json)
- [ ] Удалена директория `edge_tts_output/`
- [ ] Проверено отсутствие тестовых файлов в PR

### Изоляция изменений
- [ ] В PR только файлы close_app ядра (9 файлов)
- [ ] Нет изменений в audio/text_processing/grpc/update
- [ ] Нет изменений в `requirements.txt` (если не связаны)

### Тестирование
- [ ] `test_mcp_chain.py` проходит (5/5 тестов)
- [ ] `test_close_app_e2e.py` проходит (полный цикл)
- [ ] Readiness скрипты работают

### Документация
- [ ] Все 7 документов close_app включены
- [ ] Документация актуальна и полна

---

## 🚨 Критические проверки

### 1. Проверка импортов gemini_live_provider

**Команда:**
```bash
grep -r "gemini_live_provider" server/
```

**Результат:** ✅ Нет импортов (проверено)

### 2. Проверка артефактов

**Команда:**
```bash
find server/server/scripts -name "*.mp3" -o -name "*edge_tts*.json" | grep -v ".git"
```

**Действие:** Удалить все найденные файлы перед merge

### 3. Проверка scope изменений

**Команда:**
```bash
git diff --name-only main...HEAD | grep -E "(audio|text_processing|grpc|update)" | grep -v "close_app"
```

**Действие:** Исключить все найденные файлы из PR #1

---

## ✅ Итоговый статус

### PR #1: Close_app
- **Статус:** ✅ Готово к merge после очистки
- **Файлов:** 9 core + 7 docs = 16 файлов
- **Тесты:** ✅ Проходят
- **Риск:** ✅ Низкий (изолированные изменения)

### PR #2/3: Unrelated изменения
- **Статус:** ⚠️ Требуют отдельного ревью
- **Риск:** ⚠️ Средний (широкий scope)

---

## 📌 Рекомендации

1. **Немедленно:** Удалить все артефакты перед merge
2. **Перед merge PR #1:** Убедиться, что нет unrelated изменений
3. **Отдельно:** Создать PR #2/3 для audio/text_processing изменений
4. **После merge PR #1:** Прогнать полный smoke test на production

---

## 🔧 Скрипт автоматической очистки

```bash
#!/bin/bash
# cleanup_artifacts.sh

echo "🧹 Очистка артефактов..."

# Удалить edge_tts_output директорию
if [ -d "server/server/scripts/edge_tts_output" ]; then
    rm -rf server/server/scripts/edge_tts_output/
    echo "✅ Удалена директория edge_tts_output/"
fi

# Удалить тестовые mp3 файлы
rm -f server/server/scripts/test_edge_tts_streaming.mp3
rm -f server/server/scripts/test_edge_tts_output.mp3
echo "✅ Удалены тестовые mp3 файлы"

# Удалить JSON отчеты
rm -f server/server/scripts/edge_tts_check_report.json
echo "✅ Удалены JSON отчеты"

echo "✅ Очистка завершена"
```
