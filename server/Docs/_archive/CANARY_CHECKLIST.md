> [!WARNING] ARCHIVE NOTICE
> Этот документ архивный и не является source of truth.
> Актуальные каноны:
> - `server/Docs/SERVER_DEPLOYMENT_GUIDE.md` (деплой кода на удаленный сервер)
> - `server/Docs/RELEASE_AND_UPDATE_GUIDE.md` (публикация DMG/PKG и update-канал)
> - `server/Docs/DEPLOY_INCIDENT_RUNBOOK.md` (инциденты, зависимости, конфиги, rollback)

# Canary Checklist - финальный чеклист перед выкаткой

## Быстрый префлайт (10 минут)

### 1. Префлайт-проверки

```bash
# Общая проверка
./scripts/preflight_check.sh 20.151.51.172 443

# Проверка интерсепторов (timeout/unavailable/cancelled)
python scripts/test_interceptor_errors.py 20.151.51.172 443

# Проверка backpressure (51 стрим, idle timeout, rate limit)
python scripts/test_backpressure.py 20.151.51.172 443
```

**Ожидаемый результат:** Все проверки должны пройти ✅

---

### 2. Проверка конфигурации

```bash
# Проверка backpressure конфига
python -c "from config.unified_config import get_config; c = get_config(); print('Backpressure:', c.backpressure.__dict__)"

# Проверка окружения
echo $NEXY_ENV  # Должно быть: prod, stage или dev
```

**Ожидаемый результат:**
- Backpressure конфиг загружен
- Окружение соответствует ожидаемому

---

### 3. Проверка Nginx конфига

```bash
# Проверка наличия конфига
ls -l nginx/grpc-passthrough.conf

# Проверка ключевых параметров
grep -E "http2|grpc_pass|grpc_read_timeout|proxy_request_buffering off" nginx/grpc-passthrough.conf
```

**Ожидаемый результат:**
- Конфиг существует
- Все ключевые параметры присутствуют

---

## Этап A — 1% (30–60 мин)

### Гвардрайлы

- [ ] p95 `StreamAudio` ≤ 1000ms
- [ ] error-rate ≤ 5%
- [ ] нет всплеска `decision=retry|abort` > базовой линии ×1.5
- [ ] отказов backpressure ≤ 1% от попыток

### Проверка

```bash
# Проверка гвардрайлов
./scripts/check_ramp_guardrails.sh server.log 100

# Live-мониторинг
./scripts/monitoring_jq.sh server.log
```

**Если чисто — идём дальше.**

---

## Этап B — 25% (2–4 часа)

### Повтор гвардрайлов

- [ ] p95 `StreamAudio` ≤ 1000ms
- [ ] error-rate ≤ 5%
- [ ] нет всплеска `decision=retry|abort` > базовой линии ×1.5
- [ ] отказов backpressure ≤ 1% от попыток

### Отдельно следим

- [ ] Nginx 499 (client closed) — не должно быть всплесков
- [ ] Nginx 502 (bad gateway) — не должно быть всплесков

### Проверка Nginx

```bash
# Проверка Nginx ошибок
tail -1000 /var/log/nginx/grpc-error.log | grep -E ' 499 | 502 ' | wc -l

# Топ ошибок Nginx
tail -1000 /var/log/nginx/grpc-error.log | grep -E ' 499 | 502 ' | awk '{print $9}' | sort | uniq -c | sort -rn
```

**Если чисто — на 50%.**

---

## Этап C — 50% (полдня)

### Наблюдаем

- [ ] drift p95 (нет постепенного роста)
- [ ] валидируем graceful-shutdown на «живом» трафике одной реплике

### Проверка drift p95

```bash
# p95 по 5-минутным окнам
for i in {0..11}; do
    window_start=$(date -d "$i*5 minutes ago" +%s)
    window_end=$(date -d "$((i+1))*5 minutes ago" +%s)
    p95=$(grep -E "ts=.* dur_ms=" server.log | awk -v start=$window_start -v end=$window_end '$2 >= start && $2 <= end {print $NF}' | grep -oE 'dur_ms=([0-9]+)' | cut -d= -f2 | sort -n | awk '{latencies[NR]=$1} END {n=length(latencies); p95_idx=int(n*0.95); print latencies[p95_idx]}')
    echo "Window $i: p95 = $p95 ms"
done
```

### Тест graceful-shutdown

