
from met import *
from instances import *
import datetime
from datetime import datetime


def datum_be():
    datum_str = input("Adja meg a dátumot (ÉÉÉÉ-HH-NN formátumban): ")
    try:
        return datetime.strptime(datum_str, '%Y-%m-%d')
    except ValueError:
        print("Érvénytelen dátumformátum.")
        return None


def main():
    szalloda = Szalloda("Példa Hotel")
    szalloda.szoba_hozzaad(Szoba1)
    szalloda.szoba_hozzaad(Szoba2)
    szalloda.szoba_hozzaad(Szoba3)
    szalloda.szoba_hozzaad(Szoba4)
    szalloda.szoba_hozzaad(Szoba5)
    szalloda.szoba_hozzaad(Szoba6)
    szalloda.szoba_hozzaad(Szoba7)
    szalloda.szoba_hozzaad(Szoba8)

    while True:
        print("\n1. Szoba foglalása")
        print("2. Foglalás törlése")
        print("3. Foglalások listázása")
        print("4. Kilépés")
        valasztas = input("Válassza ki a kívánt opciót: ")

        if valasztas == '1':
            szobaszam = int(input("Adja meg a szoba számát: "))
            datum = datum_be()
            if datum:
                eredmeny = szalloda.szoba_foglal(szobaszam, datum)
                print(eredmeny)
        elif valasztas == '2':
            szobaszam = int(input("Adja meg a szoba számát: "))
            datum = datum_be()
            if datum:
                eredmeny = szalloda.foglalas_torol(szobaszam, datum)
                print(eredmeny)
        elif valasztas == '3':
            szalloda.foglalasok_listazasa()
        elif valasztas == '4':
            break
        else:
            print("Érvénytelen választás.")


if __name__ == "__main__":
    main()
