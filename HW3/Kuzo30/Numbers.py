def product(number):
    result = 1
    for n in number:
        result *= int(n)
    print(result)


def reversed_number(number):
    result = ""
    for i in reversed(number):
        result += i
    print(result)


def sort(number):
    number_array = str(number)
    number_array.split()
    res = int("".join(map(str, sorted(number_array))))
    print(res)


if __name__ == '__main__':
    product("1234")
    reversed_number("1234")
    sort(4321)