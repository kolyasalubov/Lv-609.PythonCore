class Human:
    species = "Homosapiens"

    def __init__(self,name) -> None:
        self.name = name
    
    def greet(self):
        print(f'Hello, {self.name}')
    
    @classmethod
    def species(cls):
        return f'{Human.species}'
    
    @staticmethod
    def message():
        print('Python')