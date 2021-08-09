class Polygon:
    def __init__(self,number_of_sides):
        self.sides = number_of_sides
        
    def inputSides(self):
        self.side_measures = [float(input(f"Enter side {i+1}:" ))for i in range(self.sides)]
    

class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2)

    def findArea(self):
        print(f'The area of your rectangle is {self.side_measures[0] * self.side_measures[1]}')

t = Rectangle()
t.inputSides()
t.findArea()