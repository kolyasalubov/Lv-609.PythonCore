fibonacci = 423
result = 0
first = 0
second = 1
print(first)
while fibonacci >= result:
    result = first + second
    first = second
    second = result
    print(first)