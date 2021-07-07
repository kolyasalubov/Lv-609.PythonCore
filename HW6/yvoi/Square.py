def rectangle_square(a, b):
    """
    :param a: float
    :param b: float
    :return: rectangle square (type: float)
    """
    return a * b


def triangle_square(h, a):
    """
    :param h: float
    :param a: float
    :return: triangle square (type: float)
    """
    return 0.5 * a * h


def circle_square(r):
    """
    :param r: float
    :return: circle square (type: float)
    """
    return 3.14 * r ** 2


user_choice = input("What square do you want to calculate?\n1)Rectangle\n2)Triangle\n3)Circle\nEnter number(1, 2, 3): ")
if user_choice == '1':
    side_1 = float(input("Enter first rectangle side: "))
    side_2 = float(input("Enter second rectangle side: "))
    square = rectangle_square(side_1, side_2)
    print(f"Rectangle square is {square}")
elif user_choice == '2':
    hight = float(input("Enter triangle hight: "))
    base = float(input("Enter triangle base: "))
    square = triangle_square(hight, base)
    print(f"Triangle square is {square}")
else:
    radius = float(input("Enter circle radius: "))
    square = circle_square(radius)
    print(f"Circle square is {square}")