# Чек-лист проверки артефактов упаковки

**Версия:** 1.0  
**Дата:** 2025-12-31  
**Источник истины:** `Docs/PACKAGING_FINAL_GUIDE.md`

---

## Быстрая проверка (автоматическая)

```bash
cd client
./scripts/verify_packaging_artifacts.sh
```

---

## Ручная проверка (пошаговая)

### 1. Сборка

```bash
cd client
./packaging/build_final.sh
```

**Ожидаемый результат:**
- ✅ Сборка завершена без ошибок
- ✅ Все артефакты созданы в `dist/`

---

### 2. Проверка .app

**ВАЖНО:** `build_final.sh` удаляет `.app` после создания PKG/DMG. Если `.app` отсутствует в `dist/`, проверьте `.app` из PKG (раздел 3) или DMG (раздел 5).

**Если .app присутствует в dist/ (например, после локальной сборки через `NEXY_SKIP_NOTARIZATION=1 ./packaging/build_final.sh`):**

```bash
# Проверка подписи
codesign --verify --deep --strict --verbose=2 dist/Nexy.app

# Проверка нотаризации (не обязательна при NEXY_SKIP_NOTARIZATION=1)
xcrun stapler validate dist/Nexy.app

# Проверка архитектуры
lipo -info dist/Nexy.app/Contents/MacOS/Nexy
# Ожидается: Architectures in the fat file: x86_64 arm64
```

**Ожидаемый результат:**
- ✅ Подпись корректна
- ✅ Нотаризация корректна (если не пропущена через `NEXY_SKIP_NOTARIZATION=1`)
- ✅ Universal 2 архитектура подтверждена

**Если .app отсутствует:**
- ✅ Это нормально для `build_final.sh` — проверка выполняется из PKG/DMG

---

### 3. Проверка .app внутри PKG

```bash
# Распаковка PKG
rm -rf /tmp/pkg_test /tmp/payload_test
pkgutil --expand dist/Nexy.pkg /tmp/pkg_test

# Поиск вложенного PKG
NESTED=$(find /tmp/pkg_test -name "*.pkg" -type d | head -1)

# Распаковка Payload
mkdir -p /tmp/payload_test
(cd /tmp/payload_test && gzip -dc "$NESTED/Payload" | cpio -idm 2>/dev/null)

# Проверка подписи .app из PKG
codesign --verify --deep --strict --verbose=2 /tmp/payload_test/Applications/Nexy.app

# Проверка нотаризации .app из PKG
xcrun stapler validate /tmp/payload_test/Applications/Nexy.app

# Очистка
rm -rf /tmp/pkg_test /tmp/payload_test
```

**Ожидаемый результат:**
- ✅ .app найден в Payload
- ✅ Подпись .app из PKG корректна
- ✅ Нотаризация .app из PKG корректна (если не пропущена через `NEXY_SKIP_NOTARIZATION=1`)

**Примечание:** Если нотаризация была пропущена (`NEXY_SKIP_NOTARIZATION=1`), команда `xcrun stapler validate` может вернуть ошибку — это нормально.

---

### 4. Проверка PKG

```bash
# Проверка подписи PKG
pkgutil --check-signature dist/Nexy.pkg

# Проверка через spctl
spctl -a -vv --type install dist/Nexy.pkg

# Проверка нотаризации PKG
xcrun stapler validate dist/Nexy.pkg
```

**Ожидаемый результат:**
- ✅ Подпись PKG корректна
- ✅ spctl проверка прошла (или предупреждение для непронотаризованного)
- ✅ Нотаризация PKG корректна (если не пропущена через `NEXY_SKIP_NOTARIZATION=1`)

**Примечание:** Если нотаризация была пропущена (`NEXY_SKIP_NOTARIZATION=1`), команда `xcrun stapler validate` может вернуть ошибку — это нормально.

---

### 5. Проверка DMG

