from abc import ABC, abstractmethod


class SprawaZUS(ABC):
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
