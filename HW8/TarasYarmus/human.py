class Human:
    def __init__(self,name):
        self.n = name

    def method(self):
        return f'Welcome {self.n}!'

    def classmethod(cls):
        return f'It is a species of Homosapiens'

    @staticmethod
    def staticmethod():
        return 'Arbitrary message in staticmethod'

h = Human('Taras')
print (h.method())
print (h.classmethod())
print (h.staticmethod())