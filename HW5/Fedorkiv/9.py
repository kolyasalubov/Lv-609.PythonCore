even_nums = []
divisible_by_three = []
divisible_by_two_three = []
for i in range(1, 11):
    if i % 2 == 0:
        even_nums.append(i)
    elif i % 3 == 0:
        divisible_by_three.append(i)
    elif not i % 2 == 0 and not i % 3 == 0:
        divisible_by_two_three.append(i)

print(f'even numbers that are divisible by 2 {even_nums}')
print(f'odd numbers, which are divisible by 3 {divisible_by_three}')
print(f'numbers that are not divisible by 2 and 3 {divisible_by_two_three}')