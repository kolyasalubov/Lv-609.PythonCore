import re
while True:
    password = input("""Create your password
    Validation:
    At least 1 letter between [a-z] and 1 letter between [A-Z].
    At least 1 number between [0-9].
    At least 1 character from [$#@].
    Minimum length 6 characters.
    Maximum length 16 characters.
    """)
    pattern = re.compile(r'^(?=.* ?[A-Z])(?=.* ?[a-z])(?=.* ?[0-9])(?=.* ?[#?!@$^&*_-]).{6,20}$')
    if not pattern.search(password):
        print("Invalid password! Try again.")
    else:
        print("Password is valid.")
        break
