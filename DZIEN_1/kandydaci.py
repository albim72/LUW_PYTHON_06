wyrazenia = [
    "x+1",
    "x*2",
    "x**2",
    "x*x+1"
]

print(wyrazenia)

for expr in wyrazenia:
    print(expr)
print("_"*70)
print(wyrazenia[1])
print(wyrazenia[-1])

t = "lajkonik"
print(t)
print(t[0])
print(t[2])
print(t[0:5]) #slice cięcie na plasterki kolekcji... lewa strona zawiera się prawa nie zawiera się !!
print(t[5:])
print(t[:4])
print(t[1:6:2]) #(t[lewa,prawa,skok])

s1 = "Kazimierz"
s2 = "kajak"

print(s1[::-1])
print(s2[::-1])


