class Vehicle:
    def __init__(self, spz):
        self.spz = spz

    def __str__(self):
        return f"Vozidlo s SPZ: {self.spz}"

    def start(self):
        print(f"Startuji vozidlo... {self}")


class Motorcycle(Vehicle):
    def __init__(self, spz, category):
        super().__init__(spz)
        self.category = category

    def __str__(self):
        return f"Motocykl s SPZ: {self.spz}, kategorie: {self.category}"

    def start(self):
        print(f"Startuji motorku... {self}")


class Car(Vehicle):
    def __init__(self, spz, number_of_doors):
        super().__init__(spz)
        self.number_of_doors = number_of_doors

    def __str__(self):
        return f"Auto s SPZ: {self.spz}, počet dveří: {self.number_of_doors}"

    def start(self):
        print(f"Startuji auto... {self}")


class SportCar(Car):
    def __init__(self, spz, number_of_doors, max_speed):
        super().__init__(spz, number_of_doors)
        self.max_speed = max_speed

    def __str__(self):
        return (f"Sportovní auto s SPZ: {self.spz}, "
                f"počet dveří: {self.number_of_doors}, "
                f"maximální rychlost: {self.max_speed}")


class Bus(Vehicle):
    def __init__(self, spz, number_of_seats):
        super().__init__(spz)
        self.number_of_seats = number_of_seats

    def __str__(self):
        return f"Bus s SPZ: {self.spz}, počet sedadel: {self.number_of_seats}"


if __name__ == "__main__":
    vehicle1 = Vehicle("AB1234")
    print(vehicle1)
    moto1 = Motorcycle("M77788", "250")
    print(moto1)
    car1 = Car("AA99885", 5)
    print(car1)
    sport_car1 = SportCar("123456", 3, 180)
    print(sport_car1)
    bus1 = Bus("BUS123", 45)
    print(bus1)

    vehicle1.start()
    vehicle2 = moto1
    vehicle2.start()
    vehicle3 = car1
    vehicle3.start()
    vehicle4 = sport_car1
    vehicle4.start()
    vehicle5 = bus1
    vehicle5.start()

    vehicles = [vehicle1, vehicle2, vehicle3, vehicle4, vehicle5]
    for vehicle in vehicles:
        print(vehicle.__repr__)
        vehicle.start()

