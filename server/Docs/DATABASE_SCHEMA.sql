-- Nexy Server PostgreSQL schema (baseline)
-- This schema matches the tables and functions used by the database module.

BEGIN;

CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY,
    hardware_id_hash TEXT NOT NULL UNIQUE,
    metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
    short_term_memory TEXT,
    long_term_memory TEXT,
    memory_updated_at TIMESTAMPTZ,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS sessions (
    id UUID PRIMARY KEY,
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
    status TEXT NOT NULL DEFAULT 'active',
    start_time TIMESTAMPTZ NOT NULL DEFAULT now(),
    end_time TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS commands (
    id UUID PRIMARY KEY,
    session_id UUID NOT NULL REFERENCES sessions(id) ON DELETE CASCADE,
    prompt TEXT NOT NULL,
    language TEXT NOT NULL DEFAULT 'en',
    metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS llm_answers (
    id UUID PRIMARY KEY,
    command_id UUID NOT NULL REFERENCES commands(id) ON DELETE CASCADE,
    prompt TEXT NOT NULL,
    response TEXT NOT NULL,
    model_info JSONB NOT NULL DEFAULT '{}'::jsonb,
    performance_metrics JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS screenshots (
    id UUID PRIMARY KEY,
    session_id UUID NOT NULL REFERENCES sessions(id) ON DELETE CASCADE,
    file_path TEXT,
    file_url TEXT,
    metadata JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS performance_metrics (
    id UUID PRIMARY KEY,
    session_id UUID NOT NULL REFERENCES sessions(id) ON DELETE CASCADE,
    metric_type TEXT NOT NULL,
    metric_value JSONB NOT NULL DEFAULT '{}'::jsonb,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_sessions_user_id ON sessions(user_id);
CREATE INDEX IF NOT EXISTS idx_commands_session_id ON commands(session_id);
CREATE INDEX IF NOT EXISTS idx_llm_answers_command_id ON llm_answers(command_id);
CREATE INDEX IF NOT EXISTS idx_screenshots_session_id ON screenshots(session_id);
CREATE INDEX IF NOT EXISTS idx_performance_metrics_session_id ON performance_metrics(session_id);
CREATE INDEX IF NOT EXISTS idx_users_memory_updated_at ON users(memory_updated_at);

DROP FUNCTION IF EXISTS cleanup_expired_short_term_memory(INT);
CREATE OR REPLACE FUNCTION cleanup_expired_short_term_memory(hours INT)
RETURNS INT
LANGUAGE plpgsql
AS $$
DECLARE
    affected_rows INT;
BEGIN
    UPDATE users
    SET short_term_memory = NULL
    WHERE short_term_memory IS NOT NULL
      AND memory_updated_at IS NOT NULL
      AND memory_updated_at < (now() - (hours || ' hours')::interval);

    GET DIAGNOSTICS affected_rows = ROW_COUNT;
    RETURN affected_rows;
END;
$$;

DROP FUNCTION IF EXISTS get_memory_stats();
CREATE OR REPLACE FUNCTION get_memory_stats()
RETURNS TABLE (
    total_users BIGINT,
    users_with_memory BIGINT,
    total_short_memory_chars BIGINT,
    total_long_memory_chars BIGINT
)
LANGUAGE sql
AS $$
    SELECT
        COUNT(*) AS total_users,
        COUNT(*) FILTER (WHERE short_term_memory IS NOT NULL OR long_term_memory IS NOT NULL) AS users_with_memory,
        COALESCE(SUM(LENGTH(COALESCE(short_term_memory, ''))), 0) AS total_short_memory_chars,
        COALESCE(SUM(LENGTH(COALESCE(long_term_memory, ''))), 0) AS total_long_memory_chars
    FROM users;
$$;


CREATE TABLE IF NOT EXISTS token_usage (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    hardware_id VARCHAR(255) NOT NULL,
    session_id UUID,
    source VARCHAR(50) NOT NULL,  -- 'main_llm', 'memory_analyzer', 'browser_agent'
    input_tokens INT NOT NULL DEFAULT 0,
    output_tokens INT NOT NULL DEFAULT 0,
    total_tokens INT GENERATED ALWAYS AS (input_tokens + output_tokens) STORED,
    model_name VARCHAR(100),
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_token_usage_hardware_id ON token_usage(hardware_id);
CREATE INDEX IF NOT EXISTS idx_token_usage_created_at ON token_usage(created_at);
CREATE INDEX IF NOT EXISTS idx_token_usage_source ON token_usage(source);

COMMIT;
