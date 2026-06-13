import os
import platform
import shutil
from pathlib import Path

# Determine the platform (Windows, macOS, or Linux)
current_platform = platform.system()

# Set the downloads path depending on the platform
if current_platform == "Darwin":  # macOS
    downloads_path = str(Path.home() / "Downloads")
elif current_platform == "Windows":
    downloads_path = str(Path.home() / "Downloads")
elif current_platform == "Linux":
    downloads_path = str(Path.home() / "Downloads")
else:
    raise Exception("Unsupported OS")

# Now, you can use the `downloads_path` variable for file sorting
print(f"Downloads path is set to: {downloads_path}")

# File type mappings
file_types = {
    "Images": [
        ".jpg",
        ".jpeg",
        ".png",
        ".gif",
        ".bmp",
        ".webp",
        ".heic",
        ".svg",
        ".HEIC",
    ],
    "Documents": [".doc", ".docx", ".txt", ".odt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Archives": [".zip", ".tar", ".gz", ".bz2", ".rar", ".7z"],
    "Audio": [".mp3", ".wav", ".aac", ".ogg", ".flac"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv"],
    "PDFs": [".pdf"],
    "App": [".dmg", ".exe"],
    "OS": [".iso"],
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
