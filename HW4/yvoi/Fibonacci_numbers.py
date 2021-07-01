number = int(input("Enter last value of Fibonacci numbers: "))
fib = first = 0
second = 1

while fib <= number:
    print(fib)
    fib = first + second
    first, second = second, fib


"""-----RESULT-----
Enter last value of Fibonacci numbers: 100
0
1
2
3
5
8
13
21
34
55
89
"""