"""
Smoke tests for SLO metrics validation.

Checks that SLO thresholds are met:
- tcc_prompt_duration_ms (p95 ≤ 5s)
- permission_flow_success (≥ 99%)
- permission_restart_success_rate (≥ 98%)
- permission_restart_latency_ms (p95 ≤ 15s)

See .cursorrules section 20 for SLO requirements.
"""
import re
from pathlib import Path
from typing import Dict, List, Optional

import pytest


# SLO thresholds
SLO_THRESHOLDS = {
    "tcc_prompt_duration_ms": {"p95_max": 5000, "description": "TCC prompt duration (p95 ≤ 5s)"},
    "permission_flow_success": {"min": 0.99, "description": "Permission flow success rate (≥ 99%)"},
    "permission_restart_success_rate": {"min": 0.98, "description": "Permission restart success rate (≥ 98%)"},
    "permission_restart_latency_ms": {"p95_max": 15000, "description": "Permission restart latency (p95 ≤ 15s)"},
}


def extract_metric_from_logs(log_content: str, metric_name: str) -> Optional[float]:
    """Extract metric value from logs."""
    # Pattern: metric_name=value or metric_name: value
    patterns = [
        rf"{metric_name}=(\d+(?:\.\d+)?)",
        rf"{metric_name}:(\d+(?:\.\d+)?)",
        rf"{metric_name}\s*=\s*(\d+(?:\.\d+)?)",
    ]
    
    for pattern in patterns:
        match = re.search(pattern, log_content, re.IGNORECASE)
        if match:
            try:
                return float(match.group(1))
            except ValueError:
                continue
    
    return None


def extract_percentile_from_logs(log_content: str, metric_name: str, percentile: int = 95) -> Optional[float]:
    """Extract percentile value from logs (e.g., p95)."""
    # Pattern: metric_name p95=value or metric_name_p95=value
    patterns = [
        rf"{metric_name}\s+p{percentile}=(\d+(?:\.\d+)?)",
        rf"{metric_name}_p{percentile}=(\d+(?:\.\d+)?)",
        rf"{metric_name}\s*\(p{percentile}\)\s*=\s*(\d+(?:\.\d+)?)",
    ]
    
    for pattern in patterns:
        match = re.search(pattern, log_content, re.IGNORECASE)
        if match:
            try:
                return float(match.group(1))
            except ValueError:
                continue
    
    return None


@pytest.mark.smoke
class TestSLOSmoke:
    """Smoke tests for SLO metrics."""
    
    @pytest.mark.skip(reason="Requires actual log file - implement when metrics are logged")
    def test_tcc_prompt_duration_p95(self):
        """Test that tcc_prompt_duration_ms p95 ≤ 5s."""
        # TODO: Load actual log file and extract metric
        log_file = Path.home() / "nexy.log"
        
        if not log_file.exists():
            pytest.skip(f"Log file not found: {log_file}")
        
        with open(log_file, "r", encoding="utf-8") as f:
            log_content = f.read()
        
        p95_value = extract_percentile_from_logs(log_content, "tcc_prompt_duration_ms", 95)
        
        if p95_value is None:
            pytest.skip("tcc_prompt_duration_ms p95 not found in logs")
        
        threshold = SLO_THRESHOLDS["tcc_prompt_duration_ms"]["p95_max"]
        assert p95_value <= threshold, \
            f"tcc_prompt_duration_ms p95 ({p95_value}ms) exceeds threshold ({threshold}ms)"
    
    @pytest.mark.skip(reason="Requires actual log file - implement when metrics are logged")
    def test_permission_flow_success_rate(self):
        """Test that permission_flow_success ≥ 99%."""
        log_file = Path.home() / "nexy.log"
        
        if not log_file.exists():
            pytest.skip(f"Log file not found: {log_file}")
        
        with open(log_file, "r", encoding="utf-8") as f:
            log_content = f.read()
        
        success_rate = extract_metric_from_logs(log_content, "permission_flow_success")
        
        if success_rate is None:
            pytest.skip("permission_flow_success not found in logs")
        
        threshold = SLO_THRESHOLDS["permission_flow_success"]["min"]
        assert success_rate >= threshold, \
            f"permission_flow_success ({success_rate:.2%}) below threshold ({threshold:.2%})"
    
    @pytest.mark.skip(reason="Requires actual log file - implement when metrics are logged")
    def test_permission_restart_success_rate(self):
        """Test that permission_restart_success_rate ≥ 98%."""
        log_file = Path.home() / "nexy.log"
        
        if not log_file.exists():
            pytest.skip(f"Log file not found: {log_file}")
        
        with open(log_file, "r", encoding="utf-8") as f:
            log_content = f.read()
        
        success_rate = extract_metric_from_logs(log_content, "permission_restart_success_rate")
        
        if success_rate is None:
            pytest.skip("permission_restart_success_rate not found in logs")
        
        threshold = SLO_THRESHOLDS["permission_restart_success_rate"]["min"]
        assert success_rate >= threshold, \
            f"permission_restart_success_rate ({success_rate:.2%}) below threshold ({threshold:.2%})"
    
    @pytest.mark.skip(reason="Requires actual log file - implement when metrics are logged")
    def test_permission_restart_latency_p95(self):
        """Test that permission_restart_latency_ms p95 ≤ 15s."""
        log_file = Path.home() / "nexy.log"
        
        if not log_file.exists():
            pytest.skip(f"Log file not found: {log_file}")
        
        with open(log_file, "r", encoding="utf-8") as f:
            log_content = f.read()
        
        p95_value = extract_percentile_from_logs(log_content, "permission_restart_latency_ms", 95)
        
        if p95_value is None:
            pytest.skip("permission_restart_latency_ms p95 not found in logs")
        
        threshold = SLO_THRESHOLDS["permission_restart_latency_ms"]["p95_max"]
        assert p95_value <= threshold, \
            f"permission_restart_latency_ms p95 ({p95_value}ms) exceeds threshold ({threshold}ms)"
    
    def test_slo_thresholds_defined(self):
        """Test that all SLO thresholds are defined."""
        assert len(SLO_THRESHOLDS) > 0, "SLO thresholds must be defined"
        
        for metric_name, threshold_info in SLO_THRESHOLDS.items():
            assert "description" in threshold_info, f"Metric '{metric_name}' must have description"
            
            # Check that either min or p95_max is defined
            has_min = "min" in threshold_info
            has_p95_max = "p95_max" in threshold_info
            
            assert has_min or has_p95_max, \
                f"Metric '{metric_name}' must have either 'min' or 'p95_max' threshold"




