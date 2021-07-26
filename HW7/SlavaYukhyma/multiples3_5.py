
def solution(number):
    res = []
    if number > 0:
        # return sum([i  for i in range(number)if(i%3 == 0 or i %5 == 0)])
        for i in range(number):
            if i in res:
                continue
            elif i % 3 == 0 or i % 5 == 0:
                res.append(i)
    return sum(res)


def solution2(number2):
    if number2 > 0:
        res2 = []
        for i in range(number2):
            if i % 3 == 0 or i % 5 == 0:
                res2.append(i)
    a = set(res2)
    print(sum(a))
    return(sum(a))


solution2(10)
