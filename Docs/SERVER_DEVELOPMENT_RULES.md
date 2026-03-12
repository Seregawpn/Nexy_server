# Правила разработки серверной части Nexy (v2.1)

**Обновлено:** 11 января 2026  
**Назначение:** единый набор правил разработки и релизов серверной части Nexy. Документ закрепляет обязательные гейты, формат версий, контракты с клиентом и проверки, на которые уже опираются живые процессы (Sparkle, health, состояние разрешений, gRPC).

---

## 📚 Связанные документы

**Основные источники истины:**

- `Docs/ARCHITECTURE_OVERVIEW.md` — архитектура, FSM, таблицы исключений, backpressure, graceful shutdown
- `Docs/STATE_CATALOG.md` — оси состояний, метрики, владельцы (ответственный: Tech Lead клиента)
- `Docs/BACKPRESSURE_README.md` — политика лимитов, конфиг, troubleshooting
- `Docs/CI_GRPC_CHECKS.md` — CI-workflow, проверки, валидация размеров
- `Docs/RELEASE_AND_UPDATE_GUIDE.md` — канон системы обновлений (форматы версий, публикация, манифест, синхронизация размеров)
- `Docs/_archive/RAMP_PLAN.md` — историческая справка по раскатке (не канон)
- `Docs/SERVER_DEPLOYMENT_GUIDE.md` — процедура отката и kill-switch
- `Docs/ADR_TEMPLATE.md` — шаблон решений (ADR) с полями для осей/guards
- `monitor_inbox/` — локальная папка авто-публикации инцидентов (оперативный triage)

---

## 0. Архитектурные правила (обязательные)

### 0.1 Incident Inbox First (обязательно)

- Перед любым ручным SSH/Azure-troubleshooting сначала проверять `monitor_inbox/` в текущем workspace.
- Если есть свежий `*__incident__server-monitor.md`, он считается первичным входом для triage.
- Если `monitor_inbox/` пуст, запускаем one-shot проверку:

```bash
server/scripts/publish_server_incident_local.sh
```

- Для постоянного локального мониторинга использовать watcher:

```bash
server/scripts/start_local_server_monitor.sh
```

- Остановка watcher:

```bash
server/scripts/stop_local_server_monitor.sh
```

- `server/modules/*` — только бизнес-логика. Оркестрация и сценарии располагаются в `server/integrations/{core,service_integrations,workflow_integrations}`.
- Прямых импортов между модулями нет; все обращения идут через `ModuleCoordinator` (`server/integrations/service_integrations/module_coordinator.py`).
- Каждый модуль реализует `UniversalModuleInterface`:
  - **Прямая реализация:** `text_processing` использует `module.py` (напрямую реализует интерфейс)
  - **Адаптеры:** Остальные модули используют `adapter.py` (обёртка над существующими процессорами), предоставляющие `initialize/process/cleanup/status`
- **Опциональные модули:** `database`, `audio_generation`, `text_filtering`, `interrupt_handling` — сервер может работать без них при ошибке инициализации (graceful degradation).
- `GrpcServiceManager` создаёт capability через `ModuleFactory`, а не прямыми импортами.
- LoggingInterceptor (`modules/grpc_service/core/grpc_interceptor.py`) подключается всегда. Он переупаковывает `RpcMethodHandler` через `_replace` и фиксирует `decision=start|abort|complete`.
- Единственный proto-файл — `modules/grpc_service/streaming.proto`. Изменения обновляют его и `Docs/GRPC_PROTOCOL_AUDIT.md`.
- Лимиты, таймауты и флаги читаются из `server/config/unified_config.py` или env-override; хардкоды запрещены.

---

## 1. Гейты перед мерджем

### **Hard Architecture Gate (обязательно, CI fail)**

`Server Quality Gate` обязан запускать и успешно завершать:

```bash
python scripts/verify_docs_root_server_links.py
python server/scripts/verify_pr_single_owner_check.py
python server/scripts/verify_feature_flags.py
python server/scripts/verify_architecture_guards.py
```

