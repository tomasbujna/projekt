sklad = {
    "jablko": {"cena": 1.50, "počet": 20},
    "chleba": {"cena": 1.20, "počet": 10},
    "mlieko": {"cena": 0.95, "počet": 15}
}

kosik = []

def aplikujZlavu(cena):
    print("\nDostupné kupóny: ZLAVA10 (10% zľava), ZLAVA20 (20% zľava)")
    kupon = input("Zadaj zľavový kupón (alebo stlač Enter pre pokračovanie): ").strip().upper()
    
    if kupon == "ZLAVA10":
        print("✓ Kupón aplikovaný: 10% zľava!")
        return cena * 0.9
    elif kupon == "ZLAVA20":
        print("✓ Kupón aplikovaný: 20% zľava!")
        return cena * 0.8
    elif kupon != "":
        print("× Neplatný kupón, pokračuje sa bez zľavy.")
    
    return cena

print("Vitaj v obchode!")

while True:
    print("\nDostupný tovar:")
    for nazov, info in sklad.items():
        print(f"- {nazov}: {info['cena']}€ (na sklade: {info['počet']} ks)")

    volba = input("\nZadaj názov tovaru (alebo napíš 'koniec'): ").lower()

    if volba == 'koniec':
        break

    if volba in sklad and sklad[volba]["počet"] > 0:
        kosik.append({"nazov": volba, "cena": sklad[volba]["cena"]})
        sklad[volba]["počet"] -= 1
        print(f"'{volba}' bol pridaný do košíka.")
    else:
        print("Tento tovar nie je dostupný alebo neexistuje.")

# Zhrnutie nákupu
print("\n--- ZHRNUTIE NÁKUPU ---")
celkova_suma = 0

for polozka in kosik:
    print(f"- {polozka['nazov']}: {polozka['cena']}€")
    celkova_suma += polozka['cena']

print(f"Suma pred zľavou: {celkova_suma:.2f}€")

# Volanie funkcie na zľavu
celkova_suma = aplikujZlavu(celkova_suma)

print(f"Spolu k úhrade: {celkova_suma:.2f}€")
print("Ďakujem za nákup!")
