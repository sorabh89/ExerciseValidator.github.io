import os
import shutil

SOURCE_DIR = "/Users/shanky/Documents/MyDrive/Takat/Personal/Gym/gym/gifs/merged/"
TARGET_DIR = "/Users/shanky/Documents/MyDrive/Learning/Development/Github/dockerized-takat-app/ExerciseValidator.github.io/assets/images/merged/"

def copy_180_files(source_root, target_root):
    no_180_folders = []

    for current_path, dirs, files in os.walk(source_root):
        # Check files containing _180
        files_180 = [f for f in files if "_180" in f]

        # If no 180 files in this folder, record the folder path
        if not files_180:
            no_180_folders.append(current_path)
            continue

        # Build equivalent target path
        rel_path = os.path.relpath(current_path, source_root)
        target_path = os.path.join(target_root, rel_path)

        # Ensure that target directory exists
        os.makedirs(target_path, exist_ok=True)

        # Copy only the *_180* files
        for filename in files_180:
            src_file = os.path.join(current_path, filename)
            dst_file = os.path.join(target_path, filename)
            shutil.copy2(src_file, dst_file)

    return no_180_folders


if __name__ == "__main__":
    missing_180_folders = copy_180_files(SOURCE_DIR, TARGET_DIR)

    print("Folders without any _180 files:")
    for folder in missing_180_folders:
        print(folder)
