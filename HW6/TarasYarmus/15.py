import re

password = input('Enter your password: ')


while True:
    if not re.search('[a-z]', password):
        print('Valid password!')
        break
    elif not re.search('[A-Z]', password):
        print('Valid password!')
        break
    elif not re.search('[0-9]', password):
        print('Valid password!')
        break
    elif not re.search('[$#@]', password):
        print('Valid password!')
        break
    elif (len(password)<6 or len(password)>16):
        print('Valid password!')
        break
    else:
        print('Not valid password! Try again!')