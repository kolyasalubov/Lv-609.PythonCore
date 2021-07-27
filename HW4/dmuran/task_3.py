fibonacci = 12
result = 0
first = 0
second = 1
print(first)
if fibonacci > 0:
    while fibonacci >= result:
        result = first + second
        first = second
        second = result
        print(first)
