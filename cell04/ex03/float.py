try:
    num_str = input("Give me a number: ")
    number = float(num_str)

    if number.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")

except ValueError:
    print("Error: That is not a valid number.")