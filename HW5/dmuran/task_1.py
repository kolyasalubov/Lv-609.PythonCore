even_by_two = [value for value in range(1, 11) if value % 2 == 0]
odd_by_three = [value for value in range(1, 11) if value % 3 == 0]
numbers_not_div_by_two_and_three = [value for value in range(1,11) if not (value % 2 == 0 or value % 3 == 0)]
print(f'Even numbers that are divisible by 2 : {even_by_two}')
print(f'Odd numbers that are divisible by 3 : {odd_by_three}')
print(f'Numbers that are not divisible by 2 and 3 : {numbers_not_div_by_two_and_three}')