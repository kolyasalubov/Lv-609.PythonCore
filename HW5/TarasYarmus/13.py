def func(word):
    '''
    This function will calculate the number
    of characters included in string
    Output type: dict
    '''
    return {characters: word.count(characters) for characters in word}

enter_word = input('Hello! Please enter your word: ')
count_character = func(enter_word)
print(count_character)