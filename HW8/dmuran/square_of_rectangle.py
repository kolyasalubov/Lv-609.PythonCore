class Polygon:
    def __init__(self, num_of_sides):
        self.n = num_of_sides
        self.sides = [0 for i in range(num_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : "))
                      for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side", i+1, "is", self.sides[i])


class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2)

    def findArea(self):
        a, b = self.sides
        area = a*b
        print(f'The area of the Rectangle is {area}')


A = Rectangle()
A.inputSides()
A.dispSides()
A.findArea()
# ##########################################
# Enter side 1 : 7
# Enter side 2 : 8
# Side 1 is 7.0
# Side 2 is 8.0
# The area of the Rectangle is 56.0
############################################
