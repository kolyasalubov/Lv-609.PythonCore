def counter(string):
    """
    Calculate count of elements in string.

    """
    result = [f'Count of {elem} = {string.count(elem)}\n'for elem in set(string)] 
    return "".join(result)