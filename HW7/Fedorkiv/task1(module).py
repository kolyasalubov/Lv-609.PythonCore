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

