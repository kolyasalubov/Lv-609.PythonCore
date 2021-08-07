class Employee:
    counter_of_employee= 0
    list_of_employee = []

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        info_of_employee = [self.name, self.salary]
        Employee.counter_of_employee += 1
        Employee.list_of_employee.append(info_of_employee)
        
    def general_counter_empl(self):
        return f'{Employee.counter_of_employee} - it is numbers of employees'

    def general_info(self):
        return Employee.list_of_employee
    
    
person1 = Employee("Den", 35000)
person2 = Employee("Anna", 45000)


# print(Employee.counter_of_employee)
# print(person1.general_counter_empl())
# print(person2.general_info())

print(f'Employee __base__: {Employee.__base__}')
print(f'Employee __dict__: {Employee.__dict__}')
print(f'Employee __name__: {Employee.__name__}')
print(f'Employee __module__: {Employee.__module__}')
print(f'Employee __doc__: {Employee.__doc__}')