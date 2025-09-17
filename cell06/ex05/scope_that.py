def add_one(number):
  number = number + 1
  print(f"Inside the method, the value is: {number}")

my_variable = 42

print(f"Before calling the method, the value is: {my_variable}")

add_one(my_variable)

print(f"After calling the method, the value is: {my_variable}")