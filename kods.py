import json
from tabulate import tabulate

# Faila nosaukums rezultātu glabāšanai
REZULTĀTU_FAILS = "rezultati.json"

# Valūtu kursi pret EUR
valūtas_kursi = {
    "GBP": 0.86,  # Britu mārciņa
    "CHF": 0.92,  # Šveices franks
    "NOK": 11.5,  # Norvēģijas krona
    "CZK": 25.3,  # Čehijas krona
    "PLN": 4.55,  # Polijas zloti
    "DKK": 7.45   # Dānijas krona
}

# Funkcija ievaddatu validācijai (jābūt skaitlim)
def iegūt_skaitli(ziņojums):
    while True:
        ievade = input(ziņojums)
        try:
            return float(ievade)
        except ValueError:
            print("Lūdzu, ievadi skaitli!")

# Funkcija izvēles validācijai
def iegūt_izvēli():
    while True:
        izvēle = input("Izvēlies opciju (1 - no EUR uz citu, 2 - no citas valūtas uz EUR): ")
        if izvēle in ["1", "2"]:
            return izvēle
        print("Nederīga izvēle. Mēģini vēlreiz.")

# Sagatavo rezultātu glabāšanas sarakstu
rezultāti = []

# Lietotāja izvēles apstrāde
izvēle = iegūt_izvēli()

# Ja izvēlēts pārveidot no EUR uz citām valūtām
if izvēle == "1":
    summa = iegūt_skaitli("Ievadi summu EUR: ")

    # Iterē caur valūtu kursiem un aprēķina rezultātu
    for valūtas_kods, kurss in valūtas_kursi.items():
        rezultāts = summa * kurss
        rezultāti.append(["EUR", valūtas_kods, f"{rezultāts:.2f} {valūtas_kods}"])

# Ja izvēlēts pārveidot no citas valūtas uz EUR
elif izvēle == "2":
    summa = iegūt_skaitli("Ievadi summu svešvalūtā: ")

    # Iterē caur valūtu kursiem un aprēķina rezultātu
    for valūtas_kods, kurss in valūtas_kursi.items():
        rezultāts = summa / kurss
        rezultāti.append([valūtas_kods, "EUR", f"{rezultāts:.2f} EUR"])

# Izvade tabulas formātā
print(tabulate(rezultāti, headers=["No", "Uz", "Rezultāts"], tablefmt="grid"))

# Saglabā rezultātus JSON failā
arhīvs = []
try:
    with open(REZULTĀTU_FAILS, "r", encoding="utf-8") as f:
        arhīvs = json.load(f)
except FileNotFoundError:
    pass  # Fails neeksistē, sāksim ar tukšu sarakstu

# Pievieno jaunos rezultātus un saglabā failā
arhīvs.extend(rezultāti)
with open(REZULTĀTU_FAILS, "w", encoding="utf-8") as f:
    json.dump(arhīvs, f, ensure_ascii=False, indent=4)
