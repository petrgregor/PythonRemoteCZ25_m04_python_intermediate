import pickle
from datetime import date

from p05_OOP_methods import Person


if __name__ == "__main__":
    person1 = Person("Radek", "Svobodný", date(1998, 10, 12))
    person2 = Person("Eva", "Svobodová", date(1997, 5, 6))
    persons = [person1, person2]

    with open("dump/persons.pickle", "wb") as f:
        pickle.dump(persons, f)

