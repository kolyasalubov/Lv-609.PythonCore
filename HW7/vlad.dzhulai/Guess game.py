from random import randint


def random_number():
    i = randint(1, 100)
    guess = int(input("Please, enter an integer number from 1 to 100: "))
    while not guess == i:
        if guess < i:
            guess = int(input("Your number is lower then random number. Please, try again: "))
            continue
        elif guess > i:
            guess = int(input("Your number is higher then random number. Please, try again: "))
            continue
    return "You have successfully guessed a number! Congrats!"


print(random_number())
