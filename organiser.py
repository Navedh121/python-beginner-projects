import os
import shutil

folder = input("Enter folder path: ")

file_types = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".pdf": "PDFs",
    ".txt": "Documents",
    ".docx": "Documents",
    ".mp3": "Audio",
    ".mp4": "Videos",
    ".mov": "Videos",
    ".aae": "Others",
}

files = os.listdir(folder)

for file in files:
    name, extension = os.path.splitext(file)
    extension = extension.lower()  # ← fixes capital letters

    if extension in file_types:
        subfolder = file_types[extension]
        destination_folder = os.path.join(folder, subfolder)
        os.makedirs(destination_folder, exist_ok=True)

        source = os.path.join(folder, file)
        destination = os.path.join(folder, subfolder, file)
        shutil.move(source, destination)

        print(f"Moved {file} → {subfolder}/")
    else:
        print(f"Skipped {file} — unknown type")