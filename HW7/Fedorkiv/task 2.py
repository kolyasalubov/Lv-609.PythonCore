from re import search
def check_valid_password(password):
    if len(password) < 6 or len(password) > 16:
        return 'Minimum 6, maximum 16'
    elif not search('[a-z]', password):
        return 'At least 1 letter between [a-z] and 1 letter between [A-Z]'
    elif not search('[A-Z]', password):
        return 'At least 1 letter between [a-z] and 1 letter between [A-Z]'
    elif not search('[0-9]', password):
        return 'At least 1 number between [0-9]'
    elif not search('[#$@]', password):
        return 'At least 1 character from [$#@]'
    else:
        return True
while True:
    password = input('Enter your password:')
    if check_valid_password(password) != True:
        print(check_valid_password(password))
        print('Try another password')
        continue
    else:
        print('Valid password')
        break