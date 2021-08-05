import math


def square_rectangle(*a):
    a=int(input("Enter side length of rectangle, a="))
    b=int(input("b="))
    print("Square of ​​a rectangle =", a*b)
    return a*b
  
def square_triangle(*a):
    ab=int(input("Enter the length of the triangle, ab="))
    h=int(input("Enter the height of the triangle, h="))
    print("Square of ​​a triangle=", 1/2*ab*h)
    return  1/2*ab*h

def square_circle (*a):
    r=int(input("Enter the radius of the circle, r="))
    print("Square of ​​a circle=", math.pi *(math.pow(r,2)))
    return  math.pi *(math.pow(r,2))
    
