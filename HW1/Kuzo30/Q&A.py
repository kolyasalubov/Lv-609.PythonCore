import os
import time


def main():
    cls = lambda: os.system('cls')
    try:
        user_name = str(input("What is your name?...."))
        user_age = int(input("How old are you?......"))
        user_city = str(input("Where do you live?...."))

        print(f"\n{'-' * 20}\nHello, {user_name}.\n"
              f"Your age is {user_age}.\n"
              f"You live in {user_city}.")
        time.sleep(3)
    except ValueError:
        print("You entered wrong values! Try again...")
        time.sleep(2)
        cls()
        main()



if __name__ == '__main__':
    main()
