def square(figure):
    """
    This function calculates the square of ​​a rectangle, triangle and circle.
    You may choose only one of the figures (rectangle, triangle, circle).
    Example: square('circle')

    """  
    if figure == 'rectangle':
        print('For rectangle you need values of sides (a) & (b)')
        a = int(input('Side a = '))
        b = int(input('Sde b = '))
        S = a*b
        return f'Sguare of {figure} = {S}'
    elif figure == 'triangle':
        print('For triangle you need values of side (a) & height (h)')
        a = int(input('Side a = '))
        h = int(input('Height = '))
        S = 0.5*a*h
        return f'Sguare of {figure} = {S}'
    elif figure == 'circle':
        print('For circle you need values of radius (R)')
        R = int(input('R = '))
        S = 3.14*(R*R)
        return f'Sguare of {figure} = {S}'
    else:
        print('You may choose only one of the figures (rectangle, triangle, circle)')
    
