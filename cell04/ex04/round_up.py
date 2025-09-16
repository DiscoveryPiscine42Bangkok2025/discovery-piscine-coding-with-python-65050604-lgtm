import math

try:
    num_str = input("Give me a number: ")
    number = float(num_str)
    rounded_up = math.ceil(number)
    print(int(rounded_up))
except ValueError:
    print("Error: Please enter a valid number.")