import os

input_log_file = "logs/system_logs.txt"
output_log_file = "logs/cleaned_logs.txt"

# Ensure input file exists
if not os.path.exists(input_log_file):
    raise FileNotFoundError(f"❌ Log file not found: {input_log_file}")

# Read logs
with open(input_log_file, "r", encoding="utf-8") as f:
    logs = f.readlines()

# Filter logs (only keep error or failure messages)
cleaned_logs = [log.strip() for log in logs if "error" in log.lower() or "failed" in log.lower()]

# Debugging: Print logs found
print(f"🔍 Found {len(cleaned_logs)} relevant logs.")

# Ensure logs are not empty
if not cleaned_logs:
    raise ValueError("❌ No relevant logs found! Log file may be incomplete.")

# Save cleaned logs
with open(output_log_file, "w", encoding="utf-8") as f:
    f.writelines("\n".join(cleaned_logs))

print(f"✅ Cleaned logs saved to {output_log_file}")