```bash
# Проверка целостности DMG
hdiutil verify dist/Nexy.dmg

# Монтирование DMG
MOUNT_POINT=$(hdiutil attach dist/Nexy.dmg -nobrowse -readonly -noautoopen 2>&1 | grep -E "/Volumes/" | awk '{print $3}' | head -1)

# Проверка .app в DMG
codesign --verify --deep --strict --verbose=2 "$MOUNT_POINT/Nexy.app"

# Размонтирование
hdiutil detach "$MOUNT_POINT" >/dev/null 2>&1
```

**Ожидаемый результат:**
- ✅ DMG целостность подтверждена
- ✅ .app найден в DMG
- ✅ Подпись .app в DMG корректна

**Примечание:** Если нотаризация была пропущена (`NEXY_SKIP_NOTARIZATION=1`), проверка нотаризации DMG может вернуть ошибку — это нормально.

---

### 6. Проверка Runtime Hook

**ВАЖНО:** Лог пишется в `/tmp/nexy_pyobjc_fix.log` (через `tempfile.gettempdir()`), а не в `$HOME/`.

```bash
# Проверка лога runtime hook
cat /tmp/nexy_pyobjc_fix.log 2>/dev/null || echo "Лог не найден (приложение еще не запускалось)"

# Проверка на ошибки dlsym
grep -i "dlsym.*cannot find symbol.*NSMake" /tmp/nexy_pyobjc_fix.log 2>/dev/null || echo "Ошибок dlsym не найдено"
```

**Ожидаемый результат:**
- ✅ Лог создан (после первого запуска приложения)
- ✅ Нет ошибок `dlsym cannot find symbol NSMake*`
- ✅ Сообщение: `[NEXY_INIT] INFO: All symbols already present in Foundation` или `SUCCESS: fixed_inline:...`

---

## Критерии успеха

### Обязательные проверки:
- [ ] .app подписан и валиден (проверяется напрямую или из PKG/DMG)
- [ ] .app нотаризован (если не пропущена нотаризация через `NEXY_SKIP_NOTARIZATION=1`)
- [ ] .app имеет Universal 2 архитектуру (arm64 + x86_64)
- [ ] .app внутри PKG подписан и валиден
- [ ] PKG подписан и валиден
- [ ] DMG целостность подтверждена
- [ ] Нет ошибок dlsym в runtime hook логе (`/tmp/nexy_pyobjc_fix.log`)

### Опциональные проверки:
- [ ] PKG нотаризован (если не пропущена нотаризация через `NEXY_SKIP_NOTARIZATION=1`)
- [ ] DMG нотаризован (если не пропущена нотаризация через `NEXY_SKIP_NOTARIZATION=1`)
- [ ] spctl проверка PKG прошла успешно

**Примечание:** Если `.app` отсутствует в `dist/` после `build_final.sh`, это нормально — проверка выполняется из PKG/DMG.

---

## Troubleshooting

### Ошибка: "invalid signature"
**Решение:** Пересоберите с полной очисткой:
```bash
rm -rf dist/* build/* dist-arm64 dist-x86_64 build-arm64 build-x86_64
./packaging/build_final.sh
```

### Ошибка: "stapler validate failed"
**Решение:** Проверьте, что нотаризация не была пропущена:
```bash
# Если нужно пропустить нотарификацию:
NEXY_SKIP_NOTARIZATION=1 ./packaging/build_final.sh
./scripts/verify_packaging_artifacts.sh --app-only
```

### Ошибка: "dlsym cannot find symbol NSMake*"
**Решение:** Проверьте, что runtime hook применяется:
1. Убедитесь, что в `Nexy.spec` используется абсолютный путь:
   ```python
   runtime_hooks=[
       str(client_dir / "packaging" / "runtime_hook_pyobjc_fix.py"),
   ],
   ```
2. Пересоберите приложение
3. Запустите и проверьте `/tmp/nexy_pyobjc_fix.log` (лог пишется через `tempfile.gettempdir()`)

---

## Связанные документы

- `Docs/PACKAGING_FINAL_GUIDE.md` — полная инструкция по сборке
- `scripts/verify_packaging_artifacts.sh` — автоматическая проверка артефактов
- `packaging/build_final.sh` — скрипт полной сборки
- `.cursorrules` §11.2 — Packaging Regression Checklist
