# Анализ: не запрашиваются все разрешения

## Контекст
Пользователь сообщает, что не все разрешения запрашиваются в first-run.

## Гипотезы
1) First-run flow обрывается после одного из разрешений из-за отсутствия события `permissions.changed`.
2) permission_restart происходит раньше завершения цепочки first_run.
3) Флаги first-run уже существуют, поэтому шаги пропускаются.

## Рекомендуемая проверка
- Проверить наличие флагов first_run в `~/Library/Application Support/Nexy/`.
- Посмотреть логи Nexy на `permissions.first_run_*` и `permission_restart.*`.
- Сверить текущий конфиг `permissions.first_run.*` в `config/unified_config.yaml`.
