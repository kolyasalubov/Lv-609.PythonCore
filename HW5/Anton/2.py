LOGIN = 'First'
while True:
    login = input('\033[37m Login ---> ')
    if login == LOGIN:
        print('\033[32m {}'.format('Okey, Come in!'))
        break
    else:
        print('\033[31m {}'.format('Error message: incorect login input'))
        print('\033[33m {}'.format('TIP: try another login!'))
        continue
