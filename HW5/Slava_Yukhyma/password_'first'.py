password = "first"
guess = input('write your password, please: ')
while guess != password:
    print('Your password is incorrect, try again')
    guess = input('write your password, please: ')
    if guess == password:
        print('You have written right password!')
