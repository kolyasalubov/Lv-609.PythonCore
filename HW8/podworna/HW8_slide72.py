class Human:
    def __init__(self,name):
        self.name = name
    
    def displays_welcome (self):
        return f'Welcome, {self.name}'

    @classmethod
    def species(cls):
        return f'Is a species of Homosapiens'

    @staticmethod
    def general_welcom():
        return 'Welcome, Homosapiens'
    
    
person1 = Human('Den')
print(person1.displays_welcome())
print(person1.species())
print(person1.general_welcom())
    
