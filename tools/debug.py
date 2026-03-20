import platform
import psutil
import subprocess
import pyfiglet
from colorama import Fore, Style, init
from tools import web_status, calculator, base64_tool, speed_test, port_scanner, temp_nuker, ping_tool, rann_gen, info

def run():

    def get_system_info():
        # 1. Get Linux Distribution
        # platform.freedesktop_os_release() is the modern way (Python 3.10+)
        try:
            distro_info = platform.freedesktop_os_release()
            distro = f"{distro_info.get('NAME')} {distro_info.get('VERSION_ID')}"
        except AttributeError:
            distro = platform.system()

        # 2. Get RAM (Total)
        # We divide by (1024**3) to convert bytes to Gigabytes
        total_ram = round(psutil.virtual_memory().total / (1024**3), 2)

        # 3. Get Graphics (GPU)
        # On Linux, the most reliable way is to query the 'lspci' command
        try:
            gpu_raw = subprocess.check_output("lspci | grep -E 'VGA|3D'", shell=True).decode()
            # Clean up the string to show just the relevant hardware part
            gpu = gpu_raw.split(':')[-1].strip()
        except Exception:
            gpu = "Could not detect GPU"


    init(autoreset=True)

    def logo():
        text = pyfiglet.figlet_format("PyHub")
        print(Fore.BLUE + text)

    def menu():
        print(Fore.RED + "Debug mode on!")

        print(f"--- System Specs ---")
        print(f"Distro:   {distro}")
        print(f"RAM:      {total_ram} GB")
        print(f"Graphics: {gpu}")
        print("PyHub v1.4.0")

        print(Fore.CYAN + "Select a tool:\n")

        print(Fore.YELLOW + "1." + Style.RESET_ALL + " Web Status Checker")
        print(Fore.YELLOW + "2." + Style.RESET_ALL + " Calculator")
        print(Fore.YELLOW + "3." + Style.RESET_ALL + " Base64 Encoder/Decoder")
        print(Fore.YELLOW + "4." + Style.RESET_ALL + " Speed Test")
        print(Fore.YELLOW + "5." + Style.RESET_ALL + " Local Port Scanner")
        print(Fore.YELLOW + "6." + Style.RESET_ALL + " Temp File Nuker")
        print(Fore.YELLOW + "7." + Style.RESET_ALL + " Ping Tool")
        print(Fore.YELLOW + "8." + Style.RESET_ALL + " Random Number Generator")
        print(Fore.YELLOW + "?" + Style.RESET_ALL + " PyHub Wiki")
        print(Fore.RED + "0." + Style.RESET_ALL + " Exit")

    def main():
        while True:
            logo()
            menu()

            choice = input(Fore.GREEN + "\nChoose an option: ")

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
                print(Fore.RED + "\nExiting PyHub...")
                break

            else:
                print(Fore.RED + "Invalid option")

            input(Fore.MAGENTA + "\nPress Enter to return to menu...")
            print("\n" * 2)


    if __name__ == "__main__":
        main()