```bash
# На одной реплике
kill -TERM <PID>

# Проверяем логи
tail -f server.log | grep -E 'decision=shutdown|decision=stop'
```

**Если чисто — 100% на следующий день, при включенном kill-switch.**

---

## Этап D — 100% (следующий день)

### Условия

- [ ] Все гвардрайлы пройдены на 50%
- [ ] Graceful-shutdown протестирован
- [ ] Kill-switch включен и проверен
- [ ] Мониторинг настроен

---

## Мониторинг (алёрты)

### Настройка алёртов

```bash
# Примеры команд из scripts/setup_alerts.sh
./scripts/setup_alerts.sh server.log
```

### Пороги

- **p95 latency:**
  - Warn: > 1000ms
  - Page: > 1500ms

- **Error rate:**
  - Warn: > 5%
  - Page: > 10%

- **Рост unavailable/retry/abort:**
  - Page: ×2 от медианы за 24ч

---

## Rollback (быстрый откат)

### Шаги

1. **Включить kill-switch:**
   ```bash
   export NEXY_KS_DISABLE_<FEATURE>=true
   # или через unified_config
   ```

2. **Проверить health:**
   ```bash
   curl https://20.151.51.172/health
   curl https://20.151.51.172/status | jq
   ```

3. **Прогнать тесты:**
   ```bash
   python scripts/grpc_smoke.py 20.151.51.172 443
   ./scripts/check_ramp_guardrails.sh server.log 100
   ```

4. **Post-mortem:**
   - Собрать 5-минутное окно логов до/после
   - Агрегаты p95/error-rate/decision_rate
   - Документировать в `Docs/CURRENT_STATUS_REPORT.md`

---

## Зоны риска (держать в фокусе)

### 1. Тихие клиенты

**Проверка:**
```bash
grep -c 'decision=stream_idle_timeout' server.log
```

**Ожидаемое поведение:**
- Idle timeout прерывает через 5 минут (300s)
- Код: `DEADLINE_EXCEEDED` с `error_type: "stream_idle_timeout"`

---

### 2. Спайк подключений

**Проверка:**
```bash
grep -c 'error_type=stream_limit_exceeded' server.log
```

**Если отказов >1%:**
- Поднять лимит в конфиге: `BACKPRESSURE_MAX_STREAMS=75`
- Или отрегулировать клиентские ретраи (exponential backoff + jitter)

---

### 3. Nginx 499/502

**Проверка:**
```bash
tail -1000 /var/log/nginx/grpc-error.log | grep -E ' 499 | 502 ' | wc -l
```

**Если всплески:**
- Проверить `grpc_read/send_timeout 300s` в nginx конфиге
- Проверить `worker_connections` в nginx
- Проверить системные `ulimit` (file descriptors)

---

### 4. Версионные гонки

**Проверка:**
```bash
# CI-gate должен ловить
bash scripts/validate_updates.sh 20.151.51.172 443

# Проверка Cache-Control
curl -I -k https://20.151.51.172/updates/appcast.xml | grep Cache-Control
curl -I -k https://20.151.51.172/updates/health | grep Cache-Control
```

**Ожидаемые значения:**
- `appcast.xml`: `Cache-Control: public, max-age=60`
- `/updates/health`: `Cache-Control: public, max-age=30`

---

## Критерии перехода между этапами

### Обязательные условия

- [x] p95 `StreamAudio` ≤ 1000ms
- [x] error-rate ≤ 5%
- [x] отказов backpressure ≤ 1%
- [x] нет всплесков `retry/abort` (>×1.5 от baseline)

### Проверка

```bash
./scripts/check_ramp_guardrails.sh server.log 100
```

**Если все зелёные — переходим на следующий этап.**

---

## Ссылки

- `Docs/RAMP_PLAN.md` — детальный план раскатки
- `Docs/BACKPRESSURE_README.md` — руководство по backpressure
- `Docs/BETA_GATE_CHECKLIST.md` — чеклист для beta gate
- `scripts/preflight_check.sh` — префлайт-проверка
- `scripts/check_ramp_guardrails.sh` — проверка гвардрайлов
- `scripts/monitoring_jq.sh` — jq-выражения для мониторинга
- `scripts/setup_alerts.sh` — примеры алёртов

---

**Последнее обновление:** PR-7 завершён  
**Статус:** ✅ Готово к canary выкатке

