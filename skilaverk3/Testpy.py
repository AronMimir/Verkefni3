from nemi import Hermannanemi, Flokkstjorannemi, Foringjanemi

def display_nemendur(nemendur):
    for nemi in nemendur:
        print(nemi)

def count_kyn(nemendur):
    kk_count = sum(1 for nemi in nemendur if nemi.kyn == "kk")
    kvk_count = sum(1 for nemi in nemendur if nemi.kyn == "kvk")
    other_count = len(nemendur) - kk_count - kvk_count
    print(f"KK nemendur: {kk_count}")
    print(f"KVK nemendur: {kvk_count}")
    print(f"Aðrir: {other_count}")

def filter_by_initial(initial, nemendur):
    filtered_nemendur = [nemi for nemi in nemendur if nemi.nafn.startswith(initial)]
    for nemi in filtered_nemendur:
        print(nemi)
def display_flokkstjorar(flokkstjorar):
    for nemi in flokkstjorar:
        print(nemi)

def find_landher(flokkstjorar):
    landher_nemendur = [nemi for nemi in flokkstjorar if nemi.her == "landher"]
    for nemi in landher_nemendur:
        print(f"Nafn: {nemi.nafn}, Herdeild: {nemi.herdeild}, Simi: {nemi.simanumer}")

def find_eldri_enn_20(flokkstjorar):
    current_year = 2024
    elder_than_20 = [nemi for nemi in flokkstjorar if int(nemi.kennitala[:2]) < current_year - 20]
    for nemi in elder_than_20:
        print(f"Nafn: {nemi.nafn}, Kennitala: {nemi.kennitala}")
def display_foringjar(foringjar):
    for nemi in foringjar:
        print(nemi)

def herlan_debtors(foringjar):
    debtors = [(nemi.nafn, nemi.herlan) for nemi in foringjar if nemi.herlan > 0]
    for debtor in debtors:
        print(f"Nafn: {debtor[0]}, Herlánsskuldir: {debtor[1]}")

def total_herlan_debt(foringjar):
    total_debt = sum(nemi.herlan for nemi in foringjar)
    print(f"Heildarupphæð herlánaskulda allra nemanda: {total_debt}")

def main():
    hermannanemar = [
        Hermannanemi("123456-7890", "Jón Jónsson", "kk", "1234567", "9", "1", "2022"),
        Hermannanemi("234567-8901", "Guðrún Guðmundsdóttir", "kvk", "2345678", "2", "2", "2020"),
        Hermannanemi("345678-9012", "Björn Björnsson", "kk", "3456789", "3", "3", "2021"),
        Hermannanemi("456789-0123", "Anna Jónsdóttir", "kvk", "4567890", "4", "4", "2015"),
        Hermannanemi("567890-1234", "Pétur Pétursson", "kk", "5678901", "5", "5", "2022"),
        Hermannanemi("678901-2345", "Sigríður Sigurðardóttir", "kvk", "6789012", "6", "6", "2022")
    ]

    flokkstjorar = [
        Flokkstjorannemi("123-4567", "Eiríkur Eiríksson", "kk", "1234567", "Herdeild 1", "landher"),
        Flokkstjorannemi("234-5678", "Helga Helgadóttir", "kvk", "2345678", "Herdeild 2", "sjóher"),
        Flokkstjorannemi("345-6789", "Árni Árnason", "kk", "3456789", "Herdeild 3", "flugher"),
        Flokkstjorannemi("456-7890", "Brynhildur Brynjólfsdóttir", "kvk", "4567890", "Herdeild 4", "landher"),
        Flokkstjorannemi("567-8901", "Kristján Kristjánsson", "kk", "5678901", "Herdeild 5", "sjóher"),
        Flokkstjorannemi("678-9012", "Sara Jónsdóttir", "kvk", "6789012", "Herdeild 6", "flugher")
    ]

    foringjar = [
        Foringjanemi("1234-5678", "Arnar Árnason", "kk", "1234567", "BS", 200000, 100000),
        Foringjanemi("2345-6789", "Guðrún Guðjónsdóttir", "kvk", "2345678", "MS", 250000, 150000),
        Foringjanemi("3456-7890", "Bjarni Bjarnason", "kk", "3456789", "BS", 200000, 100000),
        Foringjanemi("4567-8901", "Anna Jónsdóttir", "kvk", "4567890", "MS", 250000, 150000),
        Foringjanemi("5678-9012", "Pétur Pétursson", "kk", "5678901", "BS", 200000, 100000),
        Foringjanemi("6789-0123", "Sigrún Sigurðardóttir", "kvk", "6789012", "MS", 250000, 150000)
    ]

    while True:
        print("Veldu flokk af nemendum:")
        print("1. Hermannanemar")
        print("2. Flokkstjóranemar")
        print("3. Foringjanemar")
        print("4. Hætta")

        val = input("Veldu flokk: ")

        if val == "1":
            print("\n1. Prenta út alla Hermannanemar")
            print("2. Prenta út fjölda kk nemanda, kvk nemanda og aðra")
            print("3. Leita að Hermannanemum eftir upphafsstaf")
            print("4. Hætta")
            val2 = input("Veldu aðgerð: ")
            if val2 == "1":
                display_nemendur(hermannanemar)
            elif val2 == "2":
                count_kyn(hermannanemar)
            elif val2 == "3":
                initial = input("Stafur til að leita eftir: ")
                filter_by_initial(initial, hermannanemar)
            elif val2 == "4":
                print("Hætt í Hermannanemar")
            else:
                print("Ógild valmynd, vinsamlegast veldu aftur.")
        elif val == "2":
            print("\n1. Prenta út alla Flokkstjóranemar")
            print("2. Finna þá nemendur sem eru í landhernum")
            print("3. Finna alla sem eru eldri en 20 ára")
            print("4. Hætta")
            val2 = input("Veldu aðgerð: ")
            if val2 == "1":
                display_flokkstjorar(flokkstjorar)
            elif val2 == "2":
                find_landher(flokkstjorar)
            elif val2 == "3":
                find_eldri_enn_20(flokkstjorar)
            elif val2 == "4":
                print("Hætt í Flokkstjóranemar")
            else:
                print("Ógild valmynd, vinsamlegast veldu aftur.")
        elif val == "3":
            print("\n1. Prenta út alla Foringjanemar")
            print("2. Nafn og upphæð hjá þeim sem skulda herlán")
            print("3. Heildarupphæð herlánaskulda allra nemanda")
            print("4. Hætta")
            val2 = input("Veldu aðgerð: ")
            if val2 == "1":
                display_foringjar(foringjar)
            elif val2 == "2":
                herlan_debtors(foringjar)
            elif val2 == "3":
                total_herlan_debt(foringjar)
            elif val2 == "4":
                print("Hætt í Foringjanemar")
            else:
                print("Ógild valmynd, vinsamlegast veldu aftur.")

        elif val == "4":
            print("Hætt í forriti.")
            break
        else:
            print("Ógild valmynd, vinsamlegast veldu aftur.")

if __name__ == "__main__":
    main()