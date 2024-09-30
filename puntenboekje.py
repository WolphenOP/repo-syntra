from colorama import init, Fore, Style

init()

# Leerlingen toevoegen
def voeg_leerling_toe(namen, punten_lijsten):
    naam = input("Geef de naam van de leerling: ")
    punten = []
    vakken = ["Wiskunde", "Nederlands", "Geschiedenis", "Biologie", "Engels"]
    for vak in vakken:
        punt = input(f"Geef het punt voor {vak} (0-10): ")
        # Controleer of het punt een geldig nummer is tussen 0 en 10
        while not punt.isdigit() or not (0 <= int(punt) <= 10):
            punt = input("Voer een geldig punt in tussen 0 en 10: ")

        punten.append(int(punt))  # Voeg het punt toe aan de lijst als integer

    # Voeg de naam en punten toe aan de lijsten
    namen.append(naam)
    punten_lijsten.append(punten)

# Bereken resultaten
def toon_resultaten(namen, punten_lijsten):
    vakken = ["Wiskunde", "Nederlands", "Geschiedenis", "Biologie", "Engels"]
    # Print de header van de tabel
    print("\n\n")
    print(f"{'Leerling':<30}", end="")
    for vak in vakken:
        print(f"{vak:<15}", end="")
    print(f"{'Totaal':<10}{'Gemiddelde':<15}")
    print("\n")

    totaal_per_vak = [0] * len(vakken)
    totaal_leerlingen = len(namen)

    for index, naam in enumerate(namen):
        punten = punten_lijsten[index]
        totaal = sum(punten)
        gemiddelde = totaal / len(punten)
        # Naam en punten
        print(f"{naam:<30}", end="")
        for punt in punten:
            if punt < 5:
                print(f"{Fore.RED}{punt:<15}{Style.RESET_ALL}", end="")  # Rood voor buis
            else:
                print(f"{punt:<15}", end="")

        # Totaal en gemiddelde
        gemiddelde_kleur = f"{Fore.RED}{gemiddelde:.1f}{Style.RESET_ALL}" if gemiddelde < 5 else f"{gemiddelde:.1f}"
        print(f"{totaal:<10}{gemiddelde_kleur:<15}")

        # Optellen voor gemiddelde per vak
        for i in range(len(punten)):
            totaal_per_vak[i] += punten[i]

    # Print gemiddelden per vak
    print("\n")
    print(f"{'Gemiddelde per vak ':<30}", end="")
    for totaal in totaal_per_vak:
        print(f"{totaal / totaal_leerlingen:<15.1f}", end="")
    print()

# Main functie
def main():
    namen = []
    punten_lijsten = []

    while True:
        voeg_leerling_toe(namen, punten_lijsten)
        meer_leerlingen = input("Wilt u nog een leerling toevoegen? (ja/nee): ")
        if meer_leerlingen.lower() != 'ja':
            break

    toon_resultaten(namen, punten_lijsten)

if __name__ == "__main__":
    main()
