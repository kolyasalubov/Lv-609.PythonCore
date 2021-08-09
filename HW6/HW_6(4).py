def largest_number(num_1, num_2):
    """
    Function that returns the largest
    number from 2 inputs.
    """
    if num_1 > num_2:
        return num_1
    elif num_1 < num_2:
        return num_2


numb_1 = int(input('numb1: '))
numb_2 = int(input('numb2: '))
largest_number(numb_1, numb_2)
print(largest_number(numb_1, numb_2))
