fib_1 = 0
fib_2 = 1
number = int ( input ("Enter number: "))
for item in range (0,number):
    fib_1, fib_2 = fib_2, fib_1+fib_2
    print(fib_1, end=" ")

