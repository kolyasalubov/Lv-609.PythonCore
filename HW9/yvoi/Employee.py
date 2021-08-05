class Employee:
    """This is employee class
    it can return info about number of employees
    also it can return info about each employee"""
    number_of_employees = 0
    name: str
    salary: int

    def __init__(self, name, salary):
        Employee.number_of_employees += 1
        self.name = name
        self.salary = salary

    def info(self):
        print(f'{self.name}\'s salary is {self.salary}')


first = Employee("Yura", 50000)
second = Employee("Nika", 500000)
third = Employee("Dana", 1234)

second.info()
print(Employee.number_of_employees)
