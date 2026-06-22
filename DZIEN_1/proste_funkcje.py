print("funkcja bez parametrów, która nic nie zwraca....")

def opis():
    print("to jest bardzo prosta funkcja")

opis()
opis()
opis()
opis()

print("funkcja z parametrem, która zwraca....")
def instrukcja(i):
    return f"nowa instrukcja: {i}"

print(instrukcja(2))
print(instrukcja(3))
print(instrukcja("takie tam abc"))
print(instrukcja(True))
print(instrukcja(-0.004))

w = instrukcja("kilka ważnych słów...")

print(f"wynik fuknkcji -> instukcja :{w}")

print("funkcja z parametrami, która zwraca.... z pełną anotacją!")
def policz(a:float,b:float,c:float)->float:
    return a+b*(c-1)

print(policz(2,3,4))
print(policz(56,0,1))
print(policz(7.33,-3.45,0.223))

print("funkcja z parametrami i wartością domyślną")
def policz_rabat(kwota:float, stala:float, rabat:float= 0.12)->float:
    return kwota*rabat+stala

print(policz_rabat(2500,12,0.17))
print(policz_rabat(2900,100,0.12))
print(policz_rabat(2500,88))
print("fukcja z wieloma wartoścami domyślnymi")
def oblicz_f(n:float,m:float,k:int=9,z:float=3.3)->float:
    return 2*n+k*m+z**2

print(oblicz_f(2,3,4))
print(oblicz_f(24,2,4,8))
print(oblicz_f(-2,3))
print(oblicz_f(56,86))
print(oblicz_f(7.33,-3.45,z=7))
print(oblicz_f(7.33,-3.45,k=4,z=7))
print(oblicz_f(m=7.8,k=1.34,n=9,z=0.44))



