question = input(
    '''
    Hello! I will calculate square by your arguments! 
    Calculate square for rectangle: press 1.
    Calculate square for triangle: press 2.
    Calculate square for circle: press 3.
    Make your choice: ''')

if question != '1' and question != '2' and question != '3':
    print('Wrong option! Try again!')

def rectangle(arg1, arg2):
    '''
    This function calculate square of the rectangle
    Type: float
    Input: your arguments
    '''
    return float(arg1*arg2)

if question == '1':
    rectangle1 = float(input('Enter first side length: '))
    rectangle2 = float(input('Enter second side length: '))
    result_rectangle = rectangle(rectangle1, rectangle2)
    print(f'Square of your rectangle is: {result_rectangle}')

def triangle(height, basis):
    '''
    This function calculate square of the triangle
    Type: float
    Input: your arguments'''
    return float(height/2)*basis

if question == '2':
    triangle1 = float(input('Enter your height: '))
    triangle2 = float(input('Enter your basis: '))
    result_triangle = triangle(triangle1, triangle2)
    print(f'Square of your triangle is: {result_triangle}')

def circle(r):
    '''
    This function calculate square of the circle
    Type: float
    Input: enter number for first argument "r"'''
    return float(3.14*r)**2

if question == '3':
    circle1 = float(input('Enter numeric for "r": '))
    result_circle = circle(circle1)
    print(f'Square of your circle is: {result_circle}')