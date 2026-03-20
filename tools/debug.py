import platform
import psutil
import subprocess
import pyfiglet
from colorama import Fore, Style, init
from tools import web_status, calculator, base64_tool, speed_test, port_scanner, temp_nuker, ping_tool, rann_gen, info

def get_system_info():
    # 1. Get Linux Distribution
    try:
        distro_info = platform.freedesktop_os_release()
        distro = f"{distro_info.get('NAME')} {distro_info.get('VERSION_ID')}"
    except Exception:
        distro = platform.system()

    # 2. Get RAM (Total)
    total_ram = round(psutil.virtual_memory().total / (1024**3), 2)

    # 3. Get Graphics (GPU)
    try:
        gpu_raw = subprocess.check_output("lspci | grep -E 'VGA|3D'", shell=True).decode()
        gpu = gpu_raw.split(':')[-1].strip()
    except Exception:
        gpu = "Could not detect GPU"
    
    return distro, total_ram, gpu

def run():
    init(autoreset=True)
    
    # Fetch system specs once when debug starts
    distro, total_ram, gpu = get_system_info()

    while True:
        # Draw Logo
        text = pyfiglet.figlet_format("PyHub")
        print(Fore.BLUE + text)

        # Show Debug Header
        print(Fore.RED + Style.BRIGHT + "DEBUG MODE ACTIVE")
        print(Fore.WHITE + "--- System Specs ---")
        print(f"Distro:   {distro}")
        print(f"RAM:      {total_ram} GB")
        print(f"Graphics: {gpu}")
        print(f"Version:  PyHub v1.4.0")
        print(Fore.WHITE + "--------------------")

        print(Fore.CYAN + "\nSelect a tool (Debug Context):\n")

        print(Fore.YELLOW + "1." + Style.RESET_ALL + " Web Status Checker")
        print(Fore.YELLOW + "2." + Style.RESET_ALL + " Calculator")
        print(Fore.YELLOW + "3." + Style.RESET_ALL + " Base64 Encoder/Decoder")
        print(Fore.YELLOW + "4." + Style.RESET_ALL + " Speed Test")
        print(Fore.YELLOW + "5." + Style.RESET_ALL + " Local Port Scanner")
        print(Fore.YELLOW + "6." + Style.RESET_ALL + " Temp File Nuker")
        print(Fore.YELLOW + "7." + Style.RESET_ALL + " Ping Tool")
        print(Fore.YELLOW + "8." + Style.RESET_ALL + " Random Number Generator")
        print(Fore.YELLOW + "?" + Style.RESET_ALL + " PyHub Wiki")
        print(Fore.RED + "0." + Style.RESET_ALL + " Back to Main Menu")

        choice = input(Fore.GREEN + "\n[DEBUG] Choose an option: ")

        if choice == "1":
            web_status.run()
        elif choice == "2":
            calculator.run()
        elif choice == "3":
            base64_tool.run()
        elif choice == "4":
            speed_test.run()
        elif choice == "5":
            port_scanner.run()
        elif choice == "6":
            temp_nuker.run()
        elif choice == "7":
            ping_tool.run()
        elif choice == "8":
            rann_gen.run()
        elif choice == "?":
            info.run()
        elif choice == "0":
            print(Fore.YELLOW + "\nReturning to standard mode...")
            return # This exits debug.run() and goes back to main.py
        else:
            print(Fore.RED + "Invalid option")

        input(Fore.MAGENTA + "\nPress Enter to return to Debug Menu...")
        print("\n" * 2)