import re


def check_valid_password(password):
    """
    Input: password
    Type: string
    Return: Valid Password. / Wrong password!
    """
    x = 'Wrong password!'

    while True:
        if len(password) < 6 or len(password) > 16:
            return x
        elif not re.search('[a-z]', password):
            return x
        elif not re.search('[A-Z]', password):
            return x
        elif not re.search('[0-9]', password):
            return x
        elif not re.search('[$#@]', password):
            return x
        else:
            return 'Valid Password'


print (check_valid_password(input("Enter your Password : ")))
