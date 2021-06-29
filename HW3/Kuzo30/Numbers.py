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


if __name__ == '__main__':
    product("1234")
    reversed_number("1234")