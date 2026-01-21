-- =============================================================================
-- СХЕМА БАЗЫ ДАННЫХ ДЛЯ NEXY VOICE ASSISTANT
-- =============================================================================
-- Создание всех необходимых таблиц для работы сервера
-- Дата создания: 28 ноября 2025
-- =============================================================================

-- Включаем расширение для UUID
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- =============================================================================
-- ТАБЛИЦА: users (Пользователи)
-- =============================================================================
CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    hardware_id_hash VARCHAR(64) UNIQUE NOT NULL,
    metadata JSONB DEFAULT '{}',
    short_term_memory TEXT,
    long_term_memory TEXT,
    memory_updated_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Индексы для users
CREATE INDEX IF NOT EXISTS idx_users_hardware_id_hash ON users(hardware_id_hash);
CREATE INDEX IF NOT EXISTS idx_users_created_at ON users(created_at);

-- =============================================================================
-- ТАБЛИЦА: sessions (Сессии пользователей)
-- =============================================================================
CREATE TABLE IF NOT EXISTS sessions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    status VARCHAR(20) DEFAULT 'active' CHECK (status IN ('active', 'ended', 'paused')),
    metadata JSONB DEFAULT '{}',
    start_time TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    end_time TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Индексы для sessions
CREATE INDEX IF NOT EXISTS idx_sessions_user_id ON sessions(user_id);
CREATE INDEX IF NOT EXISTS idx_sessions_status ON sessions(status);
CREATE INDEX IF NOT EXISTS idx_sessions_start_time ON sessions(start_time);
CREATE INDEX IF NOT EXISTS idx_sessions_created_at ON sessions(created_at);

