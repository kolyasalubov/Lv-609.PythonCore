import math
def  square_rectangle(a,b):
    return a*b  
def  square_triangle(ab,h):
    return 1/2*ab*h
def  square_circle (r):
    return math.pi *(r**2)
    
input_shape= input("Select a shape to calculate the square: 1.Rectangle, 2.Triangle, 3.Circle: ")
if input_shape == "1" or input_shape == "Rectangle" or input_shape == "rectangle":
    a=int(input("Enter side length of rectangle, a="))
    b=int(input("b="))
    print("Square of ​​a rectangle =", square_rectangle(a,b))
elif input_shape == "2" or input_shape == "Triangle" or input_shape == "triangle":
    ab=int(input("Enter the length of the triangle, ab="))
    h=int(input("Enter the height of the triangle, h="))
    print("Square of ​​a triangle=", square_triangle(ab,h))
elif input_shape == "3" or input_shape == "Circle" or input_shape == "circle":
    r=int(input("Enter the radius of the circle, r="))
    print("Square of ​​a circle=", square_circle(r))
else:
    print("The shape is entered incorrectly")

