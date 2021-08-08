class Employee(object):
    _counter = 0
    _emp_dict = list()

    def __init__(self, name, salary):
        Employee._counter += 1
        self.name = name
        self.salary = salary
        Employee._emp_dict += [[name, salary]]

    def emp_amount(self):
        print(f"You have {Employee._counter} employees")

    def emp_info(self):
        for i in range(Employee._counter):
            print(f"Employee {Employee._emp_dict[i][0]} gets {Employee._emp_dict[i][1]}$")


if __name__ == "__main__":
    e1 = Employee("Carl", 1300)
    e2 = Employee("David", 12123)
    e3 = Employee("Yura", 1254)
    Employee.emp_info(Employee)
