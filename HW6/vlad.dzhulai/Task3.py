def letters_count():
    """
    This function taking input from the user (word),
    and returning a dictionary, where a key - a letter in the word,
    and a value is quantity of each letter.
    """
    word = input("Enter a word: ")
    return{letter: word.count(letter) for letter in word}


print(letters_count())
