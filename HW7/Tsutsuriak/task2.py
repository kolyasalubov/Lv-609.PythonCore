import re

pattern = str(input("Enter your password: "))

var = True

while var:

    valid1 = re.findall("[a-z]", pattern) 
    valid2 = re.findall("[A-Z]", pattern)
    valid3 = re.findall("[0-9]", pattern)
    valid4 = re.findall("[$#@]", pattern)
    min_len = 6
    max_len = 16 

    if valid1 and valid2 and valid3 and valid4 and (len(pattern) >= min_len) and (len(pattern) <= max_len):
        print("Password are valid!")
        var = False
    else:
        pattern = str(input("Password are not valid! Enter your password: "))
