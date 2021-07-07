def largest_num(number1, number2):
    """
    This function returns the largest number of two numbers.
    """
    if number1 > number2:
        return number1
    elif number2 > number1:
        return number2
    else:
        return number1, number2
