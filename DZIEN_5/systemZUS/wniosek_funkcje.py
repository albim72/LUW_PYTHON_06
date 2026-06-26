def pokaz_wszystkie_sprawy(lista_spraw):
    """
    Wyświetla dane wszystkich spraw przekazanych na liście.
    Funkcja zakłada, że każdy obiekt posiada metody:
    - pokaz_dane()
    - opis_sprawy()
    - oblicz_czas_obslugi()
    """
    for sprawa in lista_spraw:
        print("=" * 40)
        print(sprawa.pokaz_dane())
        print(sprawa.opis_sprawy())
        print(f"Przewidywany czas obsługi: {sprawa.oblicz_czas_obslugi()} dni")


def policz_laczny_czas_obslugi(lista_spraw):
    """
    Zwraca łączny przewidywany czas obsługi wszystkich spraw.
    """
    suma = 0

    for sprawa in lista_spraw:
        suma += sprawa.oblicz_czas_obslugi()

    return suma
