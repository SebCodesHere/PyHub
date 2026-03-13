import os
import shutil
import tempfile
from colorama import Fore

def run():
    temp_dir = tempfile.gettempdir()
    print(Fore.CYAN + f"Cleaning temporary files in: {temp_dir}")

    try:
        for filename in os.listdir(temp_dir):
            file_path = os.path.join(temp_dir, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(Fore.RED + f"Failed to delete {file_path}. Reason: {e}")

        print(Fore.GREEN + "Temporary files cleaned successfully!")
    except Exception as e:
        print(Fore.RED + f"Error cleaning temp files: {e}")