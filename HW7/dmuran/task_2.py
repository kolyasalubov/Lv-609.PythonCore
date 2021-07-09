import re


def check_valid_pass(password):
    """
    Input: password
    Type: string
    Return: is valid password
    """
    while True:
        if len(password) < 6:
            return 'Not a Valid Password'
        elif len(password) > 16:
            return 'Not a Valid Password'
        elif not re.search('[a-z]', password):
            return 'Not a Valid Password'
        elif not re.search('[A-Z]', password):
            return 'Not a Valid Password'
        elif not re.search('[0-9]', password):
            return 'Not a Valid Password'
        elif not re.search('[$#@]', password):
            return 'Not a Valid Password'
        else:
            return 'Valid Password'


print(check_valid_pass(input("Input your Password : ")))
