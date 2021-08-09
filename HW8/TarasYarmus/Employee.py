class Employee:
    number_of_employers = 0
    employers = list()
    def __init__(self, name, salary):
        self.n = name
        self.s = salary
        Employee.number_of_employers += 1
        Employee.employers += [name, salary]

    def __str__(self):
        return f'Загальна кількість працівників: {number_of_employers}.'

    def __str__(self):
        for i in range(Employee.number_of_employers):
            print(f'Працівник: {Employee.employers[0]} | Заробітня плата: {Employee.employers[1]}')