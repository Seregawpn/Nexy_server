## План вывода Nexy в тестовую бету (macOS)

**Обновлено:** 15 января 2025  
**Назначение:** единый источник истины о готовности серверной части к закрытой бете. Системный обзор (клиент + сервер) — `Docs/SYSTEM_CONCEPT.md`.

---

## 1. Картина на сегодня

| Канал | Статус | Комментарии / ссылки |
|-------|--------|----------------------|
| Dev (server) | ✅ активен | Все сервисы поднимаются через `server/server/main.py`. |
| Beta (server) | ✅ деплой проверен | gRPC + health + update service доступны. |
| Production rollout | ⏳ чек-лист в работе | Инфраструктура готова, финализируем `Docs/GLOBAL_DELIVERY_PLAN.md` (DELIVERY-002). |

**Основные утверждения:**
- ✅ **Сервер** развёрнут на Azure VM (20.151.51.172): gRPC (50051), TLS-прокси (443), HTTP health (8080), Update service (8081). Точки входа — `server/server/main.py` и `server/server/modules/grpc_service/core/grpc_server.py`.
- ✅ **Мониторинг и тесты**: `scripts/run_release_suite.py`, `scripts/pre_build_gate.sh`, `scripts/prepare_release.sh` — зелёные.
- ✅ Системный обзор (клиент + сервер): `Docs/SYSTEM_CONCEPT.md`.

**Активные риски:**  
`TCC-AX-001` — миграция с приватного `TCCAccessRequest` на публичный API.  
`AUDIO-035` — уточнить retry для CoreAudio HAL Error 35.  
`DELIVERY-002` — зафиксировать все шаги Azure/AppCast в `GLOBAL_DELIVERY_PLAN.md`.

---

## 2. Архитектура платформы (сервер)
- **Точка входа:** `server/server/main.py` — запускает aiohttp endpoints (`/health`, `/status`) и асинхронный gRPC сервер.
- **gRPC стек:** `server/server/modules/grpc_service/core/grpc_server.py` + `grpc_service_manager`. Контроль нагрузки (`backpressure.py`), перехватчики (`grpc_interceptor.py`).
- **Доменные модули:** `server/server/modules/audio_generation`, `text_processing`, `session_management`, `interrupt_handling`, `update`.
- **Конфигурация:** `server/server/config/unified_config.py` — один YAML/ENV источник (метаданные версии, порты, ключи Azure TTS, Gemini Live).
- **Обновления:** `server/server/modules/update` выдаёт AppCast/DMG, синхронизирован с клиентским конфигом (порты и URL).
- **Мониторинг и логирование:** `server/server/utils/logging_formatter.py`, `metrics_collector.py`; логика используется main.py и gRPC сервером.

---

## 3. Принципы разработки и эксплуатации

1. **Single Source of Truth:** версия сервера задаётся в `server/server/config/unified_config.py`.
2. **Никаких «скрытых» параметров** — все фичефлаги и приоритеты описаны в YAML.
3. **Безопасные обновления:** только HTTPS (допускается self-signed на бете), проверка контрольных сумм.
4. **Scriptable Releases:** каждый шаг релиза автоматизирован — см. раздел 5.

---

## 4. Обновления, упаковка и распространение

- **Упаковка:** PyInstaller → pkgbuild/productbuild → notarization. Скрипт: `scripts/prepare_release.sh` (включает pre-build gate, release suite, сборку PKG/DMG, валидацию).
- **Артефакты:** подписанный `.app`, `pkg`, `dmg`. Хранятся в `dist/` и загружаются на Azure VM в каталог `/var/www/updates`.
- **AppCast:** `https://20.151.51.172/updates/appcast.xml` (stable), а также beta/alpha каналы — задаются в `updater.default.channels`.
- **Сервер обновлений:** часть `server/server/modules/update`, подключена в `server/server/main.py`. Следит за версией (`SERVER_VERSION`, `SERVER_BUILD`) и выдаёт JSON для health/status.

---

## 5. Проверки и автоматизация (сервер)

| Скрипт / документ | Назначение |
|------------------|-----------|
| `Docs/CI_GRPC_CHECKS.md` | CI проверки совместимости gRPC, health/status. |
| `Docs/GRPC_PROTOCOL_AUDIT.md` | Аудит протокола, риски и изменения. |
| `Docs/FLOW_INTERACTION_SPEC.md` | Канон серверных flow и контрактов. |

В CI запускаются проверки gRPC и health/status.

---

## 6. Операционное тестирование (сервер)

1. **Поток запроса:** см. `Docs/FLOW_INTERACTION_SPEC.md` (StreamAudio Flow).  
2. **Health/Status:** `/health` и `/status` должны отвечать стабильно.  
3. **Нагрузка:** latency и RPS валидируются нагрузочным тестом.  

---

## 7. План движения и критерии готовности (сервер)

### 7.1 Состояние циклов
- ✅ **Цикл 1 — Локальный сервер:** gRPC + health/status.
- ✅ **Цикл 2 — Деплой на VM:** TLS, прокси, monitoring.
- ⏳ **Цикл 3 — Нагрузочные проверки:** стабилизация параметров под целевой RPS.

### 7.2 Требования ко входу в Цикл 4
1. Подписанный PKG/DMG загружены на AppCast, проверены вручную на 2–3 машинах.
2. Подготовлены инструкция для тестеров (permissions, hotkey, примеры сценариев) и канал обратной связи (Discord/email).
3. Минимальная телеметрия сервера включена (см. `Docs/CI_GRPC_CHECKS.md`).
4. Скрипты `run_release_suite.py` и `prepare_release.sh` прошли на последнем билде.

### 7.3 Действия на время беты
1. Сформировать волну 20–50 пользователей (US/CA accessibility community).
2. Выпустить билд N на AppCast, подтвердить автообновление на контрольной группе.
3. Провести «консьерж»-сессию с 3 пилотами и зафиксировать проблемы (логирование + обратная связь).
4. Запланировать мини-спринт на критические фидбеки, подготовить билд N+1.
5. Сформировать отчёт: TTV, успешность сценариев, топ-проблемы, предложения по улучшению UX.

---

## 8. Риски и next steps

| ID | Описание | Что делаем |
|----|----------|------------|
| TCC-AX-001 | Перевести проверку Accessibility на публичный API | Исследование API Accessibility Inspector + обновление `permissions`/`permission_restart`. |
| AUDIO-035 | Дебаунс/ретраи для HAL Error 35 | Анализ логов `default_audio` и `voice_recognition`, настройка `silent_window_seconds`, `retry_delay`. |
| DELIVERY-002 | Закрепить Azure/AppCast план | Обновить `Docs/GLOBAL_DELIVERY_PLAN.md`, описать выкладку AppCast и сервера обновлений. |

**Проект готов к закрытому бета-тестированию.** Следующий рубеж — успешное завершение Цикла 4 и блокировка Production rollout чек-листа.
