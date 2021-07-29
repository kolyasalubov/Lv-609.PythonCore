from M1 import rectangle, triangle, circle


def square():
    start = int(input(
        'Please, choose\n 1: to calculate the area of rectangle\n 2: to calculate the area of triangle\n 3: for circle'))

    if start == 1:
        rectangle()
    elif start == 2:
        triangle()
    elif start == 3:
        circle()
    else:
        print('Please, type corect answer')
        square()


square()
