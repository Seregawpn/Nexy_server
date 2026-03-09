from pathlib import Path
import sys

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from utils.metrics_collector import MetricsCollector


def test_normalize_full_grpc_method_for_request_and_decision() -> None:
    collector = MetricsCollector()

    collector.record_request("/streaming.StreamingService/StreamAudio", 123.0, is_error=False)
    collector.record_decision("/streaming.StreamingService/StreamAudio", "complete")

    snapshot = collector.get_snapshot()

    assert "StreamAudio" in snapshot.total_requests
    assert "/streaming.StreamingService/StreamAudio" not in snapshot.total_requests
    assert snapshot.total_requests["StreamAudio"] == 1
    assert snapshot.decision_rate["StreamAudio"]["complete"] == 1


def test_keep_short_method_as_is() -> None:
    collector = MetricsCollector()

    collector.record_request("GenerateWelcomeAudio", 77.0, is_error=False)
    snapshot = collector.get_snapshot()

    assert snapshot.total_requests["GenerateWelcomeAudio"] == 1
