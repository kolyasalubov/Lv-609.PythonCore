class Employee(object):
    _counter = 0
    _emp_dict = list()

    def __init__(self, name, salary):
        Employee._counter += 1
        self.name = name
        self.salary = salary
        Employee._emp_dict += [[name, salary]]

    def __base__(self):
        print("My class is inherited from \"object\" class")

    def __dict__(self):
        print("'__init__': <slot wrapper '__init__' of 'object' objects>\n"
              "'__base__': 'When called, it accepts no arguments and returns a class from which the employee class is inherited\n"
              "'__dict__': tells about every single method in class\n"
              "'__name__': returns name of class\n"
              "'__module__': returns name of module where class is\n"
              "'__doc__': returns doc-string about Employee class\n"
              "'emp_amount': returns amount of employees(objects of class)\n"
              "'emp_info': returns info about every single employee\n"
              "'_counter': private variable to count employees\n"
              "'_emp_dict': private variable to contain info about every single employee(name and salary)\n")

    def __name__(self):
        print("Employee")

    def __module__(self):
        print("Task4.py")

    def __doc__(self):
        print("My own class\n\n Call '__dict__' to know about every method")

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
    e3.__dict__()
