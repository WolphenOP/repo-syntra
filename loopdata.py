# Loper toevoegen
def voeg_loper_toe(lopers, afstanden):
    naam = input("Geef de naam van de loper: ")
    lopers.append(naam)
    afstanden.append([])
# Loper verwijderen
def verwijder_loper(lopers, afstanden):
    naam = input("Geef de naam van de loper die je wilt verwijderen: ")
    if naam in lopers:
        index = lopers.index(naam)
        del lopers[index]  # Verwijder loper
        del afstanden[index]  # Verwijder bijbehorende afstanden
        print(f"Loper '{naam}' is verwijderd.")
    else:
        print(f"Loper '{naam}' bestaat niet.")
# Afstand toevoegen
def voeg_afstand_toe(lopers, afstanden):
    naam = input("Geef de naam van de loper: ")
    afstand = float(input("Voer de afstand in kilometers in: "))
    if naam in lopers:
        index = lopers.index(naam)
        afstanden[index].append(afstand)  # Voeg afstand toe aan de juiste loper
    else:
        print(f"Loper '{naam}' bestaat niet.")
# Totaal per dag
def afstand_per_dag(afstanden):
    dagen = max(len(a) for a in afstanden)  # Max aantal dagen
    totalen_per_dag = [0] * dagen

    for dag in range(dagen):
        for afstanden_loper in afstanden:
            if dag < len(afstanden_loper):
                totalen_per_dag[dag] += afstanden_loper[dag]

    return totalen_per_dag
# Totale afstand
def totale_afstand(afstanden):
    totaal = 0
    for afstanden_loper in afstanden:
        totaal += sum(afstanden_loper)
    return totaal
# Stats
def statistieken(totalen_per_dag):
    totaal = sum(totalen_per_dag)
    gemiddeld = totaal / len(totalen_per_dag) if totalen_per_dag else 0
    min_afstand = min(totalen_per_dag) if totalen_per_dag else 0
    max_afstand = max(totalen_per_dag) if totalen_per_dag else 0

    print("\nStatistieken per dag:")
    print(f"Totaal: {totaal}")
    print(f"Gemiddeld: {gemiddeld:.2f}")
    print(f"Minimum: {min_afstand}")
    print(f"Maximum: {max_afstand}")

# Define main
def main():
    lopers = []  # Lijst om lopers bij te houden
    afstanden = []  # Lijst om afstanden bij te houden

    while True:
        keuze = input("\nKies een optie: \n1. Voeg loper toe \n2. Verwijder loper \n3. Voeg afstand toe \n4. Toon totalen \n5. Toon statistieken \n6. Stop \nKies een optie (1-6): ")

        if keuze == '1':
            voeg_loper_toe(lopers, afstanden)
        elif keuze == '2':
            verwijder_loper(lopers, afstanden)
        elif keuze == '3':
            voeg_afstand_toe(lopers, afstanden)
        elif keuze == '4':
            for i in range(len(lopers)):
                print(f"{lopers[i]} heeft in totaal {sum(afstanden[i])} km gelopen.")
            totaal = totale_afstand(afstanden)
            print(f"Totaal gelopen door alle lopers: {totaal} km")
        elif keuze == '5':
            totalen_per_dag = afstand_per_dag(afstanden)
            statistieken(totalen_per_dag)
        elif keuze == '6':
            print("Programma gestopt.")
            break
        else:
            print("Ongeldige keuze. Probeer het opnieuw.")

if __name__ == "__main__":
    main()
