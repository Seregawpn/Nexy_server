import sys

print(f"sys.frozen: {getattr(sys, 'frozen', 'NOT_SET')}")
print(f"sys.executable: {sys.executable}")
