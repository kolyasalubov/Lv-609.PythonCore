def solution(number):
    threes = range(3, number, 3)
    fives = range(5, number, 5)
    return sum(list(set(threes + fives)))
