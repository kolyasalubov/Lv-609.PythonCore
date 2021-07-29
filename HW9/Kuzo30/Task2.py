class Car:
    def __init__(self, name, kind, model):
        self.name = name
        self.kind = kind
        self.model = model

    def start(self):
        print(f"{self.name}, you just started {self.kind} {self.model}")

    def stop(self):
        print(f"{self.name}, you just stopped {self.kind} {self.model}")


if __name__ == "__main__":
    BMW_X5 = Car("Yura", "BMW", "X5")
    BMW_X5.start()
    BMW_X5.stop()
