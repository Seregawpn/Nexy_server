> [!WARNING] ARCHIVE NOTICE
> Этот документ архивный и не является source of truth.
> Актуальные каноны:
> - `server/Docs/SERVER_DEPLOYMENT_GUIDE.md` (деплой кода на удаленный сервер)
> - `server/Docs/RELEASE_AND_UPDATE_GUIDE.md` (публикация DMG/PKG и update-канал)
> - `server/Docs/DEPLOY_INCIDENT_RUNBOOK.md` (инциденты, зависимости, конфиги, rollback)

# Ramp Plan - План раскатки трафика (PR-7)

## Этап A — 1% (30–60 мин)

**Гвардрайлы:**
- [ ] p95 `StreamAudio` ≤ 1000 ms
- [ ] error-rate ≤ 5%
- [ ] нет всплеска `decision=retry|abort` > базовой линии ×1.5
- [ ] отказов backpressure ≤ 1% от попыток

**Если чисто — идём дальше.**

### Проверка гвардрайлов:

```bash
# p95 latency
grep -E 'dur_ms=[0-9]+.*method=StreamAudio' server.log | tail -100 | grep -oE 'dur_ms=([0-9]+)' | cut -d= -f2 | sort -n | awk '{latencies[NR]=$1} END {n=length(latencies); p95_idx=int(n*0.95); print latencies[p95_idx]}'

# error rate
total=$(grep -c 'scope=grpc method=StreamAudio' server.log | tail -100)
errors=$(grep -c 'decision=error.*method=StreamAudio' server.log | tail -100)
error_rate=$(echo "scale=2; $errors * 100 / $total" | bc)
echo "Error rate: $error_rate%"

# decision_rate всплеск
retry_abort=$(grep -c 'decision=(retry|abort)' server.log | tail -100)
baseline=$(grep -c 'decision=(retry|abort)' server.log | head -100)
if [ $retry_abort -gt $((baseline * 3 / 2)) ]; then
    echo "⚠️ Всплеск retry/abort: $retry_abort > $((baseline * 3 / 2))"
fi

# backpressure отказы
backpressure_rejects=$(grep -c 'RESOURCE_EXHAUSTED.*stream' server.log | tail -100)
total_streams=$(grep -c 'decision=stream_acquired' server.log | tail -100)
if [ $total_streams -gt 0 ]; then
    reject_rate=$(echo "scale=2; $backpressure_rejects * 100 / $total_streams" | bc)
    echo "Backpressure reject rate: $reject_rate%"
    if [ $(echo "$reject_rate > 1" | bc) -eq 1 ]; then
        echo "❌ Backpressure reject rate превышен: $reject_rate%"
    fi
fi
```

---

## Этап B — 25% (2–4 часа)

**Повтор гвардрайлов:**
- [ ] p95 `StreamAudio` ≤ 1000 ms
- [ ] error-rate ≤ 5%
- [ ] нет всплеска `decision=retry|abort` > базовой линии ×1.5
- [ ] отказов backpressure ≤ 1% от попыток

**Отдельно следим:**
- [ ] Nginx 499 (client closed) — не должно быть всплесков
- [ ] Nginx 502 (bad gateway) — не должно быть всплесков

**Если чисто — на 50%.**

### Проверка Nginx ошибок:

```bash
# Nginx 499/502
tail -1000 /var/log/nginx/grpc-error.log | grep -E ' 499 | 502 ' | wc -l

# Топ ошибок Nginx
tail -1000 /var/log/nginx/grpc-error.log | grep -E ' 499 | 502 ' | awk '{print $9}' | sort | uniq -c | sort -rn
```

---

## Этап C — 50% (полдня)

**Наблюдаем:**
- [ ] drift p95 (нет постепенного роста)
- [ ] валидируем graceful-shutdown на «живом» трафике одной реплике

**Если чисто — 100% на следующий день, при включенном kill-switch.**

### Проверка drift p95:

```bash
# p95 по 5-минутным окнам
for i in {0..11}; do
    window_start=$(date -d "$i*5 minutes ago" +%s)
    window_end=$(date -d "$((i+1))*5 minutes ago" +%s)
    p95=$(grep -E "ts=.* dur_ms=" server.log | awk -v start=$window_start -v end=$window_end '$2 >= start && $2 <= end {print $NF}' | grep -oE 'dur_ms=([0-9]+)' | cut -d= -f2 | sort -n | awk '{latencies[NR]=$1} END {n=length(latencies); p95_idx=int(n*0.95); print latencies[p95_idx]}')
    echo "Window $i: p95 = $p95 ms"
done
```

### Тест graceful-shutdown:

```bash
# На одной реплике
kill -TERM <PID>

# Проверяем логи
tail -f server.log | grep -E 'decision=shutdown|decision=stop'
```

---

## Этап D — 100% (следующий день)

**Условия:**
- [ ] Все гвардрайлы пройдены на 50%
- [ ] Graceful-shutdown протестирован
- [ ] Kill-switch включен и проверен
- [ ] Мониторинг настроен

**Мониторинг:**
- [ ] Алёрты на p95 > 1000ms (warn), >1500ms (page)
- [ ] Алёрты на error-rate > 5% (warn), >10% (page)
- [ ] Алёрты на рост unavailable/retry/abort в ×2 от медианы

---

## Kill-Switch

**Включение:**
```bash
export NEXY_KS_DISABLE_<FEATURE>=true
# или через unified_config
```

**Проверка:**
```bash
python -c "from config.unified_config import get_config; c = get_config(); print(c.is_kill_switch_active('disable_<feature>'))"
```

---

## Post-Mortem Checklist

После каждого этапа:
- [ ] Собрать метрики: p95, error-rate, decision_rate
- [ ] Проверить логи на аномалии
- [ ] Документировать результаты в `Docs/CURRENT_STATUS_REPORT.md`
- [ ] Принять решение о переходе на следующий этап

