

def calculate_square():
    """
    Function calculate a square for three figures,
    depending on user choise.
    Return - the square of chosen figure
    """
    figure = input('choose the figure: rectangle, triangle, circle: ')

    if figure == 'rectangle':
        h = int(input('Indicate height of the rectangle: '))
        w = int(input('Indicate width of the rectangle: '))
        print(f'Your rectangle is {w*h} cm2')
        return w*h

    if figure == 'triangle':
        a = int(input('Write the base of your triangle: '))
        h_triangle = int(input('Write the height of your triangle: '))
        print(f'The square is {a*h_triangle*0.5}')
        return a*h_triangle

    if figure == 'circle':
        r = int(input('Enter the radius of your circle'))
        square_circle = 3, 14 * (r**2)
        print(f'Your circle is {square_circle}sm2')
        return square_circle


calculate_square()
