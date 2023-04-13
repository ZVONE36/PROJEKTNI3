def ispis_kartice(kartica):
    print("Informacije o kartici: ")
    print(f"\t IBAN: {kartica['iban']}")
    print(f"\t Pin: {kartica['pin']}")
    print(f"\t Korisnicki broj: {kartica['k_broj']}")