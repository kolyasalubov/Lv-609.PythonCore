class Employee():
    counter = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.counter += 1

    def total_number(self):
        print(f'The total amount of the employees is {Employee.counter}')

    def display_info(self):
        print(f'Employee {self.name} has {self.salary} salary')


emp1 = Employee('Anna', 12345)
emp2 = Employee('Bob', 1234)
emp1.total_number()
print(Employee.counter)

print(f'Employee __base__:  {Employee.__base__}')
print(f'Employee __dict__: {Employee.__dict__}')
print(f'Instance dict : {emp1.__dict__}')
print(f'Employee __name__: {Employee.__name__}')
print(f'Employee __module__: {Employee.__module__}')
print(f'Employee __doc__: {Employee.__doc__}')
