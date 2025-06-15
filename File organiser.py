import os
import shutil

def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print(" Folder does not exist!")
        return

    # Define file type categories
    file_types = {
        "Images": [".png", ".jpg", ".jpeg", ".gif"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Videos": [".mp4", ".mkv", ".mov"],
        "Audio": [".mp3", ".wav"],
        "Archives": [".zip", ".rar"],
        "Code": [".py", ".html", ".css", ".js"]
    }

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1]
            moved = False
            for category, extensions in file_types.items():
                if ext.lower() in extensions:
                    target_folder = os.path.join(folder_path, category)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_folder, file))
                    moved = True
                    break
            if not moved:
                others_folder = os.path.join(folder_path, "Others")
                os.makedirs(others_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(others_folder, file))

    print(" Files organized successfully!")

#  Run
folder = input("Enter folder path to organize: ")
organize_files(folder)