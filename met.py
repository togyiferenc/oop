from abc import ABC, abstractmethod
from datetime import datetime


class Szoba(ABC):
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam
        self.foglalasok = []

    def foglalas_hozzaad(self, foglalas):
        self.foglalasok.append(foglalas)

    def foglalas_torol(self, foglalas):
        self.foglalasok.remove(foglalas)

    def szabad(self, datum):
        return all(foglalas.datum != datum for foglalas in self.foglalasok)

    @abstractmethod
    def get_info(self):
        pass


class EgyagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam):
        super().__init__(ar, szobaszam)

    def get_info(self):

        return "Egyágyas Szoba Információ"


class KetagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam):
        super().__init__(ar, szobaszam)

    def get_info(self):

        return "Kétágyas Szoba Információ"


class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

    def foglalas_info(self):
        return f"Foglalás - Dátum: {self.datum.strftime('%Y-%m-%d')}, Szoba: {self.szoba.get_info()}"


class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def szoba_hozzaad(self, szoba):
        self.szobak.append(szoba)

    def szoba_foglal(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam and szoba.szabad(datum):
                foglalas = Foglalas(szoba, datum)
                szoba.foglalas_hozzaad(foglalas)
                return f"Foglalás rögzítve. Ár: {szoba.ar}"
        return "Nincs ilyen szobaszám vagy a szoba nem szabad."

    def foglalas_torol(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                for foglalas in szoba.foglalasok:
                    if foglalas.datum == datum:
                        szoba.foglalasok.remove(foglalas)
                        return "Foglalás törölve."
        return "Nincs ilyen foglalás."

    def foglalasok_listazasa(self):
        for szoba in self.szobak:
            for foglalas in szoba.foglalasok:
                print(foglalas.foglalas_info())
