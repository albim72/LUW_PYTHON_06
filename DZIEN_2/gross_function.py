#fukcja calc_gross_price() - licząca wartość brutto produktu

def calc_gross_price(net_price:float,vat_percent:float)->float:
    gross_price = net_price + net_price * vat_percent/100
    return gross_price

"""
program oparty na funkcji fukcja calc_gross_price()
może wykonać dowolene obliczenie dla każdego produktu z dowlony m VAT
parametry:
net_price:float,
vat_percent:float
"""

price = calc_gross_price(121,23)
print(f"cena brutto wynosi: {price:.2f} zł")

opis = """
program oparty na funkcji fukcja calc_gross_price()
może wykonać dowolene obliczenie dla każdego produktu z dowlony m VAT
parametry:
net_price:float,
vat_percent:float
"""

print(opis)

#ceny wielu produktów
prices = [22.6,304,101.99,20,89,3.4,1023.77,202,90]

"""
zadanie uzupełniające - użyj fukcji calc_gross_price() do policzenia cen brutto dla
wszystkich cen netto produktów zawartych w liście prices 
"""

for price in prices:
    gross = calc_gross_price(price, 23)
    print(f"Netto: {price:.2f} zł, Brutto: {gross:.2f} zł")
