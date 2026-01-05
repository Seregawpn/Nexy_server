# Troubleshooting нотарификации

**Версия:** 1.0  
**Проблема:** Ошибка 403 при нотарификации

---

## Ошибка: "A required agreement is missing or has expired"

### Причина

Apple Developer аккаунт требует подписания соглашений перед нотарификацией.

### Решение

#### Шаг 1: Проверка соглашений

1. Откройте https://developer.apple.com/account
2. Войдите в аккаунт
3. Перейдите в раздел **Agreements, Terms, and Guidelines**
4. Проверьте статус всех соглашений

#### Шаг 2: Подписание соглашений

Если есть неподписанные соглашения:
- Нажмите на соглашение
- Прочитайте условия
- Подпишите соглашение

#### Шаг 3: Повторная нотарификация

После подписания соглашений:

```bash
# Вариант 1: Полная переупаковка
./packaging/build_final.sh

# Вариант 2: Только нотарификация (если .app уже готов)
xcrun notarytool submit dist/Nexy-app-for-notarization.zip \
    --keychain-profile "nexy-notary" \
    --apple-id "seregawpn@gmail.com" \
    --wait

# После успешной нотарификации
xcrun stapler staple /tmp/Nexy.app
```

---

## Другие возможные ошибки

### Ошибка: "Invalid credentials"

**Причина:** Неправильный keychain profile или Apple ID

**Решение:**
```bash
# Проверка keychain profile
xcrun notarytool store-credentials nexy-notary \
    --apple-id "seregawpn@gmail.com" \
    --team-id "5NKLL2CLB9" \
    --keychain-profile "nexy-notary"
```

### Ошибка: "The signature of the binary is invalid"

**Причина:** Подпись нарушена или бинарник не Universal 2

**Решение:**
```bash
# Проверка архитектур
lipo -info dist/Nexy.app/Contents/MacOS/Nexy

# Переподпись
codesign --force --timestamp --options=runtime \
    --sign "Developer ID Application: Sergiy Zasorin (5NKLL2CLB9)" \
    --entitlements packaging/entitlements.plist \
    dist/Nexy.app
```

### Ошибка: "The package is missing required files"

**Причина:** Отсутствуют обязательные файлы в .app

**Решение:**
- Проверить структуру .app через `validate_release_bundle.py`
- Убедиться, что все ресурсы на месте

---

## Проверка статуса нотарификации

```bash
# История нотаризаций
xcrun notarytool history \
    --keychain-profile "nexy-notary" \
    --apple-id "seregawpn@gmail.com"

# Проверка конкретной заявки
xcrun notarytool log <submission-id> \
    --keychain-profile "nexy-notary" \
    --apple-id "seregawpn@gmail.com"
```

---

## Связанные документы

- `Docs/PACKAGING_FINAL_GUIDE.md` — полная инструкция по упаковке
- `Docs/TESTING_PACKAGED_APP.md` — тестирование упакованного приложения
