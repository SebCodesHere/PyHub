import requests
from colorama import Fore

def run():
    url = input("Enter website URL: ")
    try:
        r = requests.get("http://" + url)
        print(Fore.GREEN + f"{url} is online! Status Code: {r.status_code}")
    except:
        print(Fore.RED + f"{url} is offline or unreachable.")