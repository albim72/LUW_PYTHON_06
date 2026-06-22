from collections import defaultdict, Counter


nb = [6,3,6,3,7,2,89,9,35,72,4,79,0,22,1] #lista -- list()
tpnb = (84,24,6,24,799,3,79) #krotka - -tuple()
drzewa = {"dąb","sosna","jesion","wiśnia"} #zbiór - set()
slownik = {"imię":"Jan","nazwisko":"Nowak","wiek":40} #słownik - -dict()

liczby = [4,6,2,7,4,4,6,89,9,2,3,4,4,1,84,6,89,11,11,3,4,89]

#zbuduj listę liczby_bez_dupliktów


liczby_bez_dupliktów = list(set(liczby))
print(liczby_bez_dupliktów)

#dane z punktów kontrolnych zawodów biegowych -> (numer_startowy, punkt, czas_minuty)
# CTRL+D - duplikacja linii - bloku tekstu
# CTRL + / - komentowanie/ odkomentowanie bloków tekstu
checkpoints = [
    (101,"Start",0),
    (102,"Start",0),
    (103,"Start",0),
    (104,"Start",0),
    (101,"Kościelisko",56),
    (102,"Kościelisko",67),
    (103,"Kościelisko",69),
    (104,"Kościelisko",23),
    (101,"Ornak",230),
    (102,"Ornak",267),
    (103,"Ornak",366),
    (104,"Ornak",88),
    (101,"Meta",428),
    (102,"Meta",546),
    (104,"Meta",145),
]
