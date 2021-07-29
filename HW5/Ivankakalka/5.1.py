even_numbers = []
odd_numbers = []
numbers_not_divisible_2_3 = []
for x in range (1,11):
    if x % 2 == 0:
        even_numbers.append(x)
    elif x % 3 == 0:
        odd_numbers.append(x)
    else:
        numbers_not_divisible_2_3.append(x)

print ('Even numbers that are devisible by 2: {}'.format (even_numbers))
print ('Odd numbers that are devisible by 3: {}'.format (odd_numbers))
print ('Numbers that are not devisible by 2 and 3: {}'.format (numbers_not_divisible_2_3))
