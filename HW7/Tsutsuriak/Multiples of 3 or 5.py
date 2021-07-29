def solution(number):
    sum = 0
    i = 0
    while i < number:
        if number <= 0:
            sum == 0
            break
        elif i % 3 == 0 or i % 5 == 0:
            sum += i
        i += 1
    return sum
