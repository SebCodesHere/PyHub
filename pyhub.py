#!/usr/bin/env python3
import pyfiglet
from tools import web_status, calculator, base64_tool, speed_test, port_scanner, temp_nuker

def main():
    print(pyfiglet.figlet_format("PyHub"))

    while True:
        print("\n--- PyHub Toolkit ---")
        print("1. Web Status Checker")
        print("2. Calculator")
        print("3. Base64 Encoder/Decoder")
        print("4. Speed Test")
        print("5. Local Port Scanner")
        print("6. Temp File Nuker")
        print("7. Exit")

        choice = input("Choose an option: ")

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
            print("Exiting PyHub...")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()