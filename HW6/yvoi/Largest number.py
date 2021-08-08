def largest_number(num_1, num_2):
    """
    Input parameter: num_1 , num_2
    Type input parameter: int or float
    Return: largest number
    """
    if num_1 > num_2: return num_1
    elif num_1 < num_2: return num_2


a = 26
b = 31.45
print(largest_number(a, b))
print(largest_number.__doc__)
