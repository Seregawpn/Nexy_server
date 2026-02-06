# Summary
- Исправил loop-mismatch для server welcome audio: вызовы gRPC теперь проксируются в loop, где создан channel.
- Зафиксировал loop канала в ConnectionManager как источник истины.

# Changes
- Stored gRPC channel loop in ConnectionManager and exposed getter.
- Wrapped `GrpcClient.generate_welcome_audio()` to run in channel loop when called from другой loop.

# Files
- modules/grpc_client/core/connection_manager.py
- modules/grpc_client/core/grpc_client.py

# Tests
- Not run (not requested).
