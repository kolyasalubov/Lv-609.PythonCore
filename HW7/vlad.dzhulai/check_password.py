import re


def password_checker():
    users_input = input("Please, enter a new password: ")
    if 6 <= len(users_input) <= 16 and \
       re.findall("[0-9]", users_input) != [] and \
       re.findall("[a-z]", users_input) != [] and \
       re.findall("[A-Z]", users_input) != [] and \
       re.findall("[$#@]", users_input) != []:
        print("Your password is valid!")
    else:
        print("Sorry. Your password is not valid.")


password_checker()
