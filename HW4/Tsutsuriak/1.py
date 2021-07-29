number = int(input("Введіть число: "))
factorial = 1
x = 1
if number == 0:
    print("Факторіал числа 0 = 1.")
elif number == 1:
    print("Факторіал числа 1 = 1.")
else:
    while x <= number:
        factorial *= x
        x += 1
    print("Факторіал числа ", number, " = ", factorial, ".", sep="")
