def counting_characters(string):
    """
    This function take's as argument string.
    Return dictionary that count number of each character
    """
    return {character: string.count(character) for character in string}

new_string = input("Enter string to count characters: ")

characters = counting_characters(new_string)
print(characters)