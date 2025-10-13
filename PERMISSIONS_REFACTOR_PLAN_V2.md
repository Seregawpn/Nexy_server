# 🔧 План рефакторинга системы разрешений v2

**Дата:** 2025-10-12  
**Версия:** 2.0 (с учётом фидбека)  
**Цель:** Реактивная система с лёгким кэшем, без блокировки

---

## ✅ **УЛУЧШЕНИЯ V2:**

1. ✅ **Лёгкий кэш с TTL (1-2 сек)** - не гоняем tccutil каждый раз
2. ✅ **Центральный PermissionsIntegration** - не создаём дубли менеджеров
3. ✅ **Проверка подписчиков событий** - миграция на новые события
4. ✅ **Синхронизация в sequential** - обновляем missing после каждого диалога
5. ✅ **Проверки во всех модулях** - не только SpeechRecognizer
6. ✅ **Голосовые подсказки** - для незрячих пользователей
7. ✅ **sudo предупреждения** - в smoke-тестах

---

## 📋 **ШАГ 1: Лёгкий кэш с TTL**

```python
import time
from typing import Dict, Optional

class PermissionsIntegration(BaseIntegration):
    def __init__(self, event_bus: EventBus, error_handler: ErrorHandler, config: dict):
        # ...
        
        # Лёгкий кэш с TTL для защиты от spam-запросов к TCC
        self._cached_results: Optional[Dict[PermissionType, PermissionResult]] = None
        self._last_refresh: float = 0
        self._cache_ttl: float = 2.0  # секунды (настраивается через config)
        
        # Флаги для избежания повторных запросов
        self._request_in_progress: bool = False
        self._input_monitoring_prompted: bool = False
    
    async def _refresh_permissions(self, force: bool = False) -> Dict[PermissionType, PermissionResult]:
        """Получить статусы разрешений (с кешем TTL 2 сек)
        
        Args:
            force: Принудительное обновление, игнорируя кэш
        """
        try:
            now = time.monotonic()
            
            # Возвращаем кэш если не истёк TTL
            if not force and self._cached_results is not None:
                if now - self._last_refresh < self._cache_ttl:
                    logger.debug(f"📦 Используем кэш разрешений (TTL: {now - self._last_refresh:.1f}s)")
                    return self._cached_results
            
            logger.debug("🔄 Обновляем статусы разрешений...")
            results = await self.permission_manager.check_all_permissions()
            
            # Обновляем кэш
            self._cached_results = results
            self._last_refresh = now
            
            # Публикуем события
            for perm_type, result in results.items():
                await self.event_bus.publish("permissions.status_checked", {
                    "permission": perm_type.value,
                    "status": result.status.value,
                    "success": result.success,
                    "message": result.message
                })
            
            logger.debug(f"✅ Статусы обновлены и закешированы (TTL: {self._cache_ttl}s)")
            return results
            
        except Exception as e:
            logger.error(f"❌ Ошибка обновления статусов разрешений: {e}")
            # При ошибке возвращаем старый кэш или пустой словарь
            return self._cached_results if self._cached_results else {}
```

---

## 📋 **ШАГ 2: Центральный доступ к PermissionsIntegration**

### В SimpleModuleCoordinator добавить геттер:

```python
class SimpleModuleCoordinator:
    def __init__(self, ...):
        # ...
        self.permissions_integration: Optional[PermissionsIntegration] = None
    
    async def start(self):
        # ... при инициализации интеграций ...
        self.permissions_integration = PermissionsIntegration(...)
        await self.permissions_integration.initialize()
        # ...
    
    def get_permissions_integration(self) -> Optional[PermissionsIntegration]:
        """Получить ссылку на PermissionsIntegration"""
        return self.permissions_integration
```

### В SpeechRecognizer принимать ссылку:

