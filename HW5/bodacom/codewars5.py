def count_sheeps(sheeps):
    number_of_sheeps = 0
    for place in sheeps:
        if place:
            number_of_sheeps += 1
    return number_of_sheeps