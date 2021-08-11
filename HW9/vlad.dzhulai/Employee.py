class Employee:
    """
    This class is showing an employee's salary,
    name and counting number of employees.
    """
    employee_count = 0

    def __init__(self, name: str, salary: int):
        Employee.employee_count += 1
        self.name = name
        self.salary = salary

    def get_name_and_salary(self):
        print(f"An employee's name is {self.name}, "
              f"and his salary is {self.salary} USD")

    @staticmethod
    def get_employee_count():
        return f"Quantity of employees is {Employee.employee_count}"


employee1 = Employee("John", 2100)
employee2 = Employee("Alex", 3000)
employee3 = Employee("Audrey", 1800)

print(Employee.get_employee_count())

print(employee2.get_name_and_salary())

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)