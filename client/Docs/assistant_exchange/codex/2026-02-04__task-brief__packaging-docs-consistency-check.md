# Task Brief

## Context
Проверка всей документации, относящейся к упаковке, выявила частичную рассинхронизацию: в гайде не было явного отражения новых автоматических gate шагов внутри `build_final.sh`, а referenced файлы чек-листов отсутствовали.

## Changes
1. `Docs/PACKAGING_FINAL_GUIDE.md`
- Обновлен раздел "Что делает build_final.sh автоматически".
- Добавлены первые 2 обязательных шага:
  - `scripts/verify_packaging_readiness.py`
  - `REQUIRE_BASEDPYRIGHT_IN_SCAN=true scripts/problem_scan_gate.sh`

2. Добавлены отсутствующие документы:
- `Docs/PRE_PACKAGING_VERIFICATION.md`
- `Docs/PACKAGING_READINESS_CHECKLIST.md`

Оба документа синхронизированы с текущим quality/release контуром.

## Verification
- Проверено наличие и консистентность ссылок на упаковочные документы в `Docs/*`.
- Проверено, что referenced checklist/verification документы теперь реально существуют.

## Impact
- Документация упаковки снова целостна: ссылки не битые, канон отражает фактический `build_final.sh` pipeline.
