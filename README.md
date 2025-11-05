# 🎤 Nexy - Интеллектуальный голосовой ассистент

**Production-ready голосовой ассистент с архитектурой уровня enterprise**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production-green.svg)]()
[![Compliance](https://img.shields.io/badge/Compliance-100%25-brightgreen.svg)](server/COMPLIANCE_REPORT.md)

---

## 🎯 О проекте

Nexy - это профессиональный голосовой ассистент с модульной архитектурой, готовый к масштабированию до 100 одновременных пользователей. Проект полностью соответствует enterprise стандартам разработки и документирования.

### ✨ Ключевые особенности

- 🎙️ **Push-to-Talk** - интуитивное управление голосом
- 🧠 **AI интеграция** - Gemini API + Azure TTS
- 📸 **Контекстный захват** - автоматический скриншот экрана
- 🔄 **Real-time streaming** - gRPC с HTTP/2
- 🆔 **Hardware ID** - уникальная идентификация устройств
- 🌐 **Кроссплатформенность** - macOS, Windows, Linux
- ⚡ **Масштабируемость** - до 100 одновременных пользователей
- 🛡️ **Enterprise архитектура** - ModuleCoordinator, FSM, backpressure
- 📊 **Structured logging** - полная наблюдаемость системы
- 🔒 **Graceful shutdown** - безопасное завершение сессий

---

## 📊 Статус проекта

### ✅ Production Ready

| Компонент | Статус | Compliance |
|-----------|--------|------------|
| **Клиентская часть** | ✅ Готова | 100% |
| **Серверная часть** | ✅ Готова | 100% |
| **Документация** | ✅ Полная | 100% |
| **Тестирование** | ✅ Покрыто | 90%+ |
| **Система обновлений** | ✅ Работает | 100% |
| **Мониторинг** | ✅ Реализован | 100% |

**Общее соответствие стандартам:** [100% ✅](server/COMPLIANCE_REPORT.md)

**Готовность к production:** ✅ **100%**

---

## 🏗️ Архитектура

### Клиентская часть (macOS)

```
client/
├── main.py                      # Точка входа
├── config/                      # Единая конфигурация
│   └── unified_config.yaml
├── integration/                 # Слой интеграций
│   ├── core/                    # EventBus, StateManager
│   ├── integrations/            # 19 интеграций
│   └── workflows/               # ListeningWorkflow, ProcessingWorkflow
└── modules/                     # 18 самодостаточных модулей
```

**Ключевые принципы:**
- Event-driven архитектура (EventBus)
- Централизованное управление состоянием (StateManager)
- Workflows для координации режимов
- Модули не знают про EventBus

### Серверная часть (Python)

```
server/
├── main.py                      # Точка входа с graceful shutdown
├── config/
│   ├── unified_config.py        # Единый источник конфигурации
│   └── config.env               # Переменные окружения
├── integrations/                # Координация модулей
│   └── core/
│       └── module_coordinator.py  # ModuleCoordinator
└── modules/                     # 9 серверных модулей
    ├── grpc_service/            # gRPC с backpressure (PR-7)
    ├── text_processing/         # Gemini API
    ├── audio_generation/        # Azure TTS
    └── ...                      # 6 других модулей
```

**Ключевые принципы:**
- ModuleCoordinator для изоляции модулей (ADR-001)
- gRPC с backpressure и interceptors (PR-7)
- Graceful shutdown (PR-7)
- Structured logging (PR-4)
- Feature-flags и kill-switches

**Детальная архитектура:**
- Клиент: [`client/Docs/ARCHITECTURE_OVERVIEW.md`](client/Docs/ARCHITECTURE_OVERVIEW.md)
- Сервер: [`server/Docs/ARCHITECTURE_OVERVIEW.md`](server/Docs/ARCHITECTURE_OVERVIEW.md)

---

## 🚀 Быстрый старт

### Предварительные требования

**Клиент:**
- macOS 12.0+ (основная платформа)
- Python 3.8+
- Микрофон и динамики

**Сервер:**
- Python 3.8+
- PostgreSQL (опционально)
- Azure Speech API key
- Gemini API key

### Установка

1. **Клонируйте репозиторий**
   ```bash
   git clone https://github.com/Seregawpn/Nexy_server.git
   cd Nexy_server
   ```

2. **Установите зависимости**
   ```bash
   # Клиент
   cd client
   pip install -r requirements.txt

   # Сервер
   cd ../server
   pip install -r requirements.txt
   ```

3. **Настройте переменные окружения**
   ```bash
   cd server
   cp config.env.example config.env
   nano config.env  # Заполните API ключи
   ```

   **Обязательные переменные:**
   - `GEMINI_API_KEY` - ключ Gemini API
   - `AZURE_SPEECH_KEY` - ключ Azure Speech
   - `DB_PASSWORD` - пароль PostgreSQL (если используется)

### Запуск

**Сервер:**
```bash
cd server
source config.env
python main.py
```

**Клиент:**
```bash
cd client
python main.py
```

---

## 🎮 Управление

| Действие | Клавиша/Действие | Описание |
|----------|------------------|----------|
| **Начать запись** | Зажать Пробел | Активация микрофона |
| **Продолжить запись** | Удерживать Пробел | Запись команды |
| **Отправить команду** | Отпустить Пробел | Распознавание и обработка |
| **Прервать воспроизведение** | Короткое нажатие Пробел | Остановка ответа ассистента |
| **Выход** | Cmd+Q (macOS) | Graceful shutdown |

---

## 📚 Документация

### Основные документы

| Документ | Описание | Статус |
|----------|----------|--------|
| [`server/COMPLIANCE_REPORT.md`](server/COMPLIANCE_REPORT.md) | **Отчет о соответствии стандартам** | ✅ 100% |
| [`server/Docs/SERVER_DEVELOPMENT_RULES.md`](server/Docs/SERVER_DEVELOPMENT_RULES.md) | **Канон правил разработки** | ✅ v2.0 |
| [`server/Docs/ARCHITECTURE_OVERVIEW.md`](server/Docs/ARCHITECTURE_OVERVIEW.md) | Архитектура сервера | ✅ Актуальна |
| [`client/Docs/ARCHITECTURE_OVERVIEW.md`](client/Docs/ARCHITECTURE_OVERVIEW.md) | Архитектура клиента | ✅ Актуальна |
| [`server/Docs/STATE_CATALOG.md`](server/Docs/STATE_CATALOG.md) | Каталог состояний | ✅ Актуален |

### ADR (Architecture Decision Records)

| ADR | Тема | Статус |
|-----|------|--------|
| [`ADR-001`](server/Docs/decisions/ADR-001-modular-architecture.md) | Модульная архитектура с ModuleCoordinator | ✅ Accepted |

### Специализированные документы

**Система обновлений:**
- [`server/Docs/VERSION_FORMAT_CRITICAL_FIX.md`](server/Docs/VERSION_FORMAT_CRITICAL_FIX.md) - Канон форматов версий
- [`server/Docs/UPDATE_SYSTEM_FIXES.md`](server/Docs/UPDATE_SYSTEM_FIXES.md) - Канон обновлений
- [`server/Docs/GITHUB_UPDATE_SYSTEM.md`](server/Docs/GITHUB_UPDATE_SYSTEM.md) - GitHub интеграция

**Масштабирование и производительность:**
- [`server/Docs/BACKPRESSURE_README.md`](server/Docs/BACKPRESSURE_README.md) - Политика лимитов
- [`server/Docs/RAMP_PLAN.md`](server/Docs/RAMP_PLAN.md) - План раскатки
- [`SCALING_100_USERS_GUIDE.md`](SCALING_100_USERS_GUIDE.md) - Масштабирование до 100 пользователей

**gRPC и протоколы:**
- [`server/Docs/GRPC_PROTOCOL_AUDIT.md`](server/Docs/GRPC_PROTOCOL_AUDIT.md) - Аудит протокола
- [`server/Docs/CI_GRPC_CHECKS.md`](server/Docs/CI_GRPC_CHECKS.md) - CI проверки

**Деплоймент:**
- [`server/Docs/SERVER_DEPLOYMENT_GUIDE.md`](server/Docs/SERVER_DEPLOYMENT_GUIDE.md) - Процедура деплоя
- [`server/Docs/CANARY_CHECKLIST.md`](server/Docs/CANARY_CHECKLIST.md) - Canary чеклист
- [`server/Docs/BETA_GATE_CHECKLIST.md`](server/Docs/BETA_GATE_CHECKLIST.md) - Beta gate чеклист

---

## 🔧 Технологический стек

### Клиент
- **Python 3.8+** - основной язык
- **asyncio** - асинхронная архитектура
- **gRPC** - коммуникация с сервером
- **PortAudio** - кроссплатформенное аудио
- **Quartz/pynput** - обработка клавиатуры
- **EventBus** - событийная архитектура

### Сервер
- **Python 3.8+** - основной язык
- **gRPC + HTTP/2** - streaming с backpressure
- **Gemini API** - обработка текста
- **Azure Speech TTS** - генерация аудио
- **PostgreSQL** - база данных (опционально)
- **Nginx** - reverse proxy для production
- **Structured logging** - наблюдаемость

---

## 📦 Структура проекта

```
Nexy_server/
├── client/                      # 🖥️ Клиентская часть (macOS)
│   ├── main.py
│   ├── config/
│   ├── integration/             # EventBus, Workflows, 19 интеграций
│   ├── modules/                 # 18 модулей
│   └── Docs/                    # Документация клиента
│
├── server/                      # 🖥️ Серверная часть (Python)
│   ├── main.py
│   ├── config/
│   │   ├── unified_config.py
│   │   └── config.env           # Переменные окружения
│   ├── integrations/
│   │   └── core/
│   │       └── module_coordinator.py  # Координатор модулей
│   ├── modules/                 # 9 модулей
│   │   ├── grpc_service/        # gRPC с backpressure
│   │   ├── text_processing/
│   │   ├── audio_generation/
│   │   └── ...
│   ├── scripts/                 # Скрипты валидации
│   ├── Docs/                    # Документация сервера
│   │   ├── decisions/           # ADR документы
│   │   └── ...
│   ├── COMPLIANCE_REPORT.md     # ✅ Отчет о соответствии
│   └── README.md
│
├── modules/                     # 🔄 Синхронизированные модули (legacy support)
├── updates/                     # 📦 Система обновлений
├── scripts/                     # 🔧 Корневые скрипты
└── Docs/                        # 📚 Общая документация
```

---

## 🧪 Тестирование

### Автоматические тесты

**Серверные тесты:**
```bash
cd server

# gRPC smoke-тесты
python scripts/grpc_smoke.py localhost 50051

# Health check
python scripts/check_grpc_health.py localhost 50051

# Контракт-тесты
python scripts/grpc_contract_tests.py

# Backpressure тесты
python scripts/test_backpressure.py

# Проверка прямых импортов
python scripts/verify_no_direct_module_calls.py
```

**Валидация обновлений:**
```bash
cd server
bash scripts/validate_updates.sh
```

### Чеклисты для деплоя

- [`server/Docs/BETA_GATE_CHECKLIST.md`](server/Docs/BETA_GATE_CHECKLIST.md) - Beta gate
- [`server/Docs/CANARY_CHECKLIST.md`](server/Docs/CANARY_CHECKLIST.md) - Canary deployment
- [`server/Docs/PR_CHECKLIST_TEMPLATE.md`](server/Docs/PR_CHECKLIST_TEMPLATE.md) - Pull request

---

## 🐛 Troubleshooting

### Проблемы с аудио (macOS)

**PortAudio ошибки:**
```bash
pip uninstall sounddevice
pip install sounddevice --force-reinstall
```

**Разрешения микрофона:**
Проверьте разрешения в `System Preferences → Security & Privacy → Microphone`

### Проблемы с gRPC

**Проверка health:**
```bash
curl http://localhost:8080/health
curl http://localhost:8080/status
```

**Логи сервера:**
```bash
tail -f server/server.log
```

### Система обновлений

**Проверка версий:**
```bash
curl http://localhost:8081/health | jq '.latest_version, .latest_build'
```

**Валидация размеров:**
```bash
bash server/scripts/validate_updates.sh localhost 8081
```

---

## 🎯 Roadmap

### Завершено ✅

- [x] Модульная архитектура (client + server)
- [x] Event-driven клиент с Workflows
- [x] gRPC streaming с backpressure (PR-7)
- [x] Graceful shutdown (PR-7)
- [x] Structured logging (PR-4)
- [x] ModuleCoordinator (ADR-001)
- [x] Система обновлений (HTTP + GitHub CDN)
- [x] Масштабирование до 100 пользователей
- [x] Полная документация (100% compliance)
- [x] ADR процесс
- [x] Feature-flags и kill-switches

### В разработке 🔄

- [ ] Web интерфейс администратора
- [ ] Мобильное приложение (iOS/Android)
- [ ] Мультиязычность (internationalization)

### Планируется 📅

- [ ] Офлайн режим
- [ ] Интеграция с умным домом
- [ ] Голосовые команды на разных языках
- [ ] Kubernetes deployment

---

## 🤝 Вклад в проект

Мы приветствуем вклад в развитие проекта!

### Процесс разработки

1. **Изучите документацию:**
   - [`server/Docs/SERVER_DEVELOPMENT_RULES.md`](server/Docs/SERVER_DEVELOPMENT_RULES.md) - правила разработки
   - [`server/Docs/ADR_TEMPLATE.md`](server/Docs/ADR_TEMPLATE.md) - шаблон ADR

2. **Создайте feature branch:**
   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **Разработка с соблюдением стандартов:**
   - Следуйте SIMPLE-гейту (≤60 LOC, ≤1 файл) или Impact-гейту
   - Создайте ADR для архитектурных изменений
   - Добавьте тесты (8-14 pairwise + ≥2 негативных)
   - Обновите документацию

4. **Создайте Pull Request:**
   - Используйте [`server/Docs/PR_CHECKLIST_TEMPLATE.md`](server/Docs/PR_CHECKLIST_TEMPLATE.md)
   - Приложите `.impact/change_impact.yaml` (если применимо)
   - Добавьте ссылки на тест-результаты

### Стандарты кода

- **Backward compatibility:** все изменения gRPC должны быть обратно совместимы
- **Feature-flags:** используйте feature-flags для новых фич
- **Kill-switches:** добавляйте kill-switches для быстрого отката
- **Structured logging:** все логи в структурированном формате

---

## 📄 Лицензия

Этот проект распространяется под лицензией MIT. См. файл [LICENSE](LICENSE) для деталей.

---

## 👥 Авторы

- **Seregawpn** - *Lead Developer* - [GitHub](https://github.com/Seregawpn)

---

## 🙏 Благодарности

- **Google Gemini API** - обработка текста и контекста
- **Azure Speech Services** - генерация высококачественного TTS
- **gRPC** - efficient streaming protocol
- **PortAudio** - кроссплатформенное аудио
- **Anthropic Claude** - AI-ассистент для документации и рефакторинга

---

## 📞 Поддержка

**Возникли вопросы или проблемы?**

- 📧 Создайте [Issue](https://github.com/Seregawpn/Nexy_server/issues)
- 📖 Изучите [документацию](server/Docs/)
- 🔍 Проверьте [COMPLIANCE_REPORT.md](server/COMPLIANCE_REPORT.md)

**Перед созданием issue:**
1. Проверьте [`server/Docs/STATE_CATALOG.md`](server/Docs/STATE_CATALOG.md)
2. Запустите smoke-тесты: `python server/scripts/grpc_smoke.py`
3. Проверьте логи: `tail -f server/server.log`

---

## 🌟 Статус проекта

[![Compliance](https://img.shields.io/badge/Compliance-100%25-brightgreen.svg)](server/COMPLIANCE_REPORT.md)
[![Documentation](https://img.shields.io/badge/Documentation-Complete-brightgreen.svg)](server/Docs/)
[![Tests](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)]()
[![Production](https://img.shields.io/badge/Production-Ready-brightgreen.svg)]()

**⭐ Если проект вам понравился, поставьте звездочку! ⭐**

---

**Последнее обновление:** 5 ноября 2025
**Версия документации:** 2.0
**Compliance статус:** ✅ 100% (см. [COMPLIANCE_REPORT.md](server/COMPLIANCE_REPORT.md))
