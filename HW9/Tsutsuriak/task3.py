class Employee:
    '''This is class Employee'''
    counter = 0
    list_of_employee = []

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        a = [self.name, self.salary]
        Employee.counter +=1
        Employee.list_of_employee.append(a)
        
    def counter_employee(self):
        return f'Total numbers of employees: {Employee.counter}'

    def Information(self):
        return Employee.list_of_employee

emp1 = Employee("Ivan", 100)
emp2 = Employee("Petro", 150)
emp3 = Employee("Vasyl", 125)

print(Employee.counter)
print(emp1.counter_employee())
print(*emp1.Information())

print(f'Employee __base__: {Employee.__base__}')
print(f'Employee __dict__: {Employee.__dict__}')
print(f'Employee __name__: {Employee.__name__}')
print(f'Employee __module__: {Employee.__module__}')
print(f'Employee __doc__: {Employee.__doc__}')
