#How to calculate a factorial

factorial_input = int(input("Enter a number: "))
result = 1

if factorial_input == 0 or factorial_input == 1:
    print("Factorial equal to 1")
else:
    for i in range(1,factorial_input+1):
        result = result * i
    print(f"Factorial is {result}")

