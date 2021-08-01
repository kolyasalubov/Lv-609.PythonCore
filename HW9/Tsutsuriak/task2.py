class Human:
    '''This is class Human'''
    species = "Human"

    def __init__(self, name):
        self.name = name
       
    def welcome(self):
        return f'Welcome {self.name}!'

    @classmethod
    def info(cls):
        if Human.species == "Human":
            return f'You are Homosapiens!'
        else:
            return f'You are not Homosapiense!'
    
    @staticmethod
    def message():
        return f'Message'

obj1 = Human('Ivan')

print(obj1.welcome())
print(obj1.info())
print(obj1.message())
