original_array = [2, 8, 9, 48, 8, 22, -12, 2]

processed_list = [num + 2 for num in original_array if num > 5]

unique_numbers_set = set(processed_list)

print(original_array)
print(unique_numbers_set)