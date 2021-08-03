class Employee():
    """create employee"""
    counter = 0

    def __init__(self, name, salary) -> None:
        Employee.counter += 1
        self.name = name
        self.salary = salary

    def count_of_employee(self):
        print(f'{Employee.counter}')

    def info(self):
        print(f'{self.name} has {self.salary}$')


emp1 = Employee("Ivan", 100)
emp2 = Employee("Petro", 150)
emp3 = Employee("Vasyl", 125)


print(emp1.count_of_employee())
print(emp3.info())

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)
