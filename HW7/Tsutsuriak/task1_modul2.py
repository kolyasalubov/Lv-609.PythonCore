import task1_modul1

value = int(input("1-square rectangle, 2-square triangle, 3-square circle: "))

if value == 1:
    print("Square rectangle: ", task1_modul1.square_rectangle(int(input("length: ")), int(input("width: "))))
elif value == 2:
    print("Square triangle: ", task1_modul1.square_triangle(int(input("height: ")), int(input("base: "))))
else:
    print("Square circle: ", task1_modul1.square_circle(int(input("radius: "))))
