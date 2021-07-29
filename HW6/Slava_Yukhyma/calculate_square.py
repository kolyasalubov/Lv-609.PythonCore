PI = 3.14


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
        square_circle = PI * (r**2)
        print(f'Your circle is {square_circle}sm2')
        return square_circle

    else:
        print('Input error!')


calculate_square()
########################################################################################


def return_rectangle_square():
    height = (int(input('Enter hight of the rectangle: ')))
    width = (int(input('Enter width of the rectangle: ')))
    return f'The square of the rectangle is: {height*width}'


def return_circle_square():
    PI = 3.14
    r = float(input('Enter radius of the circle: '))
    return f'Radius of circle is {PI * r ** 2}'


def return_triangle_square():
    base = (float(input('Enter base side of the triangle: ')))
    height = (float(input("Enter height of your triangle: ")))
    return f'Square of your triangle is {base * height* 0.5}'


def figure():
    figure = (input('enter your figure: 1-rectangle, 2-circle, 3-triangle: '))

    if figure == '1':
        return return_rectangle_square()

    elif figure == '2':
        return return_circle_square()

    elif figure == '3':
        return return_triangle_square()


print(figure())
