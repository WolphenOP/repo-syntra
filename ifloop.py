# input vragen
getal = int(input("Geef getal: "))

# elif loop
if getal < 10:
    print(f"{getal} is kleiner dan 10.")
elif getal > 1000:
    print(f"{getal} is groter dan 1000.")
elif getal > 100:
    print(f"{getal} is groter dan 100 maar kleiner dan 1000.")
elif getal > 10:
    print(f"{getal} is groter dan 10, maar kleiner dan 100.")
else:
    print(f"{getal} is exact 10.")
