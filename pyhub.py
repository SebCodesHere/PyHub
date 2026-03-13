#!/usr/bin/env python3
import os
import pyfiglet
from colorama import init, Fore, Style
from tools import web_status, calculator, base64_tool, speed_test, port_scanner, temp_nuker

# Initialize colorama
init(autoreset=True)

# Print colored ASCII logo
logo = pyfiglet.figlet_format("PyHub")
print(Fore.BLUE + logo)
print(Fore.WHITE + Style.BRIGHT + "Your Python CLI Toolkit\n")

def main():
    try:
        while True:
            # Colored menu
            print(Fore.CYAN + "--- PyHub Toolkit ---")
            print(Fore.GREEN + "1. Web Status Checker")
            print(Fore.YELLOW + "2. Calculator")
            print(Fore.MAGENTA + "3. Base64 Encoder/Decoder")
            print(Fore.BLUE + "4. Speed Test")
            print(Fore.RED + "5. Local Port Scanner")
            print(Fore.LIGHTBLACK_EX + "6. Temp File Nuker")
            print(Fore.WHITE + "7. Exit\n")

            choice = input(Fore.CYAN + "Choose an option: " + Fore.WHITE)

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
                print(Fore.CYAN + "Exiting PyHub...")
                break
            else:
                print(Fore.RED + "Invalid option!")

    except KeyboardInterrupt:
        print(Fore.CYAN + "\nExiting PyHub...")

if __name__ == "__main__":
    main()