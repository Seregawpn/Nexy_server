import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from integrations.workflow_integrations.streaming_workflow_integration import StreamingWorkflowIntegration


def test_enrich_context_does_not_inject_forced_payment_command():
    workflow = StreamingWorkflowIntegration.__new__(StreamingWorkflowIntegration)

    runtime_memory = workflow._build_runtime_memory_context(
        memory_context=None,
        subscription_context={"status": "paid", "reason": "unlimited_access"},
    )

    assert "YOU MUST EXECUTE COMMAND" not in runtime_memory
    assert "URGENT INSTRUCTION" not in runtime_memory
    assert "Subscription Status: paid" in runtime_memory
