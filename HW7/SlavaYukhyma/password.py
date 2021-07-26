password = input('Enter your pasword: ')

if 6 < len(password) < 16:

    for i in range(5):
        if password[i] in 'abcdefghijklmnopqrstuvwxyz' or password[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or password[i] in [r'$3@'] or password[i] in '1234567890':
            print(True)
    
else:
    print('Unadequate lenght')


# if  6 > len(password) < 16 and
