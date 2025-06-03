import os

WEBHOOK_DIR = "webhook_data"

for filename in os.listdir(WEBHOOK_DIR):
    file_path = os.path.join(WEBHOOK_DIR, filename)
    if os.path.isfile(file_path) and os.path.getsize(file_path) == 0:
        print(f"Deleting empty file: {filename}")
        os.remove(file_path)
