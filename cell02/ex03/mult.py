num1_str = input("Enter the first number: ")
num1 = int(num1_str)

num2_str = input("Enter the second number: ")
num2 = int(num2_str)

result = num1 * num2

print(f"{num1} x {num2} = {result}")

if result < 0:
    print("The result is negative.")
elif result > 0:
    print("The result is positive.")
else:
    print("The result is both positive and negative.")