```python
class SpeechRecognizer:
    def __init__(self, event_bus: EventBus, permissions_integration: Optional[PermissionsIntegration] = None):
        self.event_bus = event_bus
        self.permissions_integration = permissions_integration
        # ...
    
    async def start_listening(self) -> bool:
        """Начинает прослушивание микрофона"""
        try:
            if self.state != RecognitionState.IDLE:
                logger.warning(f"⚠️ Невозможно начать прослушивание в состоянии {self.state.value}")
                return False
            
            # Проверяем разрешение микрофона ПЕРЕД запуском
            if self.permissions_integration:
                results = await self.permissions_integration._refresh_permissions()
                mic_result = results.get(PermissionType.MICROPHONE)
                
                if not mic_result or mic_result.status != PermissionStatus.GRANTED:
                    logger.error("❌ Microphone permission not granted")
                    logger.info("ℹ️ Запрашиваем разрешение микрофона...")
                    
                    # Запрашиваем разрешение
                    missing = {PermissionType.MICROPHONE: PermissionStatus.NOT_DETERMINED}
                    await self.permissions_integration._request_required_permissions(missing)
                    
                    # Проверяем повторно
                    results = await self.permissions_integration._refresh_permissions(force=True)
                    mic_result = results.get(PermissionType.MICROPHONE)
                    
                    if not mic_result or mic_result.status != PermissionStatus.GRANTED:
                        logger.error("❌ Microphone permission still not granted")
                        return False
            
            self.state = RecognitionState.LISTENING
            self.is_listening = True
            # ... остальной код ...
```

### В VoiceRecognitionIntegration передавать ссылку:

```python
class VoiceRecognitionIntegration(BaseIntegration):
    async def initialize(self) -> bool:
        try:
            # ... другой код ...
            
            # Получаем ссылку на permissions_integration
            coordinator = self.event_bus._coordinator  # или через DI
            permissions_integration = coordinator.get_permissions_integration()
            
            self.speech_recognizer = SpeechRecognizer(
                event_bus=self.event_bus,
                permissions_integration=permissions_integration
            )
            
            # ...
```

---

## 📋 **ШАГ 3: Проверка и миграция событий**

### Найти подписчиков старых событий:

```bash
cd /Users/sergiyzasorin/Development/Nexy/client
grep -r "permissions.app_blocked" --include="*.py"
grep -r "permissions.app_unblocked" --include="*.py"
```

### Заменить на новые события:

**Старые:**
- `permissions.app_blocked` → ❌ УДАЛИТЬ
- `permissions.app_unblocked` → ❌ УДАЛИТЬ

**Новые:**
- `permissions.missing` - когда не хватает критичных разрешений
- `permissions.all_granted` - когда все критичные разрешения получены
- `permissions.status_checked` - при проверке конкретного разрешения

---

## 📋 **ШАГ 4: Синхронизация в sequential**

