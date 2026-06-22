#zakupy kawy z ostatnigo miesiąca

kawa = ["lavazza oro","lavazza black", "coffee mauro", "jacobs barista","lavazza oro","lavazza black",
        "plantation arabica kenia"]

kawa_set = set(kawa)
print(kawa_set)

dokupione = ["blue drop arabica", "cofee and sons chocolate"]

kawa_set.update(dokupione)

print(kawa_set)

kawa.extend(dokupione)

print(kawa)
