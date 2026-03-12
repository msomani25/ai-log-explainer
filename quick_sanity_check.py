# quick_sanity_check.py

from main import explain_log_locally
import os

log_folder = "logs"

for f in os.listdir(log_folder):
    file_path = os.path.join(log_folder, f)
    with open(file_path) as file:
        log_text = file.read()
    result = explain_log_locally(log_text)
    print(f"\n--- {f} ---")
    print("Detected Error:", result["error"])
    print("Explanation:", result["explanation"])
    print("Suggested Fix:", result["fix"])