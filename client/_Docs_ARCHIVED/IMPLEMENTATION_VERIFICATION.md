# Implementation Verification Guide

**Цель**: Воспроизводимое подтверждение, что логика реализована на обеих сторонах (клиент и сервер).

## Быстрый старт

```bash
# Проверка клиента и сервера
python scripts/verify_implementation.py

# Только клиент
python scripts/verify_implementation.py --client-only

# Только сервер
python scripts/verify_implementation.py --server-only

# Сохранить артефакты в другую директорию
python scripts/verify_implementation.py --output-dir ./my_verification
```

## Что проверяется

### Клиент

1. **Соответствие документации коду (СТРОГАЯ ПРОВЕРКА)**
   - `ARCHITECTURE_OVERVIEW.md` ↔ `simple_module_coordinator.py`
   - **Точное сравнение порядка интеграций** из `_create_integrations()` со списком в документации
   - FAIL при любом расхождении порядка или отсутствии интеграции

2. **Автоматические проверки**
   - `verify_architecture.py` — архитектурные правила
   - `verify_feature_flags.py` — регистрация feature flags

### Сервер

1. **Соответствие документации коду (СТРОГАЯ ПРОВЕРКА)**
   - `ARCHITECTURE_OVERVIEW.md` ↔ структура `server/server/modules/`
   - **Точное сравнение списка модулей** из документации с фактической структурой
   - FAIL при отсутствии документации модуля или наличии лишних модулей

2. **Конфигурация**
   - `unified_config.yaml` существует и доступен

### Общие проверки

1. **gRPC протокол (СТРОГАЯ ПРОВЕРКА)**
   - `streaming.proto` должен находиться **только** по каноническому пути: `server/server/modules/grpc_service/streaming.proto`
   - FAIL если файл найден в другом месте или отсутствует
   - Проверка наличия всех ключевых определений (service, rpc, message, stream)

## Артефакты

Скрипт генерирует следующие артефакты в директории `.verification/` (или указанной через `--output-dir`):

### 1. `verification_report.json`

Полный JSON-отчет со всеми проверками:

```json
{
  "timestamp": "2025-12-29T12:14:49.068618",
  "client_git_sha": "28143f2f01bc046149102caac1d3e01dea17f91f",
  "server_git_sha": "9594834284892782f7113e0938ebac7fa2e5d566",
  "checks": [...],
  "summary": {
    "pass": 5,
    "fail": 1,
    "skip": 0
  }
}
```

### 2. `checklist.md`

Человекочитаемый чек-лист с результатами всех проверок:

```markdown
# Implementation Verification Checklist

**Generated**: 2025-12-29T12:14:49.068618

**Client git SHA**: 28143f2f01bc046149102caac1d3e01dea17f91f
**Server git SHA**: 9594834284892782f7113e0938ebac7fa2e5d566

## Checks

- ✅ **Client Architecture Docs**: PASS
- ❌ **Client Architecture Verification**: FAIL
- ✅ **Client Feature Flags Verification**: PASS
...
```

### 3. `*_output.txt`

Выводы всех запущенных скриптов для детального анализа:
- `client_architecture_verification_output.txt`
- `client_feature_flags_verification_output.txt`
- и т.д.

## Exit codes

- `0` — все проверки пройдены
- `1` — хотя бы одна проверка провалена

## Использование в CI/CD

```yaml
# Пример для GitHub Actions
- name: Verify Implementation
  run: |
    python scripts/verify_implementation.py
    # Артефакты автоматически сохраняются в .verification/
  
- name: Upload Verification Artifacts
  uses: actions/upload-artifact@v3
  with:
    name: verification-artifacts
    path: .verification/
```

## Интерпретация результатов

### ✅ Pass
Проверка пройдена успешно. **PASS означает реальное совпадение, а не "похоже"**.

### ❌ Fail
Проверка провалена. **FAIL при любом расхождении** фактического порядка/путей. Смотрите детали в:
- `verification_report.json` → `details`
- Соответствующий `*_output.txt` файл

**Важно**: Все проверки **строгие**:
- Порядок интеграций должен совпадать **точно**
- Структура модулей должна совпадать **точно**
- gRPC протокол должен быть по **каноническому пути**

### ⏭️ Skip
Проверка пропущена (например, файл не найден, но это ожидаемо).

## Рекомендации

1. **Перед мерджем**: Запускайте `verify_implementation.py` и прикладывайте `checklist.md` к PR
2. **После изменений**: Повторяйте проверки после любых изменений в логике/конфиге
3. **Артефакты**: Сохраняйте `.verification/` в git (или как артефакт CI) для истории

## Связанные документы

- `ARCHITECTURE_OVERVIEW.md` — архитектурный обзор
- `FEATURE_FLAGS.md` — реестр feature flags
- `scripts/verify_architecture.py` — архитектурные проверки
- `scripts/verify_feature_flags.py` — проверка feature flags
