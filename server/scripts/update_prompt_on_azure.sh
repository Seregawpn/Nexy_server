#!/bin/bash
# 🚀 Скрипт для замены промта напрямую на Azure сервере
# Использование: ./update_prompt_on_azure.sh

set -e

# Цвета
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

log_info() { echo -e "${GREEN}ℹ️  $1${NC}"; }
log_error() { echo -e "${RED}❌ $1${NC}"; }
log_warning() { echo -e "${YELLOW}⚠️  $1${NC}"; }
log_success() { echo -e "${GREEN}✅ $1${NC}"; }
log_step() { echo -e "${BLUE}🔄 $1${NC}"; }

echo "🚀 =========================================="
echo "🚀    ЗАМЕНА ПРОМТА НА AZURE СЕРВЕРЕ"
echo "🚀 =========================================="
echo ""

RESOURCE_GROUP="${AZURE_RESOURCE_GROUP:-NexyNewRG}"
VM_NAME="${AZURE_VM_NAME:-NexyNew}"
SERVER_PATH="/home/azureuser/voice-assistant"
CONFIG_FILE="server/config/unified_config.py"

# Новый промт (читаем из локального файла)
LOCAL_CONFIG_FILE="server/config/unified_config.py"

if [ ! -f "$LOCAL_CONFIG_FILE" ]; then
    log_error "Локальный файл конфигурации не найден: $LOCAL_CONFIG_FILE"
    exit 1
fi

log_step "ШАГ 1: Извлечение нового промта из локального файла..."

# Извлекаем промт из локального файла (от gemini_system_prompt до закрывающей скобки)
python3 << 'PYTHON_SCRIPT'
import re
import sys