**Что блокируется автоматически:**
- PR без заполненного блока `Single Owner Check`:
  - `Owner (SoT):`
  - `Duplicate Removed:`
  - `No Second Path Rationale:`
  - `Legacy Removal Date:`
- Новые `sys.path.insert(...)` в runtime-слоях (`server/modules`, `server/integrations`, `server/api`, `server/main.py`).
- Новые `legacy`-ветки без явного срока удаления `LEGACY_REMOVE_BY: YYYY-MM-DD`.
- Новые runtime ветки по флагам `use_*` / `disable_*` без регистрации в `Docs/FEATURE_FLAGS.md`.
- Нарушение правила `one event, one owner` для критичного события `mcp.command_request` (owner: `integrations/core/assistant_response_parser.py`).

**Принцип:** если проверка падает, merge запрещен до устранения причины (локальные workaround запрещены).

### **Flags Discovery (ОБЯЗАТЕЛЬНО перед изменениями)**

**ОБЯЗАТЕЛЬНО**: Перед любыми правками логики запустить discovery режим для модуля/интеграции:

```bash
python scripts/verify_feature_flags.py --module <path>
```

**Результаты discovery**:
- Все найденные флаги (env и config) с метаданными из реестра
- Контекст использования (файл, строка, функция/класс, код)
- YAML пути для config-флагов
- Незарегистрированные флаги помечены как `[UNREGISTERED]`

**Включение в план**: Результаты discovery должны быть включены в план изменений в раздел "Flags Discovery" для предотвращения дублирования и конфликтов.

### **SIMPLE-гейт (до Impact)**

### **SIMPLE-гейт (до Impact)**
- [ ] v0 ≤60 LOC, ≤1 файл, без новых фича-флагов/демонов/зависимостей
- [ ] 1 happy + 1 негативный тест

Если условия не выполняются — обязательна микро-ADR (не менее 7 строк: контекст, альтернатива «попроще», обоснование, ожидаемый эффект).

### **Impact-гейт (перед мерджем)**
- [ ] Приложен `.impact/change_impact.yaml` (оси, инварианты, guards, тест-стратегия, метрики, роллаут)
- [ ] `Docs/STATE_CATALOG.md` обновлён, если затронуты оси/читатели/писатели; приложена ссылка или дифф на внешний канон матрицы взаимодействий (клиентский `interaction_matrix.yaml`)
- [ ] 8–14 pairwise тестов + ≥2 негативных по заявленным осям / сценариям
- [ ] Логи решений/апдейтов собираются и доступны локально
- [ ] `/health` отдаёт `latest_version` и `latest_build` как строки, `/updates/appcast.xml` содержит тот же номер; логи апдейта без ошибок
- [ ] Фича-флаг + kill-switch прописаны (если релиз инкрементальный)
- [ ] CI-проверки (lint, contract, validate_release_size) выполняются по `Docs/CI_GRPC_CHECKS.md`
- [ ] Локальные тесты пройдены: `pytest tests/test_pr2_1_coordinator.py` и `python scripts/grpc_smoke.py localhost 50051` (или прикладываем логи из CI)

---

## 2. Версии и обновления: один канон

**Источник истины:** `Docs/RELEASE_AND_UPDATE_GUIDE.md` — раздел `Version Source of Truth` — единственный источник истины

**Перед деплоем — обязательный чеклист:**
- [ ] Версии совпадают во всех компонентах (manifest, appcast, health)
- [ ] **🔴 КРИТИЧНО:** При обновлении версии в манифесте **ОБЯЗАТЕЛЬНО** обновить размер файла (`artifact.size`) и SHA256 (`artifact.sha256`)
- [ ] Размер файла совпадает с GitHub Content-Length (проверить через `curl -sL -I <URL> | grep -i content-length`)
- [ ] Локальные DMG/артефакты отсутствуют на сервере
- [ ] Подписи (Ed25519) валидны
- [ ] Все поля версий — строковые (`"1.0.0"`)

