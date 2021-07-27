class Polygon:
    def __init__(self, count_sides):
        self.n = count_sides
        self.sides = set()

    def input_sides(self):
        for i in range(self.n):
            self.sides.add(float(input(f"Enter side {str(i + 1)}: ")))

    def show_sides(self):
        for i in range(len(self.sides)):
            print("Side", i + 1, "is", list(self.sides)[i])


class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)

    def find_area(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print(f'The area of the triangle is {round(area, 2)}')


class Rectangle(Polygon):
    def __init__(self, count_of_sides):
        self.sides_count = count_of_sides
        Polygon.__init__(self, count_of_sides)

    def find_area(self):
        if len(self.sides) == 2:
            print(f'Area of your rectangle: {list(self.sides)[0] * list(self.sides)[1]}')
        else:
            print("Enter valid rectangle!")


if __name__ == "__main__":
    rect = Rectangle(4)
    rect.input_sides()
    rect.show_sides()
    rect.find_area()