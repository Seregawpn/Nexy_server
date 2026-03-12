-- Token Usage Tracking Migration
-- Adds table for detailed token usage tracking per user/source

BEGIN;

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

-- Optimization indexes for queries
CREATE INDEX IF NOT EXISTS idx_token_usage_hardware_id ON token_usage(hardware_id);
CREATE INDEX IF NOT EXISTS idx_token_usage_created_at ON token_usage(created_at);
CREATE INDEX IF NOT EXISTS idx_token_usage_source ON token_usage(source);

COMMIT;