**⚠️ ВАЖНОЕ ПРАВИЛО:** При обновлении версии в манифесте на сервере (`version` и `build`) **НИКОГДА** не забывайте обновлять:
1. **`artifact.size`** — получить реальный размер с GitHub CDN
2. **`artifact.sha256`** — вычислить SHA256 хеш файла
3. **`artifact.url`** — проверить, что URL указывает на актуальный файл

Несоблюдение этого правила приводит к ошибкам установки обновлений у клиентов!

**Детальная проверка:** см. `Docs/RELEASE_AND_UPDATE_GUIDE.md` и `Docs/DEPLOY_INCIDENT_RUNBOOK.md` (проверки, скрипты, troubleshooting).

---

## 3. Health, AppCast и SLA апдейтов

- `/health` — единственный источник правды для автоматизации; значения версий только строками.
- `/updates/appcast.xml` обязан содержать те же версии и корректные `length`, `sparkle:shortVersionString`, `sparkle:minimumSystemVersion`.
- Перед мерджем фиксируем вывод health + appcast в описание PR (или прикладываем лог команды).
- При сбоях — ссылка на логи обновлений (`GitHub Actions: Deploy Server`, `/home/azureuser/voice-assistant/logs/update.log` или эквивалент).

---

## 4. Проверка размеров и подписи обновления

**Источник истины:** `Docs/RELEASE_AND_UPDATE_GUIDE.md`

- Деплой и ручные проверки используют фактический размер файла с GitHub CDN.
- `scripts/deploy.sh` deprecated и заблокирован.
- Использовать только `scripts/publish_assets_and_sync.py` для публикации артефактов.
- Прямой publish в `stable` запрещен: обязательная воронка `publish --channel beta` -> validation -> `promote --source beta --target stable`.
- Канонический owner-path артефактов: `client/release_inbox/<target>/<version>` (`production`/`staging`/`local`), без смешивания target и версий в одной папке.
- Server-side beta feed gate: `UPDATE_BETA_ENABLED=true` только на время теста; после теста обязательный возврат в `false`.
- Не возвращаться к локальным DMG на сервере — очищаем `/home/azureuser/voice-assistant/updates/downloads/*.dmg`.
- Сверка размеров обязана стать частью ручного чеклиста и CI.

**Автоматическая проверка:**
```bash
# Используйте готовый скрипт
bash scripts/validate_updates.sh [HOST] [PORT]

# Или вручную (актуальный IP: nexy-prod-sergiy.canadacentral.cloudapp.azure.com)
APPCAST_SIZE=$(curl -s https://nexy-prod-sergiy.canadacentral.cloudapp.azure.com/updates/appcast.xml | grep -o 'length="[^"]*"' | cut -d'"' -f2)
GITHUB_SIZE=$(curl -s -L -I https://github.com/Seregawpn/Nexy_production/releases/download/Update/Nexy.dmg | grep -i "content-length:" | tail -1 | awk '{print $2}' | tr -d '\r\n')
echo "AppCast: $APPCAST_SIZE байт"
echo "GitHub:  $GITHUB_SIZE байт"
test "$APPCAST_SIZE" = "$GITHUB_SIZE"
```

**CI-валидация:** см. `Docs/CI_GRPC_CHECKS.md` -> шаг `validate_release_size`

---

## 5. Гейт перезапуска разрешений

- Решение о рестарте после запроса разрешений проходит **только** через `permission_restart_gateway(snapshot)`. Никаких параллельных re-check апдейтов/таймеров в обход.
- Гейт оперирует иммутабельным снапшотом: разрешения, режимы, статус апдейтов, тайминг последнего запроса.
- Периодический опрос апдейтов/разрешений допускается только под фича-флагом, выключенным по умолчанию.
- Все race-condition кейсы из [Docs/STATE_CATALOG.md] и таблицы edge-кейсов должны покрываться тестами гейта.

---

## 6. Ответы ассистента и MCP команды

**Историческая справка:** `Docs/_archive/MCP_INTEGRATION_SUMMARY.md`.

