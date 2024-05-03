import os
import shutil

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            print("Incorect src dir")
        except PermissionError as e:
            print(f"Permission error: {e}")
    return inner

@input_error
def copy_files(src_dir, dest_dir = "dist"):
    os.makedirs(os.path.dirname(src_dir), exist_ok=True)
    for item in os.listdir(src_dir):
        full_item_path = os.path.join(src_dir, item)
        if os.path.isdir(full_item_path):
            copy_files(full_item_path, dest_dir)
        elif os.path.isfile(full_item_path):
            parts = item.split(".")
            ext_path = "".join(parts[1:])
            final_dest_dir = os.path.join(dest_dir, ext_path)
            os.makedirs(final_dest_dir, exist_ok=True)
            shutil.copy(full_item_path, final_dest_dir)
            print("copied file " + item + " to dir: " + final_dest_dir)
        else:
            print(f"{full_item_path} is neither a file nor a directory")


copy_files("test_dir/", "test2")