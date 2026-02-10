# Press preempt while assistant active

## Что сделано
- Усилен preempt в `InputProcessingIntegration._handle_long_press`:
  - Условие прерывания теперь совпадает с логикой `PRESS_PREEMPT` (`playback_active || mode=PROCESSING || active_session_id`).
  - В `interrupt.request` передается активная сессия ассистента (`preempt_session_id`), а не новая сессия long-press записи.

## Почему
- При long-press во время работы ассистента прерывание могло идти с новой session_id записи и не отменять текущий processing/playback.
- После правки long-press всегда сначала прерывает текущую активную работу ассистента, затем запускает новый цикл записи.

## Измененный файл
- `integration/integrations/input_processing_integration.py`
