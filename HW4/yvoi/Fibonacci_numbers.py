number = int(input("Enter last value of Fibonacci numbers: "))
next = first = 0
second = 1

while next <= number:
    print(next)
    next = first + second
    first, second = second, next


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