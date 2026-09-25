sklad = {
    "jablko": {"kategória": "Ovocie", "cena": 1.50, "počet": 20},
    "chleba": {"kategória": "Pečivo", "cena": 1.20, "počet": 10},
    "mlieko": {"kategória": "Mliečne výrobky", "cena": 0.95, "počet": 15},
    "tričko": {"kategória": "Oblečenie", "cena": 12.99, "počet": 5},
    "pero": {"kategória": "Kancelária", "cena": 0.75, "počet": 30}
}

kupony = {
    "ZLAVA10": {"zlava": 0.10, "limit": 1},
    "ZLAVA20": {"zlava": 0.20, "limit": 1},
    "ZLAVA25": {"zlava": 0.25, "limit": 1}
}

kosik = []

print("Vitaj v našom obchode!")

while True:
    print("\n--- DOSTUPNÝ SKLAD ---")
    print(f"{'Položka':<10} | {'Kategória':<17} | {'Cena':<6} | {'Na sklade':<10}")
    print("-" * 53)
    for nazov, info in sklad.items():
        print(f"{nazov:<10} | {info['kategória']:<17} | {info['cena']:>5.2f}€ | {info['počet']:>9}")
    print("-" * 53)

    volba = input("\nZadaj názov tovaru, ktorý chceš vložiť do košíka (alebo napíš 'koniec' pre ukončenie nákupu): ").strip()

    if volba.lower() == 'koniec':
        break

    if volba in sklad:
        if sklad[volba]["počet"] > 0:
            kosik.append({"nazov": volba, "cena": sklad[volba]["cena"]})
            sklad[volba]["počet"] -= 1
            print(f"'{volba}' bol úspešne pridaný do košíka.")
        else:
            print(f"Ľutujem, ale '{volba}' je momentálne vypredaný.")
    else:
        print("Tento tovar sa nenachádza v ponuke. Skús to znova.")

while True:
    print("Máte kupón?")
    odpoved = input("áno/nie): ").strip().lower()
    if odpoved == "áno":
        print("Zadaj kupón:")
        kupón = input().strip().upper()
        if kupón in kupony:
            if kupony[kupón]["limit"] > 0:
                kupony[kupón]["limit"] -= 1
                break
            else:
                print("Tento kupón už bol použitý.")
        else:
            print("Neplatný kupón. Skús to znova.")
    elif odpoved == "nie":
        break
            


print("\n" + "="*30)
print("       ZHRNUTIE NÁKUPU       ")
print("="*30)

if not kosik:
        print("Váš košík je prázdny.")
else:
    celkova_suma = 0
    print("Zakúpené položky:")
    for polozka in kosik:
        print(f"- {polozka['nazov']}: {polozka['cena']:.2f}€")
        celkova_suma += polozka['cena']
    
    print("-" * 30)
    print(f"Spolu k úhrade: {celkova_suma:.2f}€")
    print("Ďakujem za nákup a prajem pekný deň!")
