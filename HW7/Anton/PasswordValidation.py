from re import search

def check_pass(password):
    if len(password) < 6 or len(password) > 16:
        return 'Lenth must be 6 - 16'
    elif not search('[a-z]', password):
        return 'At least 1 letter between [a-z] and 1 letter between [A-Z]'
    elif not search('[A-Z]', password):
        return 'At least 1 letter between [a-z] and 1 letter between [A-Z]'
    elif not search('[#$@]', password):
        return 'At least 1 character from [$#@]'
    elif not search('[0-9]', password):
        return 'At least 1 number between [0-9]'
    else:
        return True

while True:
    password = input('Password:')
    if check_pass(password) != True:
        print(check_pass(password))
        print('Try another pass')
        continue
    else:
        print('Okey!')
        break
