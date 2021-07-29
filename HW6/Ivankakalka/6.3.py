def number_of_characters (word):
    '''
    Function, that calculates the number of characters 
    included in a given string
    '''
    return {item : word.count(item) for item in word}
y= input ( 'Enter the word: ')
print ( number_of_characters (y))