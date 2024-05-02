import os
import shutil

def main_func(output_dir, dest_dir):
    file_paths = read_dir(output_dir)
    os.makedirs(os.path.dirname(dest_dir), exist_ok=True)
    for file_path in file_paths:
        parts = file_path.split(".")
        ext_path = "".join(parts[1:])
        file_name = os.path.basename(file_path)
        final_dest_dir = os.path.join(dest_dir, ext_path)
        os.makedirs(final_dest_dir, exist_ok=True)
        #destination_file = os.path.join(final_dest_dir, file_name)
        shutil.copy(file_path, final_dest_dir)


def read_dir(path):
    files = []
    for item in os.listdir(path):
        full_item_path = os.path.join(path, item)
        print(full_item_path)
        if os.path.isdir(full_item_path):
            read_dir(full_item_path)
        elif os.path.isfile(full_item_path):
            files.append(full_item_path)
        else:
            print(f"{full_item_path} is neither a file nor a directory")
    return files        

main_func("/Users/lskorokhod/VsCodeProjects/DataAlgorithms/goit-algo-hw-02", "/Users/lskorokhod/VsCodeProjects/DataAlgorithms/test")

                 