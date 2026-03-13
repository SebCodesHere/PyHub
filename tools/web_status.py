import requests

def run():
    url = input("Enter website URL: ")
    if not url.startswith("http"):
        url = "http://" + url
    try:
        r = requests.get(url)
        print(f"{url} is online! Status Code: {r.status_code}")
    except Exception as e:
        print(f"Cannot reach {url}. Error: {e}")