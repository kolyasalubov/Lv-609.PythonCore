import random

random_number = random.randint(1, 100)

value = int(input("Enter the number: "))

while value != random_number:
    if value < random_number:
        print("Your number is less than random.")
        value = int(input("Enter the number: "))
    elif value > random_number:
        print("Your number is greater than random.")
        value = int(input("Enter the number: "))

print("My congratulations! You guessed the number.")
