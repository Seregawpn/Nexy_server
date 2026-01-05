# Case Study: Ошибка 403 при нотарификации

**Ошибка:** `HTTP status code: 403. A required agreement is missing or has expired.`

**Канон troubleshooting:** `Docs/NOTARIZATION_TROUBLESHOOTING.md` — общий гайд по решению проблем нотарификации.

**Этот документ:** детальный case-study конкретной ошибки 403.

---

## Что это означает?

Apple блокирует нотарификацию, потому что в вашем Apple Developer аккаунте **не подписаны необходимые соглашения**.

### Почему это происходит?

Apple требует, чтобы разработчики подписывали юридические соглашения перед использованием сервисов нотарификации. Это включает:
- **Paid Applications Agreement** (для платных приложений)
- **Free Applications Agreement** (для бесплатных приложений)
- **Apple Developer Program License Agreement** (общее соглашение)

---

## Как проверить статус соглашений?

### Вариант 1: Через веб-интерфейс

1. Откройте https://developer.apple.com/account
2. Войдите в аккаунт
3. Перейдите в раздел **Agreements, Terms, and Guidelines**
4. Проверьте статус каждого соглашения:
   - ✅ **Active** — соглашение подписано и активно
   - ⚠️ **Pending** — требуется подписание
   - ❌ **Expired** — соглашение истекло, требуется обновление

### Вариант 2: Через командную строку (если доступно)

```bash
# Проверка через altool (устаревший, но может показать детали)
xcrun altool --list-providers -u "seregawpn@gmail.com" -p "@keychain:nexy-notary"
```

---

## Как исправить?

### Шаг 1: Подписать соглашения

1. Откройте https://developer.apple.com/account
2. Перейдите в **Agreements, Terms, and Guidelines**
3. Найдите соглашения со статусом **Pending** или **Expired**
4. Нажмите на соглашение
5. Прочитайте условия
6. Подпишите соглашение

### Шаг 2: Дождаться активации

После подписания соглашение может активироваться:
- **Мгновенно** — для большинства случаев
- **До 24 часов** — в редких случаях требуется проверка Apple

### Шаг 3: Повторная нотарификация

После активации соглашений:

```bash
# Попробовать снова
xcrun notarytool submit dist/Nexy-app-for-notarization.zip \
    --keychain-profile "nexy-notary" \
    --apple-id "seregawpn@gmail.com" \
    --wait
```

---

## Альтернативные причины ошибки 403

### 1. Проблемы с аккаунтом

- **Аккаунт не активен** — проверьте статус Apple Developer Program
- **Просроченная подписка** — обновите подписку
- **Ограничения аккаунта** — проверьте, нет ли ограничений

### 2. Проблемы с сертификатами

- **Сертификат истек** — обновите Developer ID сертификаты
- **Неправильный Team ID** — проверьте соответствие Team ID

### 3. Проблемы с keychain profile

- **Неправильный profile** — пересоздайте keychain profile
- **Устаревшие credentials** — обновите credentials

---

## Проверка всех компонентов

### 1. Проверка аккаунта

```bash
# Проверка Team ID
security find-identity -v -p codesigning | grep "Developer ID"
```

### 2. Проверка keychain profile

```bash
# Список сохраненных profiles
xcrun notarytool store-credentials --list

# Пересоздание profile (если нужно)
xcrun notarytool store-credentials nexy-notary \
    --apple-id "seregawpn@gmail.com" \
    --team-id "5NKLL2CLB9" \
    --keychain-profile "nexy-notary"
```

### 3. Проверка подписи

```bash
# Проверка подписи .app
codesign --verify --deep --strict /tmp/Nexy.app

# Проверка подписи PKG
pkgutil --check-signature dist/Nexy.pkg
```

---

## Частые вопросы

### Q: Могу ли я использовать приложение без нотарификации?

**A:** Да, но с ограничениями:
- ✅ Работает локально (после разрешения Gatekeeper)
- ❌ Gatekeeper блокирует на других компьютерах
- ❌ Не подходит для распространения через интернет

### Q: Сколько времени занимает активация соглашения?

**A:** Обычно мгновенно, но может занять до 24 часов в редких случаях.

### Q: Нужно ли пересобирать приложение после подписания соглашения?

**A:** Нет, можно использовать уже созданные артефакты:
- `dist/Nexy-app-for-notarization.zip` — для нотарификации .app
- `dist/Nexy.dmg` — для нотарификации DMG
- `dist/Nexy.pkg` — для нотарификации PKG

### Q: Что делать, если соглашения уже подписаны, но ошибка остается?

**A:** Проверьте:
1. Статус аккаунта Apple Developer Program
2. Срок действия подписки
3. Правильность Team ID в keychain profile
4. Попробуйте пересоздать keychain profile

---

## Следующие шаги

1. ✅ Проверьте статус соглашений в Apple Developer Portal
2. ✅ Подпишите все необходимые соглашения
3. ✅ Дождитесь активации (обычно мгновенно)
4. ✅ Повторите нотарификацию

---

## Связанные документы

- `Docs/NOTARIZATION_TROUBLESHOOTING.md` — **канон troubleshooting нотарификации** (общие решения)
- `Docs/PACKAGING_FINAL_GUIDE.md` — полная инструкция по упаковке
- `Docs/TESTING_PACKAGED_APP.md` — тестирование упакованного приложения
