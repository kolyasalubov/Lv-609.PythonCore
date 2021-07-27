def circle_area(radius):
    """
    input radius size, type integer or float; returns the area of given circle.
    """
    return 3.14 * radius ** 2 if type(radius) == int or type(radius) == float else "Please input an integer or a float."

def triangle_area(height, width):
    """
    input height and width, type integer or float; returns the area of given triangle.
    """
    return height * width * 0.5 if (type(height)==int or type(height)==float) and (type(width)==int or type(width)==float) else "Please input valid dimensions."

def rectangle_area(height, width):
    """
    input height and width, type integer or float; returns the area of given rectangle.
    """
    return height * width if (type(height)==int or type(height)==float) and (type(width)==int or type(width)==float) else "Please input valid dimensions."
