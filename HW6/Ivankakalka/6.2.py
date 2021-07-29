Pi = 3.14
def calculate_square():
    """
    Function calculates the square for three figures,
    depending on the user's choise.
    Returns the square of chosen figure.
    Type - integer(rectangle,triangle), float(circle)
    """
    figure = input('choose the figure: rectangle, triangle, circle: ')

    if figure == 'rectangle':
        h = int(input('Enter the height of the rectangle cm:  '))
        w = int(input('Enter the width of the rectangle  cm:  '))
        print(f'Your rectangle is {h*w} cm2')
        return h*w

    if figure == 'triangle':
        s = int(input('Enter the base of the triangle  cm:  '))
        h_t = int(input('Enter the height of the triangle  cm  : '))
        print(f'Your triangle is {s*h_t*0.5} cm2')
        return s*h_t*0,5

    if figure == 'circle':
        r = float(input('Enter the radius of the circle  cm  :  '))
        print(f'Your circle is {Pi*r**2} cm2')
        return Pi*r**2
calculate_square()  
