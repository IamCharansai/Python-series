import os

def lock_folder(folder_path):
    try:
        os.system(f'attrib +h +s "{folder_path}"')
        print(" Folder locked successfully.")
    except:
        print(" Error locking the folder.")

def unlock_folder(folder_path):
    try:
        os.system(f'attrib -h -s "{folder_path}"')
        print(" Folder unlocked successfully.")
    except:
        print(" Error unlocking the folder.")

print(" Folder Locker")
print("1. Lock a folder")
print("2. Unlock a folder")

choice = input("Choose an option (1 or 2): ")

folder = input("Enter full folder path: ")

if choice == '1':
    lock_folder(folder)
elif choice == '2':
    unlock_folder(folder)
else:
    print(" Invalid choice")
