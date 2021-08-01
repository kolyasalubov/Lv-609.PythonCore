class Polygon():
    
    def __init__(self, count_of_sides):
        self.n = count_of_sides
        self.sides = []
    
    def input_sides(self):
        for i in range(self.n):
            self.sides.append(int(input(f'Side {i+1}: ')))
        return self.sides
    
    def info(self):
        for i in range(self.n):
            print(f'Side {i+1} = {self.sides[i]}')
        return '=========='

class Rect(Polygon):
    def __init__(self):
        Polygon.__init__(self, 2)

    def square(self, a, b):
        return f'Square of rectangle = {a*b}'
        
rect = Rect()
print(rect.square(3, 5))
    
        