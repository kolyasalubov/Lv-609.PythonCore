# HW5 task 2

# Write a script that checks the login that the user enters. 
# If the login is "First", then greet the users. If the login is different, send an error message. 
# (need to use loop while)

login = input("Please enter your login: ")
#print(login)

while not login == "First":
    print("Login incorrect. Please enter proper login: ")
    login = input()

print("Hello, %s" % login)