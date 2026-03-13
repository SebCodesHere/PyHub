import socket

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
    host = input("Enter host/IP (example: 127.0.0.1): ")
    port_range = input("Enter port range (example: 20-100): ")

    try:
        start, end = map(int, port_range.split("-"))
    except:
        print("Invalid range format.")
        return

    print(f"\nScanning {host} from port {start} to {end}...\n")

    for port in range(start, end + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((host, port))

        if result == 0:
            service = COMMON_PORTS.get(port, "Unknown")
            print(f"[OPEN ] Port {port} - {service}")
        else:
            print(f"[CLOSED] Port {port}")

        sock.close()

    print("\nScan complete.")