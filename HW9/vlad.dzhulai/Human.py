class Human:
    human_type = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def greetings(self):
        return f"Welcome back, {self.name}"

    @classmethod
    def species(cls):
        return f"It's a species of {Human.human_type}"

    @staticmethod
    def staticmethod():
        return "Hello!"
