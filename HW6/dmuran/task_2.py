PI = 3.14


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
    return (arg1*arg2)/2


def square_of_circle(radius):
    """
    Input : radius
    Type : int, float
    Return : Square
    """
    return PI*(radius**2)


# Output : 8
print(square_of_rectangle(2, 4))

# Output : 20
print(square_of_triangle(5, 8))

# Output : 50.24
print(square_of_circle(4))
