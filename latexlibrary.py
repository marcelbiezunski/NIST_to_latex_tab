def rename_and_copy_files(main_folder, target_filename):
    
    import os
    import shutil

    try:
        if not os.path.exists(main_folder):
            print("Folder doesnt exist.")
            return

        file_name_without_extension, _ = os.path.splitext(target_filename)
        destination_folder = os.path.join(main_folder, f"all_{file_name_without_extension}")
        os.makedirs(destination_folder, exist_ok=True)

        counter = 1

        new_files = []

        for root, dirs, files in os.walk(main_folder):
            for file in files:
                if file == target_filename:
                    source_path = os.path.join(root, file)

                    file_name, file_extension = os.path.splitext(file)

                    new_name = f"{file_name}_{counter}{file_extension}"
                    destination_path = os.path.join(destination_folder, new_name)

                    shutil.copy(source_path, destination_path)
                    print(f"Copied: {source_path} -> {destination_path}")

                    new_files.append(destination_path)

                    counter += 1

        print(f"All files named {target_filename} has been copied.")

    except Exception as e:
        print(f"Error: {e}")


def replace_spaces_with_ampersand(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.readlines()

        import re
        modified_content = [re.sub(r'\s+', ' & ', line.strip()) + '\\\\ \\hline' for line in content]

        new_file_path = file_path.replace('.txt', '_modified.txt')
        with open(new_file_path, 'w', encoding='utf-8') as file:
            file.write('\n'.join(modified_content))

        print(f"The changed content has been saved to the file: {new_file_path}")
    except FileNotFoundError:
        print("File not found. Make sure you have specified the correct path.")
    except Exception as e:
        print(f"Error: {e}")


def change_name(file_in):
    import re

    slownik = {
        'Frequency': 'Częstości pojedynczych bitów',
        'BlockFrequency': 'Blokowy test częstości',
        'CumulativeSums': 'Skumulowanych sum*',
        'Runs': 'Sekwencji',
        'LongestRun': 'Najdłuższej sekwencji w bloku',
        'Rank': 'Stopnia macierzy binarnej',
        'FFT': 'Spektralny DFT',
        'NonOverlappingTemplate': 'Dopasowania nienakładających na siebie wzorców*',
        'OverlappingTemplate': 'Dopasowania nakładających na siebie wzorców',
        'ApproximateEntropy': 'Przybliżonej entropii',
        'Universal': 'Uniwersalny Maurera',
        'RandomExcursions': 'Losowych wędrówek*',
        'RandomExcursionsVariant': 'Zmienności losowych wędrówek*',
        'Serial': 'Seryjny*',
        'LinearComplexity': 'Złożoności liniowej',
    }

    try:
        with open(file_in, 'r', encoding='utf-8') as f_in:
            lines = f_in.readlines()

        modified_lines = []
        for line in lines:
            modified_line = line.strip()
            for old_name, new_name in slownik.items():
                if old_name != '.':  
                    
                    pattern = r"&\s*" + re.escape(old_name) + r"\b"
                    match = re.search(pattern, modified_line)
                    if match:
                        
                        modified_line = re.sub(pattern, '', modified_line).strip()
                        
                        modified_line = f"{new_name} & {modified_line}"
                        break  

            modified_line = modified_line.replace('.', ',')

            modified_lines.append(modified_line)

        file_out = file_in.replace('_modified.txt', '_modified2.txt')
        with open(file_out, 'w', encoding='utf-8') as f_out:
            f_out.write('\n'.join(modified_lines))

        print(f"The changed content has been saved to the file: {file_out}")
    except FileNotFoundError:
        print("File not found. Make sure you have specified the correct path.")
    except Exception as e:
        print(f"Error: {e}")

