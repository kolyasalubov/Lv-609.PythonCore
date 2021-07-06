even = []
odd = []
not_div = []

for i in range(1,11):
    if i%2 == 0 :
        even.append(i)
    elif i%2 and i%3 != 0:
        not_div.append(i)
    else:
        odd.append(i)

print(f'\nEven: {even}\nOdd: {odd}\nNot divisible: {not_div}\n')
