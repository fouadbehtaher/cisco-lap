import os
import shutil
categories = {
    "Images": [".png", ".jpg", ".jpeg"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav", ".flac"],
    "Documents": [".pdf", ".docx", ".txt"]
}
def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist.")
        return

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        if os.path.isdir(file_path):
            print(f"Skipping directory: {file_name}")
            continue

        _, extension = os.path.splitext(file_name)
        
        for category, extensions in categories.items():
            if extension.lower() in extensions:
                category_folder = os.path.join(folder_path, category)
                os.makedirs(category_folder, exist_ok=True)
                
                new_file_path = os.path.join(category_folder, file_name)
                try:
                    shutil.move(file_path, new_file_path)
                    print(f"Moved: {file_name} -> {category}/")
                except Exception as e:
                    print(f"Error moving {file_name}: {e}")
                break
        else:
            print(f"No category found for: {file_name}, skipping.")
folder_to_organize = r"C:\Users\Administrator\Downloads"
organize_files(folder_to_organize)
