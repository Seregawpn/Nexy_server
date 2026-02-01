Goal: unify session_id to uuid4 strings in input processing so gRPC requests are not dropped.

Scope:
- Generate uuid4 at PTT press/long-press in InputProcessingIntegration.
- Store session_id as Optional[str] and remove float conversions.
- Keep selectors as the single validation guard.

Changes:
- integration/integrations/input_processing_integration.py: uuid4 generation, session_id typing, selectors-based reads.

Verification:
- PTT long press then release; expect voice.recognition_completed with uuid4 and grpc.request_started.
