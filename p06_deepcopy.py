from copy import deepcopy


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"Person(name={self.name}, surname={self.surname})"


if __name__ == "__main__":
    person1 = Person("Adam", "Bernau")
    print(person1)
    person2 = person1
    print(person2)
    person1.surname = "Novák"
    print(f"person1: {person1}")
    print(f"person2: {person2}")
    person1_deep_copy = deepcopy(person1)
    person1.surname = "Svoboda"
    print(f"person1: {person1}")
    print(f"person1_deep_copy: {person1_deep_copy}")
