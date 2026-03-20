import platform
import psutil
import subprocess
import pyfiglet
import os
from colorama import Fore, Style, init
from tools import web_status, calculator, base64_tool, speed_test, port_scanner, temp_nuker, ping_tool, rann_gen, info

def get_system_info():
    # 1. Get OS/Distro Name
    current_os = platform.system()
    if current_os == "Linux":
        try:
            distro_info = platform.freedesktop_os_release()
            os_name = f"{distro_info.get('NAME')} {distro_info.get('VERSION_ID')}"
        except:
            os_name = "Linux (Generic)"
    else:
        os_name = f"Windows {platform.release()}"

    # 2. Get RAM (Works on both OS)
    total_ram = round(psutil.virtual_memory().total / (1024**3), 2)

    # 3. Get GPU (The only part that needs "if/else")
    gpu = "Unknown GPU"
    try:
        if current_os == "Windows":
            # Windows command for GPU
            gpu_raw = subprocess.check_output("wmic path win32_VideoController get name", shell=True).decode()
            gpu = gpu_raw.split('\n')[1].strip()
        else:
            # Linux command for GPU
            gpu_raw = subprocess.check_output("lspci | grep -E 'VGA|3D'", shell=True).decode()
            gpu = gpu_raw.split(':')[-1].strip()
    except:
        gpu = "Could not detect GPU"
    
    return os_name, total_ram, gpu

def run():
    init(autoreset=True)
    os_name, total_ram, gpu = get_system_info()

    while True:
        text = pyfiglet.figlet_format("PyHub")
        print(Fore.BLUE + text)

        print(Fore.RED + Style.BRIGHT + "DEBUG MODE ACTIVE")
        print(Fore.WHITE + "--- System Specs ---")
        print(f"OS/Distro: {os_name}")
        print(f"RAM:       {total_ram} GB")
        print(f"Graphics:  {gpu}")
        print(f"Version:   PyHub v1.4.0")
        print(Fore.WHITE + "--------------------")

        print(Fore.CYAN + "\nSelect a tool:\n")
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

        # Tool mapping
        tools = {
            "1": web_status, "2": calculator, "3": base64_tool,
            "4": speed_test, "5": port_scanner, "6": temp_nuker,
            "7": ping_tool, "8": rann_gen, "?": info
        }

        if choice in tools:
            tools[choice].run()
        elif choice == "0":
            return
        else:
            print(Fore.RED + "Invalid option")

        input(Fore.MAGENTA + "\nPress Enter to return to Debug Menu...")
        print("\n" * 2)