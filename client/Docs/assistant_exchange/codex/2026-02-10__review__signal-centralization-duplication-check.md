# Review: signal centralization / duplication check

## Scope
Проверка дублирования/конфликтов/централизации в цепочке signal + mode + playback после последних фиксов.

## Result
- Runtime цепочка корректна и централизована:
  - mode change -> SignalIntegration -> playback.signal -> AVF render.
- Явных конфликтов владельцев не найдено.
- Потенциальный техдолг: в `SignalIntegration` есть неактивный handler `_on_voice_mic_opened` (не подписан в `initialize`).

## Risks
- Текущий риск дублирования: низкий (handler не активен).
- Риск будущей путаницы: средний, если кто-то позже подпишет и начнется двойной listen_start owner.

## Recommendation
Оставить текущую логику как рабочую, и в отдельном tiny-cleanup удалить неиспользуемый `_on_voice_mic_opened` (или документированно оставить как fallback, но без подписки).
