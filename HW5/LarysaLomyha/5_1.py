even_numbers = [value for value in range(1, 10) if value % 2 == 0]
odd_numbers = [value for value in range(1, 10) if value % 2 != 0 and value % 3 == 0]
simple_numbers = [value for value in range(1, 10) if value % 2 != 0 and value % 3 != 0]
print(even_numbers, odd_numbers, simple_numbers)