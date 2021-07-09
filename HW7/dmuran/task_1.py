import task_1_module as tm

user_choice = int(input(
    "1 - rectangle\n2 - triangle\n3 - circle\nSelect the area of the shape you want to get: "))

while user_choice != 1 and user_choice != 2 and user_choice != 3:
    user_choice = int(input(
        "1 - rectangle\n2 - triangle\n3 - circle\nSelect the area of the shape you want to get: "))
else:
    if user_choice == 1:
        print(tm.square_of_rectangle(
            int(input("Input height : \n")), int(input("Input width : \n"))))
    elif user_choice == 2:
        print(tm.square_of_triangle(
            int(input("Input height : \n")), int(input("Input width : \n"))))
    elif user_choice == 3:
        print(tm.square_of_circle(int(input("Input radius : \n"))))
