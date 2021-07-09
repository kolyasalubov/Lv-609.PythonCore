from math import (pi, pow)


def square_of_rectangle(height, width):
    """
    Input : height, width
    Type : int, float
    Return : Square 
    """
    return height * width


def square_of_triangle(arg1, arg2):
    """
    Input : arg1, arg2
    Type : int, float
    Return : Square
    """
    return pow(arg1*arg2, 0.5)


def square_of_circle(radius):
    """
    Input : radius
    Type : int, float
    Return : Square
    """
    return round(pi * (radius**2), 2)
