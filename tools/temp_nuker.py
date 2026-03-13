import os
import tempfile
import shutil

def run():
    temp_dir = tempfile.gettempdir()
    confirm = input(f"This will delete all temp files in {temp_dir}. Continue? (y/n): ")
    if confirm.lower() == 'y':
        try:
            shutil.rmtree(temp_dir)
            os.makedirs(temp_dir)
            print("Temp files nuked!")
        except Exception as e:
            print("Failed:", e)
    else:
        print("Cancelled.")