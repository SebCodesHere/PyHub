from colorama import Fore

def run():
    expr = input("Enter expression: ")
    try:
        result = eval(expr)
        print(Fore.YELLOW + f"Result: {result}")
    except:
        print(Fore.RED + "Invalid expression!")