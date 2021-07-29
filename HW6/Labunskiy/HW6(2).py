def square_of_a_rectangle():
    print("Прямоугольник")


def square_of_a_triangle():
    a = int(input(':::'))
    print(((1/3)**a**2)/4,2)


def square_of_a_circle():
    print("круг")


def choose_figure():
    choose = int(input("choose_figure, 0 or circle,\
 3 or tringle, 4 or rectangle :::"))
    if choose == 0:
        square_of_a_circle()
    elif choose == 3:
        square_of_a_triangle()
    elif choose == 4:
        square_of_a_rectangle()
    else:
        choose_figure()


choose_figure()