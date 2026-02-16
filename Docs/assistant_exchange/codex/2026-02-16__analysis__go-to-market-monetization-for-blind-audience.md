# Analysis: Go-to-market и монетизация для Nexy (аудитория: незрячие)

## Контекст
- Продукт voice-first, доступностный фокус (VoiceOver/assistive сценарии), сервер и платежный контур близки к готовности.
- Цель: начать выручку быстро, без реархитектуры.

## Primary стратегия (90 дней)
1. Запустить B2C подписку напрямую (Stripe Checkout + portal):
   - Free: базовые лимиты.
   - Pro: безлимит/повышенные лимиты + приоритет.
   - Результат: быстрый запуск MRR без длинных продаж.
2. Добавить B2B-lite для организаций:
   - Пакеты мест для школ/реабилитационных центров/НКО (5/20/50 seats).
   - Единый инвойс, админ-кабинет позже (сначала вручную через CRM + Stripe invoice).
3. Канал продаж через экосистему незрячих:
   - Сообщества, каталоги приложений, профильные конференции и локальные организации.

## Почему это архитектурно оптимально
- Не требует новых runtime-owner путей в клиенте/сервере.
- Монетизация концентрируется в существующем payment owner-контуре (server owner logic + client UX contracts).
- Минимизирует дубли: один checkout + один subscription state + один entitlement gate.

## Коммерческие пакеты (старт)
- `Free`: ограничение по сессиям/командам в месяц.
- `Pro Individual`: $15–25/мес.
- `Pro Plus`: $30–49/мес (интенсивное использование, приоритет в очереди).
- `Org Starter`: от $99/мес (5 seats), дальше по seat.

## План запуска (практический)
### Неделя 1
- Довести платежку до production-ready:
  - webhook idempotency, статусы подписки, downgrade/cancel path, billing portal.
- Встроить понятный paywall-триггер:
  - после исчерпания free-лимита и в onboarding.
- Добавить 7-дневный trial (без сложной логики, стандарт Stripe flow).

### Неделя 2
- 20–30 целевых бета-пользователей:
  - через blind community, чаты, локальные NFB/state groups.
- Формат оффера:
  - 30 минут персонального onboarding + 1 месяц Pro за фидбек.
- Собрать 5–10 видео/аудио testimonials с акцентом на конкретный outcome.

### Неделя 3–4
- Публичный лонч:
  - лендинг с 3 сценариями (работа/сообщения/браузер),
  - 1 CTA: Start free trial.
- Параллельно:
  - outreach в 30 организаций (комиссии по слепым, training centers, НКО).

## KPI (чтобы понимать, что деньги пошли)
- Activation D1: >=35% дошли до “полезного результата”.
- Trial->Paid: >=15%.
- Refund rate: <5%.
- 30-day retention paid: >=70%.
- B2B pilot: минимум 2 организации в первый месяц после лонча.

## Риски и guardrails
- Риск: высокий churn из-за сложного first-run.
  - Guard: персональный onboarding + voice-first walkthrough.
- Риск: race в биллинге (повторные webhook события).
  - Guard: idempotency key + single subscription owner на сервере.
- Риск: слишком ранний B2B enterprise.
  - Guard: сначала B2C+Org-lite, enterprise позже.

## Внешние каналы и подтверждения (актуальные ссылки)
- AppleVis App Directory (канал обнаружения приложений незрячими): https://www.applevis.com/apps
- CSUN AT Conference 2026 (крупная AT-площадка): https://www.csun.edu/cod/conference
- iCanConnect / NDBEDP (федеральная программа, локальные контакты): https://www.icanconnect.org/
- iCanConnect eligibility/how-to-apply (актуальные критерии): https://www.icanconnect.org/how-to-apply/
- Association of Blind Citizens Assistive Technology Fund: https://blindcitizens.org/assistive-technology-fund/
- RSA regulations index (VR framework): https://rsa.ed.gov/statute-legislation-and-policy/regulations
- 34 CFR 361.53 (rehabilitation technology в перечне VR services): https://www.law.cornell.edu/cfr/text/34/361.53

## Итог
Самый быстрый путь к выручке: `B2C подписка + free tier + trial`, затем `Org-lite пакеты` через существующие blind/rehab каналы, без усложнения архитектуры и без запуска дорогого enterprise-процесса на старте.
