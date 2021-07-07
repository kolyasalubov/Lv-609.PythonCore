def calculate_number_characters(text):
    """
    Input : text
    Type : string
    Return : calculates the number of characters included in a given string
    """
    return {item : text.count(item) for item in text}

# Output : {'h': 1, 'e': 1, 'l': 2, 'o': 1}
print(calculate_number_characters("hello"))
