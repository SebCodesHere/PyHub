import random

# Colors
blue = "\033[94m"
red = "\033[91m"
reset = "\033[0m"

# Colored questions
digits = int(input(blue + "How many digits should the number have? " + reset))
times = int(input(red + "How many times to print? " + reset))

# Generate numbers
min_num = 10**(digits - 1)
max_num = (10**digits) - 1

for _ in range(times):
    num = random.randint(min_num, max_num)
    print(num)
