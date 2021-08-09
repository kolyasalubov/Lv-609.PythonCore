n = int(input('Enter number: '))
factorial = 1
if n >= 0:
    for fact in range(1, n+1):
        factorial *= fact
    print(factorial)
else:
    print("Invalid number")
