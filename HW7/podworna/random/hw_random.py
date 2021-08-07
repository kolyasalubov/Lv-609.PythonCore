import random

random_number=random.randint(1,100)
print(random_number)

enter_number=int(input("Guess the random number - "))

while enter_number != random_number:
    if enter_number > random_number:
        enter_number=int(input('Try a smaller number - '))
    elif enter_number < random_number:
        enter_number=int(input('Try a larger number - '))
    if enter_number == random_number:
        print('Сongratulations, you made it up !!!')
