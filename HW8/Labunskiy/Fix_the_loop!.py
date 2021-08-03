def list_animals(animals):
    list = ''
    for i in range(len(animals)):
        list += str(int(i) + 1) + '. ' + animals[i] + '\n'
    return list