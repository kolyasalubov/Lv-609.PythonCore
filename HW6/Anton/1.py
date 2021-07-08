def largest(num1, num2):
    """
    This function returns largest number of two numbers.
    Example: largest(12, 99)

    """
    if num1 != num2:
        return f'largest {num1}' if num1 > num2 else f'largest {num2}' 
    else:
        return 'They eguals'

