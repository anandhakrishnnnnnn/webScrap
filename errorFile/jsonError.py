import json

# Load the error log file
with open("error_logs.json") as f:
    logs = json.load(f)

print("== ERROR LOG ENTRIES ==")
for log in logs:
    if log.get("level") == "ERROR":
        timestamp = log.get("timestamp", "Unknown time")
        message = log.get("message", "No message provided")
        print(f"[{timestamp}] ❌ {message}")