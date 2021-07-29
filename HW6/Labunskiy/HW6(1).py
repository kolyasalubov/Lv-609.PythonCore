def max_numbr(*numbers):
    max_n = 0
    for x in numbers:
        if x > max_n:
            max_n = x
    return max_n


print(max_numbr(15, 10, 20))