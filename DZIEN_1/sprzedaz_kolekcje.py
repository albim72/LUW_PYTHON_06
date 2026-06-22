sales = [
    ("herbata", 3),
    ("kawa", 2),
    ("herbata", 1),
    ("cukier", 5),
    ("kawa", 4),
    ("miód", 2),
    ("herbata", 2)
]

print("wszystkie sprzedaze")

for product,amount in sales:
    print(f"produkt: {product}, liczba sztuk {amount}")

unique_products = list(set(sales))
print(unique_products)

unique_names = set() #pusty zbiór

for product,amount in sales:
    unique_names.add(product)

print(unique_names)
print(len(unique_names))

#podsumowanie sprzedazy
summary = {}
for product,amount in sales:
    if product in summary:
        summary[product] += amount
    else:
        summary[product] = amount

print("podsumowanie sprzedazy")
for product,total_amount in summary.items():
    print(f"{product}, sprzedano razem : {total_amount}")
