def list_animals(animals):
    """
    Function takes a list of the strings( names of the animals)
    Returns the string of the animals with orderings and newlines added.
    """

    list_of_animals = ''
    for i in range(len(animals)):
        list_of_animals += str(i + 1) + '. ' + animals[i] + '\n'
    return list_of_animals
