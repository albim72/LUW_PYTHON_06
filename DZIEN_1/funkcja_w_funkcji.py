def witaj(imie):
    return f"witaj {imie}"

def konkurs(imie,miejsce,punkty):
    return f"konkurs {imie} -> {miejsce}: {punkty}"

def bouns(punkty):
    if punkty >50:
        bn = punkty + 10
    else:
        bn = punkty
    return f'liczba punktów z bonusem {bn}'

def multiosoba(*args):
    return f"opublikowane wyniki konkursu: {bouns(args[1])}, {konkurs(*args)}"

#funkcja wyższego rzędu...
def osoba(funkcja, *args):
    return f"powitanie -> {funkcja(*args)}"

print(osoba(witaj, "Jerzy"))
print(osoba(witaj, "Anna"))
print(osoba(witaj, "Leon"))
print(osoba(konkurs, "Jerzy",45,64))
print(osoba(multiosoba,"Anna",78,32))
