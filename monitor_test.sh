#!/bin/bash
# Root-level monitor helper (legacy-safe).
# Не зависит от удалённых legacy-тестов.

set -euo pipefail

echo "Root monitor check"
echo ""

echo "1) Проверка root-файлов:"
for f in main.py verify_imports.py requirements.txt AGENTS.md; do
  if [[ -f "$f" ]]; then
    echo "   OK: $f"
  else
    echo "   MISSING: $f"
  fi
done

echo ""
echo "2) Быстрая проверка синтаксиса root Python:"
python3 -m py_compile main.py verify_imports.py && echo "   OK: py_compile passed"

echo ""
echo "3) Legacy client/server test runners в root больше не используются."
echo "   Канонические проверки запускаются из профильных каталогов (client/server)."
