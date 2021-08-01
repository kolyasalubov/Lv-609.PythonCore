class Employer(object):
    count = 0
    emp_info = list()

    def __init__(self, name, salary):
        Employer.count += 1
        self.name = name
        self.salary = salary
        Employer.emp_info += [[name, salary]]

    def amount(self):
        print(f"Count: {Employer.count}")

    def info(self):
        for i in range(Employer.count):
            print(f"{Employer.emp_info[i][0]}: {Employer.emp_info[i][1]}")
