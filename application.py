import os
from latexlibrary import rename_and_copy_files
from latexlibrary import replace_spaces_with_ampersand
from latexlibrary import change_name

def main():
    main_folder = os.path.join(os.getcwd(), "nist_folders")
    target_filename = "finalAnalysisReport.txt"

    rename_and_copy_files(main_folder, target_filename)

    destination_folder = os.path.join(main_folder, f"all_{target_filename.split('.')[0]}")

    for filename in os.listdir(destination_folder):
        if filename.startswith(target_filename.split('.')[0]):
            file_path = os.path.join(destination_folder, filename)
            replace_spaces_with_ampersand(file_path)

    for filename in os.listdir(destination_folder):
        if filename.startswith(target_filename.split('.')[0]) and filename.endswith('modified.txt'):
            file_path = os.path.join(destination_folder, filename)
            change_name(file_path)

if __name__ == "__main__":
    main()