number = int(input("Enter your number:"))
result = 1
while(number>0):
    result = result * number
    number = number-1
print("Factorial of your number is:", result)