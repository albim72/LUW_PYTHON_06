person = {
    "imie":"Karolina",
    "wiek":33,
    "wzrost":1.87,
    "waga":67,
    "miasto":"Kraków"
}

print(person)
print(type(person))

print(person["imie"])
print(person["wiek"])

person["zawód"] = "programista"

print(person)

for key in person.keys():
    print(f"klucze: {key}")

for val in person.values():
    print(f"wartość: {val}")

for key,value in person.items():
    print(f"{key}: wartość -> {value}")
