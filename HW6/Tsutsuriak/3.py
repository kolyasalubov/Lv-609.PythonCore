def number_of_characters(string):
    """
    This function calculates the number of characters included in a given string.
    """
    return {characters: string.count(characters) for characters in string}
