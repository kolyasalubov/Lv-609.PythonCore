n = int(input())
Fibonacci = []
if n == 0 or n == 1:
    print(n)
else:
    fibonacci_number_1 = 0
    fibonacci_number_2 = 1
    for i in range(0, n - 1):
        fibonacci_number_2 = fibonacci_number_1 + fibonacci_number_2
        fibonacci_number_1 = fibonacci_number_2 - fibonacci_number_1
        if fibonacci_number_2 > n:
            break
        else:
            Fibonacci.append(fibonacci_number_2)
print(Fibonacci)
