from module import *

x = ''
while x != 'z':
    choise = int(input("Choose one of them:\ntriange --> 1\nrectangle --> 2\ncircle --> 3\n? --> "))
    if choise == 1:
        print('Triangle:\n')
        h = int(input('h = '))
        a = int(input('a = '))
        print(S_triangle(h, a))
        x = str(input('Do you want continue?\nif no press Z else press Enter --> '))
        continue
    elif choise == 2:
        a = int(input('a = '))
        b = int(input('b = '))
        print(S_rectangle(a, b))
        x = str(input('Do you want continue?\nif no press Z else press Enter --> '))
        continue
    elif choise == 3:
        r = int(input('r = '))
        print(S_circle(r))
        x = str(input('Do you want continue?\nif no press Z else press Enter --> '))
        continue