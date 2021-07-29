from math import pow, pi


def rectangle():
    print('You want to calculate the area of rectangle')
    a = int(input('Please, enter height of rectangle'))
    b = int(input('Please, enter weight of rectangle'))
    print(f'The area of your rectangle is {a*b} ')
    return a*b


def triangle():
    print("You are going to calculate triangle's square.")
    a = int(input("Please, enter the lenght of the base of the triangle: "))
    h = int(input('And the height of the triangle too: '))
    print(f'The area of your triangle is {0.5 * a * h}')
    return 0.5 * a * h


def circle():
    print("You decided to calculate the area of the circle.")
    r = int(input('Please, enter the radius of the circle: '))
    print(f'The area of your circle is {round(pi * pow(r, 2), 2)}')
    return round(pi * pow(r, 2), 2)


if __name__ == '__main__':
    circle()
