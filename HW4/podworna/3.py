input_number=int(input("Entered number, n="))

fibonacci_number_0, fibonacci_number_1 = 0, 1
while fibonacci_number_1 <= input_number:
    fibonacci_number_0, fibonacci_number_1=fibonacci_number_1, fibonacci_number_0 + fibonacci_number_1
    print(fibonacci_number_0)