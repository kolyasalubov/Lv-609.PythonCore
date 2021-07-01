number = int(input("Enter the number you want to get factorial of: "))
user_number = number
factorial = 1
while number > 1:
    factorial *= number
    number -= 1
print(f"Factorial of {user_number} is {factorial}")


"""----- RESULT -----
Enter the number you want to get factorial: 10
Factorial of 10 is 3628800
"""