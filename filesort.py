import os
import shutil
from pathlib import Path

# Path to Downloads folder
downloads_path = str(Path.home() / "Downloads")

# File type mappings
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".heic", ".svg", ".HEIC"],
    "Documents": [".doc", ".docx", ".txt", ".odt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Archives": [".zip", ".tar", ".gz", ".bz2", ".rar", ".7z"],
    "Audio": [".mp3", ".wav", ".aac", ".ogg", ".flac"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv"],
    "PDFs": [".pdf"]
}

# Organize files
for file_name in os.listdir(downloads_path):
    file_path = os.path.join(downloads_path, file_name)

    if os.path.isfile(file_path):
        _, ext = os.path.splitext(file_name)
        ext = ext.lower()

        for folder, extensions in file_types.items():
            if ext in extensions:
                target_folder = os.path.join(downloads_path, folder)
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(target_folder, file_name))
                print(f"Moved {file_name} to {folder}/")
                break