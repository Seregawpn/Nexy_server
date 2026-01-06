# Release Build Checklist

**Версия:** 1.1  
**Дата:** 2026-01-04

## ⚠️ КРИТИЧЕСКИ ВАЖНО: Канонический путь сборки

**ЕДИНСТВЕННЫЙ КАНОНИЧЕСКИЙ ПУТЬ:**
```bash
./packaging/build_final.sh            # Релизная сборка с нотаризацией
NEXY_SKIP_NOTARIZATION=1 ./packaging/build_final.sh  # Локальная сборка без нотаризации
```

**НЕ ИСПОЛЬЗУЙТЕ:**
- ❌ Удаленные скрипты (`build_universal_app_only.sh`, `scripts/prepare_release.sh` и т.д.)
- ❌ Ручные операции с `.app` после сборки (Finder, `cp -R`, `xattr -cr`)
- ❌ Дополнительные скрипты проверки (финальная проверка встроена в `build_final.sh`)

**ЗАЩИТА ПОДПИСИ (ОБЯЗАТЕЛЬНО):**
- ❌ НЕ открывайте `.app` в Finder после сборки (может изменить extended attributes)
- ❌ НЕ выполняйте `xattr -cr` на `.app` (удаляет подпись!)
- ❌ НЕ копируйте `.app` через Finder или `cp -R` (используйте `ditto --noextattr --noqtn`)
- ✅ Используйте только `safe_copy_preserve_signature` (встроено в `build_final.sh`)
- ✅ Проверяйте подпись через `codesign --verify --deep --strict`

---

## Предварительные проверки

- [ ] Все изменения закоммичены в git
- [ ] Версия обновлена в `config/unified_config.yaml`
- [ ] Версия обновлена в `client/VERSION_INFO.json` (если используется)
- [ ] Проверены зависимости (`requirements.txt`, `pyproject.toml`)
- [ ] Проверены сертификаты в keychain:
  ```bash
  security find-identity -v -p codesigning | grep "Developer ID"
  ```
- [ ] Проверен notarytool профиль:
  ```bash
  xcrun notarytool history --keychain-profile nexy-notary
  ```

## Релизная сборка

- [ ] Запущена релизная сборка через канонический путь:
  ```bash
  cd client
  ./packaging/build_final.sh
  ```
- [ ] Сборка завершена без ошибок
- [ ] Финальная проверка выполнена автоматически (встроена в скрипт)
- [ ] Все checkpoint-ы прошли успешно (проверить лог)
- [ ] Нотаризация прошла успешно (статус: Accepted)
- [ ] Логи сохранены в `dist/`:
  - [ ] `dist/packaging_verification.log` (лог финальной проверки)
  - [ ] `dist/packaging_verification.log` (лог проверки артефактов)

## Проверка артефактов

- [ ] `.app` валиден:
  ```bash
  codesign --verify --deep --strict dist/Nexy.app
  xcrun stapler validate dist/Nexy.app
  ```
- [ ] `PKG` валиден:
  ```bash
  pkgutil --check-signature dist/Nexy.pkg
  xcrun stapler validate dist/Nexy.pkg
  ```
- [ ] `DMG` валиден:
  ```bash
  codesign --verify dist/Nexy.dmg
  hdiutil verify dist/Nexy.dmg
  ```
- [ ] Автоматическая проверка прошла (встроена в `build_final.sh`):
  - [ ] Проверка подписи всех артефактов
  - [ ] Проверка нотаризации всех артефактов
  - [ ] Проверка архитектуры (Universal 2)
  - [ ] Проверка целостности (hash)
  - [ ] Лог сохранен в `dist/packaging_verification.log`

## First-Run тестирование

- [ ] Сброшены TCC разрешения:
  ```bash
  sudo ./scripts/reset_permissions.sh
  ```
- [ ] Очищены first-run флаги:
  ```bash
  python3 scripts/clear_first_run_flags.py
  ```
- [ ] Запущен новый `.app`:
  ```bash
  open dist/Nexy.app
  ```
- [ ] First-run прошел без зависаний:
  - [ ] Нет пауз 2-3 минуты после Screen Recording
  - [ ] Нет ошибок "TCCAccessRequest for kTCCServiceAccessibility"
  - [ ] Нет ошибок "coreaudiod is not a TCC manager"
  - [ ] Разрешения запрашиваются последовательно
  - [ ] Автоматический перезапуск работает
- [ ] После перезапуска:
  - [ ] Приветствие играет только после перезапуска
  - [ ] Нет логов CoreAudio о записи микрофона до перезапуска
  - [ ] В логах есть "Перезапуск после first_run завершён успешно"

## Финальная проверка

- [ ] Проверены логи на критические ошибки:
  ```bash
  tail -100 $(ls -t /var/folders/*/T/nexy_debug.log 2>/dev/null | head -1)
  ```
- [ ] Проверен runtime hook log:
  ```bash
  cat /tmp/nexy_pyobjc_fix.log
  ```
- [ ] Проверен packaging verification log:
  ```bash
  cat dist/packaging_verification.log
  ```
- [ ] Все артефакты готовы к распространению:
  - [ ] `dist/Nexy.pkg` (для установки)
  - [ ] `dist/Nexy.dmg` (для drag-and-drop)
  - [ ] `dist/Nexy.app` (для проверки, если не удален)

## Критерии успеха

- ✅ Все checkpoint-ы прошли успешно
- ✅ Нотаризация успешна (статус: Accepted)
- ✅ Все артефакты валидны (codesign + stapler)
- ✅ First-run проходит без зависаний
- ✅ Автоматический перезапуск работает корректно
- ✅ Нет критических ошибок в логах

## Примечания

### Канонический путь сборки

**ЕДИНСТВЕННЫЙ СПОСОБ:**
- `./packaging/build_final.sh` — релизная сборка с нотаризацией
- `NEXY_SKIP_NOTARIZATION=1 ./packaging/build_final.sh` — локальная сборка без нотаризации
- `TIMESTAMP_MODE=none NEXY_SKIP_NOTARIZATION=1 ./packaging/build_final.sh` — локальная сборка без timestamp

### Защита подписи

- **НЕ открывайте `.app` в Finder** после сборки (может изменить extended attributes)
- **НЕ выполняйте `xattr -cr`** на `.app` (удаляет подпись!)
- **НЕ копируйте `.app`** через Finder или `cp -R` (используйте `ditto --noextattr --noqtn`)
- Если подпись ломается, проверьте checkpoint-ы в `/tmp/checkpoint_<name>_codesign.log`

### Timestamp сервис

- Если timestamp сервис недоступен, используйте локальный режим:
  ```bash
  TIMESTAMP_MODE=none NEXY_SKIP_NOTARIZATION=1 ./packaging/build_final.sh
  ```
- Локальный режим не выполняет нотаризацию (требуется timestamp для нотаризации)

### Логи

- Логи сборки автоматически сохраняются:
  - `dist/packaging_verification.log` — детальный лог финальной проверки артефактов
  - `/tmp/checkpoint_<name>_codesign.log` — детальные логи checkpoint-ов подписи
