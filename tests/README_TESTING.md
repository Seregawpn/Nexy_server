# Тестирование модулей PermissionRestart и UpdateNotification

Этот набор тестов позволяет изолированно проверить работу двух новых модулей:
- **PermissionRestartIntegration** - автоматический перезапуск после предоставления критических разрешений
- **UpdateNotificationIntegration** - голосовые уведомления о ходе обновления

## Быстрые тесты

### 1. Тест UpdateNotificationIntegration
```bash
cd /Users/sergiyzasorin/Development/Nexy/client
python tests/quick_test_update_notification.py
```

**Что проверяется:**
- Публикация событий `speech.playback.request` для голосовых уведомлений
- Публикация событий `signal.play` для звуковых сигналов
- Обработка событий: `updater.update_started`, `updater.download_progress`, `updater.install_progress`, `updater.update_completed`

**Ожидаемый результат:**
- В логах должны появиться события голосовых уведомлений
- Сигналы должны воспроизводиться (если настроено)

### 2. Тест PermissionRestartIntegration
```bash
cd /Users/sergiyzasorin/Development/Nexy/client
python tests/quick_test_permission_restart.py
```

**Что проверяется:**
- Публикация событий `permission_restart.scheduled` при предоставлении критических разрешений
- Публикация событий `permission_restart.executing` при планировании перезапуска
- Обработка событий: `permissions.changed` с критическими разрешениями

**Ожидаемый результат:**
- В логах должны появиться события планирования перезапуска
- ⚠️ **ВНИМАНИЕ**: В реальном приложении это приведет к перезапуску!

## Комплексные тесты

### 3. Полный тест UpdateNotificationIntegration
```bash
python tests/test_update_notification_integration.py
```

**Включает:**
- Основной тест с полным циклом обновления
- Тест с `dry_run=True` (без реального воспроизведения)
- Тест обработки ошибок обновления

### 4. Полный тест PermissionRestartIntegration
```bash
python tests/test_permission_restart_integration.py
```

**Включает:**
- Основной тест с критическими разрешениями
- Тест с активными сессиями (отложенный перезапуск)
- Тест отключенной интеграции
- Тест с некритическими разрешениями

### 5. Комплексный тест обеих интеграций
```bash
python tests/test_both_integrations.py
```

**Включает:**
- Тест работы обеих интеграций вместе
- Тест изоляции интеграций
- Тест обработки ошибок

## Конфигурация для тестирования

### UpdateNotificationIntegration
```yaml
integrations:
  update_notification:
    enabled: true
    speak_start: true
    speak_progress: true
    speak_complete: true
    speak_error: true
    progress_interval_sec: 30.0
    progress_step_percent: 20
    use_signals: true
    voice: "ru-RU"
    dry_run: false  # Установите true для тестирования без звука
```

### PermissionRestartIntegration
```yaml
integrations:
  permission_restart:
    enabled: true
    critical_permissions:
      - microphone
      - accessibility
      - input_monitoring
      - screen_capture
    restart_delay_sec: 5.0
    max_restart_attempts: 3
    respect_active_sessions: true
    respect_updates: true
```

## Безопасное тестирование

### Для UpdateNotificationIntegration
- Используйте `dry_run: true` для тестирования без реального воспроизведения
- Все события публикуются, но звук не воспроизводится
- Идеально для CI/CD и автоматического тестирования

### Для PermissionRestartIntegration
- ⚠️ **КРИТИЧЕСКИ ВАЖНО**: В реальном приложении модуль может вызвать перезапуск!
- Для безопасного тестирования используйте переменную окружения `NEXY_DISABLE_AUTO_RESTART=true`
- Или тестируйте только логику планирования без реального перезапуска

## Интерпретация результатов

### Успешный тест UpdateNotificationIntegration
```
✅ Тест ПРОЙДЕН: Голосовые уведомления работают
✅ Тест ПРОЙДЕН: Сигналы работают
```

### Успешный тест PermissionRestartIntegration
```
✅ Тест ПРОЙДЕН: Перезапуск запланирован
```

### Проблемы и решения

**Нет голосовых уведомлений:**
- Проверьте конфигурацию `speak_*` параметров
- Убедитесь, что `dry_run: false`
- Проверьте подключение SpeechPlaybackIntegration

**Нет событий перезапуска:**
- Проверьте список `critical_permissions`
- Убедитесь, что разрешения действительно критические
- Проверьте состояние приложения (активные сессии, режим)

**Ошибки инициализации:**
- Проверьте зависимости модулей
- Убедитесь в корректности конфигурации
- Проверьте права доступа к файлам

## Интеграция в основное приложение

После успешного тестирования модули готовы к интеграции:

1. **Проверьте конфигурацию** в `config/unified_config.yaml`
2. **Убедитесь в правильном порядке** инициализации в `SimpleModuleCoordinator`
3. **Проведите ручное тестирование** с реальными разрешениями и обновлениями
4. **Мониторьте логи** на предмет ошибок и неожиданного поведения

## Поддержка

При возникновении проблем:
1. Проверьте логи приложения
2. Убедитесь в корректности конфигурации
3. Проведите изолированное тестирование модулей
4. Обратитесь к документации модулей в `modules/*/README.md`



