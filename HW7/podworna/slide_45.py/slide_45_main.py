import slide_45_def

input_shape= input("Select a shape to calculate the square:\n1.Rectangle, \n2.Triangle, \n3.Circle\n - ")

if input_shape == "1" or input_shape == "Rectangle" or input_shape == "rectangle":
    slide_45_def.square_rectangle() 
elif input_shape == "2" or input_shape == "Triangle" or input_shape == "triangle":
    slide_45_def.square_triangle()  
elif input_shape == "3" or input_shape == "Circle" or input_shape == "circle":
    slide_45_def.square_circle()
else:
    print("The shape is entered incorrectly")

