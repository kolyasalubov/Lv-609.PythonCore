def count_sheep(sheep):
    numbers = 0
    for i in sheep:
        if i is True:
            numbers += 1
    return numbers
