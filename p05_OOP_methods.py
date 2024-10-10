from datetime import date


class Person:
    def __init__(self, name, surname, date_of_birth):
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth

    def __repr__(self):
        return f"Person(name={self.name}, surname={self.surname}, date_of_birth={self.date_of_birth})"

    def __str__(self):
        return f"{self.name} {self.surname} ({self.age()})"

    def __eq__(self, other):
        if (self.name == other.name and
                self.surname == other.surname and
                self.date_of_birth == other.date_of_birth):
            return True
        return False

    def age(self):
        today = date.today()
        return round((today - self.date_of_birth).days/365, 0)

    @staticmethod
    def is_name_correct(name):
        return name[0].isupper() and len(name) > 3

    @classmethod
    def create_from_string(cls, sentence):
        name, surname, date_of_birth_str = sentence.split()
        year, month, day = date_of_birth_str.split('-')
        date_of_birth = date(int(year), int(month), int(day))
        return cls(name, surname, date_of_birth)


if __name__ == "__main__":
    person1 = Person("Martin", "Novák", date(2000, 10, 12))
    print(person1)
    person2 = Person("Lenka", "Dvorská", date(1998, 5, 4))
    print(person2)
    persons = [person1, person2]
    print(persons)
    person3 = Person("Martin", "Novák", date(2000, 10, 12))
    if person1 == person3:
        print(f"{person1} == {person3}")
    else:
        print(f"{person1} != {person3}")
    if person1 == person2:
        print(f"{person1} == {person2}")
    else:
        print(f"{person1} != {person2}")

    print(f"{person1} má věk {person1.age()}")

    print("=" * 80)
    print("Statická metoda:")
    name = "Martin"
    print(f"Je '{name}' správně? {person1.is_name_correct(name)}")
    print(f"Je '{name}' správně? {Person.is_name_correct(name)}")
    #print(f"{Person.age()}")  # TypeError: Person.age() missing 1 required positional argument: 'self'

    print("=" * 80)
    print("Třídní metoda")
    sentence = "Adam Bernau 1985-03-02"
    person4 = Person.create_from_string(sentence)
    print(person4)
    try:
        person5 = Person.create_from_string("Bedřich")
    except ValueError as e:
        print(e)

    print("Konec")
