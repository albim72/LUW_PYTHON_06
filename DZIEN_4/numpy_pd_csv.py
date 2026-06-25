import pandas as pd
import numpy as np

#tworzymy dane w numpy
names = np.array(["Jan","Anna","Piotr","Maria"])
surnames = np.array(["Kowal","Kot","Kos","Nowak"])
points = np.array([80,82,56,71])

print(names)
print(type(names))

#Ramka Pandas -rodzaj arkusza, tabeli
df = pd.DataFrame({"name":names,"surname":surnames,"points":points})

print(df)

#zapis do pliki csv
df.to_csv("studens.csv", index=False,encoding="utf-8")
print("dane zapisane.....")

#odczyt danych z pliku csv
df_from_csv = pd.read_csv("studens.csv",encoding="utf-8")
print("dane odczytane z pliku CSV")
print(df_from_csv)

#prosta analiza danych
avg_points = df_from_csv["points"].mean()
max_points = df_from_csv["points"].max()

print(f"średnia liczba punktów: {avg_points}")
print(f"max liczba punktów: {max_points}")


