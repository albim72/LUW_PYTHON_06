from sprawazus import SprawaZUS


class WniosekRentowy(SprawaZUS):
    def __init__(self, numer_sprawy, imie, nazwisko, pesel, status, stopien_niezdolnosci):
        super().__init__(numer_sprawy, imie, nazwisko, pesel, status)
        self.stopien_niezdolnosci = stopien_niezdolnosci

    def oblicz_czas_obslugi(self):
        if self.stopien_niezdolnosci == "całkowita":
            return 21
        elif self.stopien_niezdolnosci == "częściowa":
            return 35
        else:
            return 40

    def opis_sprawy(self):
        return (
            f"Wniosek rentowy osoby: {self.imie} {self.nazwisko}. "
            f"Stopień niezdolności do pracy: {self.stopien_niezdolnosci}."
        )