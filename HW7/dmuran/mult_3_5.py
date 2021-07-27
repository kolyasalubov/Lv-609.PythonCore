def solution(number):
    list1 = [x for x in range(1, number)]
    res = 0
    for x in list1:
        if x % 3 == 0 or x % 5 == 0:
            res += int(x)
    return res
