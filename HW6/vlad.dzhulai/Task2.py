def square_of_rectangle():
    """
    Function that calculates the square of rectangle.
    """
    w = int(input("Enter the length of the first side: "))
    b = int(input("Enter the length of the second side: "))
    a = w * b
    return a


def square_of_triangle():
    """
    Function that calculates the square of triangle.
    """
    w = int(input("Enter the length of the first side: "))
    h = int(input("Enter the length of the second side: "))
    a = 0.5 * w * h
    return a


def square_of_circle():
    """
    Function that calculates the square of circle.
    """
    r = int(input("Enter a radius: "))
    a = 3.14 * r ** 2
    return a


users_choice = input("Choose a square you'd like to calculate:"
                     "\na. Rectangle"
                     "\nb. Triangle"
                     "\nc. Circle"
                     "\nYour pick: ")

if users_choice == "a":
    print("Square = ", square_of_rectangle())
elif users_choice == "b":
    print("Square = ", square_of_triangle())
elif users_choice == "c":
    print("Square = ", square_of_circle())
else:
    print("You have entered incorrect choice!")
