import socket
from colorama import Fore

# Common ports and services
COMMON_PORTS = {
    20: "FTP",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP-Alt"
}

def run():
    host = input(Fore.CYAN + "Enter host/IP (example: 127.0.0.1): " + Fore.WHITE)
    port_range = input(Fore.CYAN + "Enter port range (example: 20-100): " + Fore.WHITE)

    try:
        start, end = map(int, port_range.split("-"))
    except:
        print(Fore.RED + "Invalid range format.")
        return

    print(Fore.BLUE + f"\nScanning {host} from port {start} to {end}...\n")

    for port in range(start, end + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((host, port))

        if result == 0:
            service = COMMON_PORTS.get(port, "Unknown")
            print(
                Fore.GREEN + "[OPEN ] "
                + Fore.WHITE + f"Port {port} - "
                + Fore.YELLOW + service
            )
        else:
            print(Fore.RED + f"[CLOSED] Port {port}")

        sock.close()

    print(Fore.BLUE + "\nScan complete.\n")