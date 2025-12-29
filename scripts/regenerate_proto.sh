#!/bin/bash
# Скрипт для регенерации protobuf pb2 файлов из .proto
# Использование: ./scripts/regenerate_proto.sh [--check]

set -e

# Определяем корень проекта: ищем директорию, содержащую и server/, и client/
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# Если скрипт вызывается через симлинк, находим реальный путь (совместимо с macOS)
REAL_SCRIPT="${BASH_SOURCE[0]}"
while [ -L "$REAL_SCRIPT" ]; do
    REAL_SCRIPT="$(readlink "$REAL_SCRIPT")"
    # Если относительный путь, делаем абсолютным
    if [ "${REAL_SCRIPT:0:1}" != "/" ]; then
        REAL_SCRIPT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && cd "$(dirname "$REAL_SCRIPT")" && pwd)/$(basename "$REAL_SCRIPT")"
    fi
done
REAL_SCRIPT_DIR="$(cd "$(dirname "$REAL_SCRIPT")" && pwd)"
# Пробуем найти корень проекта: идем вверх, пока не найдем директорию с server/ и client/
CURRENT_DIR="$REAL_SCRIPT_DIR"
PROJECT_ROOT=""
while [ "$CURRENT_DIR" != "/" ]; do
    if [ -d "$CURRENT_DIR/server" ] && [ -d "$CURRENT_DIR/client" ]; then
        PROJECT_ROOT="$CURRENT_DIR"
        break
    fi
    CURRENT_DIR="$(dirname "$CURRENT_DIR")"
done
# Если не нашли, используем старую логику
if [ -z "$PROJECT_ROOT" ]; then
    PROJECT_ROOT="$(cd "$REAL_SCRIPT_DIR/.." && pwd)"
fi

# Цвета для вывода
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

CHECK_ONLY=false
if [[ "$1" == "--check" ]]; then
    CHECK_ONLY=true
fi

# Проверка наличия grpc_tools.protoc
if ! python3 -m grpc_tools.protoc --version &>/dev/null; then
    echo -e "${RED}❌ Ошибка: grpc_tools.protoc не найден${NC}"
    echo "Установите: pip install grpcio-tools"
    exit 1
fi

# Функция для регенерации pb2 файлов
regenerate_proto() {
    local proto_file="$1"
    local proto_dir="$2"
    local python_out="$3"
    local grpc_python_out="$4"
    
    echo -e "${GREEN}🔄 Регенерация pb2 из ${proto_file}...${NC}"
    
    python3 -m grpc_tools.protoc \
        -I "$proto_dir" \
        --python_out="$python_out" \
        --grpc_python_out="$grpc_python_out" \
        "$proto_file"
    
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✅ Успешно: ${proto_file}${NC}"
        return 0
    else
        echo -e "${RED}❌ Ошибка при регенерации: ${proto_file}${NC}"
        return 1
    fi
}

# Функция для проверки актуальности pb2 файлов
check_proto_stale() {
    local proto_file="$1"
    local pb2_file="$2"
    
    if [ ! -f "$pb2_file" ]; then
        echo -e "${RED}❌ pb2 файл отсутствует: ${pb2_file}${NC}"
        return 1
    fi
    
    if [ "$proto_file" -nt "$pb2_file" ]; then
        echo -e "${YELLOW}⚠️  pb2 файл устарел: ${pb2_file}${NC}"
        echo "   .proto файл новее pb2 файла"
        return 1
    fi
    
    return 0
}

# Регенерация для сервера
SERVER_PROTO="$PROJECT_ROOT/server/server/modules/grpc_service/streaming.proto"
SERVER_DIR="$PROJECT_ROOT/server/server/modules/grpc_service"
SERVER_PB2="$SERVER_DIR/streaming_pb2.py"

if [ ! -f "$SERVER_PROTO" ]; then
    echo -e "${RED}❌ Файл не найден: ${SERVER_PROTO}${NC}"
    exit 1
fi

# Регенерация для клиента
CLIENT_PROTO="$PROJECT_ROOT/client/modules/grpc_client/proto/streaming.proto"
CLIENT_DIR="$PROJECT_ROOT/client/modules/grpc_client/proto"
CLIENT_PB2="$CLIENT_DIR/streaming_pb2.py"

if [ ! -f "$CLIENT_PROTO" ]; then
    echo -e "${RED}❌ Файл не найден: ${CLIENT_PROTO}${NC}"
    exit 1
fi

ERRORS=0

if [ "$CHECK_ONLY" = true ]; then
    echo -e "${YELLOW}🔍 Проверка актуальности pb2 файлов...${NC}"
    
    # Проверка сервера
    if ! check_proto_stale "$SERVER_PROTO" "$SERVER_PB2"; then
        ERRORS=$((ERRORS + 1))
    fi
    
    # Проверка клиента
    if ! check_proto_stale "$CLIENT_PROTO" "$CLIENT_PB2"; then
        ERRORS=$((ERRORS + 1))
    fi
    
    if [ $ERRORS -eq 0 ]; then
        echo -e "${GREEN}✅ Все pb2 файлы актуальны${NC}"
        exit 0
    else
        echo -e "${RED}❌ Найдено ${ERRORS} устаревших pb2 файлов${NC}"
        echo "Запустите: ./scripts/regenerate_proto.sh для регенерации"
        exit 1
    fi
else
    echo -e "${GREEN}🚀 Регенерация protobuf файлов...${NC}"
    
    # Регенерация сервера
    if ! regenerate_proto "$SERVER_PROTO" "$SERVER_DIR" "$SERVER_DIR" "$SERVER_DIR"; then
        ERRORS=$((ERRORS + 1))
    fi
    
    # Регенерация клиента
    if ! regenerate_proto "$CLIENT_PROTO" "$CLIENT_DIR" "$CLIENT_DIR" "$CLIENT_DIR"; then
        ERRORS=$((ERRORS + 1))
    fi
    
    if [ $ERRORS -eq 0 ]; then
        echo -e "${GREEN}✅ Все pb2 файлы успешно регенерированы${NC}"
        exit 0
    else
        echo -e "${RED}❌ Ошибки при регенерации (${ERRORS} файлов)${NC}"
        exit 1
    fi
fi