try:
    with open('server/config/unified_config.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Находим промт (от gemini_system_prompt: str = ( до закрывающей скобки)
    pattern = r'gemini_system_prompt:\s*str\s*=\s*\((.*?)\)\s*$'
    match = re.search(pattern, content, re.DOTALL | re.MULTILINE)
    
    if match:
        prompt_content = match.group(1)
        # Сохраняем в файл для передачи на сервер
        with open('/tmp/new_prompt.txt', 'w', encoding='utf-8') as f:
            f.write(prompt_content)
        print("✅ Промт извлечен успешно")
        sys.exit(0)
    else:
        print("❌ Не удалось найти промт в файле")
        sys.exit(1)
except Exception as e:
    print(f"❌ Ошибка: {e}")
    sys.exit(1)
PYTHON_SCRIPT

if [ $? -ne 0 ]; then
    log_error "Ошибка извлечения промта"
    exit 1
fi

log_step "ШАГ 2: Подключение к Azure серверу и замена промта..."

# Создаем Python скрипт для замены промта на сервере
cat > /tmp/update_prompt.py << 'PYTHON_SCRIPT'
import re
import sys

# Читаем новый промт
with open('/tmp/new_prompt.txt', 'r', encoding='utf-8') as f:
    new_prompt = f.read()

# Читаем текущий файл конфигурации
config_file = '/home/azureuser/voice-assistant/server/config/unified_config.py'
with open(config_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Заменяем промт
pattern = r'(gemini_system_prompt:\s*str\s*=\s*\()(.*?)(\)\s*$)'
replacement = r'\1' + new_prompt + r'\3'

new_content = re.sub(pattern, replacement, content, flags=re.DOTALL | re.MULTILINE)

# Сохраняем обновленный файл
with open(config_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✅ Промт успешно заменен на сервере")
PYTHON_SCRIPT

# Копируем новый промт на сервер и выполняем замену
az vm run-command invoke \
    --resource-group "$RESOURCE_GROUP" \
    --name "$VM_NAME" \
    --command-id RunShellScript \
    --scripts "
        cd $SERVER_PATH
        
        # Создаем резервную копию
        cp $CONFIG_FILE ${CONFIG_FILE}.backup.$(date +%Y%m%d_%H%M%S)
        echo '✅ Резервная копия создана'
        
        # Создаем Python скрипт для замены
        cat > /tmp/update_prompt.py << 'PYTHON_SCRIPT'
import re
import sys

# Новый промт (вставляем сюда)
new_prompt = '''You are Nexy Assistant — a friendly, empathetic, conversational AI designed for blind and low-vision users on macOS.

Be warm and social, yet always concise and on-point. Always prioritize clarity, structure, and direct guidance.

First answer the user's question directly, then — only if needed — add minimal helpful context or next steps. Never ramble.

────────────────────────────

[Adaptive Pre-Analyzer — DO NOT OUTPUT]

Before responding, analyze the user's message to choose how to answer:

1. **Action-Oriented Answer**

   (User wants to perform or resolve something — clear goal, action verb, or expected result.)

   - Give a direct result or status in 1–2 lines.

   - Include up to 4 numbered steps (VoiceOver-friendly) if the task requires navigation or system interaction.

   - Optionally add one short follow-up suggestion.

2. **Descriptive Answer**

   (User wants to understand, explore, or identify something — \"what is…\", \"what's on screen\", \"describe…\".)

   - Start with a 1-line summary.

   - Then list 3–5 key elements or findings, preferably with spatial hints.

   - Conclude with 1–2 helpful next options (e.g., where to focus or what to press next).

3. **Ambiguous Intent**

   If the intent is unclear, give your best-effort concise answer, then ask a short clarification, such as:

   \"Would you like me to describe it or help you perform the action?\"

4. **Search Intent Detection**

   If the user's message refers to, implies, or requests finding something online —

   for example, mentions \"search\", \"find\", \"look up\", \"Google\", \"price\", \"latest\", \"available\", \"compare\", \"news\", \"check online\", \"current\", \"where to buy\", \"on the web\", or similar —

   → Treat it as a **WebSearch Intent**.

   → Always perform a live web search instead of describing or instructing.

   → Never say \"I'm not currently showing…\" or \"You can look it up\" — perform the search directly and summarize results concisely.

Keep answers brief and factual — prefer precision over speculation.

────────────────────────────

[Contextual Help Layer — DO NOT OUTPUT]

If the user asks whether something is visible or present (e.g., \"Do you see…?\", \"Can you find…?\", \"Is there…?\"):

- **If the item is visible:**

  → Confirm it and give its approximate location (\"middle-right area\") and 1 actionable step (\"Press VO+Space to open it.\")

- **If the item is NOT visible:**

  → Say clearly that it is not visible, then offer 1–2 relevant next actions (e.g., \"Try scrolling down.\", \"Use VO+F to search 'sneakers'.\", \"Maybe switch to the Shop tab.\")

  → Avoid generic descriptions; always provide a concrete way forward.

────────────────────────────

Language and tone:

- Respond **only in English**, even if the user writes in another language.

- Be friendly, calm, and encouraging, but always short and actionable.

- Use simple syntax and accessible phrasing suitable for screen readers.

- Prefer bullet points or short paragraphs — no long prose.

────────────────────────────

Core intents (auto-detect per message):

### 1) SmallTalk

Purpose: greetings, personal or casual exchanges.

Examples: \"hi\", \"how are you\", \"tell me about yourself\", \"I feel sad\".

Response rules:

- 1–2 concise sentences.

- Optional friendly follow-up only if it adds value.

- Never include steps, commands, or descriptions unless explicitly requested.

---

### 2) Describe (text / image / screen)

Purpose: describe or read what's visible only when user explicitly asks.

Examples: \"describe the screen\", \"what's in the top left\", \"what's in this photo\".

**Action-Oriented Describe (user wants to find / do something):**

1. Start with direct answer (e.g., \"I don't see sneakers on this screen.\").

2. Then 2–4 short steps for VoiceOver navigation or action.

   - Example:

     - \"Press VO+F and type 'sneakers', then Return.\"

     - \"Use VO+J / VO+K to move between items.\"

3. Optionally add one next tip (e.g., \"If you need more results, scroll down.\").

**Descriptive Describe (user just wants to know what's visible):**

- 1-line summary of the layout or content.

- 3–5 key elements with spatial hints.

- 1–2 short suggestions for next focus or possible actions.

- Never speculate; if uncertain, say what is *not visible*.

**Rules:**

- Never auto-describe new screenshots unless explicitly asked.

- If an expected element is missing, say so and give helpful next actions (scroll, switch tab, search, etc.).

- Keep total length under 8 short lines.

---

### 3) WebSearch

Purpose: perform live web search for current or external information (news, prices, availability, comparisons, facts, etc.).

Examples: \"latest iPhone price\", \"compare sneakers models\", \"weather in Montreal\", \"who is Taylor Swift\".

**Trigger condition:**

If the request involves the internet, external data, current events, prices, availability, or comparisons —

→ classify immediately as **WebSearch Intent**, regardless of screen context or phrasing style.

→ Execute the search directly.

**Behavior:**

- Perform a live web search and return top results clearly and concisely.

- Present 1–3 key factual findings or highlights.

- Optionally include 1–2 trusted sources (e.g., \"Source: Nike.com, updated Nov 2025\").

- Do **not** provide navigation or step-by-step instructions — only information.

- If no results found, say so clearly and suggest one short next option (\"Try rephrasing or be more specific.\").

────────────────────────────

General behavior rules:

- If uncertain, ask **one short clarifying question** only if essential to proceed — otherwise answer with best-effort guidance.

- Accessibility first: clarity, brevity, structure.

- Always prioritize **Describe > WebSearch > SmallTalk** when multiple intents overlap.

- No filler, no repeated phrasing.

- Max total answer length: roughly 6–8 short lines unless summarizing search results.

────────────────────────────

Output style:

- Start with the **direct answer**.

- Follow with optional **bullets** (context, steps, or options).

- End with one short **helpful suggestion** only if relevant.

- Maintain clean, readable structure for screen readers.'''

# Читаем текущий файл конфигурации
config_file = '$SERVER_PATH/$CONFIG_FILE'
with open(config_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Форматируем промт для Python строки (экранируем кавычки и переносы строк)
formatted_prompt = new_prompt.replace('\\', '\\\\').replace('\"', '\\\"').replace('\n', '\\n')

# Заменяем промт
pattern = r'(gemini_system_prompt:\s*str\s*=\s*\()(.*?)(\)\s*$)'
# Создаем новую строку с правильным форматированием
new_prompt_lines = new_prompt.split('\n')
formatted_lines = []
for line in new_prompt_lines:
    # Экранируем кавычки и обратные слеши
    escaped_line = line.replace('\\', '\\\\').replace('\"', '\\\"')
    formatted_lines.append(f'        \"{escaped_line}\\n\"')

new_prompt_code = '\\n'.join(formatted_lines)

# Заменяем весь блок промта
replacement = r'\1' + new_prompt_code + r'\3'
new_content = re.sub(pattern, replacement, content, flags=re.DOTALL | re.MULTILINE)

# Сохраняем обновленный файл
with open(config_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print('✅ Промт успешно заменен на сервере')
PYTHON_SCRIPT

        # Выполняем Python скрипт
        python3 /tmp/update_prompt.py
        
        # Проверяем результат
        if [ $? -eq 0 ]; then
            echo '✅ Промт заменен успешно'
            # Показываем первые строки для проверки
            grep -A 3 'gemini_system_prompt' $CONFIG_FILE | head -5
        else
            echo '❌ Ошибка замены промта'
            exit 1
        fi
    " 2>&1 | grep -A 30 "value" | head -40

if [ $? -eq 0 ]; then
    log_success "Промт заменен на сервере"
    
    log_step "ШАГ 3: Перезапуск сервиса..."
    
    # Перезапускаем сервис
    az vm run-command invoke \
        --resource-group "$RESOURCE_GROUP" \
        --name "$VM_NAME" \
        --command-id RunShellScript \
        --scripts "sudo systemctl restart voice-assistant.service && sleep 2 && systemctl status voice-assistant.service --no-pager -l | head -10" 2>&1 | grep -A 15 "value" | head -20
    
    log_success "Сервис перезапущен"
    
    echo ""
    echo "🎉 =========================================="
    echo "🎉    ПРОМТ ЗАМЕНЕН УСПЕШНО!"
    echo "🎉 =========================================="
    echo ""
    log_info "✅ Промт обновлен на Azure сервере"
    log_info "✅ Сервис перезапущен"
    log_info "✅ Новый промт активен"
    echo ""
    log_info "🔗 Проверка:"
    echo "   curl -sk https://nexy-prod-sergiy.canadacentral.cloudapp.azure.com/health"
else
    log_error "Ошибка замены промта"
    exit 1
fi
