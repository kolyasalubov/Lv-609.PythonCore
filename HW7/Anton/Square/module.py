from math import pi

def S_triangle(h, a):
    """
    CALCULATE SQUARE OF TRIANGLE 
    EXAMPLE: S_triangle("height", "side (a)")
    """
    return f'SQUARE OF TRIANGLE = {round(0.5 * h * a)}'

def S_rectangle(a, b):
    """
    CALCULATE SQUARE OF RECTANGLE
    EXAMPLE: S_rectangle("side a", "side b")
    """
    return f'SQUARE OF RECTANGLE = {a*b}'

def S_circle(r):
    """
    CALCULATE SQUARE OF CIRCLE
    EXAMPLE: S_circle("radius")
    """
    return f'SQUARE OF CIRCLE = {pi*r**2}'


