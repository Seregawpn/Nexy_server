# Payment Flow (Root Index)

Root-документ является индексом и не содержит runtime-логики.

Канонические источники по оплатам:
- Клиентские требования и UX-контракты: `client/Docs/PROJECT_REQUIREMENTS.md`
- Серверная архитектура и owner-логика: `server/server/Docs/ARCHITECTURE_OVERVIEW.md`
- Серверные release/update правила: `server/server/Docs/RELEASE_AND_UPDATE_GUIDE.md`
- Архив исходных детальных материалов:
  - `Docs/_archive/PAYMENT_UPDATE_CONTROLLER.md`
  - `Docs/_archive/PAYMENT_REQUIREMENTS.md`

Правило централизации:
- Решения gate/квот/статусов оплаты описываются только в каноне владельца.
- Root содержит только ссылки и рамки координации.
