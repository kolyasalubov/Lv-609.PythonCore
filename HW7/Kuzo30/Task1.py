import re

def pass_valid(username, password):
    password_pattern = r"^(?=.+\d)(?=.+[$#@])(?=.+[a-z])(?=.+[A-Z])(?=.+[a-zA-Z]).{16}$"
    if re.fullmatch(password_pattern, password):
        return f"Hello {username}, you are welcome!"
    else:
        print("You entered not valid password, try again")
        return pass_valid(username, input("Enter password: "))


if __name__ == "__main__":
    print(pass_valid("Yura Kuzo", "yurakzA2jUuibn0$")) # yurakzA2asdaad0$