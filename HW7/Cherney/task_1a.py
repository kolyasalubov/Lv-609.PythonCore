import task_1b

try:
    sel = int(input("Please type 1 to calculate the area of a rectangle,\npress 2 to calculate area of a triangle,\n press 3 to calculate the area of a circle "))
    if sel==1:
        a = int(input("You've chosen to calculate the area of a rectangle, input width: "))
        b = int(input("Input height: "))
        print(f"The area of the rectangle is: {task_1b.calc_rectan_area(a,b)}")
    elif sel==2:
        a = int(input("Please input the height of triangle: "))
        b = int(input("Please input the base of triangle: "))
        print(f"The area of the tringle is: {task_1b.calc_triangle_area(a,b)}")
    elif sel==3:
        r = int(input("Please input the radius of the circle: "))
        print(f"The area of the circle is: {task_1b.calc_circle_area(r)}")
except:
    print("Please type 1, 2 or 3")