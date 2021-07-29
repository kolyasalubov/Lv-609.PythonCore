def calculates_the_number_of_characters(string):
    return {character: string.count(character) for character in string}


print(calculates_the_number_of_characters("hello")) 
