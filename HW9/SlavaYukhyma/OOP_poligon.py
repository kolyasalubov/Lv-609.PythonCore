
class Poligon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 in range(no_of_sides)]

    def input_sides(self):
        self.sides = [
            float(input(f'Enter lenght of the side {str(i+1)}: ')) for i in range(self.n)]

    def disp_sides(self):
        for i in range(self.n):
            print(f' Side {i+1} is {self.sides[i]}')


class Triangle(Poligon):
    def __init__(self):
        super().__init__(3)

    def find_area(self):
        a, b, c = self.sides
        s = (a+b+c)/2
        area = (s*(s-a)*(s-b)*(s - c))**0.5
        print(f'The area of the triangle is {area}')


# t = Triangle()
# t.input_sides()
# t.disp_sides()
# t.find_area()


class Rectangle(Poligon):
    def __init__(self):
        super().__init__(2)

    def find_area(self):
        a, b = self.sides
        area = a * b
        print(f'The area of the rectangle is {area}')


r = Rectangle()
r.input_sides()
r.disp_sides()
r.find_area()
