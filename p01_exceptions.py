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

print("=" * 80)
print("Konec")
