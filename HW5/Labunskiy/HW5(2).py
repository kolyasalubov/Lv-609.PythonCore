def login_check(login):
    true_login = "First"
    number_of_attempts = 0
    attempts = 3
    if login == true_login:
        print('Welcome')
    else:
        attempts -= 1
        print('Login wrong')
        while login != true_login and number_of_attempts < 3:
            login = input('Enter your login ::: ')
            if login == true_login:
                print('Welcome')
            else:
                print(f'Login wrong  {attempts} attempts left')
                number_of_attempts += 1
                attempts -= 1


login = input('Enter your login ::: ')


login_check(login)        