**Основные принципы:**
1. Решения об action принимает ассистент (LLM), сервер только транслирует команды клиенту
2. Парсер: `integrations/core/assistant_response_parser.py` — толерантен к "кривым" данным (fallback на обычный текст)
3. Фича-флаг: `features.forward_assistant_actions` (по умолчанию `false`) — включает передачу JSON на клиента
4. Kill-switch: `kill_switches.disable_forward_assistant_actions` — немедленное отключение без релиза

**Формат ответа ассистента:**
- Обычный ответ: только поле `text` (идёт на TTS и стриминг)
- Action-ответ: JSON с полями `session_id`, `command`, `args`, `text` (текст на TTS, JSON на клиента)

**Документация:**
- `Docs/ARCHITECTURE_OVERVIEW.md` → раздел "Ответы ассистента и MCP команды"
- `Docs/_archive/MCP_INTEGRATION_SUMMARY.md` — итоговый summary (исторический).
- `Docs/_archive/MCP_COMMAND_INTEGRATION_PLAN.md` — исторический план (для справки).

---

## 7. Политика совместимости gRPC (PR-3)

**Канон:** proto-файл хранится только в `modules/grpc_service/streaming.proto`; альтернативные пути запрещены.

1. Допускается только **добавление optional полей** или новых RPC с backward-совместимой сигнатурой.
2. Для breaking-изменений — отдельный `v2` сервис/метод + feature-флаг на сервере.
3. Поддерживаем обе версии минимум **2 релиза**; общие клиенты переключаются флагом.
4. Перед мерджем — smoke-тест с текущим клиентом (`python scripts/grpc_smoke.py` или эквивалент) + ссылка на результат в PR.

**Документация:**
- `Docs/GRPC_PROTOCOL_AUDIT.md` — полный аудит протокола, таблицы полей, правила совместимости
- `SMOKE_TEST_QUICK_START.md`, `READY_FOR_SMOKE_TEST.md` — актуальные команды smoke/health перед релизом
- `scripts/grpc_smoke.py` (production) и `scripts/grpc_smoke.py` (локально) — smoke-тест для проверки совместимости
- `scripts/check_grpc_health.py` — проверка health/status/портов

**Автоматические проверки:**
- Smoke-тест: `python scripts/grpc_smoke.py [HOST] [PORT]`
- Health check: `python scripts/check_grpc_health.py [HOST] [PORT]`
- CI гейты: health, status, порт 50051, версии в AppCast

**Регенерация protobuf:**
```bash
cd server/modules/grpc_service
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. streaming.proto
```

---

## 8. Политика роллаута (PR-7)

**Лимиты стримов/таймаутов:** см. `Docs/BACKPRESSURE_README.md` (политика лимитов, конфиг, troubleshooting)

### Правила роллаута изменений

Любое изменение, затрагивающее взаимодействие >2 осей/модулей, должно проходить через контролируемый роллаут:

1. **Feature-flag обязателен**
   - Все изменения поведенческих правил включаются через feature-flag в `unified_config`
   - Пример: `features.use_new_workflow: true`

2. **Этапы роллаута**
   - **1%** → тестирование на ограниченной группе
   - **25%** → расширенное тестирование
   - **100%** → полный роллаут
   - Процент контролируется через конфигурацию (можно добавить в `unified_config`)

3. **Kill-switch обязателен**
   - Для каждого feature-flag должен быть соответствующий kill-switch
   - Формат: `NEXY_KS_DISABLE_<FEATURE_NAME>` в окружении/конфиге
   - Kill-switch выключает поведение немедленно без релиза

4. **Shadow-mode (опционально)**
   - Считаем решение, но не применяем (для сбора метрик)
   - Включается через feature-flag: `features.shadow_mode_<feature>: true`

5. **Минимальная поддержка**
   - Минимум **2 релиза** поддерживаются обе версии (старая и новая)
   - После 2 релизов можно удалить старую версию

### Пример конфигурации роллаута

```yaml
features:
  use_new_workflow: true
  rollout_percentage: 25  # 1%, 25%, 100%

kill_switches:
  disable_new_workflow: false
```

### Документация в PR

В PR для изменений с роллаутом должно быть:
- Описание feature-flag и kill-switch
- План роллаута (этапы, метрики)
- Условия отката (когда включать kill-switch)
- Метрики успешности (SLO, ошибки и т.д.)

