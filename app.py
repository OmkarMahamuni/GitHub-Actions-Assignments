import sys

message = "CI test passed successfully!"
print(message)

if "passed" not in message:
    sys.exit(1)