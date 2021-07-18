from math import (pi,
                pow)
import import_math as functions

question = input(
    '''
    Hello! I will calculate square by your arguments! 
    Calculate square for rectangle: press 1.
    Calculate square for triangle: press 2.
    Calculate square for circle: press 3.
    Make your choice: ''')

if question == '1':
    rectangle1 = float(input('Enter first side length: '))
    rectangle2 = float(input('Enter second side length: '))
    result_rectangle = functions.rectangle(rectangle1, rectangle2)
    print(f'Square of your rectangle is: {result_rectangle}')
elif question == '2':
    triangle1 = float(input('Enter your height: '))
    triangle2 = float(input('Enter your basis: '))
    result_triangle = functions.triangle(triangle1, triangle2)
    print(f'Square of your triangle is: {result_triangle}')
elif question == '3':
    circle1 = float(input('Enter numeric for "r": '))
    result_circle = functions.circle(circle1)
    print(f'Square of your circle is: {result_circle}')
else:
    print('Wrong option! Try again!')