import pickle

try:
    with open("dump/persons.pickle", "rb") as f:
        persons = pickle.load(f)
        print(persons)
        for person in persons:
            print(person)
except FileNotFoundError as e:
    print(e)

print("Konec")
