from math import (pi, pow)


def square_of_rectangle(height, width):
    return height * width


def square_of_triangle(height, width):
    return pow(height*width, 0.5)


def square_of_circle(radius):
    return round(pi * (radius**2), 2)
