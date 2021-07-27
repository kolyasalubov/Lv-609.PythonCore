import random


def return_random():
    number = random.randint(1, 100)
    print(number)
    user_number = int(input("Guess the number : "))
    while user_number != number:
        if user_number < number:
            print("Try again(your number is less than expected)")
            user_number = int(input("Guess the number : "))
        elif user_number > number:
            print("Try again(your number is greater than expected)")
            user_number = int(input("Guess the number : "))
    else:
        print(f"Congratulation! You guessed the number {number}")


return_random()