-- =============================================================================
-- ТАБЛИЦА: commands (Команды пользователей)
-- =============================================================================
CREATE TABLE IF NOT EXISTS commands (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    session_id UUID NOT NULL REFERENCES sessions(id) ON DELETE CASCADE,
    prompt TEXT NOT NULL,
    language VARCHAR(10) DEFAULT 'en',
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Индексы для commands
CREATE INDEX IF NOT EXISTS idx_commands_session_id ON commands(session_id);
CREATE INDEX IF NOT EXISTS idx_commands_created_at ON commands(created_at);
CREATE INDEX IF NOT EXISTS idx_commands_language ON commands(language);

-- =============================================================================
-- ТАБЛИЦА: llm_answers (Ответы LLM на команды)
-- =============================================================================
CREATE TABLE IF NOT EXISTS llm_answers (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    command_id UUID NOT NULL REFERENCES commands(id) ON DELETE CASCADE,
    prompt TEXT NOT NULL,
    response TEXT NOT NULL,
    model_info JSONB DEFAULT '{}',
    performance_metrics JSONB DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Индексы для llm_answers
CREATE INDEX IF NOT EXISTS idx_llm_answers_command_id ON llm_answers(command_id);
CREATE INDEX IF NOT EXISTS idx_llm_answers_created_at ON llm_answers(created_at);

-- =============================================================================
-- ТАБЛИЦА: screenshots (Скриншоты сессий)
-- =============================================================================
CREATE TABLE IF NOT EXISTS screenshots (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    session_id UUID NOT NULL REFERENCES sessions(id) ON DELETE CASCADE,
    file_path VARCHAR(512),
    file_url VARCHAR(512),
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Индексы для screenshots
CREATE INDEX IF NOT EXISTS idx_screenshots_session_id ON screenshots(session_id);
CREATE INDEX IF NOT EXISTS idx_screenshots_created_at ON screenshots(created_at);

-- =============================================================================
-- ТАБЛИЦА: performance_metrics (Метрики производительности)
-- =============================================================================
CREATE TABLE IF NOT EXISTS performance_metrics (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    session_id UUID NOT NULL REFERENCES sessions(id) ON DELETE CASCADE,
    metric_type VARCHAR(50) NOT NULL,
    metric_value JSONB NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Индексы для performance_metrics
CREATE INDEX IF NOT EXISTS idx_performance_metrics_session_id ON performance_metrics(session_id);
CREATE INDEX IF NOT EXISTS idx_performance_metrics_type ON performance_metrics(metric_type);
CREATE INDEX IF NOT EXISTS idx_performance_metrics_created_at ON performance_metrics(created_at);

-- =============================================================================
-- ТАБЛИЦА: short_term_memory (Краткосрочная память)
-- =============================================================================
CREATE TABLE IF NOT EXISTS short_term_memory (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    hardware_id_hash VARCHAR(64) NOT NULL,
    memory TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP WITH TIME ZONE
);

-- Индексы для short_term_memory
CREATE INDEX IF NOT EXISTS idx_short_term_memory_hardware_id ON short_term_memory(hardware_id_hash);
CREATE INDEX IF NOT EXISTS idx_short_term_memory_expires_at ON short_term_memory(expires_at);
CREATE INDEX IF NOT EXISTS idx_short_term_memory_created_at ON short_term_memory(created_at);

-- =============================================================================
-- ТАБЛИЦА: long_term_memory (Долгосрочная память)
-- =============================================================================
CREATE TABLE IF NOT EXISTS long_term_memory (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    hardware_id_hash VARCHAR(64) NOT NULL,
    memory TEXT NOT NULL,
    importance_score FLOAT DEFAULT 0.0,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Индексы для long_term_memory
CREATE INDEX IF NOT EXISTS idx_long_term_memory_hardware_id ON long_term_memory(hardware_id_hash);
CREATE INDEX IF NOT EXISTS idx_long_term_memory_importance ON long_term_memory(importance_score DESC);
CREATE INDEX IF NOT EXISTS idx_long_term_memory_created_at ON long_term_memory(created_at);

-- =============================================================================
-- ФУНКЦИИ ДЛЯ АВТОМАТИЧЕСКОГО ОБНОВЛЕНИЯ updated_at
-- =============================================================================

-- Функция для автоматического обновления updated_at
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Триггеры для автоматического обновления updated_at
CREATE TRIGGER update_users_updated_at
    BEFORE UPDATE ON users
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_sessions_updated_at
    BEFORE UPDATE ON sessions
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_long_term_memory_updated_at
    BEFORE UPDATE ON long_term_memory
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

-- =============================================================================
-- ФУНКЦИИ ДЛЯ ОЧИСТКИ И СТАТИСТИКИ
-- =============================================================================

-- Функция очистки устаревшей краткосрочной памяти
CREATE OR REPLACE FUNCTION cleanup_expired_short_term_memory(hours_to_keep INTEGER DEFAULT 24)
RETURNS INTEGER AS $$
DECLARE
    deleted_count INTEGER;
BEGIN
    DELETE FROM short_term_memory
    WHERE expires_at < CURRENT_TIMESTAMP - (hours_to_keep || ' hours')::INTERVAL
       OR (expires_at IS NULL AND created_at < CURRENT_TIMESTAMP - (hours_to_keep || ' hours')::INTERVAL);
    
    GET DIAGNOSTICS deleted_count = ROW_COUNT;
    RETURN deleted_count;
END;
$$ LANGUAGE plpgsql;

-- Функция получения статистики памяти
CREATE OR REPLACE FUNCTION get_memory_stats()
RETURNS TABLE (
    total_short_term_records BIGINT,
    total_long_term_records BIGINT,
    total_users_with_memory BIGINT,
    avg_short_term_size NUMERIC,
    avg_long_term_size NUMERIC
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        (SELECT COUNT(*) FROM short_term_memory)::BIGINT,
        (SELECT COUNT(*) FROM long_term_memory)::BIGINT,
        (SELECT COUNT(DISTINCT hardware_id_hash) FROM (
            SELECT hardware_id_hash FROM short_term_memory
            UNION
            SELECT hardware_id_hash FROM long_term_memory
        ) AS combined)::BIGINT,
        (SELECT COALESCE(AVG(LENGTH(memory)), 0) FROM short_term_memory)::NUMERIC,
        (SELECT COALESCE(AVG(LENGTH(memory)), 0) FROM long_term_memory)::NUMERIC;
END;
$$ LANGUAGE plpgsql;

-- =============================================================================
-- ПРАВА ДОСТУПА
-- =============================================================================

-- Даем права пользователю базы данных
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO voice_assistant_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO voice_assistant_user;
GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA public TO voice_assistant_user;

-- =============================================================================
-- ЗАВЕРШЕНИЕ
-- =============================================================================

-- Выводим информацию о созданных таблицах
DO $$
DECLARE
    table_count INTEGER;
BEGIN
    SELECT COUNT(*) INTO table_count
    FROM information_schema.tables
    WHERE table_schema = 'public'
      AND table_name IN ('users', 'sessions', 'commands', 'llm_answers', 'screenshots', 'performance_metrics', 'short_term_memory', 'long_term_memory');
    
    RAISE NOTICE '✅ Схема базы данных инициализирована: создано % таблиц', table_count;
END $$;







