# Production Rules Summary

**Версия**: 1.0  
**Дата**: 2025-01-15

---

## Краткое резюме правил продакшн-уровня

Этот документ — краткое резюме всех правил уровня продакшн для Nexy Client. Полные правила см. `.cursorrules`.

### 10 критических артефактов

1. **STATE_CATALOG.md** — единый источник истины для осей состояния + таблица ownership
2. **interaction_matrix.yaml** — правила взаимодействия осей с приоритетами
3. **Gateway layer** (`integration/core/gateways/`) — логика принятия решений на основе осей (decision_engine.py, rule_loader.py, predicates.py, base.py, common.py, permission_gateways.py)
4. **test_gateways.py** — тесты с проверкой decision-логов в каноническом формате
5. **change_impact.yaml** — обязателен для изменений >2 осей (шаблон в `.impact/`)
6. **schemas/** — JSON Schema для валидации unified_config.yaml и interaction_matrix.yaml
7. **FEATURE_FLAGS.md** — карта feature flags/kill-switches → код
8. **registry.md** — реестр метрик с SLO порогами
9. **test_slo.py** — smoke-тесты для проверки SLO порогов
10. **golden tests** — фикс-набор снепшотов осей → ожидаемое решение

### Правила синхронизации

**Инвариант**: "изменил поведение? обнови 4 артефакта"
1. ✅ `Docs/STATE_CATALOG.md`
2. ✅ `config/interaction_matrix.yaml`
3. ✅ **Gateway layer** (`integration/core/gateways/*.py`)
4. ✅ Тесты gateways (≥8–14 pairwise + 2 негативных)

### Machine-enforced правила

- **Запрет прямого доступа к состоянию**: `pyproject.toml` + `scripts/verify_no_direct_state_access.py`
- **Валидация схем**: `tests/test_schemas.py` + `scripts/validate_schemas.py`
- **CI как процесс-гейт**: `.github/workflows/ci.yml` (lint, schema-validate, contracts-test, impact-gate)

### Decision-логи (обязательный формат)

```
decision=<start|abort|retry|degrade> ctx={mic=...,screen=...,device=...,network=...,firstRun=...,appMode=...} source=<domain> duration_ms=<int>
```

**ОБЯЗАТЕЛЬНОСТЬ**: Все gateways логируют решения в этом формате. Проверяется в тестах через `assert_decision_logged()` helper.

### Связанные документы

- **STATE_CATALOG.md** — оси состояния + ownership (единый источник истины)
- **interaction_matrix.yaml** — правила взаимодействия осей (синхронизирован с STATE_CATALOG.md)
- **.cursorrules** — правила разработки клиента
- **FEATURE_FLAGS.md** — карта flags/kill-switches → код
- **client/metrics/registry.md** — метрики + SLO пороги
- **.cursorrules** — полные правила разработки (раздел 1.1 — источник истины)

---

**Владелец**: Tech Lead клиента  
**Последнее обновление**: 2025-01-15

