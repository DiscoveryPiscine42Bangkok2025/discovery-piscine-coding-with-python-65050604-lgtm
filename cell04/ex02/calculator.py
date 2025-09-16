try:
    num1_str = input("Give me the first number: ")
    num1 = int(num1_str)

    num2_str = input("Give me the second number: ")
    num2 = int(num2_str)

    print("Thank you!")

    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    print(f"{num1} / {num2} = {int(num1 / num2)}")
    print(f"{num1} * {num2} = {num1 * num2}")

except ValueError:
    print("Error: Please enter valid numbers.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")