# HW6

# Write a program that calculates the square of ​​a rectangle, triangle and circle 
# (write three functions to calculate the square, and call them in the main program depending on the user's choice).

def triangle(base, height):
    square = 0.5*base*height
    return square

def rectangle(a, b):
    square = a * b
    return square

def circle(r):
    PI = 3.142
    square = PI*r**2
    return square

figure_type = input("Enter the figure type: ")

if figure_type == "triangle":
    # Ask for some parameters needed to calculate the square
    # Give the parameters into function
    triangle()

elif figure_type == "rectangle":
    # Ask for some parameters needed to calculate the square
    # Give the parameters into function
    rectangle()

else:
    # Ask for some parameters needed to calculate the square
    # Give the parameters into function
    circle()