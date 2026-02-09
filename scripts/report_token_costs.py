#!/usr/bin/env python3
import sys
import os
import argparse
from typing import Dict, Any

# Add server path
current_dir = os.getcwd()
server_dir = os.path.join(current_dir, 'server', 'server')
if server_dir not in sys.path:
    sys.path.insert(0, server_dir)

try:
    from dotenv import load_dotenv
    # Load env from server/config.env
    env_path = os.path.join(current_dir, 'server', 'config.env')
    if os.path.exists(env_path):
        load_dotenv(env_path)
    
    from modules.database.repository.token_usage_repository import TokenUsageRepository
except ImportError as e:
    print(f"Error importing repository: {e}")
    sys.exit(1)

# Pricing per 1M tokens (Approximate)
# Source: Google Cloud Vertex AI Pricing (as of late 2024/early 2025)
PRICING = {
    # Flash models
    "gemini-2.0-flash":       {"input": 0.10, "output": 0.40},
    "gemini-2.0-flash-exp":   {"input": 0.10, "output": 0.40},
    "gemini-1.5-flash":       {"input": 0.075, "output": 0.30},
    "gemini-1.5-flash-8b":    {"input": 0.0375, "output": 0.15},
    "gemini-3-flash-preview": {"input": 0.10, "output": 0.40}, # Assuming similar to 2.0 Flash
    
    # Pro models
    "gemini-1.5-pro":         {"input": 3.50, "output": 10.50},
    "gemini-1.5-pro-002":     {"input": 3.50, "output": 10.50},
    
    # Default fallback
    "default":                {"input": 0.10, "output": 0.40}
}

def calculate_cost(model_name: str, input_tokens: int, output_tokens: int) -> float:
    """Calculate cost in USD."""
    model_key = model_name if model_name in PRICING else "default"
    prices = PRICING.get(model_key, PRICING["default"])
    
    input_cost = (input_tokens / 1_000_000) * prices["input"]
    output_cost = (output_tokens / 1_000_000) * prices["output"]
    
    return input_cost + output_cost

def format_currency(value: float) -> str:
    return f"${value:.4f}"

def main():
    parser = argparse.ArgumentParser(description="Token Usage Cost Report")
    parser.add_argument('--period', choices=['daily', 'weekly', 'monthly', 'all'], default='daily', help='Time period for stats')
    args = parser.parse_args()

    print(f"Loading Token Usage Report (Period: {args.period})...\n")
    
    repo = TokenUsageRepository()
    if not repo.db_url:
        print("Error: DATABASE_URL not set.")
        sys.exit(1)
        
    stats = repo.get_global_stats(period=args.period)
    
    if not stats:
        print("No usage data found for this period.")
        return

    # Header
    print(f"{'User ID':<15} | {'Model':<25} | {'Requests':<10} | {'Input':<10} | {'Output':<10} | {'Cost (USD)':<12}")
    print("-" * 95)
    
    total_cost = 0.0
    
    for row in stats:
        hw_id = row['hardware_id']
        short_id = hw_id[:12] + "..." if len(hw_id) > 15 else hw_id
        model = row['model_name'] or "unknown"
        requests = row['request_count']
        inputs = float(row['input_tokens'] or 0)
        outputs = float(row['output_tokens'] or 0)
        
        cost = calculate_cost(model, inputs, outputs)
        total_cost += cost
        
        print(f"{short_id:<15} | {model:<25} | {requests:<10} | {int(inputs):<10} | {int(outputs):<10} | {format_currency(cost):<12}")

    print("-" * 95)
    print(f"{'TOTAL':<56} | {format_currency(total_cost):<12}")

if __name__ == "__main__":
    main()
