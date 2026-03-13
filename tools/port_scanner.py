import socket

def run():
    host = input("Enter host/IP: ")
    ports = input("Enter ports to scan (e.g., 20-25): ")
    try:
        start, end = map(int, ports.split('-'))
    except:
        print("Invalid port range.")
        return

    print(f"Scanning {host}...")
    for port in range(start, end + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()