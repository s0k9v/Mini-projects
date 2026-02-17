import os
import shutil

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Videos": [".mp4", ".mkv", ".flv", ".avi", ".mov"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Data": [".csv", ".json", ".xml"],
    "Others": [],
    "Executable": [".exe", ".bat", ".sh"]   
    }

def organize_files(source_folder):
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()
            category = get_file_category(file_extension)
            category_folder = os.path.join(source_folder, category)

            if not os.path.exists(category_folder):
                os.makedirs(category_folder)
                

            shutil.move(file_path, os.path.join(category_folder, filename))
def get_file_category(file_extension):
    for category, extensions in FILE_CATEGORIES.items():
        if file_extension in extensions:
            return category
    return "Others"

if __name__ == "__main__":
    source_folder = input("Enter the path of the folder to organize: ")
    if os.path.exists(source_folder) and os.path.isdir(source_folder):
        organize_files(source_folder)
        print("Files have been organized successfully.")
    else:
        print("Invalid folder path. Please try again.")