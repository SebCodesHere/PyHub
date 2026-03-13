import subprocess
import platform

def run():
    host = input("Enter host (example: google.com): ")

    system = platform.system().lower()

    if system == "windows":
        cmd = ["ping", "-n", "4", host]
    else:
        cmd = ["ping", "-c", "4", host]

    print("\nPinging...\n")

    try:
        subprocess.run(cmd)
    except Exception as e:
        print("Error running ping:", e)