### Регистрация флагов (ОБЯЗАТЕЛЬНО)

**ВАЖНО**: Все флаги (env и config) должны быть зарегистрированы в `Docs/FEATURE_FLAGS.md` ДО использования в коде.

**Правила**:
1. **Новый флаг запрещён без добавления в `Docs/FEATURE_FLAGS.md`** и прохождения `scripts/verify_feature_flags.py`
2. **Config flags** (`features.*`, `kill_switches.*`) так же обязаны быть зарегистрированы в реестре
3. **Env overrides** (`USE_*`, `FORWARD_ASSISTANT_ACTIONS`) обязаны быть зарегистрированы в реестре (тип: `env_override`)
4. **Проверка перед мерджем**: `python scripts/verify_feature_flags.py` должен проходить без ошибок
5. **Формат регистрации**: см. `Docs/FEATURE_FLAGS.md` (таблица с колонками: name, type, owner, default, scope, kill_switch, description)
6. **Исключения**: env переменные, которые не являются feature flags (например, `USE_GITHUB`, `USE_TLS`), должны быть добавлены в список исключений в `scripts/verify_feature_flags.py` и документированы в `Docs/FEATURE_FLAGS.md` (раздел "Исключения")

**Пример**:
```bash
# Перед использованием нового флага
# 1. Добавить в Docs/FEATURE_FLAGS.md
# 2. Запустить проверку
python scripts/verify_feature_flags.py
# 3. Только после успешной проверки использовать флаг в коде
```

---

## 9. STATE_CATALOG и матрица взаимодействий

- Любое изменение осей состояний или читателей/писателей фиксируется в `Docs/STATE_CATALOG.md` (сервер) и отражается во внешнем каноне матрицы взаимодействий (клиентский `interaction_matrix.yaml`).
- В PR прикладываем ссылку/дифф на клиентский репозиторий + обоснование того, как серверное изменение отражается на клиенте.
- Без синхронизации каталогов мердж запрещён.

**Ответственный за актуальность:** Tech Lead клиента (указан в `Docs/STATE_CATALOG.md`)

---

## 10. Конфигурация и секреты

- Ориентир для всех окружений — `server/config.env`. Формат не меняем без отдельного ADR.
- Обязательный шаблон:

```dotenv
NEXY_ENV=prod
GITHUB_TOKEN=...
GRPC_HOST=auto
GRPC_PORT=50051
HTTP_HOST=auto
HTTP_PORT=8080
UPDATE_HOST=auto
UPDATE_PORT=8081
```

- Новые переменные добавляем только после описания в ADR + обновления шаблона. Все значения храним в секретах (GitHub, Azure).
- Значение `auto` для `GRPC_HOST`/`HTTP_HOST`/`UPDATE_HOST` переключает биндинг в зависимости от `NEXY_ENV`: dev → `0.0.0.0`, stage/prod → `127.0.0.1`.

---

## 11. Док-статусы: только факты

- Статусы в `Docs/_archive/CURRENT_STATUS_REPORT.md`, `Docs/ARCHITECTURE_OVERVIEW.md`, релиз-заметки и отчёты используют только факты: ссылки на тест-планы, логи запусков, хэши билдов.
- Формулировки «готово/почти готово» заменяем на: «прогонен скрипт X», «загружен билд SHA256=...», «см. лог GitHub Actions job #123».
- Любая маркетинговая речь удаляется; документ = проверяемая истина.

---

## 12. Руководство: быстрый откат (PR-7)

**Процедура отката и kill-switch:** см. `Docs/SERVER_DEPLOYMENT_GUIDE.md` → раздел "Rollback"

### Шаги быстрого отката

При обнаружении критической проблемы в production:

1. **Toggle kill-switch**
   ```bash
   # Установить в config.env или через переменные окружения
   export NEXY_KS_DISABLE_<FEATURE_NAME>=true
   # Или через unified_config
   # kill_switches.disable_<feature_name>: true
   ```

