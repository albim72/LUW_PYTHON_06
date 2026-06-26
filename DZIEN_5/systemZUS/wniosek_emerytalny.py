from sprawazus import SprawaZUS


class WniosekEmerytalny(SprawaZUS):
    def __init__(self, numer_sprawy, imie, nazwisko, pesel, status, lata_pracy):
        super().__init__(numer_sprawy, imie, nazwisko, pesel, status)
        self.lata_pracy = lata_pracy

    def oblicz_czas_obslugi(self):
        if self.lata_pracy > 35:
            return 14
        else:
            return 30

    def opis_sprawy(self):
        return (
            f"Wniosek emerytalny osoby: {self.imie} {self.nazwisko}. "
            f"Liczba lat pracy: {self.lata_pracy}."
        )