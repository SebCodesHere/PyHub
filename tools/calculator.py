def run():
    expr = input("Enter expression (e.g., 2+3*4): ")
    try:
        result = eval(expr)
        print("Result:", result)
    except:
        print("Invalid expression.")