2. **Verify /health и /status**
   ```bash
   # Проверка health endpoint
   curl https://nexy-prod-sergiy.canadacentral.cloudapp.azure.com/health
   
   # Проверка status endpoint
   curl https://nexy-prod-sergiy.canadacentral.cloudapp.azure.com/status | jq
   ```

3. **Re-run smoke tests**
   ```bash
   # Проверка базовой функциональности
   python scripts/grpc_smoke.py nexy-prod-sergiy.canadacentral.cloudapp.azure.com 443
   
   # Проверка health/status
   python scripts/check_grpc_health.py nexy-prod-sergiy.canadacentral.cloudapp.azure.com 443
   
   # Проверка гвардрайлов
   ./scripts/check_ramp_guardrails.sh server.log 100
   ```

4. **Post mortem (5-минутное окно логов)**
   - Собрать логи: `tail -n 1000 server.log | grep -E "error|ERROR|decision=error"`
   - Проверить метрики: `grep -E "p95_latency|error_rate|decision_rate" server.log | tail -20`
   - Собрать агрегаты до/после: p95, error-rate, decision_rate
   - Документировать причину отката в `Docs/_archive/CURRENT_STATUS_REPORT.md`

### Проверка после отката

После отката убедиться, что:
- [ ] Health endpoint возвращает 200 OK
- [ ] Status endpoint возвращает валидный JSON
- [ ] gRPC smoke test проходит
- [ ] Логи не содержат критических ошибок
- [ ] Метрики вернулись к нормальным значениям

**Детальный runbook:** см. также `Docs/_archive/CANARY_CHECKLIST.md` → раздел "Rollback"

---

## 13. Быстрые ссылки

### Навигационная матрица

| **Область** | **Документ** | **Описание** |
|------------|--------------|--------------|
| 🧱 Архитектура | `Docs/ARCHITECTURE_OVERVIEW.md` | Архитектура, FSM, таблицы исключений, backpressure, graceful shutdown |
| 🔄 Обновления | `Docs/_archive/GITHUB_UPDATE_SYSTEM.md` | Пайплайн деплоя, подписи, GitHub интеграция |
| 🧩 FSM/States | `Docs/STATE_CATALOG.md` | Оси состояний, метрики, владельцы |
| ⚙️ Роллаут | `Docs/_archive/RAMP_PLAN.md` | План раскатки трафика, гвардрайлы, этапы |
| 📦 Backpressure | `Docs/BACKPRESSURE_README.md` | Политика лимитов, конфиг, troubleshooting |
| 🔍 CI Checks | `Docs/CI_GRPC_CHECKS.md` | CI-workflow, проверки, валидация размеров |
| 📝 ADR | `Docs/ADR_TEMPLATE.md` | Шаблон решений (ADR) с полями для осей/guards |
| ✅ Canary | `Docs/_archive/CANARY_CHECKLIST.md` | Чеклист для canary выкатки |
| 🚀 Beta Gate | `Docs/_archive/BETA_GATE_CHECKLIST.md` | Чеклист для beta gate |
| 📊 Протокол gRPC | `Docs/GRPC_PROTOCOL_AUDIT.md` | Аудит протокола, контракт-таблицы |

### Критические фиксы

| **Область** | **Документ** | **Описание** |
|------------|--------------|--------------|
| 🔴 Версионирование | `Docs/RELEASE_AND_UPDATE_GUIDE.md` | **Канон системы обновлений** (включая форматы версий) — источник истины |
| 🔧 Update Fixes | `Docs/RELEASE_AND_UPDATE_GUIDE.md` | **Канон обновлений** — синхронизация размеров с GitHub CDN |

### Дополнительные ссылки

- Шаблон оценки влияния (change impact): `.impact/change_impact.client_template.yaml`
- План приведения к принципам: выполнен (PR-0..PR-8 завершены)
- Шаблон PR-чеклиста: `Docs/_archive/PR_CHECKLIST_TEMPLATE.md`
- Корневой README: `README.md` (навигационная матрица)

---

## 14. FSM + Guard-условия на домены

