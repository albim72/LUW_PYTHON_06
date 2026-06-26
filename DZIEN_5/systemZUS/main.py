from sprawazus import SprawaZUS
from wniosek_emerytalny import WniosekEmerytalny
from wniosek_rentowy import WniosekRentowy
from wniosek_zasilkowy import WniosekZasilkowy
from wniosek_funkcje import pokaz_wszystkie_sprawy, policz_laczny_czas_obslugi


# Tworzymy trzy różne sprawy ZUS.
# Numer sprawy generujemy przy pomocy metody klasy.
wniosek1 = WniosekEmerytalny(
    SprawaZUS.utworz_numer_sprawy(),
    "Jan",
    "Kowalski",
    "80010112345",
    "nowa",
    38
)

wniosek2 = WniosekRentowy(
    SprawaZUS.utworz_numer_sprawy(),
    "Anna",
    "Nowak",
    "75050598765",
    "w trakcie",
    "całkowita"
)

wniosek3 = WniosekZasilkowy(
    SprawaZUS.utworz_numer_sprawy(),
    "Piotr",
    "Zieliński",
    "90030345678",
    "nowa",
    10
)

wniosek4 = WniosekRentowy(
    SprawaZUS.utworz_numer_sprawy(),
    "Olga",
    "Kot",
    "75031551758",
    "nowa",
    "całkowita"
)

# Dodajemy obiekty do listy.
lista_spraw = [wniosek1, wniosek2, wniosek3, wniosek4]

# Wyświetlamy wszystkie sprawy.
print("LISTA SPRAW ZUS")
pokaz_wszystkie_sprawy(lista_spraw)

# Zmieniamy status jednej sprawy.
wniosek1.zmien_status("zakończona")

print("\nPO ZMIANIE STATUSU PIERWSZEJ SPRAWY")
print(wniosek1.pokaz_dane())

# Liczymy łączny czas obsługi.
laczny_czas = policz_laczny_czas_obslugi(lista_spraw)
print(f"\nŁączny czas obsługi wszystkich spraw: {laczny_czas} dni")

# Sprawdzamy PESEL przy pomocy metody statycznej.
pesel = "80010112345"
print(f"PESEL {pesel} poprawny: {SprawaZUS.czy_poprawny_pesel(pesel)}")
