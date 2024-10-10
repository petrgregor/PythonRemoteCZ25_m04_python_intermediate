class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"


# inheritance (dědičnost)
class Employee(Person):
    def __init__(self, name, age, rate, num_of_hours):
        super().__init__(name, age)
        self.rate = rate
        self.num_of_hours = num_of_hours

    def show_finance(self):
        return self.rate * self.num_of_hours


os1 = Person("John", 54)
os2 = Employee("Jack", 36, 20, 160)
print(os1)
print(f"os1.name: {os1.name}")
print(os2)
print(f"os2.name: {os2.name}")

print("-" * 80)


# dekompozition (dekompozice)
class Student:
    def __init__(self, name, age, scholarship):
        self.person = Person(name, age)
        self.scholarship = scholarship

    def show_finance(self):
        return self.scholarship


os3 = Student("Agatha", 22, 1000)
print(os3.person)
print(f"os3.name: {os3.person.name}")
