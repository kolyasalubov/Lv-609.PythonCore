import re

def pass_valid():
    password_pattern = r"^(?=.+\d)(?=.+[$#@])(?=.+[a-z])(?=.+[A-Z])(?=.+[a-zA-Z]).{6,16}$"
    username = input("Enter your username: ")
    password = input("Enter Password: ")
    if re.fullmatch(password_pattern, password):
        return f"Hello {username}, you are welcome!"
    else:
        print("You entered not valid password, try again")
        return pass_valid()


if __name__ == "__main__":
    print(pass_valid())