from sprawazus import SprawaZUS


class WniosekZasilkowy(SprawaZUS):
    def __init__(self, numer_sprawy, imie, nazwisko, pesel, status, liczba_dni_zwolnienia):
        super().__init__(numer_sprawy, imie, nazwisko, pesel, status)
        self.liczba_dni_zwolnienia = liczba_dni_zwolnienia

    def oblicz_czas_obslugi(self):
        if self.liczba_dni_zwolnienia <= 14:
            return 7
        else:
            return 14

    def opis_sprawy(self):
        return (
            f"Wniosek zasiłkowy osoby: {self.imie} {self.nazwisko}. "
            f"Liczba dni zwolnienia: {self.liczba_dni_zwolnienia}."
        )