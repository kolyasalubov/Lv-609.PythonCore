number = input('Enter number : ')
product_of_numbers = int(number[0]) * int(number[1]) * int(number[2]) * int(number[3])
print(f'Product of numbers "{number}" = {product_of_numbers}')

reverse_number = number[3] + number[2] + number[1] + number[0]
print(f'Reversed : {reverse_number}')

sorted_number = ''.join(sorted(number))
print(f'Sorted : {sorted_number}')

