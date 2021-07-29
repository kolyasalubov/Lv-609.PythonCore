from math import pow, sqrt


def main(a: float, b: float):
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b}")
    print(f"{a} // {b} = {a // b}")
    print(f"{a} % {b} = {a % b}")
    print(f"{a} ^ {b} = {pow(a, b)}")
    print(f"√{b} = {sqrt(2)}")



if __name__ == '__main__':
    main(1, 2)