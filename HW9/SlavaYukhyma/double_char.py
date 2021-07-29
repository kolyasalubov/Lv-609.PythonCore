def double_char(s):
    '''
    Function takes a string.
    Return a string in which each character (case-sensitive) is repeated once.
    '''
    a = list(s)
    print(a)
    i = 0
    for i in range(len(a)):
        a[i] = a[i]*2
    new_str = ''.join(a)
    # print(new_str)
    return new_str


double_char('asdf')
