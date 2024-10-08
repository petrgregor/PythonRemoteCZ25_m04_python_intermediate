from math import log

a = 3
b = [1, 0, 2]
for elem in b:
    if elem != 0:
        result = a / elem
        print(f"{a}/{elem} = {result}")
    else:
        print("Error: dělení nulou.")

print("-" * 80)

for elem in b:
    try:
        result = a / elem
        print(f"{a}/{elem} = {result}")
    except ZeroDivisionError:
        print("Error: dělení nulou.")

print("-" * 80)

i = 0
while i < 4:
    try:
        result = a / b[i]
        print(f"{a}/{b[i]} = {result}")
        #i += 1
    except ZeroDivisionError:
        print("Error: Dělení nulou.")
        #i += 1
    except IndexError:
        print("Error: index mimo rozsah.")
        #i += 1
    finally:
        i += 1

print("-" * 80)


def divide1(a, b):
    if b != 0:
        return a/b
    return None


def divide2(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return None


def divide3(a, b):
    return a/b


def divide_all(a, b_list):
    for elem in b_list:
        try:
            result = divide3(a, elem)
            print(f"{a}/{elem} = {result}")
        except ZeroDivisionError:
            print("Error: dělení nulou")
        except TypeError:
            print("Error: TypeError")


def divide_all2(a, b_list):
    for elem in b_list:
        result = divide3(a, elem)
        print(f"{a}/{elem} = {result}")


b_list = [1, 2, 3, 0, 5, 6, 7, "8", "Ahoj"]
divide_all(12, b_list)
print("-" * 40)
try:
    divide_all2(25, b_list)
except ZeroDivisionError:
    print("Error: nelze dělit nulou.")

num1 = -16
print(f"sqrt({num1}) = {num1 ** (1/2)}")
try:
    print(f"log({num1}) = {log(num1)}")
except ValueError:
    print("Error: nelze počítat logaritmus pro záporné číslo.")

print("-" * 80)


def sqrt(num):
    if num < 0:
        raise ValueError("Nelze počítat odmocninu ze záporného čísla.")
    return num ** (1/2)


numbers = [16, 4, 1, 0, -4, 4.4]
for number in numbers:
    try:
        print(f"sqrt({number}) = {sqrt(number)}")
    except ValueError as e:
        print(f"number = {number}: {e}")


class NegativeNumberError(Exception):
    def __init__(self):
        message = "Nelze počítat odmocninu ze záporného čísla."
        super().__init__(message)


def sqrt(number):
    if number < 0:
        raise NegativeNumberError()
    return number ** (1/2)


numbers = [0, 1, 4, 16, -4, -16, 25, 36]
for number in numbers:
    try:
        print(f"sqrt({number}) = {sqrt(number)}")
    except NegativeNumberError as e:
        print(f"ERROR pro parametr '{number}': NegativeNumberError: repr='{repr(e)}', str='{str(e)}'")

print("=" * 80)
print("Konec")
