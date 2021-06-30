def sep(symbol, quantity):
    print(symbol*quantity)

if __name__=='__main__':


    name = input('What is your name?: ')
    age = input('How old are you?: ')
    city = input('Where do you live?: ')

    sep("*", 30)

    print(f'Your name is {name}.\nYour age is {age} years.')
    print(f'You live in {city}.')
