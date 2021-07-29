def count_sheeps(sheep):

    amount = 0
    for item in sheep:
        if item == True:
            amount += 1
        else:
            continue
    return amount
