import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from integrations.workflow_integrations.streaming_workflow_integration import StreamingWorkflowIntegration


def test_enrich_context_does_not_inject_forced_payment_command():
    workflow = StreamingWorkflowIntegration.__new__(StreamingWorkflowIntegration)

    enriched = workflow._enrich_context(
        text="how are you today",
        memory_context=None,
        subscription_context={"status": "paid", "reason": "unlimited_access"},
    )

    assert "YOU MUST EXECUTE COMMAND" not in enriched
    assert "URGENT INSTRUCTION" not in enriched
    assert "Subscription Status: paid" in enriched

