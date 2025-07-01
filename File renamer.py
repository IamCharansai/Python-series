import os

folder_path = input("Enter the path of the folder: ")
file_prefix = input("Enter the new file name prefix (e.g., photo): ")

try:
    files = os.listdir(folder_path)
    files.sort()
    count = 1

    for file_name in files:
        file_path = os.path.join(folder_path, file_name)

        if os.path.isfile(file_path):
            ext = os.path.splitext(file_name)[1]
            new_name = f"{file_prefix}_{count}{ext}"
            new_path = os.path.join(folder_path, new_name)
            os.rename(file_path, new_path)
            print(f" Renamed: {file_name} → {new_name}")
            count += 1

    print("\n All files renamed successfully!")
except Exception as e:
    print(f" Error: {e}")
