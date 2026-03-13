import base64

def run():
    mode = input("Encode or Decode? (e/d): ").lower()
    text = input("Enter text: ")

    if mode == "e":
        encoded = base64.b64encode(text.encode()).decode()
        print("Encoded:", encoded)

    elif mode == "d":
        try:
            decoded = base64.b64decode(text.encode()).decode()
            print("Decoded:", decoded)
        except:
            print("Invalid Base64 input")

    else:
        print("Invalid option")