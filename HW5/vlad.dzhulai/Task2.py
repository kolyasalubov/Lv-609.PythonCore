login = {"Login": "First"}
counter = False
while not counter:
    login_request = input("Enter your login, please: ")
    if login_request == login["Login"]:
        print(f'You have successfully entered your login {login["Login"]}')
        counter = True
