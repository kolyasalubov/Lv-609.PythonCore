def list_animals(animals):
    list = ''
    i = 0
    for x in animals:
        list += str(animals.index(x)+1) + '. ' + x + '\n'
    return list