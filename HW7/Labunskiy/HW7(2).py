import re


def check_valid_pass(password):
    while True:
        if not re.search('[a-z]', password):
            print('Not a Valid Password. At least 1 letter between [a-z]')
            return check_valid_pass(input("Input your Password : "))
        elif not re.search('[A-Z]', password):
            print('Not a Valid Password. At least 1 letter between [A-Z]')
            return check_valid_pass(input("Input your Password : "))
        elif not re.search('[0-9]', password):
            print('Not a Valid Password. At least 1 number between [0-9]')
            return check_valid_pass(input("Input your Password : "))
        elif not re.search('[$#@]', password):
            print('Not a Valid Password. At least 1 character from [$#@]')
            return check_valid_pass(input("Input your Password : "))
        elif len(password) < 6 or len(password) > 16:
            print("Not a Valid Password. Minimum length 6 characters. Maximum length 16 characters.")
            return check_valid_pass(input("Input your Password : "))   
        else:
            print('Valid Password')
            return password


passvord = check_valid_pass(input("Input your Password : "))
print(passvord)
