def add_vat(price,percent):
    return price+price*percent/100

def add_discount(price,percent):
    return price-price*percent/100

def double_price(price):
    return price*2

def apply_operation(*args,operation):
    result = operation(*args)
    return result

gross  = apply_operation(101,8,operation=add_vat)
print(f"cena brutto: {gross:.2f} zł")

disc = apply_operation(133,12.5,operation=add_discount)
print(f"cena po rabacie: {disc:.2f} zł")

db = apply_operation(344,operation=double_price)
print(f"podwójna cena: {db:.2f} zł")

