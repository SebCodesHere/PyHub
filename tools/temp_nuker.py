import os
import tempfile

def run():
    temp_dir = tempfile.gettempdir()
    print(f"Cleaning temp files in: {temp_dir}")

    confirm = input("Continue? (y/n): ")
    if confirm.lower() != "y":
        print("Cancelled.")
        return

    deleted = 0
    failed = 0

    for item in os.listdir(temp_dir):
        path = os.path.join(temp_dir, item)

        try:
            if os.path.isfile(path) or os.path.islink(path):
                os.remove(path)
                deleted += 1
            elif os.path.isdir(path):
                # skip directories to avoid permission issues
                continue
        except Exception:
            failed += 1

    print(f"\nDeleted files: {deleted}")
    print(f"Skipped/failed: {failed}")