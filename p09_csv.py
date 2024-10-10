import csv


class Employee:
    def __init__(self, names, salary, age):
        self.name, self.surname = names.split()
        self.salary = int(salary)
        self.age = int(age)

    def __repr__(self):
        return (f"Employee(name={self.name}, "
                f"surname={self.surname}, "
                f"salary={self.salary}, "
                f"age={self.age})")

    @classmethod
    def create_from_list(cls, employee_list):
        names = employee_list[0]
        salary = int(employee_list[1])
        age = int(employee_list[2])
        return cls(names, salary, age)


try:
    with open("files/employees.csv") as f:
        rows = csv.reader(f)
        next(rows)
        employees = []
        for row in rows:
            print(row)
            employees.append(Employee.create_from_list(row))
        for employee in employees:
            print(employee)

except FileNotFoundError as e:
    print(e)
