
class Polygon:
    def __init__(self, no_of_side):
        self.n = no_of_side
        self.sides = [0 for i in range (no_of_side)]
    def inputSides (self):
        self.sides = [float (input (f'Enter side {str(i+1)}: ')) for i in range (self.n)]
    def dispSides (self):
        print ([f'Side {i+1} is {self.sides[i]}' for i in range (self.n)])

class Rectangle (Polygon):
    def __init__ (self):
        super().__init__(2)
    def findArea (self):
        a,b = self.sides
        area = a*b
        print (f'The area of rectangle is {area}')
r = Rectangle()
r.inputSides()
r.dispSides ()
r.findArea ()