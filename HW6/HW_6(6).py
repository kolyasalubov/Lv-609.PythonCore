def counter():
    """
    letters counter
    """
    word = input("Enter word: ")
    return{letters: word.count(letters) for letters in word}


print(counter())
