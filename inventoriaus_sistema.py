import json
import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

pdfmetrics.registerFont(
    TTFont("DejaVuSans", os.path.join(BASE_DIR, "DejaVuSans.ttf"))
)

pdfmetrics.registerFont(
    TTFont("DejaVuSans-Bold", os.path.join(BASE_DIR, "DejaVuSans-Bold.ttf"))
)

warehouse = {}
def menu():
    print("Sandėlio inventoriaus sistema")
    print("______________")
    print("1 - pridėti prekę")
    print("2 - pakeisti kiekį")
    print("3 - rodyti inventorių")
    print("4 - saugoti į failą")
    print("5 - užkrauti iš failo")
    print("6 - rodyti visą vertės sumą")
    print("7 - eksportuoti duomenis į PDF")
    print("0 - išeiti")


def add_product():
    productname = input("Įvesk prekės pavadinimą: ")
    while True:
        try:
            quantity = int(input("Įveskite kiekį: "))
            if quantity < 0:
                print("Kiekis negali būti neigiamas")
            else:
                break
        except ValueError:
            print("Įveskite sveiką skaičiu")
    while True:
        try:
            price = float(input("Įveskite kainą: "))
            if price < 0:
                print("Kaina negali būti neigiama")
            else:
                break
        except ValueError:
            print("Įveskite skaičiu")
    
    warehouse[productname] = {
        "kiekis": quantity,
        "kaina": price
    }
    print(f"Prekė {productname} sėkmingai pridėta")


def update_quantity():
    productname = input("Koks produkto pavadinimas? ")
    if productname not in warehouse:
        print("Nėra tokio produkto.")
        return
    while True:
        try:
            new_quantity = int(input("Įvesk naują kiekį: "))
            if new_quantity < 0:
                print("Kiekis turi būti teigiamas.")
            else:
                break
        except ValueError:
            print("įvesk tinkamą skaičių")
    warehouse[productname]["kiekis"] = new_quantity
    print("Kiekis pakeistas sėkmingai. ")
    
def show_inventory():
    if not warehouse:
        print("Sandėlis tuščias.")
        return
    print("Inventorius")
    print("-----------")
    for product, info in warehouse.items():
        print(f"Prekė: {product}")
        print(f"  Kiekis: {info['kiekis']}")
        print(f"  Kaina: {info['kaina']}")
        print()

def save_to_file():
    filepath = os.path.join(BASE_DIR, "warehouse.json")
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(warehouse, file, ensure_ascii=False, indent=4)

    print(f"Sandėlio duomenys sėkmingai išsaugoti: {filepath}")


def load_from_file():
    filename = input("Įveskite failo pavadinimą su .json gale: ")
    filepath = os.path.join(BASE_DIR, filename)

    if not os.path.exists(filepath):
        print(f"Failas '{filename}' neegzistuoja pagrindiniame aplanke.")
        return

    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)

    global warehouse
    warehouse = data

    print(f"Inventorius sėkmingai užkrautas iš '{filename}'.")
    
def show_total_value():
    if not warehouse:
        print("Sandėlis tuščias ")
        return

    total_value = 0
    for info in warehouse.values():
        total_value += info["kiekis"] * info["kaina"]

    print(f"Bendra sandėlio vertė: {total_value:.2f} €")

def main():
    while True:
        menu()
        choice = input("Pasirinkite veiksmą: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            update_quantity()
        elif choice == "3":
            show_inventory()
        elif choice == "4":
            save_to_file()
        elif choice == "5":
            load_from_file()
        elif choice == "6":
            show_total_value()
        elif choice == "7":
            pdfreport()
        elif choice == "0":
            confirm = input("Ar tikrai norite išeiti? (taip/ne): ").lower()
            if confirm == "taip":
                print("Programa uždaroma.")
                break
            else:
                print("Grįžtama į meniu.")
        else:
            print("Neteisingas pasirinkimas. Bandykite dar kartą.")

def pdfreport():
    if not warehouse:
        print("Sandėlis tuščias, nėra ką eksportuoti.")
        return

    pdf_file = os.path.join(BASE_DIR, "sandelis.pdf")
    c = canvas.Canvas(pdf_file, pagesize=A4)

    c.setFont("DejaVuSans", 20)
    c.drawString(200, 800, "Sandėlio inventorius")

    c.setFont("DejaVuSans-Bold", 12)
    c.drawRightString(
        A4[0] - 50,
        820,
        f"Data: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )
    x = 50
    y = 750

    c.setFont("DejaVuSans-Bold", 15)
    c.drawString(x, y, "Prekė")
    c.drawString(x + 200, y, "Kiekis")
    c.drawString(x + 300, y, "Kaina")
    y -= 20

    c.setFont("DejaVuSans", 13)
    total_value = 0
    for product, info in warehouse.items():
        c.drawString(x, y, product)
        c.drawString(x + 200, y, str(info["kiekis"]))
        c.drawString(x + 300, y, f"{info['kaina']:.2f} €")
        total_value += info["kiekis"] * info["kaina"]
        y -= 20

    y -= 10
    c.setFont("DejaVuSans-Bold", 13)
    c.drawString(x, y, f"Bendra vertė: {total_value:.2f} €")
    c.save()
    print(f"PDF sėkmingai sugeneruotas: {pdf_file}")

main()
