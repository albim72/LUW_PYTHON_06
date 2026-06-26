from abc import ABC, abstractmethod


class SprawaZUS(ABC):
    licznik_spraw = 0

    def __init__(self, numer_sprawy, imie, nazwisko, pesel, status):
        self.numer_sprawy = numer_sprawy
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel
        self.status = status

    def zmien_status(self, nowy_status):
        self.status = nowy_status

    def pokaz_dane(self):
        return (
            f"Numer sprawy: {self.numer_sprawy}\n"
            f"Imię: {self.imie}\n"
            f"Nazwisko: {self.nazwisko}\n"
            f"PESEL: {self.pesel}\n"
            f"Status: {self.status}"
        )

    @abstractmethod
    def oblicz_czas_obslugi(self):
        pass

    @abstractmethod
    def opis_sprawy(self):
        pass

    @staticmethod
    def czy_poprawny_pesel(pesel):
        return isinstance(pesel, str) and len(pesel) == 11 and pesel.isdigit()

    @classmethod
    def utworz_numer_sprawy(cls):
        cls.licznik_spraw += 1
        return f"ZUS/{cls.licznik_spraw}/2026"
