from math import (pi, pow)


def rectangle_square():
    """
    Return: printing message with result of rectangle square
    """
    first_side = float(input("Enter first side length: "))
    second_side = float(input("Enter second side length: "))
    print(f"Rectangle square is {first_side * second_side}")


def triangle_square():
    """
    Return: printing message with result of triangle square
    """
    height = float(input("Enter triangle height: "))
    basis = float(input("Enter triangle basis: "))
    print(f"Triangle square is {0.5 * height * basis}")


def circle_square():
    """
    Return: printing message with result of circle square
    """
    radius = float(input("Enter circle radius: "))
    print(f"Circle square is {pi * pow(radius, 2)}")
