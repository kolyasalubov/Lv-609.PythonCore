numbers_div_by_2 = []
numbers_div_by_3 = []
numbers_not_div_by_2and3 = []
for i in range(11):
    if i % 2 == 0:
        numbers_div_by_2.append(i)
    elif i % 3 == 0:
        numbers_div_by_3.append(i)
    else:
        numbers_not_div_by_2and3.append(i)
print(f'Numbers that are divisible by 2: {numbers_div_by_2}.')
print(f'Numbers that are divisible by 3: {numbers_div_by_3}.')
print(f'Numbers that are not divisible by 2 and 3: {numbers_not_div_by_2and3}.')
