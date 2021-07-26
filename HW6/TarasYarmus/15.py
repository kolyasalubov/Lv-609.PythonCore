import re

password = input('Enter your password: ')


while True:
    if not re.search('[a-z]', password):
        print('Not valid password! Try again!')
        break
    elif not re.search('[A-Z]', password):
        print('Not valid password! Try again!')
        break
    elif not re.search('[0-9]', password):
        print('Not valid password! Try again!')
        break
    elif not re.search('[$#@]', password):
        print('Not valid password! Try again!')
        break
    elif (len(password)<6 or len(password)>16):
        print('Not valid password! Try again!')
        break
    else:
        print('Valid password!')
        break