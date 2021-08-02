class Human():
    species = 'Homosapiens'

    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f'Hello, {self.name}')

    @classmethod
    def species(cls):
        print(f'{cls} is {cls.species}')

    @staticmethod
    def smth():
        print('Meaningless message.')


hum1 = Human('Bob')
hum1.greeting()
hum1.species()
hum1.smth()