```python
async def _request_permissions_sequential(self, missing: Dict[PermissionType, PermissionStatus]):
    """Последовательный запрос недостающих разрешений с синхронизацией"""
    try:
        import asyncio
        import subprocess
        
        logger.info(f"🔔 Последовательный запрос: {[p.value for p in missing.keys()]}")
        
        # КРИТИЧНО: Захватываем event loop ДО определения handlers
        loop = asyncio.get_running_loop()
        
        # 1) Microphone
        if PermissionType.MICROPHONE in missing:
            logger.info("🎤 Запрашиваем Microphone...")
            mic_future = loop.create_future()
            
            def mic_handler(granted):
                try:
                    if not mic_future.done():
                        loop.call_soon_threadsafe(mic_future.set_result, bool(granted))
                except Exception as e:
                    if not mic_future.done():
                        loop.call_soon_threadsafe(mic_future.set_exception, e)
            
            try:
                AVCaptureDevice.requestAccessForMediaType_completionHandler_(AVMediaTypeAudio, mic_handler)
                mic_granted = await asyncio.wait_for(mic_future, timeout=30.0)
                logger.info(f"🎤 Microphone: {'granted' if mic_granted else 'denied'}")
                
                # НОВОЕ: Синхронизация - проверяем реальный статус в TCC
                await asyncio.sleep(0.5)  # Даём TCC время записать
                results = await self._refresh_permissions(force=True)
                mic_result = results.get(PermissionType.MICROPHONE)
                
                if mic_result and mic_result.status == PermissionStatus.GRANTED:
                    missing.pop(PermissionType.MICROPHONE, None)
                    logger.info("✅ Microphone подтверждён в TCC")
                else:
                    logger.warning("⚠️ Microphone не подтверждён в TCC")
                    
            except asyncio.TimeoutError:
                logger.error("🎤 Microphone request timeout (30s)")
            except Exception as e:
                logger.error(f"🎤 Microphone request error: {e}")
        
        # 2) Accessibility
        if PermissionType.ACCESSIBILITY in missing:
            logger.info("♿ Запрашиваем Accessibility...")
            try:
                trusted = bool(AXIsProcessTrustedWithOptions({kAXTrustedCheckOptionPrompt: False}))
                
                if not trusted:
                    logger.info("⚠️ Accessibility не выдано, показываем диалог...")
                    trusted = bool(AXIsProcessTrustedWithOptions({kAXTrustedCheckOptionPrompt: True}))
                    
                    # НОВОЕ: Синхронизация
                    await asyncio.sleep(1.0)  # Accessibility требует больше времени
                    results = await self._refresh_permissions(force=True)
                    acc_result = results.get(PermissionType.ACCESSIBILITY)
                    
                    if acc_result and acc_result.status == PermissionStatus.GRANTED:
                        missing.pop(PermissionType.ACCESSIBILITY, None)
                        logger.info("✅ Accessibility подтверждён в TCC")
                    else:
                        logger.warning("⚠️ Accessibility не подтверждён - откройте System Settings")
                        subprocess.run(["open", "x-apple.systempreferences:com.apple.preference.security?Privacy_Accessibility"], check=False)
                else:
                    missing.pop(PermissionType.ACCESSIBILITY, None)
                    logger.info("✅ Accessibility уже выдано")
                    
            except Exception as e:
                logger.error(f"♿ Accessibility request error: {e}")
        
        # 3) Input Monitoring
        if PermissionType.INPUT_MONITORING in missing:
            logger.info("⌨️ Запрашиваем Input Monitoring...")
            try:
                import ctypes
                IOHID_LISTEN_EVENT = 1
                
                if not hasattr(self, "_iokit"):
                    self._iokit = ctypes.CDLL("/System/Library/Frameworks/IOKit.framework/IOKit")
                    self._IOHIDCheckAccess = self._iokit.IOHIDCheckAccess
                    self._IOHIDCheckAccess.argtypes = [ctypes.c_uint32]
                    self._IOHIDCheckAccess.restype = ctypes.c_bool
                    self._IOHIDRequestAccess = self._iokit.IOHIDRequestAccess
                    self._IOHIDRequestAccess.argtypes = [ctypes.c_uint32]
                    self._IOHIDRequestAccess.restype = ctypes.c_int32
                
                has_im = bool(self._IOHIDCheckAccess(ctypes.c_uint32(IOHID_LISTEN_EVENT)))
                
                if not has_im and not self._input_monitoring_prompted:
                    logger.info("⚠️ Input Monitoring не выдано, запрашиваем...")
                    result = self._IOHIDRequestAccess(ctypes.c_uint32(IOHID_LISTEN_EVENT))
                    
                    # НОВОЕ: Синхронизация
                    await asyncio.sleep(0.5)
                    
                    # Повторная проверка через IOKit (не TCC - IOKit быстрее)
                    has_im = bool(self._IOHIDCheckAccess(ctypes.c_uint32(IOHID_LISTEN_EVENT)))
                    
                    if has_im:
                        missing.pop(PermissionType.INPUT_MONITORING, None)
                        logger.info("✅ Input Monitoring подтверждён")
                    else:
                        logger.warning(f"⚠️ Input Monitoring отклонено - откройте System Settings")
                        subprocess.run(["open", "x-apple.systempreferences:com.apple.preference.security?Privacy_ListenEvent"], check=False)
                    
                    self._input_monitoring_prompted = True
                elif has_im:
                    missing.pop(PermissionType.INPUT_MONITORING, None)
                    logger.info("✅ Input Monitoring уже выдано")
                    
            except Exception as e:
                logger.error(f"⌨️ Input Monitoring request error: {e}")
        
        logger.info(f"✅ Последовательный запрос завершён. Осталось: {[p.value for p in missing.keys()]}")
        
    except Exception as e:
        logger.error(f"❌ Ошибка последовательного запроса: {e}")
```

---

## 📋 **ШАГ 5: Проверки во всех критичных модулях**

### 1. InputProcessingIntegration:

```python
class InputProcessingIntegration(BaseIntegration):
    def __init__(self, event_bus, error_handler, config, permissions_integration=None):
        # ...
        self.permissions_integration = permissions_integration
    
    async def _on_input_event(self, event_data: dict):
        """Обработчик событий клавиатуры"""
        try:
            # Проверяем разрешения перед обработкой
            if self.permissions_integration:
                results = await self.permissions_integration._refresh_permissions()
                
                acc_result = results.get(PermissionType.ACCESSIBILITY)
                im_result = results.get(PermissionType.INPUT_MONITORING)
                
                if not acc_result or acc_result.status != PermissionStatus.GRANTED:
                    logger.warning("⚠️ Accessibility не выдано - события клавиатуры недоступны")
                    return
                
                if not im_result or im_result.status != PermissionStatus.GRANTED:
                    logger.warning("⚠️ Input Monitoring не выдано - события клавиатуры недоступны")
                    return
            
            # Обрабатываем событие
            # ...
```

