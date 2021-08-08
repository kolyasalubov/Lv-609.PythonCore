def plus():
    first_num = input("Enter first number: ")
    second_num = input("Enter second number: ")
    try:
        first_num = float(first_num)
        second_num = float(second_num)
        print(f"Sum: {first_num} + {second_num} = {first_num + second_num}")
    except ValueError:
        print("Invalid type")


def minus():
    first_num = input("Enter first number: ")
    second_num = input("Enter second number: ")
    try:
        first_num = float(first_num)
        second_num = float(second_num)
        print(f"Difference: {first_num} - {second_num} = {first_num - second_num}")
    except ValueError:
        print("Invalid type")


def multiplication():
    first_num = input("Enter first number: ")
    second_num = input("Enter second number: ")
    try:
        first_num = float(first_num)
        second_num = float(second_num)
        print(f"Multiplication: {first_num} * {second_num} = {first_num * second_num}")
    except ValueError:
        print("Invalid type")


def dividing():
    first_num = input("Enter first number: ")
    second_num = input("Enter second number: ")
    try:
        first_num = float(first_num)
        second_num = float(second_num)
        print(f"Dividing: {first_num} / {second_num} = {first_num / second_num}")
    except ValueError:
        print("Invalid type")