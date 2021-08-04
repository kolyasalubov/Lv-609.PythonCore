number = int(input("Enter your number for Fibonacci:"))
result = first = 0
second = 1

while result <= number:
    print(result)
    result = first + second
    first, second = second, result