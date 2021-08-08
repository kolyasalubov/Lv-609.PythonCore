import random

number = random.randint(1, 100)
user_number = int(input("Try to guess number:"))
while number != user_number:
    if user_number > number:
        print("Number is smaller than you think. Try again")
        user_number = int(input("Try to guess number:"))
    elif user_number < number:
        print("Number is greater than you think. Try again")
        user_number = int(input("Try to guess number:"))
print(f"Congrats! {user_number} is that i guess!")
