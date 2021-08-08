import square_functions as sq

while True:
    user_choice = input("To calculate square of rectangle(1), triangle(2), circle(3) or quit(q) make choice(1, 2, 3, q): ")
    if user_choice == "1":
        sq.rectangle_square()
    elif user_choice == "2":
        sq.triangle_square()
    elif user_choice == "3":
        sq.circle_square()
    elif user_choice == "q":
        break
    else:
        print("Error! Invalid key")
