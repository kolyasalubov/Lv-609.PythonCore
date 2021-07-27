def calculate_characters(text):
    """
    input text, type str; returns dictionary with unique characters and their appearance count
    """
    return {x: text.count(x) for x in text} if type(text)==str else "Please input a string object."

