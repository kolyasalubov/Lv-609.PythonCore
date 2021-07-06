def pick_max_number(*args):
    """
    takes a tuple of numbers, their type integer or float, returns maximum number
    """
    return max(args) if all([type(x)==int or type(x)==float for x in args]) else "All of provided values should be integers!"

