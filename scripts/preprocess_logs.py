import re
import os

def clean_log(log_file, output_file):
    cleaned_lines = []

    with open(log_file, "r", encoding="utf-8") as f:
        for line in f:
            # Remove timestamps (e.g., "Mar 30 08:18:45")
            line = re.sub(r"\w{3} \d{1,2} \d{2}:\d{2}:\d{2}", "", line)

            # Keep only important log messages
            if "error" in line.lower() or "failed" in line.lower() or "warning" in line.lower():
                cleaned_lines.append(line.strip())

    with open(output_file, "w", encoding="utf-8") as f:
        for line in cleaned_lines:
            f.write(line + "\n")

    print(f"✅ Cleaned log saved to {output_file}")

# Run the script
log_file = "logs/system_logs.txt"  # Path to raw log
output_file = "logs/cleaned_logs.txt"  # Output cleaned log

if os.path.exists(log_file):
    clean_log(log_file, output_file)
else:
    print(f"❌ Log file {log_file} not found.")
