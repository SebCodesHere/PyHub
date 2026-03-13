import speedtest
import sys
import time
import threading
from colorama import Fore, init

init(autoreset=True)


def progress_bar(label, stop_event):
    bar_length = 25
    progress = 0

    while not stop_event.is_set():
        filled = int(progress * bar_length)
        bar = "█" * filled + "-" * (bar_length - filled)

        sys.stdout.write(f"\r{Fore.CYAN}{label}: [{Fore.GREEN}{bar}{Fore.CYAN}]")
        sys.stdout.flush()

        progress += 0.02
        if progress > 1:
            progress = 0

        time.sleep(0.05)

    bar = "█" * bar_length
    sys.stdout.write(f"\r{Fore.CYAN}{label}: [{Fore.GREEN}{bar}{Fore.CYAN}] ✓\n")
    sys.stdout.flush()


def run():
    print(Fore.CYAN + "\nConnection Speed Test\n")

    st = speedtest.Speedtest()

    # Ping test
    stop_event = threading.Event()
    loader = threading.Thread(target=progress_bar, args=("Ping", stop_event))
    loader.start()

    st.get_best_server()
    ping = st.results.ping

    stop_event.set()
    loader.join()

    # Download test
    stop_event = threading.Event()
    loader = threading.Thread(target=progress_bar, args=("Download", stop_event))
    loader.start()

    download = st.download() / 1_000_000

    stop_event.set()
    loader.join()

    # Upload test
    stop_event = threading.Event()
    loader = threading.Thread(target=progress_bar, args=("Upload", stop_event))
    loader.start()

    upload = st.upload() / 1_000_000

    stop_event.set()
    loader.join()

    print(Fore.YELLOW + f"\nPing: {ping:.2f} ms")
    print(Fore.YELLOW + f"Download: {download:.2f} Mbps")
    print(Fore.YELLOW + f"Upload: {upload:.2f} Mbps")