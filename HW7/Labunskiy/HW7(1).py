import HW7_mod as mod


def user_choice():
    choice = int(input(
        "1 - rectangle\n2 - triangle\n3 - circle\nSelect the area of the shape you want to get: "))
    return choice


while True:
    try:
        user_input = int(user_choice())
    except ValueError:
        continue
    else:
        if user_input == 1:
            print(mod.square_of_rectangle(
                int(input("Input height : \n")), int(input("Input width : \n"))))
            break
        elif user_input == 2:
            print(mod.square_of_triangle(
                int(input("Input height : \n")), int(input("Input width : \n"))))
            break
        elif user_input == 3:
            print(mod.square_of_circle(int(input("Input radius : \n"))))
            break
