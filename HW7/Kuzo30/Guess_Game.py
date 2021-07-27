import random


def main():
    difficulty = input("Choose difficulty of a game:\n"
                           "1 - Easy (0 - 50)\n"
                           "2 - Medium (0 - 100)\n"
                           "3 - Hard (0 - 500)\n")

    if difficulty == "1":
        gameplay(0, 50)

    if difficulty == "2":
        gameplay(0, 100)

    if difficulty == "3":
        gameplay(0, 500)


def gameplay(a, b):
    attempts = 1
    rand_number = random.randint(a, b)
    # print(rand_number)
    user_guess = int(input(f"Your number is somewhere between {a} and {b}: "))
    while user_guess != rand_number:
        if user_guess < rand_number:
            user_guess = int(input(f"\nYour guess was too low. Try going higher.\n"
                                   f"You have {attempts} attempt so far.\n"
                                   f"Try again: "))

        elif user_guess > rand_number:
            user_guess = int(input(f"\nYour guess was too high. Try going lower.\n"
                                   f"You have {attempts} attempt so far.\n"
                                   f"Try again: "))

        attempts += 1
    else:
        print(f"{'-'*50}\nYou guessed the right number!\n"
              f"Good job! You guessed the right number in {attempts - 1} tries.")



if __name__ == "__main__":
    main()