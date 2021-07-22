def largest_number ( numb1,numb2):
    '''
    function,that returns the largest number 
    from two numbers
    '''
    if numb1 > numb2:
        return numb1
    elif numb2 > numb1:
        return numb2
numb1 = int ( input ('numb1: '))
numb2 = int ( input ('numb2: '))
largest_number ( numb1, numb2)
print ( largest_number(numb1,numb2))
