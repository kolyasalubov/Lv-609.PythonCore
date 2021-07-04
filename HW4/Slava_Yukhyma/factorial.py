from math import factorial
######################################################
num = int(input(' Enter your number: '))
res = 1
i = 1
while i <= num:
    res = res * i
    i += 1
print(res)

if res == (factorial(num)):
    print('You\'ve done good job!')

#####using function#######


def count_factorial(your_num):
    result = 1
    i = 1
    while i <= your_num:
        result = result * i
        i += 1
    print(result)
    return result


count_factorial(5)
