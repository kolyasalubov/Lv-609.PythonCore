def square():
    """
    This function calculates the square of ​​a rectangle, triangle and circle.
    Returns the square of choosen figure
    """  
    figure = input('Write one of figures: rectangle, triangle, circle')
    if figure == 'rectangle':
        a = int(input('Side a = '))
        b = int(input('Sde b = '))
        print (f' square of rectangle is {a*b}')
        return a*b
    if figure == 'triangle':
        a = int(input('Write value of side a = '))
        h = int(input('Height = '))
        print (f'The square of triangle {a*h*0.5}')
        return a*h*0.5
    if figure == 'circle':
        print('Enter the radius of circle)')
        R = int(input('R = '))
        S = 3.14*(R**2)
        print (f'Square of circle is, {S}')
        return S
    else:
        print('You may choose only one of the figures (rectangle, triangle, circle)')
square()
# Через функцію
from math import pi

def square_rectangle():
    a=float(input("input width:"))
    b= float(input("input height:"))
    return "square of rectangle is ={}".format(a*b)

def square_triangle():
    a= float(input("input basis:"))
    h= float(input("input height:"))
    return "square of triangle is ={}".format(0.5 * a * h)

def square_circle():
    r= float(input("input radius:"))
    return "square of circle is ={}".format(pi * r**2)