# ADR: Миграция аудиосистемы на AVFoundation

## Что
Миграция аудиосистемы с PortAudio на AVFoundation для мониторинга устройств и воспроизведения, сохранение PortAudio для input через Google Speech Recognition.

## Почему
Текущая система на PortAudio некорректно обнаруживает новые устройства (Bluetooth, USB). AVFoundation предоставляет нативные уведомления macOS о подключении устройств через NSNotificationCenter и надежное управление output через AVAudioEngine. Это решает проблему задержек и пропусков при подключении устройств.

## Альтернативы
1. **Улучшение PortAudio мониторинга** - не решает проблему нативного обнаружения устройств macOS
2. **Использование CoreAudio напрямую** - низкоуровнево, сложнее в поддержке
3. **AVFoundation для всего** - нарушает принцип единственного владельца микрофона (Google Speech Recognition должен быть единственным владельцем)

## Решение
AVFoundation для мониторинга устройств (NSNotificationCenter + polling fallback) и output (AVAudioEngine), PortAudio для input через Google Speech Recognition. Reconcile-архитектура через AudioRouteManager для управления переходами состояний с debounce и single-flight механизмами.

## Последствия
- Новая архитектура требует feature flags для постепенного роллаута
- Новые метрики для мониторинга (device_discovery_latency_ms, input_switch_duration_ms, etc.)
- Обновление тестов и документации
- Зависимость от PyObjC (уже установлен)
- Fallback на старую систему при недоступности PyObjC

## Дата
2025-01-XX

## Откат
Kill-switches (`NEXY_KS_AVFOUNDATION_*`) для мгновенного отката на старую систему без релиза. Все компоненты проверяют kill-switches перед инициализацией.

