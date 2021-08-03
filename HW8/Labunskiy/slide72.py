class Human:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f"Hello {self.name}!")

    def species(self):
        print(f"{self.name} is Homosapiens")

    @staticmethod
    def arbitrary_message():
        message = input('Enter arbitrary message : ')
        print(message)


if __name__ == "__main__":
    yura = Human("Liubov")
    yura.hello()
    yura.species()
    yura.arbitrary_message()   