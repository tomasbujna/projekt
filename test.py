# Definícia skladu: položka -> {kategória, cena, počet kusov}
sklad = {
    "jablko": {"kategória": "Ovocie", "cena": 1.50, "počet": 20},
    "chleba": {"kategória": "Pečivo", "cena": 1.20, "počet": 10},
    "mlieko": {"kategória": "Mliečne výrobky", "cena": 0.95, "počet": 15},
    "tričko": {"kategória": "Oblečenie", "cena": 12.99, "počet": 5},
    "pero": {"kategória": "Kancelária", "cena": 0.75, "počet": 30}
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

    # Výber od používateľa
    volba = input("\nZadaj názov tovaru, ktorý chceš vložiť do košíka (alebo napíš 'koniec' pre ukončenie nákupu): ").strip()

    if volba.lower() == 'koniec':
        break

    # Kontrola, či tovar existuje v sklade
    if volba in sklad:
        if sklad[volba]["počet"] > 0:
            # Pridáme do košíka a odrátame zo skladu
            kosik.append({"nazov": volba, "cena": sklad[volba]["cena"]})
            sklad[volba]["počet"] -= 1
            print(f"'{volba}' bol úspešne pridaný do košíka.")
        else:
            print(f"Ľutujem, ale '{volba}' je momentálne vypredaný.")
    else:
        print("Tento tovar sa nenachádza v ponuke. Skús to znova.")

# Ukončenie nákupu a vyúčtovanie
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