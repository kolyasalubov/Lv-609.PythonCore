def max_number():
    """
    Function that returns the largest
    number from 2 inputs.
    """
    x = int(input("Enter the first number: "))
    y = int(input("Enter the secons number: "))
    return max(x, y)

print(max_number())