- Для доменов `audio`, `permissions`, `mode_management` решения принимаются через FSM-таблицы: `(state, event) --[guard]--> (new_state, action)`.
- Guard-условия обязаны проверять критичные оси: permissions, device, network, firstRun.
- Запрещены скрытые записи состояний в чужие домены — только через EventBus.

**FSM-таблицы:** размещаются в `server/modules/<domain>/fsm.yaml` (или в коде модуля) и документируются в `Docs/ARCHITECTURE_OVERVIEW.md` → раздел "FSM Map".

**Пример решения из снапшота состояния:**
```python
def decide_listen_action(s):
    if s.perm.mic != "granted":
        return Abort("mic_denied", ui="open_settings_mic")
    if s.device.input == "busy" and s.appMode == "LISTENING":
        return Retry("device_busy_backoff")
    if s.network == "offline":
        return Degrade("offline_mode")
    return Start()
```

---

## 15. Decision-логи и метрики (наблюдаемость решений)

Обязательны для FSM/интеграций:

`decision=<start|abort|retry|degrade> ctx={mic=...,screen=...,device=...,network=...,firstRun=...,appMode=...} source=<domain> duration_ms=<int>`

**Метрики:**
- `decision_rate{type}` — распределение решений (start/abort/retry/degrade)
- `stream_open_success_rate` — доля удачных запусков аудио
- `tcc_prompt_duration_ms` — длительность последовательности разрешений (p95)
- `p95_latency_ms` — ключевая метрика CI (p95 latency по RPC методам)

---

## 16. Политика роллаута и SLO

**Проверка гвардрайлов:** `scripts/check_ramp_guardrails.sh` (автоматическая проверка порогов)

**SLO и гвардрайлы:**
- p95 latency ≤ 1000 ms (warn), ≤ 1500 ms (page)
- error-rate ≤ 5% (warn), ≤ 10% (page)
- backpressure failures ≤ 1%
- stream_open_success_rate ≥ 98%

**План раскатки:** см. `Docs/_archive/RAMP_PLAN.md` (этапы, гвардрайлы, метрики)

---

## 17. Политика по ADR

**ADR обязателен** при любых изменениях FSM, guards или осей.

**Шаблон:** `Docs/ADR_TEMPLATE.md` (с полями для осей/guards)

**Требования:**
- ADR должен содержать раздел "Affected Axes / Guards"
- Ссылка на `Docs/STATE_CATALOG.md` и внешний канон матрицы взаимодействий (клиентский `interaction_matrix.yaml`)
- Обновления в `Docs/ARCHITECTURE_OVERVIEW.md` и `Docs/STATE_CATALOG.md`

---

## 18. Единые правила (зафиксированы окончательно)

1. **Форматы версий:** только строковые `"1.0.1"`, источник — `Docs/RELEASE_AND_UPDATE_GUIDE.md` (раздел `Version Source of Truth`)
2. **Размеры и подписи:** всегда сверяются с GitHub CDN (`Content-Length`, `SHA256`, `Ed25519`) — см. `Docs/RELEASE_AND_UPDATE_GUIDE.md`
3. **🔴 КРИТИЧНО: Обновление манифеста:** При обновлении версии (`version`/`build`) **ОБЯЗАТЕЛЬНО** обновлять `artifact.size` и `artifact.sha256` с реальными значениями с GitHub
4. **Локальные файлы:** не допускаются — проверка в CI
5. **Health/AppCast/Manifest:** должны возвращать одинаковые версии и размеры
6. **CI-gate:** блокирует релиз при расхождении версий или размеров
7. **Rollback:** только через kill-switch и post-mortem лог-окно 5 мин
8. **ADR:** обязателен при любых изменениях FSM, guards или осей
9. **Документация:** любое изменение → обновить `Docs/ARCHITECTURE_OVERVIEW.md` и `Docs/STATE_CATALOG.md`

---

Серверные релизы проходят только через этот набор правил: сначала SIMPLE-гейт, затем Impact-гейт, затем деплой с проверками версий, health и гейтами разрешений. Это исключает бесконечные обновления, гонки рестартов и рассинхронизацию с клиентом.
