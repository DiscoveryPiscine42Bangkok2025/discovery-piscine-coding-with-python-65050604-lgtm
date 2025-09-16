try:
    number_str = input("Enter a number\n")
    number = int(number_str)
    for i in range(10):
        result = i * number
        print(f"{i} x {number} = {result}")
except ValueError:
    print("Invalid input. Please enter an integer.")
except Exception as e:
    print(f"An error occurred: {e}")