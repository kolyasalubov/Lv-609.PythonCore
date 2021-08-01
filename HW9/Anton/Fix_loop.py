def list_animals(animals):
    c = 1
    list = ''
    for i in animals:
        list += f'{c}. {i}\n'
        c += 1
    return list