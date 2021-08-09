even_num = []
odd_num = []
not_div_num = []

for i in range(1, 11):
    if i % 2 == 0:
        even_num.append(i)
    elif i % 3 == 0:
        not_div_num.append(i)
    else:
        odd_num.append(i)

print(f'\nEven numbers: {even_num}\nOdd numbers: {odd_num}\nNot divisible numbers: {not_div_num}\n')
