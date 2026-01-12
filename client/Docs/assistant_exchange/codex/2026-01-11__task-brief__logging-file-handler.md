# Author
Codex

# Request/Goal
Сделать так, чтобы TRACE/диагностические логи гарантированно записывались в файл.

# Changes
- Centralized logging now creates console + file handlers from unified_config.yaml.
- main.py uses centralized logging and reports actual log file path; adds fallback file handler if none.

# Files Touched
- integration/utils/logging_setup.py
- main.py

# Verification
- Not run (manual). Expected log file: logs/nexy.log (or temp fallback if config missing).
