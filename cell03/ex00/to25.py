user_input_str = input("Enter a number less than 25\n")
start_number = int(user_input_str)

if start_number > 25:
    print("Error")
else:
    current_number = start_number
    while current_number <= 25:
        print(f"Inside the loop, my variable is {current_number}")
        current_number += 1