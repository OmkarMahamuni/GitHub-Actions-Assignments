import sys

message = "CI test failed"
print(message)

if "passed" not in message:
    sys.exit(1)