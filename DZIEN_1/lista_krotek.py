osoby = [
    ("Ala",56),
    ("Ola",88),
    ("Tola",52),
    ("Norbert",68),
    ("Maria",78),
    ("Eryk",45),
    ("Feliks",90),
]

for elem in osoby:
    print(elem)

print("_"*70)

for name,grade in osoby:
    print(f"{name} ma ocenę {grade}")

print("_"*70)

#śednia ocen - suma ocen/liczba ocen

sum_grades = 0
for name,grade in osoby:
    sum_grades += grade

avg = sum_grades/len(osoby)
print(avg)
print("_"*70)
