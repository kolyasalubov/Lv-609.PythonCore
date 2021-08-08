import def1 

value = int(input("1-square rectangle, 2-square triangle, 3-square circle: "))

if value == 1:
    print("Square rectangle: ", def1.square_rectangle(int(input("length: ")), int(input("width: "))))
elif value == 2:
    print("Square triangle: ", def1.square_triangle(int(input("height: ")), int(input("base: "))))
else:
    print("Square circle: ", def1.square_circle(int(input("radius: "))))