# Gateway Change Checklist

**Использование**: Чек-лист для PR, затрагивающих gateway layer или правила взаимодействия.

---

## ✅ Обязательные пункты (4 артефакта)

1. **STATE_CATALOG.md** — обновлена ось/правило (владелец, читатели, правила)
2. **interaction_matrix.yaml** — добавлено/изменено правило (gateway, priority, decision)
3. **Gateway layer** (`integration/core/gateways/*.py`) — реализована логика
4. **Тесты gateways** (`tests/test_gateways.py`) — ≥8–14 pairwise + 2 негативных с проверкой decision-логов

---

## ✅ Валидация

- [ ] Все ключи в `when` зарегистрированы в `predicates.py` (проверка: `scripts/verify_predicate_coverage.py`)
- [ ] Правило имеет `gateway` и `priority` (обязательно)
- [ ] Decision-логи в каноническом формате (тест проверяет наличие и структуру)
- [ ] Схема `interaction_matrix.yaml` проходит валидацию (проверка: `tests/test_schemas.py`)

---

## ✅ Телеметрия

- [ ] Rule miss логируется (WARN с ctx) — автоматически через DecisionEngine
- [ ] Fallback логируется (WARN с ctx) — автоматически через gateways
- [ ] Метрики: `decision_engine_rule_miss`, `decision_engine_fallback` (для мониторинга)

---

## ✅ Feature flags (если >2 оси)

- [ ] Feature flag зарегистрирован в `FEATURE_FLAGS.md`
- [ ] Kill-switch добавлен в `unified_config.yaml` (если требуется мгновенный откат)
- [ ] Тест на переключение флага (1 позитив + 1 негатив)

---

## ✅ Golden-лог (для first-run/permission-restart)

- [ ] Логи сверены со спецификацией из `NEXY_FIRST_RUN_LOG_EXPECTED.md`
- [ ] Нет «проигрывания приветствия до рестарта» в старом процессе
- [ ] Нет публикации `permissions.first_run_completed` в старом процессе (только `restart_pending`)
- [ ] В новом процессе есть `Перезапуск после first_run завершён успешно`
- [ ] Приветствие играет **ТОЛЬКО** после перезапуска (в новом процессе)

---

## ✅ Критические точки

- [ ] First-run и рестарт: запрещено любое приветствие/активация до полного перезапуска
- [ ] Конфликт с обновлением: нет double-restart; `update_in_progress=true` → блок/отложить
- [ ] Названия осей: маппинг между каталогом (`Permission.mic`) и предикатами (`perm.mic`) работает

---

## ✅ Документация

- [ ] Ссылки на "gateway layer" обновлены (не `gateways.py`, а `integration/core/gateways/`)
- [ ] Старые нарративные документы помечены архивными (если правила консолидированы в матрице)

---

**Владелец**: Tech Lead клиента  
**Последнее обновление**: 2025-01-30



