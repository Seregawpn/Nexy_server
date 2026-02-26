> [!WARNING] ARCHIVE NOTICE
> Этот документ архивный и не является source of truth.
> Актуальные каноны:
> - `server/Docs/SERVER_DEPLOYMENT_GUIDE.md` (деплой кода на удаленный сервер)
> - `server/Docs/RELEASE_AND_UPDATE_GUIDE.md` (публикация DMG/PKG и update-канал)
> - `server/Docs/DEPLOY_INCIDENT_RUNBOOK.md` (инциденты, зависимости, конфиги, rollback)

# Beta Gate Checklist (PR-7)

**Назначение:** Чекбокс для релиз-менеджера перед включением 25–100% роллаута

Все пункты должны быть машинно проверяемы или иметь готовые рычаги управления.

---

## ✅ Чеклист перед включением 25–100% роллаута

### 1. CI Checks (grpc-checks.yml)

- [ ] `grpc-checks.yml` зелёный: smoke/health/port/appcast/versions
  - Проверка: `GitHub Actions → последний workflow run → все шаги green`
  - Команда: `python scripts/grpc_smoke.py 20.151.51.172 443`
  - Команда: `python scripts/check_grpc_health.py 20.151.51.172 443`

### 2. Structured Logging

- [ ] В логах есть старт/стоп, RPC-ошибки, decisions, деградации
  - Проверка: `grep -E "decision=(start|stop|error|degrade)" server.log | tail -20`
  - Проверка: `grep -E "scope=(grpc|server|module)" server.log | tail -20`
  - Команда: `tail -n 100 server.log | grep -E "decision=|scope="`

### 3. Contract Tests

- [ ] Контракт-таблицы покрыты автосценариями (min 8)
  - Проверка: `python scripts/grpc_contract_tests.py 20.151.51.172 443`
  - Ожидаемый результат: минимум 8 тестов пройдено
  - Команда: `python scripts/grpc_contract_tests.py 20.151.51.172 443 | grep -E "✅|❌"`

### 4. Feature Flag & Kill-Switch

- [ ] Флаг новой функции включён на 1% + прописан kill-switch
  - Проверка: `config.env` или `unified_config.yaml` содержит `features.use_<feature>: true`
  - Проверка: `config.env` или `unified_config.yaml` содержит `kill_switches.disable_<feature>: false`
  - Команда: `python -c "from config.unified_config import get_config; c = get_config(); print(c.is_feature_enabled('use_module_coordinator'))"`

### 5. Update Invariants

- [ ] Update-инварианты прошли (версии — строки, совпали, размер ок)
  - Проверка: `bash scripts/validate_updates.sh 20.151.51.172 443`
  - Проверка: `curl -s https://20.151.51.172/health | jq '.latest_version, .latest_build'`
  - Проверка: `curl -s https://20.151.51.172/updates/appcast.xml | grep sparkle:version`

### 6. Metrics (опционально)

- [ ] Метрики собираются (p95 latency, error-rate, decision_rate)
  - Проверка: `grep -E "p95_latency|error_rate|decision_rate" server.log | tail -10`
  - Проверка: `python -c "from utils.metrics_collector import get_metrics_collector; c = get_metrics_collector(); print(c.get_snapshot())"`

### 7. Chaos Test (опционально)

- [ ] Chaos smoke тест прошёл
  - Проверка: `python scripts/chaos_smoke.py 20.151.51.172 443`
  - Ожидаемый результат: сервер стабилен, ошибки обрабатываются корректно

---

## 🔍 Автоматическая проверка

### Скрипт проверки всех пунктов

```bash
#!/bin/bash
# scripts/check_beta_gate.sh

echo "🔍 Beta Gate Checklist Check"
echo "============================"

errors=0

# 1. CI Checks
echo "1. Checking CI status..."
if python scripts/grpc_smoke.py 20.151.51.172 443 > /dev/null 2>&1; then
    echo "   ✅ Smoke test passed"
else
    echo "   ❌ Smoke test failed"
    errors=$((errors + 1))
fi

# 2. Structured Logging
echo "2. Checking structured logging..."
if grep -q "decision=" server.log 2>/dev/null; then
    echo "   ✅ Structured logging found"
else
    echo "   ⚠️ Structured logging not found (may be normal if server just started)"
fi

# 3. Contract Tests
echo "3. Checking contract tests..."
if python scripts/grpc_contract_tests.py 20.151.51.172 443 > /dev/null 2>&1; then
    echo "   ✅ Contract tests passed"
else
    echo "   ❌ Contract tests failed"
    errors=$((errors + 1))
fi

# 4. Feature Flag
echo "4. Checking feature flag..."
if python -c "from config.unified_config import get_config; c = get_config(); assert hasattr(c, 'features')" 2>/dev/null; then
    echo "   ✅ Feature flags available"
else
    echo "   ❌ Feature flags not available"
    errors=$((errors + 1))
fi

# 5. Update Invariants
echo "5. Checking update invariants..."
if bash scripts/validate_updates.sh 20.151.51.172 443 > /dev/null 2>&1; then
    echo "   ✅ Update invariants passed"
else
    echo "   ❌ Update invariants failed"
    errors=$((errors + 1))
fi

echo ""
echo "============================"
if [ $errors -eq 0 ]; then
    echo "✅ All checks passed!"
    exit 0
else
    echo "❌ $errors checks failed"
    exit 1
fi
```

---

## 📋 Ручная проверка

Если автоматическая проверка недоступна, выполните вручную:

1. **CI Checks:**
   ```bash
   python scripts/grpc_smoke.py 20.151.51.172 443
   python scripts/check_grpc_health.py 20.151.51.172 443
   ```

2. **Structured Logging:**
   ```bash
   tail -n 100 server.log | grep -E "decision=|scope="
   ```

3. **Contract Tests:**
   ```bash
   python scripts/grpc_contract_tests.py 20.151.51.172 443
   ```

4. **Feature Flag:**
   ```bash
   python -c "from config.unified_config import get_config; c = get_config(); print('Features:', c.features.__dict__)"
   ```

5. **Update Invariants:**
   ```bash
   bash scripts/validate_updates.sh 20.151.51.172 443
   ```

---

## ⚠️ Критерии отката

Если любой из следующих критериев выполняется, **откат обязателен**:

- [ ] Health endpoint не отвечает (HTTP != 200)
- [ ] gRPC smoke test не проходит
- [ ] Error rate > 5%
- [ ] p95 latency > 1000ms
- [ ] Версии не совпадают (health vs appcast)
- [ ] Размеры не совпадают (appcast vs GitHub)

При откате:
1. Включить kill-switch: `export NEXY_KS_DISABLE_<FEATURE>=true`
2. Проверить health/status
3. Перезапустить сервер
4. Задокументировать причину отката

---

## 📚 Ссылки

- `Docs/SERVER_DEVELOPMENT_RULES.md` — правила разработки
- `Docs/GRPC_PROTOCOL_AUDIT.md` — контракт-таблицы
- `scripts/grpc_smoke.py` — smoke тест
- `scripts/grpc_contract_tests.py` — контракт-тесты
- `scripts/validate_updates.sh` — валидация обновлений

