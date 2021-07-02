factorial = int(input("Enter a number : "))
result = 1
if factorial == 0:
    print(f'{factorial}! = {result}')
else:
    for value in range(1, factorial+1):
        result *= value
    print(f'{factorial}! = {result}')