### 2. ScreenshotCaptureIntegration:

```python
async def capture_screenshot(self) -> Optional[bytes]:
    """Сделать скриншот"""
    try:
        # Проверяем разрешение Screen Recording
        if self.permissions_integration:
            results = await self.permissions_integration._refresh_permissions()
            sc_result = results.get(PermissionType.SCREEN_CAPTURE)
            
            if not sc_result or sc_result.status != PermissionStatus.GRANTED:
                logger.error("❌ Screen Recording permission not granted")
                
                # Запрашиваем
                missing = {PermissionType.SCREEN_CAPTURE: PermissionStatus.NOT_DETERMINED}
                await self.permissions_integration._request_required_permissions(missing)
                
                return None
        
        # Делаем скриншот
        # ...
```

---

## 📋 **ШАГ 6: Голосовые подсказки**

```python
async def _request_required_permissions(self, missing: Optional[Dict[PermissionType, PermissionStatus]] = None):
    """Запросить недостающие разрешения"""
    try:
        # ... код ...
        
        # Если PyObjC недоступен - голосовые подсказки
        if not MACOS_IMPORTS_AVAILABLE:
            logger.warning("⚠️ PyObjC недоступен - автоматические диалоги отключены")
            
            # Голосовое оповещение
            await self._speak_permission_instructions(missing)
            
            # Открываем System Settings для каждого разрешения
            for perm in missing.keys():
                if perm == PermissionType.MICROPHONE:
                    subprocess.run(["open", "x-apple.systempreferences:com.apple.preference.security?Privacy_Microphone"], check=False)
                elif perm == PermissionType.ACCESSIBILITY:
                    subprocess.run(["open", "x-apple.systempreferences:com.apple.preference.security?Privacy_Accessibility"], check=False)
                elif perm == PermissionType.INPUT_MONITORING:
                    subprocess.run(["open", "x-apple.systempreferences:com.apple.preference.security?Privacy_ListenEvent"], check=False)
        
        # ...
    
    async def _speak_permission_instructions(self, missing: Dict[PermissionType, PermissionStatus]):
        """Произнести инструкции для выдачи разрешений"""
        try:
            import subprocess
            
            # Формируем текст инструкции
            perm_names = {
                PermissionType.MICROPHONE: "Microphone",
                PermissionType.ACCESSIBILITY: "Accessibility",
                PermissionType.INPUT_MONITORING: "Input Monitoring",
                PermissionType.SCREEN_CAPTURE: "Screen Recording"
            }
            
            missing_list = [perm_names.get(p, p.value) for p in missing.keys()]
            text = f"Nexy requires permissions: {', '.join(missing_list)}. Please open System Settings, Privacy and Security, and enable these permissions."
            
            logger.info(f"🔊 Произносим инструкцию: {text}")
            
            # Используем macOS TTS (say)
            subprocess.run(["say", text], check=False)
            
            # Или через EventBus для SpeechPlaybackIntegration
            await self.event_bus.publish("playback.signal", {
                "pattern": "info",
                "message": "permissions_required"
            })
            
        except Exception as e:
            logger.error(f"❌ Ошибка голосового оповещения: {e}")
```

---

## 📋 **ШАГ 7: sudo предупреждения в smoke-тестах**

### Обновить quick_install_and_test.sh:

```bash
#!/bin/bash

set -e

cat << 'EOF'

╔══════════════════════════════════════════════════════════════════════════╗
║     🚀 УСТАНОВКА И ТЕСТИРОВАНИЕ НОВОЙ СБОРКИ                            ║
╚══════════════════════════════════════════════════════════════════════════╝

⚠️  ВАЖНО: Этот скрипт требует права администратора (sudo)

Будет запрошен пароль для:
  • Удаления /Applications/Nexy.app
  • Копирования новой версии
  • Сброса TCC разрешений

EOF

# Проверяем sudo заранее
echo "🔐 Проверяем права администратора..."
if ! sudo -v; then
    echo "❌ Требуются права администратора!"
    exit 1
fi

# Продлеваем sudo на всё время работы скрипта
(while true; do sudo -n true; sleep 50; done) 2>/dev/null &
SUDO_KEEPER_PID=$!
trap "kill $SUDO_KEEPER_PID 2>/dev/null || true" EXIT

echo "✅ Права администратора получены"
echo ""

# ... остальной код ...
```

