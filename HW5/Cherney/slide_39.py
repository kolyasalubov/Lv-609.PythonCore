#even = [x for x in range(1, 11) if x%2 == 0]
#odd_divisible_by_3 = [y for y in range(1, 11) if y % 2 != 0 and y % 3 == 0]
#odd_not_divisible_by_3 = [z for z in range(1, 11) if z % 2 != 0 and z % 3 != 0]
#print(f"Even numbers are: {even},\nodd divisible by 3 are: {odd_divisible_by_3},\nodd non divisible by 3 are: {odd_not_divisible_by_3}")

even = []
odd_div_by_3 = []
odd_not_div_by_3 = []
for number in range(1, 11):
    if number % 2 == 0:
        even.append(number)
    elif number % 3 == 0:
        odd_div_by_3.append(number)
    elif number % 3 != 0:
        odd_not_div_by_3.append(number)
print(f"Even numbers are: {even},\nodd divisible by 3 are: {odd_div_by_3},\nodd non divisible by 3 are: {odd_not_div_by_3}")