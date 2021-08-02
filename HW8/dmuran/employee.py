class Employee:
    counter = 0

    def __init__(self, name, salary) -> None:
        Employee.counter += 1
        self.name = name
        self.salary = salary

    def count_of_employee(self):
        print(f'{Employee.counter}')

    def info(self):
        print(f'{self.name} has {self.salary}')