---

## ✅ **ИТОГОВАЯ АРХИТЕКТУРА V2:**

```
┌─────────────────────────────────────────────────────┐
│ PermissionsIntegration                              │
│                                                     │
│ • _cached_results (TTL 2 сек)                      │
│ • _refresh_permissions(force=False)                 │
│ • _evaluate_permissions(results)                    │
│ • _request_required_permissions(missing)            │
│ • _request_permissions_sequential(missing)          │
│ • _speak_permission_instructions(missing)           │
└─────────────────────────────────────────────────────┘
         ↑                    ↑                    ↑
         │                    │                    │
    ┌────┴────┐          ┌────┴────┐         ┌────┴────┐
    │ Speech  │          │  Input  │         │ Screen  │
    │Recogn.  │          │Process. │         │ Capture │
    └─────────┘          └─────────┘         └─────────┘
    
    Каждый модуль:
    1. Получает ссылку на PermissionsIntegration при создании
    2. Проверяет права перед действием (_refresh_permissions)
    3. Запрашивает если нужно (_request_required_permissions)
    4. НЕ создаёт свой PermissionsManager
```

---

## 🧪 **ОБНОВЛЁННЫЙ SMOKE-ТЕСТ:**

```bash
#!/bin/bash

cat << 'EOF'
╔══════════════════════════════════════════════════════════════════════════╗
║     🧪 SMOKE-ТЕСТ РАЗРЕШЕНИЙ v2                                         ║
╚══════════════════════════════════════════════════════════════════════════╝

⚠️  ТРЕБУЕТСЯ SUDO

EOF

# 1. Проверка sudo
echo "1️⃣  Проверяем права администратора..."
if ! sudo -v; then
    echo "❌ Требуются права администратора!"
    exit 1
fi

# 2. Сброс TCC
echo "2️⃣  Сбрасываем TCC разрешения..."
sudo tccutil reset All com.nexy.assistant

# 3. Проверка перед запуском
echo "3️⃣  Проверяем статус разрешений..."
./check_permissions.sh

# 4. Запуск приложения
echo "4️⃣  Запускаем приложение (20 сек)..."
echo ""
echo "📋 ВАШИ ДЕЙСТВИЯ:"
echo "   1. Подтвердите ВСЕ диалоги (3 шт)"
echo "   2. Удерживайте ПРОБЕЛ 3-5 сек"
echo "   3. ГОВОРИТЕ В МИКРОФОН"
echo ""

timeout 20 /Applications/Nexy.app/Contents/MacOS/Nexy 2>&1 | grep -E \
    "(Последовательный запрос|Microphone|Accessibility|Input Monitoring|Audio stream|First chunk|Статистика аудио|peak|rms)" \
    --line-buffered || true

# 5. Проверка после запуска
echo ""
echo "5️⃣  Проверяем статус после запуска..."
./check_permissions.sh

# 6. Анализ логов
echo ""
echo "6️⃣  Анализ логов..."
if [ -f ~/Library/Application\ Support/Nexy/logs/*.log ]; then
    echo "📊 Последние важные события:"
    tail -50 ~/Library/Application\ Support/Nexy/logs/*.log | grep -E \
        "(peak=|rms=|granted|denied|Статистика)"
fi

echo ""
echo "✅ Smoke-тест завершён!"
```

---

## 📝 **ЧЕКЛИСТ ВНЕДРЕНИЯ:**

- [ ] 1. Добавить лёгкий кэш с TTL в PermissionsIntegration
- [ ] 2. Добавить геттер в SimpleModuleCoordinator
- [ ] 3. Передать ссылку на PermissionsIntegration в SpeechRecognizer
- [ ] 4. Передать ссылку в InputProcessingIntegration
- [ ] 5. Передать ссылку в ScreenshotCaptureIntegration
- [ ] 6. Найти и заменить подписчиков старых событий
- [ ] 7. Добавить синхронизацию в _request_permissions_sequential
- [ ] 8. Добавить проверки в start_listening()
- [ ] 9. Добавить проверки в input event handlers
- [ ] 10. Добавить _speak_permission_instructions()
- [ ] 11. Обновить quick_install_and_test.sh с sudo проверкой
- [ ] 12. Обновить smoke-тесты
- [ ] 13. Пересборка и тестирование
- [ ] 14. Production сборка через rebuild_from_scratch.sh

---

**Следующий шаг:** Начать внедрение с шага 1 (лёгкий кэш)!


